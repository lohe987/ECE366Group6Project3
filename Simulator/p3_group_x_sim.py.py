

def execute_operation(line, data_mem, registerArray, pc, b):
    if line[0:3] == '001':  # add instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]
        if line[3:5] == '01':
            c = "1"
        elif line[3:5] == '10':
            c = "2"
        elif line[3:5] == '11':
            c = "3"
        else:
            c = "4"
        if line[5:7] == '01':
            d = "1"
        elif line[5:7] == '10':
            d = "2"
        elif line[5:7] == '11':
            d = "3"
        else:
            d = "4"
        a = "ADD"
        print(registerArray)
        registerArray[int (c)] = registerArray[ int (c)] + registerArray[int (d)]
        pc += 1

    elif line[0:3] == '011':  # sub instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]

        c = int(rx, 2)
        d = int(ry, 2)
        a = "SUB"
        print(registerArray)
        registerArray[c] = registerArray[c] - registerArray[d]
        pc += 1

    elif line[0:3] == '000':  # b instruction
        op = line[0:3]
        imm = line[3:7]
        parity = line[7:8]
        if line[3:7] == '0000':
            c = "0"
        elif line[3:7] == '0001':
            c = "1"
        elif line[3:7] == '0010':
            c = "2"
        elif line[3:7] == '0011':
            c = "3"
        elif line[3:7] == '0100':
            c = "4"
        elif line[3:7] == '0101':
            c = "5"
        elif line[3:7] == '0110':
            c = "6"
        elif line[3:7] == '0111':
            c = "7"
        elif line[3:7] == '1111':
            c = "-1"
        elif line[3:7] == '1110':
            c = "-2"
        elif line[3:7] == '1101':
            c = "-3"
        elif line[3:7] == '1100':
            c = "-4"
        elif line[3:7] == '1011':
            c = "-5"
        elif line[3:7] == '1010':
            c = "-6"
        elif line[3:7] == '1001':
            c = "-7"
        else:
            c = "-8"

        a = "B"
        if b == 1:
            pc += int(imm)
        else:
            pc += 1

    elif line[0:3] == '010':  # ADDI instruction
        op = line[0:3]
        rx = line[3:5]
        imm = line[5:7]
        parity = line[7:8]
        if line[3:5] == '01':
            c = "1"
        elif line[3:5] == '10':
            c = "2"
        elif line[3:5] == '11':
            c = "3"
        else:
            c = "4"
        if line[5:7] == '01':
            d = "1"
        elif line[5:7] == '10':
            d = "-2"
        elif line[5:7] == '11':
            d = "-1"
        else:
            d = "0"
        a = "ADDI"
        registerArray[int(c)] += int(d)
        pc += 1

    elif line[0:3] == '100':  # SLT instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]

        c = int(rx, 2)
        d = int(ry, 2)
        a = "SLT"
        rx = registerArray[c]
        ry = registerArray[d]
        if c < d:
            registerArray[6] = 1
        else:
            registerArray[6] = 0

        pc += 1

    elif line[0:3] == '101':  # XOR instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]

        c = int(rx, 2)
        d = int(ry, 2)
        a = "XOR"
        xor_value = (registerArray[c] ^ registerArray[d])
        pc += 1

    elif line[0:3] == '110':  # AND instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]

        c = int(rx, 2)
        d = int(ry, 2)
        a = "AND"
        and_value = (registerArray[c] and registerArray[d])
        pc += 1

    elif line[0:5] == '11110':  # Store instruction
        op = line[0:5]
        rx = line[5:6]
        rp = line[6:7]
        parity = line[7:8]
        if line[5:6] == '0':
            c = "2"
        else:
            c = "3"
        if line[6:7] == '0':
            p = "5"
        else:
            p = "6"
        a = "STORE"

        data_mem[registerArray[int(p)]] = registerArray[int(c)]
        pc += 1

    elif line[0:5] == '11111':  # Load instruction
        op = line[0:5]
        rx = line[5:6]
        imm = line[6:7]
        parity = line[7:8]
        if line[5:6] == '0':
            c = "2"
        else:
            c = "3"
        if line[6:7] == '0':
            p = "5"
        else:
            p = "6"
        a = "LOAD"
        registerArray[int(c)] = int(data_mem[int(p)])
        pc += 1

    elif line[0:5] == '11100':  # ADDPTR instruction
        op = line[0:5]
        rp = line[5:6]
        p = line[6:7]
        parity = line[7:8]
        if line[5:6] == '0':
            c = "5"
        else:
            c = "6"
        if line[6:7] == '0':
            p = "-1"
        else:
            p = "1"
        a = "ADDPTR"
        registerArray[int(c)] += registerArray[int(p)]
        pc += 1

    elif line[0:5] == '11101':  # RESETPTR instruction
        op = line[0:5]
        rp = line[5:6]
        p = line[6:7]
        parity = line[7:8]
        if line[5:6] == '0':
            c = "5"
        else:
            c = "6"
        if line[6:7] == '0':
            p = ""
        else:
            p = ""
        a = "RESETPTR"
        registerArray[int(c)] = int(data_mem[0])
        pc +=1

    return [data_mem, registerArray, pc, b]

def simulator(instructionFile, dataFile):
    pc = 0
    b = 0
    registerArray = [0, 0, 0, 0, 0, 0, 0]
    instr_mem = []
    data_mem= []


    # Create file variables from file name strings

    instr_mem_input = (instructionFile)

    data_mem_input = (dataFile)
    for line in instr_mem_input:
        line = line.rstrip()

        if line[0:1] == '1' or line[0:1] == '0':
           instr_mem.append(line)
    for line in data_mem_input:
        line = line.rstrip()

        if line[0:1] == '1' or line[0:1] == '0':
            data_mem.append(line)

    dic = 0

    while pc < len(instr_mem):
        # data_set is of the following format:

        # [data_mem, registerArray, pc, b]

        line = instr_mem[pc]

        print("PC: ", pc)

        data_set = execute_operation(line, data_mem, registerArray, pc, b)

        data_mem = data_set[0]

        registerArray = data_set[1]

        pc = data_set[2]

        b = data_set[3]

        print("registerArray: ", registerArray)


        print("\n")

        dic += 1


    print("Dynamic Instruction Count: ", dic)




Program1_Bin = open("Program1_Bin.txt", "r")
Program2_Bin = open("Program2_Bin.txt", "r")
Program0_Bin = open("p3_group_x_p0_imem.txt", "r")
i = input("enter which file to run:")
if(i == 1)


PatternA = open("PatternA.txt", "r")
simulator(Program2_Bin, PatternA)

