######data 1
print ("Hello World")
######data 2

num1=int(input ("ask the user to enter number1:"))
num2=int(input ("ask the user to enter number2:"))
answer=num1+num2
print(answer)

######data 3
name =input("Enter your name: ")
age=int(input("Enter your age: "))
city = input("Enter your city: ")
print(f"Hello {name}, you are {age} years old and live in {city}.")

######data 4
a1=(4*8)*6
print(a1)
a2=(2**3)/(8/3)
print(a2)
a3=(27**2)*19/4
print(a3)

######data 5
#days=minutes_late//1440
#remian=minutes_late%1440
#hours=remain//60
#minutess=remain%60

######data 6
####ser_string = input("Enter a string: ")
#####e.g
#####print(f"Modified String 8: {len(user_string)}")

#######data 7
try:
    num1=int(input())
    num2=int(input())
    answer=num1*num2
    print(answer)
except:
    print('That is not a number')
######worksheet
name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
try:
    monthly=int(input("Enter the amount you want to save each month: "))
    total_saved=monthly*12
    print(f"Total saved in the year:£{total_saved}")
    interest_rate=0.008
    total_with_interest=total_saved*(1 + interest_rate)
    print(f"Total including interest:£{total_with_interest:.2f}")
except:
    print("That is not an integer.")