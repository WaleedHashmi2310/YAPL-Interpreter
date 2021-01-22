import lexer
import parser
import ply.lex as lex
import ply.yacc as yacc
import sys

env = {}

def run(tree):
    global env
    if type(tree) == tuple:
        if tree[0] == '+':
            temp1 = run(tree[1])
            temp2 = run(tree[2]) 
            if(type(temp1) == type(temp2)):
                return temp1 + temp2
            else:
                if((type(temp1)==int or type(temp1)==float) and (type(temp2)==int or type(temp2)==float)):
                    return temp1 + temp2
                else:
                    sys.exit("TypeError")
        elif tree[0] == '-':
            return run(tree[1]) - run(tree[2])
        elif tree[0] == '*':
            return run(tree[1]) * run(tree[2])
        elif tree[0] == '/':
            return run(tree[1]) / run(tree[2])
        elif tree[0] == '^':
            return run(tree[1]) ** run(tree[2])
        elif tree[0] == '%':
            return run(tree[1]) % run(tree[2])
        elif tree[0] == '++':
            if tree[1] in env:
                if type(env[tree[1]]) == int or type(env[tree[1]]) == float:
                    env[tree[1]] = env[tree[1]] + 1
                else:
                    sys.exit("TypeError")
                                    
            else:
                sys.exit("Variable does not exist")
        elif tree[0] == '--':
            if tree[1] in env:
                if type(env[tree[1]]) == int or type(env[tree[1]]) == float:
                    env[tree[1]] = env[tree[1]] - 1
                else:
                    sys.exit("TypeError")
                                    
            else:
                sys.exit("Variable does not exist")
        elif tree[0] == 'var':
            if tree[1] in env:
                return env[tree[1]]
            else:
                sys.exit("Variable does not exist")
        elif tree[0] == 'minus':
            if tree[1] in env:
                return -env[tree[1]]
        elif tree[1] == '=':
            if tree[2] not in env:
                temp = run(tree[3])
                if tree[0] == 'int' and type(temp) == int:
                    env[tree[2]] = temp
                elif tree[0] == 'float' and type(temp) == float:
                    env[tree[2]] = temp
                elif tree[0] == 'string' and type(temp) == str:
                    env[tree[2]] = temp
                elif tree[0] == 'char' and type(temp) == str:
                    env[tree[2]] = temp
                elif tree[0] == 'bool' and type(temp) == bool:
                    env[tree[2]] = temp
                elif tree[0] == 'list':
                    if temp == None:
                        if tree[2] not in env:
                            env[tree[2]] = []
                        else:
                            sys.exit("RedeclarationError")
                    else:
                        if tree[2] not in env:
                            lst1 = []
                            lst1 = temp             
                            final_list = []
                            while (type(lst1) == list):
                                temp = lst1[0]
                                final_list.append(temp)
                                lst1 = lst1.pop()
                            final_list.append(lst1)
                            env[tree[2]] = final_list                                   
                        else:
                            sys.exit("RedeclarationError")
                else:
                    sys.exit("TypeError")
                    
            else:
                sys.exit("RedeclarationError")
                
        elif tree[0] == '=':
            if tree[1] not in env:
                sys.exit("Variable does not exist")
            else:
                if type(run(tree[2])) == type(env[tree[1]]):
                    env[tree[1]] = run(tree[2])
                else:
                    sys.exit("TypeError")
                    
        elif tree[0] == 'not':
            temp = run(tree[1])
            if type(temp) == bool:
                return not temp
            else:
                sys.exit("TypeError")
                

        elif tree[1] == 'and':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if type(temp1) == bool and type(temp2) == bool:
                return temp1 and temp2
            else:
                sys.exit("TypeError")
                

        elif tree[1] == 'or':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if type(temp1) == bool and type(temp2) == bool:
                return temp1 or temp2
            else:
                sys.exit("TypeError")
                

        elif tree[1] == '==':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if type(temp1) == type(temp2):
                if temp1 == temp2:
                    return True
                else:
                    return False
            elif temp1 == True and temp2 == 1:
                return True
            elif temp1 == True and temp2 == 0:
                return False
            elif temp1 == False and temp2 == 0:
                return True
            elif temp1 == False and temp2 == 1:
                return False
            else:
                sys.exit("TypeError")
                

        elif tree[1] == '!=':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if type(temp1) == type(temp2):
                if temp1 != temp2:
                    return True
                else:
                    return False
            elif temp1 == True and temp2 == 1:
                return False
            elif temp1 == True and temp2 == 0:
                return True
            elif temp1 == False and temp2 == 0:
                return False
            elif temp1 == False and temp2 == 1:
                return True
            else:
                sys.exit("TypeError")
                

        elif tree[1] == '>':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if (type(temp1) == int and type(temp2) == int) or (type(temp1) == float and type(temp2) == float):
                if temp1 > temp2:
                    return True
                else:
                    return False
            else:
                sys.exit("TypeError")  
                

        elif tree[1] == '<':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if (type(temp1) == int and type(temp2) == int) or (type(temp1) == float and type(temp2) == float):
                if temp1 < temp2:
                    return True
                else:
                    return False
            else:
                sys.exit("TypeError")
                

        
        elif tree[1] == '>=':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if (type(temp1) == int and type(temp2) == int) or (type(temp1) == float and type(temp2) == float):
                if temp1 >= temp2:
                    return True
                else:
                    return False
            else:
                sys.exit("TypeError")  
                

        elif tree[1] == '<=':
            temp1 = run(tree[0])
            temp2 = run(tree[2])
            if (type(temp1) == int and type(temp2) == int) or (type(temp1) == float and type(temp2) == float):
                if temp1 <= temp2:
                    return True
                else:
                    return False
            else:
                sys.exit("TypeError")   
                   

        elif tree[0] == ',':
            l1 = []
            l1.append(run(tree[1]))
            l1.append(run(tree[2]))
            return l1
    
        elif tree[0] == 'print':
            rcvd = run(tree[1])
            if type(rcvd) == list:
                final_str = ""
                res = any(isinstance(sub, list) for sub in rcvd)
                if res == True:
                    final_list2 = []
                    while (type(rcvd) == list):
                        temp = rcvd[0]
                        final_list2.append(temp)
                        rcvd = rcvd.pop()
                    final_list2.append(rcvd)
                    for x in range(len(final_list2)):
                        if x < len(final_list2)-1:
                            final_str = final_str + str(final_list2[x]) + " "
                        else:
                            final_str = final_str + str(final_list2[x])
                    print(final_str)
                else:
                    for x in range(len(rcvd)):
                        if x < len(rcvd)-1:
                            final_str = final_str + str(rcvd[x]) + " "
                        else:
                            final_str = final_str + str(rcvd[x])
                    print(final_str)
            else:
                print(rcvd)

        elif tree[0] == 'print_var':
            if tree[1] in env:
                print(env[tree[1]])
            else:
                sys.exit("Variable does not exist")

        elif tree[0] == 'slice':
            if tree[1] in env and type(env[tree[1]]) == list:
                temp = env[tree[1]]
                return str(temp[slice(tree[2], tree[3])])
            else:
                sys.exit("List does not exist")

        elif tree[0] == 'push':
            temp = tree[2]
            if tree[1] in env and type(env[tree[1]]) == list:
                if (type(tree[2]) == int) or (type(tree[2]) == float) or (type(tree[2]) == bool) or (type(tree[2]) == str):
                    env[tree[1]].append(tree[2])
                elif temp[1] in env:
                    env[tree[1]].append(env[temp[1]])
                else:
                    return "PushError"
            else:
                sys.exit("List does not exist")

        elif tree[0] == 'index':
            if tree[1] in env and type(env[tree[1]]) == list:
                temp = env[tree[1]]
                ind = tree[2]
                if (ind > len(temp)-1) or (ind<0):
                    sys.exit("IndexOutofBoundsError")
                else:
                    return temp[ind]
            else:
                sys.exit("List does not exist")
        
        elif tree[0] == 'pop':
            if tree[1] in env and type(env[tree[1]]) == list:
                temp = env[tree[1]]
                ind = tree[2]
                if (ind > len(temp)-1) or (ind<0):
                    sys.exit("IndexOutofBoundsError")
                else:
                    popped = temp.pop(ind)
                    return popped
            else:
                sys.exit("List does not exist")

        elif tree[0] == 'dowhile':
            run(tree[1])
            variable = tree[1][2]
            while(run(tree[4]) == True):
                run(tree[2])
                run(tree[3])
            del env[variable]
    else:
        return tree

myLexer = lex.lex(module=lexer)
myParser = yacc.yacc(module = parser)

filename = sys.argv[1]
filepath = "test_cases/" + filename
file1 = open(filepath, errors = 'ignore')
for lines in file1:
    myLexer.input(lines)
    parse_tree = myParser.parse(lines, lexer=myLexer)
    x = run(parse_tree)
    if x == None:
        continue
    else:
        print(x)
