#- variable declaration
#- Numbers
num1 = 42
num2 = 2.3
#- Boolean
boolean = True
#- Strings
string = 'Hello World'

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list initialize 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana')  # tupla initialize
print(type(fruit)) # tupla access value
print(pizza_toppings[1]) # list access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary change value
print(fruit[2]) # tupla access value

#- conditional
#   - if
if num1 > 45:
    print("It's greater")
#    - else
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
#    - else if
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#- for loop
for x in range(5): # start
    print(x) 
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
# while loop
while(x < 5): #start
    print(x)
    x += 1 # increment

#list delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
# dictionary delete value
person.pop('eye_color')
print(person)


#for loop
for topping in pizza_toppings:
    if topping == 'Pepperoni': #conditional if
        continue # for loop continue
    print('After 1st if statement')
    if topping == 'Olives':
        break # for loop break

#function
def print_hello_ten_times():
    for num in range(10): #argument
        print('Hello') #return

print_hello_ten_times() 

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' # - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'