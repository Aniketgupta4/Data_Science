# q1

# with open("names.txt","w") as f:

#   for i in range(5):  
#     inp = input("enter 5 user names :")
#     f.write(inp + "\n")



# with open("names.txt","r") as fs:
#   data = fs.read()
#   print(f"names as {data}")

# fs.close()



# q2

# with open("log.txt","a") as f:
#     f.write("program run successfully")


# with open("log.txt","r") as f:
#   data = f.read()
#   print(f"logs are : {data}")

# f.close()

   


# q3


# list = [5, 10, 15, 20, 25]

# new_list = [i for i in list if i > 15]

# print(new_list)




# q4

# import json

# cities = {
#     "delhi":2345672345689,
#     "mumbai":2345678987632454,
#     "bangalore":234567654231324
# }

# with open("cities.json","w") as f:
#     json.dump(cities,f,indent=4)





# with open("cities.json","r") as f:
#     data = json.load(f)


# for city, population in data.items():
#     print(f"{city} → {population}")





# new_city = input("enter city name : ")
# new_population = int(input("enter population :"))

# data[new_city] = new_population


# with open("cities.json","w") as f:
#     json.dump(data,f,indent=4)


# print("City information updated successfully!")






# q5


try:
    with open("sample.txt","r") as f:
       data = f.read()
       print(data)

except FileNotFoundError:
    print("file not found")

