# Function is a reusable block of code that performs a specific task.
# Functions help make your code organized, readable, and efficient.
# A function is defined using the keyword (def) 

#1.example: simple function
def welcome():
    print('"Welcome to the MohammadKaif-DS GitHub repository"')

welcome() # Call the function

#2.example: function with parameter
def user(name):
    print(f'Hi, {name} ')

user('Kaif') # Call the function with parameter 

#3.example: function with return value
def addition(a,b):
    return a+b

result=addition(10,20) # call and print
print(result)

#4.example: function with defualt parameter
def welcome(name='Guest'):
    print(f'Welcome, {name} ')

welcome() # Call it give defualt parameter
welcome('kaif') # Call with parameter