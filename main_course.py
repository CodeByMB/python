#--------------------#
#---Math Operators---#
#--------------------#
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)  #Gives back a float

#Advanced
print(10 ** 5)  #To the power of.
print(10 // 3)  #Floor divide it floors/trunc the number so it just removes all numbers after the comma.
print(7 % 2)  #Gives back the remainder.

print(5 + 5 * 2)  # Does standard math first, so multiply before addition.
print((5 + 5) * 2)  #This does 5 + 5 first.

num1 = 10
num2 = 5

#Exact same thing but shorter!
num1 = num1 + 5  #long version
num1 += 5
num1 -= 5
num1 *= 5
num1 /= 5

#Comparison Operators:
print(10 > 5)  #Greater than
print(10 < 5)  #Less than

#----------------#
#---Exercise 1---#
#----------------#
# Get the average of the numbers from 1 to 7
print((1 + 2 + 3 + 4 + 5 + 6 + 7) / 7)

#---------------------------------------------------------------------------------------#
#----------------#
#--- Variables---#
#----------------#

#var names are written in snake case (first_name = "Maikel")

result = 10 + 5
print(result)

result2 = result / 2
print(result2)

#----------------#
#---Exercise 2---#
#----------------#
create_a_variable = 20
create_a_variable += 20
print(create_a_variable)

#---------------------------------------------------------------------------------------#
#----------------#
#--- Functions---#
#----------------#
var_name = 'Hello'
print(len(var_name))

#absolute
print(abs(-50))


def my_function(text):
    print(text)


my_function("This is my function")

#----------------#
#---Exercise 3---#
#----------------#
#MAX get's the highest value, in this case 453
my_list = [12, 35, 453, 22, 1]

print(max(my_list))
print(min(my_list))

#---------------------------------------------------------------------------------------#
#----------------#
#-----Methods----#
#----------------#
#.upper() makes it all Upper case
#.lower() makes it all lower case
#.title() makes the first letter Capital the rest lower case
#.strip() Return a copy of the string with leading and trailing whitespace removed.
#.isalpha() gives true or false if the inhoud is within the alphabet (A space is not in there so returns false)
test = 'A word'.upper()
print(test)

#.lower()
test2 = 'A word 2'
print(test2.lower())

#.title() & .strip()
username = 'JOhn SmIthXX'.title().strip('x')
print(username)

#print(dir(username))

#.isalpha()
print(username.isalpha())

#----------------#
#---Exercise 4---#
#----------------#
#Find a method that replaces puppies with kittens
exersice_string = 'I like puppies'.replace('puppies', 'kittens')

print(exersice_string)

#---------------------------------------------------------------------------------------#
#----------------#
#-----Return-----#
#----------------#

test_variable = len('A word'.upper().replace('A', 'X'))

print(test_variable)

#---------------------------------------------------------------------------------------#
#----------------#
#----comments----#
#----------------#

#These are  single line comments ;) 

'''
This is a multiline comment
print(test_variable)
'''

#---------------------------------------------------------------------------------------#
#----------------#
#----Numbers----#
#----------------#

#int
my_first_int = 1

#float
my_first_float = 1.4
my_second_float = 1.8

#Convert to float
my_first_int = float(my_first_int)

#Convert to int (trunc not rounding)
my_first_float = int(my_first_float)

print(my_first_int)
print(my_first_float)
print(round(my_second_float))

#---------------------------------------------------------------------------------------#
#----------------#
#----Strings----#
#----------------#

#f strings
test_string = 'test 1'
test_string2 = "test 2"
# how to get values into strings 
name = 'Bob'
age = 40

greeting_string = 'Hello {one}, you are {two} years old'.format(one=name, two=age)

greeting_string_better = f'Hello {name}, you are {age + 10} years old'

print(greeting_string_better)

#---------------------------------------------------------------------------------------#
#----------------#
#----List & Tuples----#
#----------------#

# list + functions + methods 
my_list = [1, 2, 3, 4.5, 'word']
print(len(my_list))
my_list.reverse()
my_list.append(10)
print(my_list)

# tuple 
my_tuple = (1, 2, 3, 1.45, 'Word', [7, 8, 9])
#KAN NIET TUPLE IS INMUTABLE
#my_tuple.append(10)
#my_tuple.reverse()

# how to pick elements from a tuple or a list -> Indexing or slicing
print(my_list[2])
print(my_tuple[5][0])
print(my_tuple[-3])

#---------------------------------------------------------------------------------------#
#----------------#
#----slicing----#
#----------------#

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

negative_slicing = test_list[-1:4:-1]

default_slicing = test_list[::]

# exercise: 
# start from 8 and go to 2, pick every second element
solution = test_list[7:0:-2]
# print(solution)

# tuple slicing
test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#from : to : steps
print(test_tuple[0:10:2])

#---------------------------------------------------------------------------------------#
#----------------#
#----unpacking----#
#----------------#

a, b = (10, 5)
print(a)
print(b)

c, d = [20, 'Hello']
print(c)
print(d)

health, energy, weapon = 100, 50, 'Sword'
print(weapon)

# exercise
value_1 = 10
value_2 = 'test'
#switch the values of the two variables
value_1, value_2 = value_2, value_1
print(value_1)

#---------------------------------------------------------------------------------------#
#----------------#
#----strings tuples & lists----#
#----------------#
test_string = 'this is a test'
test_list = [1, 2, 3, 4]

exercise = str(test_list).strip('[').strip(']').replace(',', '').replace(' ', '')
print(exercise)

#---------------------------------------------------------------------------------------#
#----------------#
#----Dictionaries----#
#----------------#

#It always has a Key and value pair
#'key':'value', 1:[1,2,3}
#You can't duplicate keys, it must be unique Key
test_dict = {'A': 123, 'B': [1, 2, 3], 1: True}
print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())
print(len(test_dict))

#How to call a Key/Value
print("Get value from A:", test_dict['A'])
print("Get value from B:", test_dict['B'])
print("Get value from 1:", test_dict[1])

#----------------#
#----Exercise----#
#----------------#

#Update method to add another key value pair
test_dict.update({"C": 321})
test_dict.update(D='test', E='amazing')
test_dict['F'] = 'Last one'

print(test_dict)

#---------------------------------------------------------------------------------------#
#----------------#
#----Sets----#
#----------------#

#Is like a dictionary expect it only has values no keys
my_set = {1, 2, 3, 4, 4}
print(my_set)
print(len(my_set))
print(len(set(my_set)))

#---------------------------------------------------------------------------------------#
#----------------#
#----Booleans----#
#----------------#

# booleans and numbers 
# print(1 == 10) # True if is equal
# print(1 != 10) # True if is different
# print(not 10 > 10)

# booleans and lists and strings 
# print(1 in (1,2,3))
# print('e' in 'hello')
# print(4 not in [1,2,3])

# data conversion exercise 
# e_dict = {1:'one', 2: 'two', 3:'three'}
# check if a the key 1 exists in the dict
# print(1 in e_dict)

# check if the value 'four' exists in the dict 
# print('three' in e_dict.values())

# booleans by themselves 
# print(not True)

# bool function
print(bool(None))

#---------------------------------------------------------------------------------------#
#----------------#
#----If Statements----#
#----------------#
name = 'Maikel'
if name == "Maikel":
    print("You're amazing")
elif name == "Jan":
    print("lol Jan")
else:
    print("noob")

# give_me_number = int(input('Give me a number: '))

# if give_me_number == 0:
#     print('Zero')
# elif give_me_number % 2 == 0:
#     print(f'{give_me_number} is an even number')
# elif give_me_number % 2 != 0:
#     print(f'{give_me_number} is an odd number')
# else:
#     print('You didnt enter a number')

# combining conditions
# if True and True and False or True:
# 	print('True')

# Exercise 
# money_available = 100
# hungry = False
# bored = True

# check if money_available > 80 and if hungry is true or if bored
# if money_available > 80 and hungry == True or bored == True:
# 	print('eat something fancy!')

# nested if statements
# x = '1'
# if x in ['a','b','1']:
# 	print('a is in the list')

# 	if x.isalpha():
# 		print('it is a letter')

# 	if True:
# 		print('something')

# exercise 
money_available = 100
hungry = True
bored = True
# create a nest if statement that runs of all 3 conditions are true (money > 80 for the first one)
if money_available > 80:
    print('I have enough money!')
    if hungry:
        print('and I am hungry!')
        if bored:
            print('Eat something fancy :)')

#---------------------------------------------------------------------------------------#
#----------------#
#----Match case----#
#----------------#

match name:
    case "Maikel":
        print("You're amazing")
    case "Jan":
        print("lol Jan")
    case _:
        print("noob")  #Default case

# mood = 'bored' 

# match mood:
# 	case 'hungry':
# 		print('get some food')
# 	case 'thirsty':
# 		print('get some water')
# 	case 'tired':
# 		print('get some sleep')
# 	case _:
# 		print('any other mood')

# exercise 
# create a variable with an integer between 1 and 5, call it grade 
# create a match case statement that writes 'very good' when the grade is 1
# and very bad when the grade is 5 (and all other cases in between)
# there should also be some default behaviour if you get an unexpected value

grade = '2'

match grade:
    case 1:
        print('very good!')
    case 2:
        print('good')
    case 3:
        print('okay')
    case 4:
        print('needs improvement')
    case 5:
        print('very bad')
    case _:
        print('Grade not recognized')

match grade:
    case 1:
        print('very good!')
    case 2:
        print('good')
    case 3:
        print('okay')
    case 4:
        print('needs improvement')
    case 5:
        print('very bad')
    case _:
        print('Grade not recognized')
#---------------------------------------------------------------------------------------#
#----------------#
#----While loops----#
#----------------#

#break end the entire while loop
#continue Skips the current iteration

count = 0
while count != 10:
    count += 1
    print(count)
    if count == 5:
        break

print("I'm done counting")

my_count_list = []
counter = 0

while counter <= 100:
    if counter % 2 == 0 and counter != 58:
        my_count_list.append(counter)
    counter += 1

print(my_count_list)
#---------------------------------------------------------------------------------------#
#----------------#
#----For loops----#
#----------------#

# my_list1 = [1, 2, 3, 4, 5, 6, 7]

# # for i in my_list1:
# #     print(i)

# #for i in range
# for i in range(len(my_list1)):
#       print(i)

#exersice
#use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100

practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]

for nested_list in practice_list:
    #print(practice_list)
    for value in nested_list:
        if value >= 100:
            break
        if value < 50 and value >= 10:
            print('Above 10 and below 50: ', value)

#---------------------------------------------------------------------------------------#
#----------------#
#----Flow and linebreak----#
#----------------#

#ternary operator
x = 5

color = 'red' if x < 5 else 'blue'

print(color)


#---------------------------------------------------------------------------------------#
#----------------#
#----Parameters----#
#----------------#

def test_function():
    print('Hello')
    test = 1 + 2
    print(test)


# def calculator(num1, num2):
#     result = num1 + num2
#     print(result)

# test_function()
# calculator(5, 2)

def better_calc(num1, num2, operator):
    if operator == '-':
        result = num1 - num2
        print(f'{num1} - {num2} = {result}')
    elif operator == '+':
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
    else:
        print('Mwah wwah')


better_calc(5, 2, '+')
better_calc(20, 4, '-')


#What if you don't know the number of arguments?
#You can use *args as parameter when you don't know how many arguments will return
# ßß

#List unpacking
def list_unpacking(first, *args, extra):
    print(first)
    print(args)
    print(extra)

    for arg in args:
        print(arg)


#keyword unpacking
def print_more(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key} = {value}')


def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)


# list_unpacking(1, 2, 3, 'HENK', 1, 55, extra = 213)
# print_more(arg1=1, arg2='Test', arg3=3, arg4=[1, 2, 3])
print_even_more(1, 2, 3, 4, 5, 'hello', True, test=1, test2=5)

''' 
In short:
*args are used for unlimited arguments
**kwargs are used for unlimited keyword arguments (Key:value pairs)
'''


def calcu(*args):
    result = sum(args)
    print(result)


calcu(1, 5, 4, 3, 6, 7, 6)
#---------------------------------------------------------------------------------------#
#----------------#
#----Scope----#
#----------------#
''' 
Variables created inside of a function
are only available inside of that function

This is called 'Local scope'

Creating variables outside of the function is the 'Global scope'

Functions are supposed to separate from the rest of the code.
Once the code becomes more complex it is really easy to run out of variable names.

For example with the car, both the battery and the tank might have a 'capacity' variable.
Within each function that is perfectly fine since the local scope.

### Local Scopes inside of a function help to keep things organised ###

Global variables can be accessed in the local scope
But they cannot be changed(or created)

You can move between scopes with parameters,
Global and return but only use it when needed!
'''
a = 10  #Global scope


#Dont use it like this to access global variables.
def test_func():
    global a  #<-- Don't use this :)
    a += 5  #Local scope
    print(a)


test_func()

b = 10

#how you should modify global variables:
# def test_func2(b):
#     b += 2
#     return b
#
# print(test_func2(b))

''' 
Exercise
Create 2 global variables called 'multiplier' and has_calculated
Multiplier should have any integer and has_calculated should be set to the boolean False

Then create a function called multiply_calculator that takes one argument and calculates 
the multiplication of that number
inside of the function multiply the parameter with the global variable multiplier
once the calculation is done set has_calculated to True
store that new number a variable called result and return it.
print the return value of the function.

'''

multiplier = 5
has_calculated = False


def multiply_calculator(nummer1):
    global has_calculated
    has_calculated = True
    result = nummer1 * multiplier
    return result


print(multiply_calculator(10))
print(has_calculated)

#---------------------------------------------------------------------------------------#
#----------------#
#----Lambda functions----#
#----------------#

#Lambda function are single line functions
#example_1: lambda parameter:expression
#example_2: lambda x:x+1   #x is automatically returned.

a = lambda x: x + 1
print(a(10))

simple_calc = lambda a, b: a + b
print(simple_calc(2, 3))

#when will you use a lambda functions
#Some functions want other functions as argument
#For example in the sort([1,3,2,4,5] func.. lambda)

#or for GUI to program the button, on click events will use a lambda func.

#exercise_lambda = lambda numm1: if numm1 > 5: print('hello') else: print('Bye')
exercise_lambda = lambda num1: 'hello' if num1 > 5 else 'Bye'

print(exercise_lambda(3))

#---------------------------------------------------------------------------------------#
#----------------#
#----Documenting functions----#
#----------------#

''' 
Function can get complicated.
So you want to explain it.

You can either add an explainer text (docstring)

You can also hint at what types of data you expect for the parameters and the return value
'''
# def test_func2(b):
#     """Use the docstring and explain your function"""
#     b += 2
#     return b
#
# print(test_func2(b))
# print(test.__doc__)
# help(test)

#---------------------------------------------------------------------------------------#
#----------------#
#----Better for loops----#
#----------------#

# inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]

# for name, number in zip(inventory_names, inventory_numbers):
#     print(name, number)
#
# for index, name in enumerate(inventory_names):
#     print(f'{index}: {name}')
#     if index == len(inventory_names) // 2:
#         print('Halfway done!')

# for index, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
#     print(f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}')

#---------------------------------------------------------------------------------------#
#----------------#
#----List comprehension----#
#----------------#

#example:
#hardway
# my_list1 = []
# for num in range(0, 21):
#     my_list1.append(num)
#
# #short way
# my_list2 = [num for num in range(0,21)]
#
# print(f'List 1: {my_list1}')
# print(f'List 2: {my_list2}')
#
# my_list_comp = [num4 * 2 for num4 in range(0,21)]
# print(f'List 3: {my_list_comp}')
#
# my_list_comp2 = [(num5, num5, num5) if num5 < 20 else 0 for num5 in range(0,31)]
# print(f'List 4: {my_list_comp2}')


# inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]
#
# rep_list = [(name, number) for name, number in zip(inventory_names, inventory_numbers) if number < 25]
# print(rep_list)

#combine list comp

#my code
chess_board = [[(chr(x), y) for x in range(65, 73)] for y in range(8, 0, -1)]
for row in chess_board:
    print(row)

#course code:
chess_board1 = [[f'{letter}{num}' for num in range(1, 9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board1:
    print(row)

#Other comprehension
#dict_comp = (num:num for num in range(10))
dict_comp = {num: num for num in range(100)}
print(f'dict Comp: {dict_comp}')

#set_comp = {num for num in range(10)}
set_comp = {num for num in range(100)}
print(f'Set Comp: {set_comp}')

#tuple_comp = tuple(num for num in range(10))
tuple_comp = tuple(num for num in range(100))
print(f'Tuple Comp: {tuple_comp}')

exercise_comp = {letter: [1, 2, 3, 4, 5] for letter in 'ABCDE'}
print(exercise_comp)
#---------------------------------------------------------------------------------------#
#----------------#
#----Sorting data----#
#----------------#

list1 = [4, 2, 3, 1, 5]
print(sorted(list1, reverse=True))

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]


def sort_func(item):
    return item[1]


print(sorted(list2, key=sort_func))
print(sorted(list2, key=lambda item: item[1]))


#---------------------------------------------------------------------------------------#
#----------------#
#----Map and Filter----#
#----------------#

#Can use list comp instead of this.

#---------------------------------------------------------------------------------------#
#----------------#
#----File handling----#
#----------------#

#Open and close manually
# file = open('text.txt')
# print(file.read())
# file.close()
#
# #Open and close automatically
# with open('text.txt') as file:
#     #print(file.read())
#     for line in list(file):
#         print(line)

#add text to some file
# with open('text.txt', 'a') as file:
#     file.writelines('\nXXXXXXXXXHello WorldXXXXXXXXXXX')
#
# #New file:
# with open('tree.txt', 'w') as file:
#     file.writelines('     X     \n'
#                     '    XXX    \n'
#                     '   XXXXX   \n'
#                     '     X     \n')
#---------------------------------------------------------------------------------------#
#----------------#
#----Deleting data----#
#----------------#

# a = 1
# del a

# a = [1,2,3]
#
# # del a[1]
# #
# # print(a)
#
# a.remove(3)
# print(a)
# a.pop(-1)
# print(a)

#---------------------------------------------------------------------------------------#
#----------------#
#----Objects & Classes----#
#----------------#
#A object is the product from a class.
#The class is the blueprint for the object.
#In the object we specify the keys
#And in the class we will specify the values (like how much health)

# class Monster:
#     health = 90
#     energy = 40
#
#     # A method always needs at least 1 arg
#     def attack(self, amount):
#         print('The monster has attacked!')
#         print(f'The monster used 10 energy')
#         monster.energy -= 10
#         print(f'{amount} damage was dealt')
#
#     def move(self, speed):
#         print(f'Moved with a speed of {speed}')
#
# monster = Monster()
# monster.attack(40)
# monster.move(20)
#
# monster2 = Monster()
# monster2.attack(20)

#---------------------------------------------------------------------------------------#
#----------------#
#----Dunder methods----#
#----------------#

# class Monster:
#
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy
#         print('The monster was created')
#
#     #gives back the amount of health
#     def __len__(self):
#         return self.health
#
#     #gives back the amount of energy
#     def __abs__(self):
#         return self.energy
#
#     def __str__(self):
#         return f'A monster with health {self.health} and energy {self.energy}'
#
#     # A method always needs at least 1 arg
#     def attack(self, amount):
#         print('The monster has attacked!')
#         print(f'The monster used 10 energy')
#         self.energy -= 10
#         print(f'{amount} damage was dealt')
#
#     def move(self, speed):
#         print(f'Moved with a speed of {speed}')
#
# monster1 = Monster(health=100, energy=55)
# print(monster1)

#---------------------------------------------------------------------------------------#
#----------------#
#----Simple inheritance----#
#----------------#

class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        print('The monster was created')

    # A method always needs at least 1 arg
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'The monster used 10 energy')
        self.energy -= 10
        print(f'{amount} damage was dealt')

    def move(self, speed):
        print(f'Moved with a speed of {speed}')


class Shark(Monster):
    def __init__(self, health, energy, speed):
        # OLD WAY:
        # Monster.__init__(self, health, energy)

        # NEW WAY: (Super gets the parent)
        super().__init__(health, energy)
        super().move(10)
        self.speed = speed

    def bite(self):
        print(f'Shark used Bite!')

    def move(self):
        print('The shark has moved')
        print(f'Moved with a speed of {self.speed}')


shark = Shark(5, 10, 120)
shark.bite()
shark.attack(20)
shark.move()

#---------------------------------------------------------------------------------------#
#----------------#
#----External Modules----#
#----------------#


#---------------------------------------------------------------------------------------#
#----------------#
#----Creating modules----#
#----------------#
import my_module as mm
print(mm.test_var)

mm.test_function(123)
test = mm.Test()
test.do_something()

print(__name__)
#---------------------------------------------------------------------------------------#
#----------------#
#----Dunder Main----#
#----------------#
if __name__ == '__main__':
    print('The main file')
#---------------------------------------------------------------------------------------#
#----------------#
#----Exceptions----#
#----------------#


#---------------------------------------------------------------------------------------#
#----------------#
#----Eval & Exec----#
#----------------#


#---------------------------------------------------------------------------------------#
#----------------#
#----Decorators----#
#----------------#


#---------------------------------------------------------------------------------------#
