#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_" + user_name + "!")

user_name = input("Input your username: ")
hello_name(user_name)

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for i in range(1,100,2):
        print(str(i))

first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    maximum = max(a_list)
    print(f"The maximum number is {maximum}.")

a_list = []
while True:
    response = input("Input numbers into list. Type 'd' when finished. ")
    if response == 'd':
        break
    else:
        a_list.append(int(response))

print(a_list)
max_num_in_list(a_list)

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 == 1:
        print(str(a_year) + " is a leap year")
    elif a_year % 4 == 0 and a_year % 400 == 0:
        print(str(a_year) + " is a leap year")
    else:
        print(str(a_year) + " is not a leap year")

a_year = int(input("Enter the year to determine if it is a leap year: "))
is_leap_year(a_year)

#Question 5
#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

a_list = []
while True:
    response = input("Input numbers into list. Type 'd' when finished. ")
    if response == 'd':
        break
    else:
        a_list.append(int(response))

print(a_list)
is_consecutive(a_list)
        