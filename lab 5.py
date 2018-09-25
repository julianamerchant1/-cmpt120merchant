# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Juliana Merchant
# Created: 2018/11/25
def main():
# get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
# generate a Marist-style username
    uname = first + '.' + last
    print(uname)
# ask user to create a new password
    passwd = input("Create a new password, 8 characters or more: ")
# modify this to ensure the password has at least 8 characters
    while len(passwd)<8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")
    print("Account configured. Your new email address is", uname + "@marist.edu")
main()
