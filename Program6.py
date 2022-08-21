#Write a python script  which takes three digit number from the user and displays only its middle digit.
num=int(input("Enter the three digit number:"))
div=num%100
middle=div//10
print("Middle digit of the given number:",middle)