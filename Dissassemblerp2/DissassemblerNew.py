# ECE 366 Project 2 Disassembler

# This file disassembles two project files

p1_input_file = open("Program1_Bin.txt", "r")
p1_output_file = open("Program1_Asm.txt", "w")

p2_input_file = open("Program2_Bin.txt", "r")
p2_output_file = open("Program2_Asm.txt", "w")


def convert_bin_to_asm(input_file, output_file):
    for line in input_file:

        if line == "\n":  # empty lines ignored
            continue
        line = line.replace("\n", "")  # remove 'endline' character
        print("Machine Instr: ", line)  # show the asm instruction to screen


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
            a= "ADD"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")
        if line[0:3] == '011':  # sub instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:7]
            parity = line[7:8]

            c = int(rx, 2)
            d = int(ry, 2)
            a = "SUB"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")
        if line[0:3] == '000':  # Branch instruction
           op = line[0:3]
           imm= line[3:7]
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
           output_file.write(str(a) + " " + "#"+ str(c) + "\n")

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
           output_file.write(str(a) + " " + '$' + str(c) + "," + " " + str(d) + "\n")
        if line[0:3] == '100':  # SLT instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:7]
            parity = line[7:8]

            c = int(rx, 2)
            d = int(ry, 2)
            a = "SLT"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")
        if line[0:3] == '101':  # XOR instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:7]
            parity = line[7:8]

            c = int(rx, 2)
            d = int(ry, 2)
            a = "XOR"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")
        if line[0:3] == '110':  # AND instruction
            op = line[0:3]
            rx = line[3:5]
            ry = line[5:7]
            parity = line[7:8]

            c = int(rx, 2)
            d = int(ry, 2)
            a = "AND"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '$' + str(d) + "\n")
        if line[0:5] == '11110':  # Store instruction
            op = line[0:5]
            rx = line[5:6]
            imm = line[6:7]
            parity = line[7:8]
            if line[5:6] == '0':
                c = "2"
            else:
                c= "3"
            if line[6:7]== '0':
                p="$5"
            else:
                p="$6"



            a = "STORE"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '['+ str(p)+ ']' + "\n")

        if line[0:5] == '11111':  # Load instruction
            op = line[0:5]
            rx = line[5:6]
            imm = line[6:7]
            parity = line[7:8]
            if line[5:6] == '0':
                c = "2"
            else:
                c= "3"
            if line[6:7]== '0':
                p="$5"
            else:
                p="$6"
            a = "LOAD"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '[' + str(p) + ']' + "\n")

        if line[0:5] == '11100':  # ADDPTR instruction
            op = line[0:5]
            rp = line[5:6]
            p = line[6:7]
            parity = line[7:8]
            if line[5:6] == '0':
                c = "5"
            else:
                c= "6"
            if line[6:7]== '0':
                p="-1"
            else:
                p="1"
            a = "ADDPTR"
            output_file.write(str(a) + " " + '$' + str(c) + "," + " " + '#' + str(p) +"\n")

        if line[0:5] == '11101':  # RESETPTR instruction
            op = line[0:5]
            rp = line[5:6]
            p = line[6:7]
            parity = line[7:8]
            if line[5:6] == '0':
                c = "5"
            else:
                c= "6"
            if line[6:7]== '0':
                p=""
            else:
                p=""
            a = "RESETPTR"
            output_file.write(str(a) + " " + '$' + str(c) + "" + " " + '' + str(p) +"\n")



def simulator(program_name, instr_mem_file, data_mem_file):

    # Initialize pc and register array

    pc = 0

    branch = 0

    reg_arr = [0, 0, 0, 0]

    special_reg_arr = [0, 0, 0, 0]



    print(program_name)



    # Create file variables from file name strings

    instr_mem_input = open(instr_mem_file, "r")

    data_mem_input = open(data_mem_file, "r")



    instr_mem = file_to_array(instr_mem_input)

    data_mem = file_to_array(data_mem_input)

    print(len(instr_mem))

    while pc < len(instr_mem):

        # data_set is of the following format:

        # [data_mem, reg_arr, special_reg_arr, pc, branch]

        opcode = instr_mem[pc]

        print("PC: ", pc)

        data_set = execute_operation(opcode, data_mem, reg_arr, special_reg_arr, pc, branch)

        data_mem = data_set[0]

        reg_arr = data_set[1]

        special_reg_arr = data_set[2]

        pc = data_set[3]

        branch = data_set[4]

        print("reg_arr: " ,reg_arr)

        print("Data_mem[2]: ", data_mem[2])

        print("special_Reg_arr: ", special_reg_arr)

        print("\n")

convert_bin_to_asm(p1_input_file, p1_output_file)
convert_bin_to_asm(p2_input_file, p2_output_file)
