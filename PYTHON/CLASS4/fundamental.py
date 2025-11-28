# oops

# classes and objects

class student:
    id = 1234
    name = "aniket"
    subject = "python"

# default constructor
    def __init__(self):
        print("constructor is called")


s1 = student()

# memory address access
print(s1) 

# value access
print(s1.id,s1.name,s1.subject)

print(type(s1))





# methods -> only 1 init method per class

class students:

# parameterized constructor
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

# instance methods
    def __get_cgpa__(self):
        return self.cgpa    

s1 = students("aniket",9.4)
s2 = students("ani",9.2)

print(s1.name,s1.cgpa)

print(s2.__get_cgpa__())





# attributes -> 2 -> class and instance

class stu:
    # class attribute
    college_name = "apna college"

    def __init__(self,name):
        self.name = name

s1 = stu("aniket")

print(s1.name)
print(stu.college_name)
# or both valid for class attributes
print(s1.college_name)




# highest priority of instance attribute

class stud:
    # class attribute
    college_name = "apna college"

    def __init__(self,name,college_name):
        self.name = name
        # highest priority of instance attribute
        self.college_name = college_name

s1 = stud("aniket","srit")


print(s1.college_name)





# methods type -> instance

class pc:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    # instance method
    def get__info__(self):
        print(f"laptop has {self.ram} & {self.storage} & {self.storage_type}") 

s1 = pc("8","hdd")


print(s1.get__info__())






# methods type -> class

class pcs:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    # class method -> only access class attributes
    def get_storage_type(cls):
        print(f"{cls.storage_type}") 

    # instance method
    @classmethod
    def get__info__(self):
        print(f"laptop has {self.ram} & {self.storage} & {self.storage_type}") 

s1 = pcs("8","hdd")


print(s1.get_storage_type())
# or
print(pcs.get_storage_type())





# methods type -> static

class pcs:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    # class method -> only access class attributes
    def get_storage_type(cls):
        print(f"{cls.storage_type}") 

    # instance method
    @classmethod
    def get__info__(self):
        print(f"laptop has {self.ram} & {self.storage} & {self.storage_type}") 

    
    # static method
    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount * price / 100)
        print(f"{final_price}")
    

s1 = pcs("8","hdd")

s1.calc_discount(40_000,10) 






# q1 product store


class product:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        count+=1

    def get_info(self):
        print(f"price is {self.name} is rs.{self.price}")

    
    @classmethod
    def get_count(cls):
        print(f"total products is : {cls.count}")


    @staticmethod
    def calc_discount(price,discount):
        print(f"discounted price = {price - (price*discount/100)}")


p1 = product("phone",10_000)
p2 = product("laptop",100_000)

p1.get_info()

product.get_count()

p1.calc_discount(10_000,12)
# or
p1.calc_discount(p1.price,12)







# OOPS 

# ENCAPSULATION

class bankaccount:
    def __init__(self,name,balance):
        self.name = name # public
        self._balance = balance #protected by ._
                            # by .__ become private
 
acc1 = bankaccount("aniket",100_000)

print(acc1.name,acc1._balance)




# access private value by getters setters

class bankaccount:
    def __init__(self,name,balance):
        self.name = name # public
        self.__balance = balance # by .__ become private
                            
 
    def get_balance(self): # getters
        return self.__balance
    
    def set_balance(self,newbalance):
        self.__balance = newbalance
    
acc1 = bankaccount("aniket",100_000)

acc1.set_balance(200_000) # set value by setter
print(acc1.name,acc1.get_balance()) #access private values






# inheritance


class employee:
    start_time = "10"
    end_time = "4"

class admin(employee):
    def __init__(self,role):
        self.role = role


class accountant(admin):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary
        


t1 = accountant(25_0000,"math")
print(t1.start_time,t1.end_time,t1.role,t1.salary)            




# multiple level inheritance

class teacher:
    def __init__(self,salary):
        self.salary = salary

class student:
      def __init__(self,gpa):
        self.gpa = gpa     

class ta(teacher,student):
    def __init__(self,salary,gpa,name):
        super.__init__(salary)
        student.__init__(self,gpa)
        self.name = name

t1 = ta(10_000,9.4,"yes")
print(t1.name,t1.gpa,t1.gpa,t1.salary)        








# abstraction


from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(animal):
    def make_sound(self):
        print("roar")    


class Cow(animal):
    def make_sound(self):
        print("moo")  



lion = Lion()
lion.make_sound()





# polymorphism


# function overriding

class employee:
    def get_designation(self):
        print("employee")


class Teacher:
    def get_designation(self):
        print("teacher")


t1 = Teacher()
t1.get_designation()





# duck type -> same name de shakte hai function ko in different class

=






