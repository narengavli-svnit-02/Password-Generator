import itertools
import os
import colorama
from colorama import Fore
from colorama import Style

# function


def word_maker(st, usrAlpha, ed):
    for word in itertools.permutations(usrAlpha):
        passwd = "".join(word)
        passwdList.write(F"{st}{passwd}{ed}\n")


# remove exiting file
if os.path.exists("passwdList.txt"):
    os.remove("passwdList.txt")

# create new file
passwdList = open("passwdList.txt", "a")

# user input
print(Fore.LIGHTBLUE_EX + "\n1 - Enter only the alphabet from the password.")
print("2 - Stating word fix and a random word from the alphabet.")
print("3 - Ending word fix and a random word from the alphabet.")
print("4 - Starting and ending word fix and a random word from alphabet.\n" + Style.RESET_ALL)

passwdType = int(input(
    "Enter the number (1 2 3 4) for which type of password you want to create : "))

# type of password list
if passwdType == 1:
    st = ""
    usrAlpha = input(
        "Enter an alphabet and a number to generate a password : ")
    ed = ""

elif passwdType == 2:
    st = input("Enter the first fixed word : ")
    usrAlpha = input(
        "Enter an alphabet and a number to generate a password : ")
    ed = ""

elif passwdType == 3:
    st = ""
    usrAlpha = input(
        "Enter an alphabet and a number to generate a password : ")
    ed = input("Enter the last fixed word : ")

else:
    st = input("Enter the first fixed word : ")
    usrAlpha = input(
        "Enter an alphabet and a number to generate a password : ")
    ed = input("Enter the last fixed word : ")

# calling function
word_maker(st, usrAlpha, ed)

# get pwd
pwd = os.getcwd()

# printing status
if os.path.exists("passwdList.txt"):
    print(Fore.GREEN +
          F"\nYour password list was successfully created at {pwd}.\n" + Style.RESET_ALL)
else:
    print(Fore.RED + "\nSomething went wrong please try again.\n" + Style.RESET_ALL)

# closing file
passwdList.close()
