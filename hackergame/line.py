from stdlib import Machine

def main():
    machine_vector = []
    mach = Machine('127.0.0.1','Krisis234')
    mach.save_file('\\hello.txt','Hi\n\nMy name is Nathan and I am your guide on your way to Zappa Brotherhood. I\'m glad you\'ve decided to join. Therefore: fist test for you: find another message from me. It is on this computer. Good luck.')
    machine_vector.append(mach)
    mach = Machine('127.0.0.2','saito')
    mach.add_connection(machine_vector[0])
    machine_vector.append(mach)
    return machine_vector