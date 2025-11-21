# conditional statement


# if

age = 20
if age>=18 :
    print("ok")  



# if else

age = 20
if age>=18 :
    print("ok")  
else:
    print("no")


# elif


color = "red"
if color == "red" :
    print("stop")  
elif color == "green":
    print("go")
else :
    print("wait")



# questions on conditionals

# q1

age = int(input("inter age :"))
if age < 18:
    print("child")
elif age >= 13 and age < 18:
    print("teenager")
else:
    print("adult")


# q2

username = input("enter username :")
password = input("enter password :")

if(username == "admin" and password == "pass"):
    print("login")
elif(username != "admin"):
    print("wrong username")
else:
    print("wrong password")



# q3

num = int(input("enter multiple of 5 :"))
if(num % 5 == 0):
    print("multiple of 5")
else:
    print("not a multiple of 5")    


# q4


nums = int(input("enter even or odd number :"))
if(nums % 2 == 0):
    print("even")
else:
    print("odd")   



# nesting

username = input("enter username")
password = input("enter password")

if username=="admin" and password=="pass":
    print("success")
else:
    if username != "admin":
        print("wrong username")
    else:
        print("wrong password")



# match case -> alternate for if elif else

colors = input("enter color :")

match colors:
    case "green":
        print("go")
    case "yellow":
        print("wait")
    case "red":
        print("stop")  
    case _:
        print("wrong color")          



# loops

# print -> hello 5 times
i = 1
while i <= 5:
    print("hello")
    i=i+1



# infinite loop

# while 4>1:
#     print("hello")    



# q1 print number 1 to 5

i = 1
while(i<=5):
    print(i)
    i+=1


# q2 reverse a number    

i = 5
while(i>=1):
    print(i)
    i-=1


# table of n

n = int(input("enter number :"))
i = 1
while i<=10:
    mul = n * i
    print(n,"*",i,"=",mul)
    i+=1


# break 

i = 1
while(i<=10):
    if(i%6==0):
        break
    print(i)
    i+=1
print("loop over")    



# continue

i = 1
while(i<=10):
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1
print("loop over")  



# q1 -> print all odd numbers from 1 to 10

i = 1
while(i<=10):
    if i % 2 == 0:
        i+=1
        continue 
    print(i)
    i+=1



# for

string = "hello"

for i in string:
    print(i)



# q1 check existance 'o' is present or not

string = "hello"
if 'o' in string:
    print("yes")



# range(n) -> so 1 to n-1 

for i in range(5):
    print(i)


# q1 count number of 'i'

word = "artificial intelligence"
count = 0
for i in word:
    if i == "i":
        count+=1
print(count)        
        

#q2 count number of vowels 


word = "artificial"
count = 0
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count+=1
print(count)        
  


# range(start,stop,step)

for i in range(1,10,2):
    print(i)



# q1 -> print sum of 1st n natural number

n = int(input("enter number :"))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)




# functions -> block of code peform specific task

def sum(a,b): # parameters
    s = a + b
    return s

ans = sum(2,4) # arguments
print(ans)



# avg of 3 numbers functions

def cal_avg(a,b,c):
    sum = (a+b+c)/3
    return sum

print(cal_avg(2,4,8))



# defaut value

def sum(a,b=1):
    add = a + b
    return add

print(sum(2))



# lambda function

avg = lambda a,b: (a+b)/2
print(avg(2,4))


# q1 -> factorial of n


def factorial(n):
  fact = 1
  for i in range(1,n+1):
    fact*=i
  return fact  

   

num = int(input("enter number :"))
print(factorial(n)) 














