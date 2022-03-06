# 06.03.22
# This code will multiply two numbers
# By Yara ElSakka

a = input("please enter the 1st number: ")
b = input("please enter the 2nd number: ")
c = input("please enter the 3rd number: ")
d = input("please enter the 4th number: ")
options = input("1. add, 2. subtract, 3. multiply, 4. divide\n")

a = int(a)
b = int(b)
c = int(c)
d = int(d)
#options = int(options)

if options == "1" :
    answer = a + b + c + d

if options == "2" :
    answer = a - b - c - d

if options == "3" :
    answer = a * b * c * d

if options == "4" :
    answer = a / b / c / d

print("the answer is {}".format(answer))



# end of code