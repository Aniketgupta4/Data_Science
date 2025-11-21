# q1

# salary = int(input("enter salary :"))
# tax = 0
# if (salary<30000):
#     tax = 0.5 * salary
# elif (salary >= 30000 and salary<70000):
#     tax = 0.15 * salary
# else:
#     tax = 0.25 * salary

# print(tax)

  

# q2


# def even(a,b):
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)

# print(even(2,20))



# q3

# n = int(input("enter number :"))

# def digit(n):
#     while n > 0:
#         num = n % 10
#         print(num)
#         n = n // 10   # / gives float

# digit(n)


# q4


# def countnum(n):
#     count = 0
#     while(n>0):
#         num = n % 10
#         count+=1
#         n = n // 10
#     return count        


# n = int(input("enter number :"))
# c = countnum(n)
# print(c)




# q5

# def sumition(n):
#     sum = 0
#     while(n>0):
#         num = n % 10
#         sum+=num
#         n = n // 10
#     return sum

# add = sumition(1234)    
# print(add)




# q6


# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print(i)



# q7


# def posneg():
#     while True:
#        n = int(input("enter number :"))
#        if(n<0):
#            break
#        elif(n == "quit"):
#            break
#        else:
#            print(n)

# posneg()   




# q8

# a = int(input("enter a :"))
# b = int(input("enter b :"))
# operation = input("enter operaion :")
# def calc(a,b,operation):
#     match operation:
#         case "+":
#             print(a+b)
#         case "-":
#             print(a-b)
#         case "*":
#             print(a*b)
#         case "/":
#             print(a/b)
#         case _:
#             print("invalid")                 

# calc(a,b,operation)




# q9


# inp = int(input("enter number : "))

# def isprime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
    
#     i = 2
#     while i <= n // 2:        # or i <= n/2
#         if n % i == 0:
#             return False
#         i += 1
    
#     return True              

# # function call
# if isprime(inp):
#     print("prime")
# else:
#     print("not prime")



# q10

# def guessgame():
#     secret = 45
#     while True:
#         guess = int(input("enter number :"))

#         if(guess > secret):
#             print("too high")
#         elif(guess < secret):
#             print("too low")
#         else:
#             print("correct")
#             break


# guessgame()










