#!/usr/bin/python3

# Read digit recognition
# For demonstration purposes - Paweł Tomasik
# Data may be downloaded from: https://clarin-pl.eu/dspace/handle/11321/317

from keras.models import Model
from keras.layers import GRU, Conv1D, Dropout, LeakyReLU, Dense, Input, Lambda
from keras.optimizers import Adam

import editdistance  # For digit error rate
import keras
import librosa
import numpy as np
import os

# supply your own paths to data
DIGITSPATH = os.path.expanduser("~/Downloads/cyfry/digits_train")
VALIDDATA = os.path.expanduser("~/Downloads/cyfry/digits_valid")  # used as test data
NPHONES = 10
NFEATS = 39

def load_data(path):
    X, y = [], []
    for fname in (os.path.join(path, x[:-4]) for x in os.listdir(path)
            if x.endswith('.raw')):
        print(fname)
        with open(fname + '.raw') as f:
            recording = np.fromfile(f, dtype=np.int16)
            recording = extract_features(recording)
        with open(fname + '.txt') as f:
        	transcript = [x for x in f.read() if x in '0123456789']
        X.append(recording.T)
        y.append(np.array([int(x) for x in transcript]))
    return X, y

# I use MFCC with delta and delta-delta features, which is standard for ASR
def extract_features(x):
    x = x.astype(np.float32)
    x /= 2**15
    mfcc = librosa.feature.mfcc(x, sr=16000, n_mfcc=13)
    delta = librosa.feature.delta(mfcc)
    ddelta = librosa.feature.delta(mfcc, order=2)
    return np.vstack([mfcc, delta, ddelta])

# Loss function has to be implemented as a Lambda layer (ref. Keras captcha tutorial)
def ctc_loss_function(arguments):
    y_pred, y_true, input_length, label_length = arguments
    return keras.backend.ctc_batch_cost(y_true, y_pred, input_length, label_length)

def mk_model(max_label_length):
    feature_input = Input(shape = (None, NFEATS))
    layer_1 = Conv1D(48, 7, padding = 'same')(feature_input)
    layer_2 = LeakyReLU(0.01)(layer_1)
    layer_3 = Dropout(0.25)(layer_2)
    layer_4 = Conv1D(64, 5, padding = 'same')(layer_3)
    layer_5 = LeakyReLU(0.01)(layer_4)
    layer_6 = Dropout(0.25)(layer_5)
    layer_7 = Conv1D(96, 3, padding = 'same')(layer_6)
    layer_8 = LeakyReLU(0.01)(layer_7)
    layer_9 = Dropout(0.25)(layer_8)
    layer_10 = GRU(64, return_sequences = True)(layer_9)
    layer_11 = Dropout(0.25)(layer_10)
    layer_12 = GRU(48, return_sequences = True)(layer_11)
    layer_13 = Dropout(0.25)(layer_12)
    layer_14 = GRU(32, return_sequences = True)(layer_13)
    layer_15 = GRU(NPHONES + 1, return_sequences = True, activation = 'softmax')(layer_14)
    label_input = Input(shape = (max_label_length,))
    input_length = Input(name='input_length', shape=[1], dtype='int64')
    label_length = Input(name='label_length', shape=[1], dtype='int64')
    loss_lambda = Lambda(ctc_loss_function, output_shape=(1,), name='ctc')([layer_15, label_input, input_length, label_length])
    model = Model([feature_input, label_input, input_length, label_length], [loss_lambda])
    predictive = Model(feature_input, layer_15)
    return model, predictive

def train(model, trainX, trainy, trainXl, trainyl, epochs = 50):
    optimizer = Adam(0.001)
    model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer=optimizer)
    return model.fit([trainX, trainy, trainXl, trainyl], np.zeros(trainX.shape[0]), epochs = epochs)

def make_data(X, y):
    X_lengths = np.array([x.shape[0] for x in X])
    maxlen = max([x.shape[0] for x in X])
    X = [np.pad(item, ((0, maxlen - item.shape[0]), (0, 0)), 'constant') for item in X]
    y_lengths = np.array([x.shape[0] for x in y])
    maxlen = max([x.shape[0] for x in y])
    y = [np.pad(item, (0, maxlen - item.shape[0]), 'constant', constant_values = NPHONES) for item in y]
    return np.stack(X), np.stack(y), X_lengths, y_lengths

def validate(predictions, valid_length, groundtruth, target_length):
    predictions = keras.backend.ctc_decode(predictions, valid_length, False, 1000)
    predictions = predictions[0][0].eval(session=keras.backend.get_session())
    DERs = []
    for index in range(predictions.shape[0]):
        dist = float(editdistance.eval(
            [x for x in predictions[index, :] if x != -1],
            [x for x in groundtruth[index, :] if x != NPHONES]))
        DER = dist / target_length[index]
        DERs.append((DER, target_length[index]))
    return DERs

if __name__=='__main__':
    data = make_data(*load_data(DIGITSPATH))
    trn, predict = mk_model(data[1].shape[1])
    train(trn, *data, epochs=1000) # at 300 it makes sensible predictions
    valid_data = make_data(*load_data(VALIDDATA))
    predictions = predict.predict(valid_data[0])
    DERs = validate(predictions, valid_data[2], valid_data[1], valid_data[3])
    print("Validation Digit Error Rate: {}".format(sum([x[0] * x[1] for x in DERs]) / sum([x[1] for x in DERs])))
    predict.save('cyfry.pred.h5')