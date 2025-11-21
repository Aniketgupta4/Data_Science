
# assignment

# q1

name = input("enter name : ")
age = int(input("enter age : "))
print("hello " , name , ", you are ", age , " years old!")


# q2

num11 = int(input("enter num1 : "))
num22 = int(input("enter num2 : "))

sums = num11 + num22
diff = num11 - num22
prod = num11 * num22
quo = num11 / num22
print(sums , diff , prod , quo)


# q3

num111 = int(input("enter num1 : "))
num222 = int(input("enter num2 : "))
num333 = float(input("enter num1 : "))

avgs = float((num111+num222+num333)/3)
print(avgs)




# q4

numss = "45"
print(type( int(numss)))
print(type(float(numss)))
print(type(str(numss)))



# q5

print(10+3*2**2)



# q6

s = 2
t = 4
temp = s
s = t
t = temp
print(s,t) 



# q7

cel = float(input("enter temp :"))
fah = (cel * (9/5)) + 32
print(fah)



# q8

rad = float(input("enter radius : "))
area = 3.14 * rad * rad
print(area)


# q9

p = float(input("enter p : "))
r = float(input("enter r : "))
t = float(input("enter t : "))

si = (p * r * t) / 100

print(si)



# q10


num = float(input("Enter a decimal number : "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part =", integer_part)
print("Fractional part =", fractional_part)


