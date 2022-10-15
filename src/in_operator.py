# LIST
from traceback import print_tb


my_answer = input("What is your answer")
my_answer = my_answer.lower()

default = ['rock','paper','scissors']

if my_answer in default:
    print(f"{my_answer} is one of the possible answers")
else:
    print("Wrong answer. Try again!")

# DICTIONARY
key = 'age'
details = {
    "name":"Nickson",
    "age":"45",
    "gender":"Male"
}
if key in details:
    print(f"{key} is a dictionary key in details dictionary")
else:
    print(f"{key} is not a dictionary key in the details dictionary")

# SET
usr_input = int(input("Enter a number: "))
numbers ={10,20,20,40,50,69}
if usr_input in numbers:
    print("Task Completed")
    print(type(numbers))

# TUPLE
usr_input = int(input("Enter a number: "))
numbers =(10,20,20,40,50,69)
if usr_input in numbers:
    print("Task Completed")
    print(type(numbers))
    