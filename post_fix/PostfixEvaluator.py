#Qiana Pierre 09/20/2020 ASSIGNMENT 4
#Description:  This assignment a program that evaluates postfix arithmetic expressions
#involving integers and ​+, - *, / operations.
# Attribution for any sources:  Fatma, Tayloe

import sys # library that coordinates with operating system
#import process as process


def main():
    filename = sys.argv[1] # get the input file name
    fi = open(filename, "r") # open file in read mode
    line = fi.readline() # read one line from the file
    # line = ["3\n","4\n","*\n","2\n","5\n","+\n","-\n","4\n","*\n","2\n","/\n"]


    while line != '':
        line2 = []
        line3 = []
        sum  = 0
        line2 = line.split()
        for i in range(len(line2)): 
            if line2[i] == "-" : #if subtraction is selected 
                sum = int(line3[len(line3) - 2]) - int(line3[len(line3) - 1])
                del line3[len(line3)- 2]
                del line3[len(line3)- 1]
                line3.append(sum)
            elif line2[i] == "+": # if addition is selected 
               sum = int(line3[len(line3) - 2]) + int(line3[len(line3) - 1])
               del line3[len(line3) - 2]
               del line3[len(line3)- 1 ]
               line3.append(sum)
            elif line2[i] == "*": #if multiplication is selected 
               sum = int(line3[len(line3) - 2]) * int(line3[len(line3) - 1])
               del line3[len(line3) - 2]
               del line3[len(line3)- 1 ]
               line3.append(sum)
            elif line2[i] == "/": #if division is selected 
               sum = int(line3[len(line3) - 2]) / int(line3[len(line3) - 1])
               del line3[len(line3) - 2]
               del line3[len(line3)- 1 ]
               line3.append(sum)
            else:
                line3.append(line2[i])

        print(line[ :len(line)-1],"results in",line3[0]) # print everything except \n
        # get the next line # close the file after it’s all been read main()
        line = fi.readline()

    fi.close() # close the file after it’s all been read main()

main()
