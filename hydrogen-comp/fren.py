opc = ["NOP", "HLT", "ADD", "SUB", "XOR", "AND", "LDI"]
reg = ['r'+str(i) for i in range(16)]

combin = []
def tryInt(x):
    try:
        return int(x)
    except ValueError:
        return -1e9

with open("input.txt") as file:
    for line in file:    #begin handler
        regbin2 = []
        prtasm = line.strip().split(".")
        opcasm = "".join([x for x in prtasm if x in opc]).strip()
        regasm = [x for x in prtasm if x in reg]
        numasm = "".join([x for x in prtasm if 0<= tryInt(x)<65536]).strip()
        if opcasm in opc:   #translate opc
            opcind = opc.index(opcasm)
            opcbin = bin(opcind)[2:].zfill(4)
            print("<DEBUG-opc:>", opcasm, ">>", opcbin)
            regbin = ""
            for regval in regasm:    #translate reg
                if regval in reg:
                    regbin = bin(reg.index(regval))[2:].zfill(4)
                    regbin2.append(regbin)
                    
                print("<DEBUG-reg:>", regasm, ">>", regbin2)
            regbin="".join(regbin2)
            
            
            numbin = bin(int(numasm))[2:].zfill(16) if numasm else ""
            print("<DEBUG-num:>", numasm, ">>", numbin)        

            combin.append(opcbin + regbin + numbin)
            combin = [str(item).ljust(24, "0") for item in combin]
print(combin)

with open("output.txt", "w") as f:
    f.writelines([line + "\n" for line in combin])