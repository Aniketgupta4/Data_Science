# string

word = "python"
word1 = "learning"

print(word)

# length
print(len(word))

# concatenation
print(word + word1)

# particular value access
print(word[2])



# slicing 

print(word[2:5])

# default value of last is len(str)
print(word[2:]) 

# default value of first is 0
print(word[:5])

# -ve indexing
print(word[-4:-2])



# string formatting 

# way1 -> format function

a = 5
b = 10
sum = a + b

# way a -> normal formatting
print("sum is {}".format(sum))
print("sum is {} & {} is {}".format(a,b,sum))


# way b -> index based formatting
print("sum is {1} & {0} is {2}".format(a,b,sum))


# way c -> value based formatting
print("sum is {a} & {b}".format(a=2,b=4))




# way2 -> fstrings

print(f"sum of {a} & {b} is {a+b}")

print(f"avg of {a} & {b} is {(a+b)/2}")






#  Lists -> mutable -> particular index value changes

mark = [44,33,55,34,77,4,24,87]
print(mark)

# indexing -> 0 based
print(mark[2])

# length 
print(len(mark)) 
 
# change values
mark[2] = 50
print(mark)


# type -> list

print(type(mark))


# any data type value in list

marks = [1,2,1.2,"sham",'a']
print(marks)


# slicing

print(marks[0:5])

# default 0
print(marks[:5]) 

print(marks[2:])

# -ve indexing
print(marks[-4:-2])



# lists methods

lists = [1,2,4,3]


lists.append(5)
print(lists)

lists.insert(1,1.5)
print(lists)

lists.sort()
print(lists)

lists.sort(reverse=True)
print(lists)

lists.reverse()
print(lists)



# loops with lists

list1 = [3,2,5,1,6]

for val in list1:
   print(val) 



# q1 -> find index of 10 -> linear search

l1 = [1,2,3,10,4]
val = 10
idx = 0
for i in l1:
   if i == val:
      print(f"{val} found at idx={idx}")
      break
   else:
      print("not found")   
   idx+=1




# Tuples

t = (2,1,3,4,6)

print(t)

# type
print(type(t))

# length
print(len(t))


t1 = (4,3,2,5,2.4,"shan",'a')
print(t1)


# slicing

print(t1[0:4])


# loop 

for i in t1:
   print(i)


# q1 -> sum of tuple values

t2 = (4,3,2,5,2.4,8)
sum = 0
for i in t2:
   sum+=i
print(sum)


# methods of tuples

# index -> return first occurance of value
t4 = (5,4,3,2,3,4,2,4,5,2)
print(t4.index(2))

# count prints

print(t4.count(2))





#  Dictionary


dict = {
   "name":"aniket",
   "age":20,
   "roll":24,
#    dic under dict
   "subject":["math","science"],
#    valid
   3.14:"pi"
}

print(dict)
print(type(dict))
print(len(dict))
print(dict["name"])



# methods of dictionary

# print all keys of dictionary
print(dict.keys())

# print all values of dictionary
print(dict.values())

# print (key , val)
print(dict.items())

# print value according to key
print(dict.get("name"))
print(dict["name"])


# update 
dict.update({
   "city":"delhi"
})
print(dict)





# Sets in python

sets = {1,2,1,1,1,1,4,5,6,7}
print(sets)
print(type(sets))
print(len(sets))

sets.add(10)
print(sets)



# methods in sets

s = {1,2,3,54,1}
s1 = {5,4,32,2,11}

s.add(245)
print(s)

s.remove(2)
print(s)

s.pop()
print(s)

s.clear()
print(s)

s.union(s1)
print(s1)

s.intersection(s1)
print(s1)






















