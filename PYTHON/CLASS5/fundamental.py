# file i/o

# 1) read -> r
f = open("sample.txt","r")

data = f.read()
# data = f.readline()

print(type(data))
print(data)

f.close()





# modes of files

# 2) write -> w

f = open("sample1.txt","w")
f.write("ni na")
f.close()



# 3) create new and open -> x


# f = open("sample2.txt","x")
# f.write("ni na")
# f.close()



# 4) append at end -> a

f = open("sample1.txt","a")
f.write("yes yr sahi tha")
f.close()



# 5) binary mode -> b -> rt wt wb rb


# f = open("sample5.txt","rt")
# f.write("ni na")
# f.close()


# 6) + -> r+ w+ a+

f = open("sample5.txt","w+")
f.write("ni na")
print(f.read())
f.close()





# with keyword


with open("sample5.txt","r") as files:
    data = files.read()
    print(files.read())
    print(len(data))




# delete files

# import os

# os.remove("sample5.txt")






# q1 -> word search
# make a file p1.txt


data = True

with open("p1.txt","r") as f:
   while data: 
      data = f.readline()
      
      if("python" in data):
         print("word found")
         break
      
      print(data)





# exception handling

try:
   x = int(input("enter x: "))
   ans = 10 / x

except ZeroDivisionError:
   print(f"division by 0 is not allowed")

except ValueError:
   print(f"invalid input")

else:
   print(f"ans = {ans}")

finally:
   print("done")




# list comprehension

sq = [i*i for i in range(6)]
print(sq)


sq = [i*i for i in range(6) if i%2!=0]
print(sq)



# q1 -> num < 0 make it 0

nums = [-2,-3,3,4,-1,7]

nums = [0 if val < 0 else val for val in nums]
print(nums)



# q2 -> uppercase 

words = ['a','b','c','d']
w = [val.upper() for val in words]
print(w)





# json 

import json

# this both for strings 

# jsonstring to pyobj

json_str = '{"name":"aniket","age":24}'
py_obj = json.loads(json_str)
print(py_obj)



# pyobj to jsonstring

py_obj = {
   "name":"aniket",
   "age":25
}

py_str = json.dumps(py_obj)
print(py_str)





# -> create data.json file -> this is for json file

# for read
with open("data.json","r") as f:
   py_obj = json.load(f)
   print(py_obj)


# for write
d = {
   "name":"shan",
   "age":26
}

with open("data.json","w") as f:
   json.dumps(d,f,indent=4,sort_keys=True)


