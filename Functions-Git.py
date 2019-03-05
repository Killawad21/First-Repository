# 4.13.3: Greetings
# Logan Pennock
# 2.5.19
'''

name = input("what is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()
'''

# 4.13.4: Functions and Variables
# Logan Pennock
# 2.11.19

x = 10

def print_something():
    x = 3
    print('\n', x)
print('\n', x)
print_something()

# 4.13.16: Functions and Variables, part 3
# Logan Pennock
# 2.18.19

def print_number(x):
    print('\n' , x)

print_number(13)
print_number(23)

# 4.14.4: Name & Age
# Logan Pennnock
# 2.18.19

def name_and_age(name, age):
    print('Hi, my name is', name, 'and I am', str(age), 'years old')

name_and_age('Mike', 33)
name_and_age('Zane', 18)


# 4.14.5: Default Parameter Values
# Logan Pennock
# 2.19.19

def print_two_numbers(x, y = 20):
    print('First number:', x)
    print('Second number: ' + str(y))
print_two_numbers(34, 45)
print_two_numbers(78)

# 4.14.6: Print sum
# Logan Pennock
# 2.19.18

def print_sum(x, y):
    print(x + y)

print_sum(54, 99)

# 4.16.3: Enter a Number using Try & Except
# Logan Pennock
# 2.20.19


try:
    my_num = int(input('Enter an integer: '))
    print('Your number:', my_num)

except ValueError:
    print('that is not and integer!);, Off to goolag')


