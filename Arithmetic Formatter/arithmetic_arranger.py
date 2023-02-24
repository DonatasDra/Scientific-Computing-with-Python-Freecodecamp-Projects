def arithmetic_arranger(problems, show = False):

    if len(problems) > 5:
        return "Error: Too many problems."
    op1 = list()
    op2 = list()
    dashes = list()
    result = list()
    # splitting problems and constructing lists with operands/operators
    for problem in problems:
        c = problem.split()
        # c[0] = operand 1, c[1] = operator, c[2] = operand 2
        if c[1] != "+" and c[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if len(c[0]) > 4 or len(c[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if c[0].isnumeric() != True or c[2].isnumeric() != True:
             return "Error: Numbers must only contain digits."
        line1 = c[0].rjust(len(max(c[0],c[2], key= len)))
        line2 = c[1] + ' ' + c[2].rjust(len(max(c[0],c[2], key= len)))
        line3 = '--' + '-'*(len(max(c[0],c[2], key= len)))

        if c[1] == '+':
            b = str(int(c[0])+int(c[2]))
            b = b.rjust(len(line3))
        if c[1] == '-':
            b = str(int(c[0])-int(c[2]))
            b=  b.rjust(len(line3))

        op1.append(line1)
        op2.append(line2)
        dashes.append(line3)
        result.append(b)
    
    # constructing output
    line1=''
    line2=''
    line3=''
    for line in range(len(op1)):
        line1+='  ' + op1[line] + '    '
    line1 = line1.rstrip()
    for line in range(len(op2)):
        line2+=op2[line]+ '    '
    line2 = line2.rstrip()
    for line in range(len(dashes)):
        line3+=dashes[line]+ '    '
    line3 = line3.rstrip()
    arranged_problems = line1 + '\n' + line2 + '\n' + line3

    if show == True:
        line4=''
        for line in range(len(result)):
            line4+=result[line] + '    '
        line4 = line4.rstrip()    
        arranged_problems += '\n' + line4
    
    return arranged_problems