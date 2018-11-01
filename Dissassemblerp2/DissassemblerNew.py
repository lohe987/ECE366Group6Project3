# ECE 366 Project 2 Disassembler

# This file disassembles two project files

def file_to_array(file):
    return_array = []

    for line in file:

        line = line.partition('#')[0]

        line = line.rstrip()

        if line[0:1] == '1' or line[0:1] == '0':
            return_array.append(line)

    return return_array


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
        registerArray[c] = registerArray[c] + registerArray[d]
        pc += 1

    if line[0:3] == '011':  # sub instruction
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

    if line[0:3] == '000':  # b instruction
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
            pc += imm
        else:
            pc += 1

    if line[0:3] == '010':  # ADDI instruction
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

    if line[0:3] == '100':  # SLT instruction
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
            b = 1
        else:
            b = 0
        pc += 1

    if line[0:3] == '101':  # XOR instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]

        c = int(rx, 2)
        d = int(ry, 2)
        a = "XOR"
        xor_value = (registerArray[c] ^ registerArray[d])
        pc += 1

    if line[0:3] == '110':  # AND instruction
        op = line[0:3]
        rx = line[3:5]
        ry = line[5:7]
        parity = line[7:8]

        c = int(rx, 2)
        d = int(ry, 2)
        a = "AND"
        and_value = (registerArray[c] and registerArray[d])
        pc += 1

    if line[0:5] == '11110':  # Store instruction
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

    if line[0:5] == '11111':  # Load instruction
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
        registerArray[int(c)] = data_mem[int(p)]
        pc += 1

    if line[0:5] == '11100':  # ADDPTR instruction
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

    if line[0:5] == '11101':  # RESETPTR instruction
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
        registerArray[int(c)] = data_mem[0]


def simulator(progFile, instructionFile, dataFile):
    pc = 0
    b = 0
    registerArray = [0, 0, 0, 0]

    print(progFile)

    # Create file variables from file name strings

    instr_mem_input = open(instructionFile, "r")

    data_mem_input = open(dataFile, "r")

    instr_mem = file_to_array(instr_mem_input)

    data_mem = file_to_array(data_mem_input)

    while pc < len(instr_mem):
        # data_set is of the following format:

        # [data_mem, registerArray, pc, b]

        line = instr_mem[pc]

        print("PC: ", pc)

        data_set = execute_operation(line, data_mem, registerArray, pc, b)

        data_mem = data_set[0]

        registerArray = data_set[1]

        pc = data_set[3]

        b = data_set[4]

        print("registerArray: ", registerArray)

        print("MEM[4]: Highest Score ", data_mem[4])

        print("MEM[5]: Count         ", data_mem[5])

        print("\n")

        dic += 1

        # time.sleep(.001)

    print("Dynamic Instruction Count: ", dic)

    # print(instr_mem)

    # print(data_mem)


# simulator("Program 0 : Simulator Testing",

#          "p3_group_10_p0_imem.txt",

#          "p3_group_10_dmem_A.txt")


# simulator("Program 1 : Modular Exponentiation",

#            "p3_group_10_p1_imem.txt",

#            "p3_group_10_dmem_B.txt")


simulator("Program 2 : Best Matching Count", "Program2_Bin.txt", "patternA.txt")
