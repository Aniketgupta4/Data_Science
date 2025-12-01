# q1


# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_name = account_number
#         self.owner_name = owner_name
#         self.balance = balance


#     def deposit(self,amount):
#         self.balance += amount
#         print(f"{amount} deposited successfully")


#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdraw successfully")


#     def check_balance(self):
#         print(f"current balance: {self.balance}")


# acc = BankAccount(101,"alice",234567)

# acc.deposit(2000)
# acc.withdraw(3000)
# acc.check_balance()

        



# q2


# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = []


#     def add_review(self,review):
#         self.list_of_reviews.append(review)
#         print("review added successfully")  


#     def count_reviews(self):
#         return len(self.list_of_reviews)


#     def display_reviews(self):
#         if len(self.list_of_reviews) == 0:
#             print("no reviews available") 
#         else:
#             print("reviews:")
#             for r in self.list_of_reviews:
#                 print("->",r)




# b = Book("Harry Potter", "J.K. Rowling")

# b.add_review("Amazing story!")
# b.add_review("Loved the characters.")
# b.add_review("Best fantasy novel.")

# print("Total reviews:", b.count_reviews())
# b.display_reviews()







# q3



# class Student:
#     def __init__(self):
#         self.__name = None
#         self.__roll_no = None
#         self.__marks = None

#     def set_name(self, name):
#         if name is None or name.strip() == "":
#             print("Name cannot be empty!")
#         else:
#             self.__name = name

#     def set_roll_no(self, roll_no):
#         if roll_no < 1 or roll_no > 100:
#             print("Roll number must be between 1 and 100!")
#         else:
#             self.__roll_no = roll_no

#     def set_marks(self, marks):
#         if marks < 0:
#             print("Marks cannot be negative!")
#         else:
#             self.__marks = marks

#     def get_name(self):
#         return self.__name

#     def get_roll_no(self):
#         return self.__roll_no

#     def get_marks(self):
#         return self.__marks





# q4


# class shape:
#     def area(self):
#         return "Area not defined for generic shape"
    

# class circle(shape):  
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# class rectangle(shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.height * self.width        

    

# class Triangle(shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# c = circle(5)
# r = rectangle(4, 6)
# t = Triangle(8, 5)

# print("Circle Area =", c.area())
# print("Rectangle Area =", r.area())
# print("Triangle Area =", t.area())




# q5


# class vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model


# class car(vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)  # inherit from base class
#         self.seats = seats


# class Bike(vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)   # inherit from base class
#         self.engine_cc = engine_cc


# c = car("Toyota", "Fortuner", 7)
# b = Bike("Yamaha", "R15", 155)

# print(f"Car: {c.brand} {c.model}, Seats = {c.seats}")
# print(f"Bike: {b.brand} {b.model}, Engine = {b.engine_cc}cc")





# q6


# from abc import ABC , abstractmethod

# class employee(ABC):
#     def __init__(self,name):
#         self.name = name

    
#     @abstractmethod
#     def calculate_salary(self):
#         pass 



# class FullTimeEmployee(employee):
#     def __init__(self, name, monthly_salary):
#         super().__init__(name)
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.monthly_salary



# class PartTimeEmployee(employee):
#     def __init__(self, name, hours_worked, rate_per_hour):
#         super().__init__(name)
#         self.hours_worked = hours_worked
#         self.rate_per_hour = rate_per_hour

#     def calculate_salary(self):
#         return self.hours_worked * self.rate_per_hour




# class Intern(employee):
#     def __init__(self, name, stipend):
#         super().__init__(name)
#         self.stipend = stipend

#     def calculate_salary(self):
#         return self.stipend



# f = FullTimeEmployee("Alice", 50000)
# p = PartTimeEmployee("Bob", 80, 300)
# i = Intern("Charlie", 8000)

# print("Full Time Salary =", f.calculate_salary())
# print("Part Time Salary =", p.calculate_salary())
# print("Intern Salary =", i.calculate_salary())





# 7


# class person:
#     def __init__(self,name,age=None,address=None):
#         self.name = name
#         self.age = age
#         self.address = address

#     def show_details(self):
#          print(f"Name: {self.name}")
#          print(f"Age: {self.age}" if self.age is not None else "Age: Not provided")
#          print(f"Address: {self.address}" if self.address is not None else "Address: Not provided")    

   
    # or


    # if self.age is not None:
    #   print(f"Age: {self.age}")
    # else:
    #   print("Age: Not provided")



# p1 = person("Aniket")                               # name only
# p2 = person("Rohan", 22)                            # name + age
# p3 = person("Sujal", 20, "Jabalpur, MP")            # name + age + address

# p1.show_details()
# print()
# p2.show_details()
# print()
# p3.show_details()





# q8


# class player:
#     player_count = 0  # class variable

#     def __init__(self,name,level):
#         self.name = name    # instance variable
#         self.level = level  # instance variable

#         player.player_count += 1   # count number of objects created


#     def show(self):
#         print(f"Player Name: {self.name}, Level: {self.level}")    




# p1 = player("Aniket", 10)
# p2 = player("Rohan", 15)
# p3 = player("Sujal", 8)

# p1.show()
# p2.show()
# p3.show()

# print("Total players created =", Player.player_count)




# q9


# class Herbivore:
#     def eat_plants(self):
#         print("Eats plants")

# class Carnivore:
#     def eat_meat(self):
#         print("Eats meat")

# class Omnivore:
#     def eat_both(self):
#         print("Eats both plants and meat")


# class Bear(Herbivore, Carnivore, Omnivore):
#     def feature(self):
#         print("Bear is a strong animal")



# b = Bear()
# b.feature()
# b.eat_plants()
# b.eat_meat()
# b.eat_both()





# 10) MINI PROJECT -> OOP CHAT SYSTEM



# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1   # simple counter

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)  # Show message to all users

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()


# ---------------------------------------
# Example Usage
# ---------------------------------------
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()
