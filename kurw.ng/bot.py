parse = lambda sentence,model,scope: [process_sentence(tokenize(x),model,scope) for x in  \
    sentence.replace('!','.').replace('?','.').split('.') if tokenize(x)!=[]] \
    if sentence[0]!=':' else lang(sentence,model)

def lang(sentence,model):
    quit()

tokenize = lambda tokens: [x.strip('.-;:').lower() for x in tokens.split(' ') if x!='']

def process_sentence(sentence,model,scope):
    for instance in model:
        x = match_lists(instance[0],sentence,instance[1],scope)
        if x: return x
    else:
        raise BaseException('No such pattern as: '+str(sentence))

def match_lists(pattern,source,function,scope):
    pattern = [x for x in reversed(pattern)]
    source = [x for x in reversed(source)]
    args = [[]]
    while source and pattern:
        if pattern[-1] == source[-1]:
            pattern.pop()
            source.pop()
        elif type(pattern[-1]) in (list,tuple):
            if len(pattern[-1])==0:
                if len(pattern)>1 and pattern[-2]==source[-1]:
                    args.append([])
                    pattern.pop()
                    source.pop()
                    pattern.pop()
                elif len(pattern)>1 and source[-1] in pattern[-2]:
                    pattern.pop()
                    source.pop()
                    pattern.pop()
                else:
                    args[-1].append(source.pop())
            elif source[-1] in pattern[-1]:
                pattern.pop()
                source.pop()
            else: break
        else: break
    x = pattern in [[],[[]]] and source == []
    if args[-1]==[]:args.pop()
    if x: x = function(scope,*args)
    return x

#implementacja

hello = lambda mem,args: "Hello, " + ' '.join(args)

class Scope(object):
    def __init__(self,underscope=None):
        self.under = underscope 
        self._data = {}   
    def get(self,what):
        try: return self._data[what]
        except: return self.under.get(what)
    def set(self,what,to):
        self._data[what] = to

mem = Scope()

foo = None

MODEL = [(('this','is',[]),hello),
(('nakurwiaj',[]),lambda mem,x: parse(mem.get(' '.join(x)),MODEL,mem)),
(('niech',[],'to','jest',[]),lambda mem,x,y:mem.set(' '.join(x),' '.join(y))),
(('mam', 'jedna', 'pierdolona', []), foo),
(([],'na','mikrofonie'),foo),
(('powiem', 'ci', 'ze', 'to', []),foo),
(('powiesz', 'mi', 'ze', 'to', []),foo),
(([],'na','mikrofonie'),foo),
]

print(parse("Niech salto to jest kurwa. Nakurwiaj salto.",MODEL,mem)[-1])
