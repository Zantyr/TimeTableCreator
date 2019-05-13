from stdlib import Machine,HWDP

def main():
    print("Hello. You've probably playing this game for the first time. If you need help, use command `man'\n\n")
    machine_vector = []
    mach = Machine('68.12.49.71','Oppenheimer')
    mach.cra_sh_core('tim')
    mach.save_file('\\home\\tim\\Documents\\rants.txt','Cra.sh is FUUCKING leaky.\nI\'ve managed to break it\'s safety systems in like 15 minutes. I know it\'s the first OS for quantum computers, but geez, trying to seem UNIX-like with all these references and failed shell command because `the quantum memory is expensive\'. I hope I manage to fix that, I won\'t store files there otherwise.')
    mach.save_file('\\home\\tim\\Documents\\dergo.txt','From: Dergo <d3rgo@0xdeadbeef.net>\nTo: Fecking Fab <flab@hmail.com>\nSubject: VickyLeaks breached\n\nWe\'ve managed to break through the firewall to the SANDRO cluster with the GD-14 exploit. It is possible to get perms by enthropy overload. Prolly won\'t manage to do that tho, because we ain\'t have such access. We would need at least 30% of processing time to do that. Billbow and I work on it. I attach the keys to the exploit here:\n\nbdsm.dergo.personal->b4d6c3aa194560.net:1488/gd-14: 0B 01 0C 07 0D 0A')
    mach.save_file('\\home\\tim\\Documents\\billing.txt','From: KinkyLab Inc. <ceo@kinkylab.com>\nTo: Tim Anderson <tim@newparadigm.quant>\nSubject: Re: Payment request\n\nThe job was excellent. The 3d models and haptics are enormous success. Of course, implementation of all the toys will take time, and with time comes the money. I\'ve transferred $100,000 onto your account as you requested. I also forward the vibrato.hwdp file with specifications of our new products. Please send forward the estimated deadline.\n\nYours\nRoger Brand\nCEO of KinkyLab')
    mach.save_file('\\home\\tim\\Downloads\\enthropy_exploit.txt','Quantum enthropy exploit uses multiple write requests to change the contents of the vital file. As you know, touching the qbit always changes it context. Most processors need lasers to be warmed up just before performing operation, so usually several first qbits may be touched. Forceful jumping to the given qbyte slightly modifies that qbyte (and possibly qbytes after it) before system lock kicks in.\n\nIt requires from 300K to 6M write requests to modify eight qbyte password file header, so using this exploit requires nearly contants access to the processor. This is harsh requirement, but usually multiple zombie account as suffice, as 20-50% of the processing power is enough.\n\nNote it won\'t work on each quantum computer. The newest models as well as the giant clusters are so callibrated, that the laser action is near instantaneous.\n-D3rgo')
    mach.save_folder('\\home\\tim\\Documents\\project',(False,False,True))
    mach.save_file('\\home\\tim\\Documents\\project\\HELLO.TXT','\nI AM BECOME DEATH\n')
    mach.save_file('\\home\\tim\\Documents\\project\\SPECS.TXT','\n--to do--\nSome number that cipher a 2-5 word passsword to the project\'s unstable repo.\n')
    mach.save_literal_file('\\home\\tim\\Documents\\vibrato.hwdp',HWDP({'\\1.QB':'1d f5 00 ...'}))
    mach.save_file('\\qscp.out','Transfer and conversion successful\n\nSource:101.33.59.82\nTarget:68.12.49.71\n2 590 112 688 qbytes transferred\nTime: 5hrs 19mins\nDate: 2047 Feb 11 05:56:11')
    machine_vector.append(mach)
    mach = Machine('127.0.0.2','saito')
    mach.add_connection(machine_vector[0])
    machine_vector.append(mach)
    return machine_vector