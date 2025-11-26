# q1

# inp = input("enter a string :")
# flag = True
# for i in range(len(inp)):
#     if inp[i] != inp[-i-1]:
#         flag = False
#         break

# if flag:
#     print("yes")
# else:
#     print("no")    



# q2

# lists = [1,2,3,4,5]
# sum=0
# for i in range(len(lists)):
#     sum+=lists[i]
# print(sum)    



# q3

# map -> map(function, iterable)

# lists2 = list(map(int, input("enter list2 : ").split()))
# lists3 = list(map(int, input("enter list3 : ").split()))

# result = lists2 + lists3
# result.sort()

# print(result)



# q4

# numbers = (1, 2, 3, 4, 5, 6)

# even = [] # take list
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# even_tuple = tuple(even) # convert into tuple
# odd_tuple = tuple(odd)

# print(even_tuple)
# print(odd_tuple)



# q5

# students = {}    # empty dictionary

# while True:
#     print("\n---- Menu ----")
#     print("A - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit")

#     choice = input("Enter your choice: ").upper()

#     if choice == "A":
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students[name] = marks
#         print("Student added successfully!")

#     elif choice == "B":
#         name = input("Enter student name to update marks: ")
#         if name in students:
#             marks = int(input("Enter new marks: "))
#             students[name] = marks
#             print("Marks updated!")
#         else:
#             print("Student not found!")

#     elif choice == "C":
#         name = input("Enter student name to search: ")
#         if name in students:
#             print(f"{name} → {students[name]} marks")
#         else:
#             print("Student not found!")

#     elif choice == "D":
#         if len(students) == 0:
#             print("No records available!")
#         else:
#             print("\n--- Student Records ---")
#             for name, marks in students.items():
#                 print(name, "→", marks)

#     elif choice == "E":
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice! Please press A, B, C, D or E.")


# q6

# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# word_len = {}
# for w in words:
#     word_len[w] = len(w)

# print(word_len)    




# q7

# inps = input("enter values: ")
# count = 0
# for i in inps:
#     if i == " ":
#      count+=1
# print(count)



# q8

# list4 = [1,2,3,4]
# list5 = [4,3,5,6]

# comm_elem = set(list4) & set(list5)
# if comm_elem:
#    print("common element")
# else:
#    print("no common element")   


# or

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# # Convert lists to sets
# set1 = set(list1)
# set2 = set(list2)

# # Check if they have no common elements
# if set1.isdisjoint(set2):
#     print("Lists have NO common elements")
# else:
#     print("Lists have common elements")





# q9

# list6 = [5,4,5,4,6,3,2,1]
# seen = set()
# duplicate = set()
# for i in list6:
#     if i in seen:
#         duplicate.add(i) # already seen → duplicate
#     else:
#         seen.add(i) # first time → add to seen

# print(list(duplicate))



# q10


# s = input("Enter a string: ")
# unique_chars = set(s)
# print("Unique characters:", unique_chars)
# print("Count of unique characters:", len(unique_chars))

