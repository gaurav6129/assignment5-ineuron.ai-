#Write a python script which takes a three digit number from the user and displays only its last digit.
num=int(input("Enter the three digit number:"))
div=num%10
print("Number after removing the last digit:",div)