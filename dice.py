'''
The Goal: This project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the maximum number of sides on the dice is up to you.) The program will print what that number is. It then ask you if you’d like to roll again.
 * @author  Francesco Fresta
 * @version 0.5, March 2018
'''
from random import randint #python module to generate random numbers
import time #I use sleep to gives some interactivity to the outputs
def rolling_dice():
    print("Welcome. This program simulates rolling a dice.\n")
    time.sleep(2) #wait 2 seconds
    faces = int(input("How many faces has the dice got? "))
    print("I am going to print a number between 1 and ", faces, "...\n")
    time.sleep(1)
    print("LOADING...\n")
    time.sleep(1)
    return randint(1, faces) #integer from 1 to faces, endpoints included
again = "Y"
while(again == "Y"):
    value = rolling_dice()
    print("The dice says... ", value)
    again = str(input("Would you like to roll the dice again? Y/N?"))
quit()
