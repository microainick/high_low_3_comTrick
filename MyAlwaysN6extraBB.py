#import
import random

from os import system
#so the system can talk

#say hello and attempt to do some exception handeling for non mac users
try:
    system('say Hello!')
except OSError:
    print("Sorry you dont have a mac that talks to you")
#this except statement will be written after every system say command

#make a variable to allow us to conitue and stop on command
#assign boolean true to that variable
#make while loop
#get the user to pick a number as an input
#mu ha ha ha ha
keepitGoing = True
while keepitGoing == True:
    num = input("please select a number between 0 and 100: ")
    number = 0 #make new variable called number
    try: #price could be int or float so must be int type here
        number = int(num) #make it an integer with value of user input
        #exception handle
        #make sure the number is less than 100
        #check to see if the number is positive
        #allow the negative and show that the system still works
        #do not allow over 100
        if number <= 0:
            print("That's impossible, but OK, no problem!")
        if number > 100:
            print("That's impossible!")
        else:  #when coditions are satisified display entry 
            print("Thank you!")
            keepitGoing = False  #use to break out of loop 
            break #my double use for sense of security
    except:  #display help text 
        print("Please input positive number!")

#display the round number
print("Round 1")
 
#This program is a scam
#The computer is cheating
#it was designed to not give away an obvious pattern of how it works
#this is why i generate the random integer in a desired range 
comGuess = random.randint(25, 75)
print("The computer selects {}.".format(comGuess))

#computer picks a random number between 25 and 75
#asks the user to answer a question, but the answer is not needed
#the program knows the answer, to said question
#make the next guess within a somewhat close range to the actual number

input("Is your number higher or lower?")
if comGuess < number:
    dif1 = random.randint(8, 21)
    comGuess2 = number - dif1
if comGuess > number:
    dif2 = random.randint(9, 16)
    comGuess2 = number + dif2

#display the round number
print("Round 2")

#display com guess
print("The computer selects {}.".format(comGuess2))

#smoke and mirrors
input("Is your number divisible by 6?")

#make the next guess even closer but not within 5
if comGuess2 < number:
    dif3 = random.randint(5, 7)
    comGuess3 = number - dif3
if comGuess > number:
    dif4 = random.randint(5, 8)
    comGuess3 = number + dif4

#display the round number
print("Round 3")

#display next guess
print("The computer selects {}.".format(comGuess3))

#pretend to need to know the answer to this question
#this input has absolutely no value to the program
#this input is just a nice way to briefly pause the process.  
input("Higher or Lower")

#the next guess will be even closer but not within 2
if comGuess3 < number:
    dif5 = random.randint(2, 4)
    comGuess4 = number - dif5
if comGuess3 > number:
    dif6 = random.randint(2, 4)
    comGuess4 = number + dif6

#display the round number
print("Round 4")

#display computers next guess
print("The computer selects {}.".format(comGuess4))

print("No need to say higher or lower.")
#more smoke and mirros
input("Is your number a prime number?")

#the next guess will only be off by 1
if comGuess4 < number:
    comGuess5 = number + 1
if comGuess4 > number:
    comGuess5 = number - 1

#display the round number
print("Round 5")

#display computer guess
print("The computer selects {}.".format(comGuess5))

#slight pause for dramatic affect
input("Higher or Lower")

print("Last chance for the AI")

#display the round number
print("Round 6")

#display the final guess. 
print("The Computer says your number must be {}.".format(number))

#talk to user
#handle error for non mac users
try:
    system('say Robots do not need a seventh guess')
except OSError:
    print("Sorry you dont have a mac that talks to you")
#this except statement will be written after every system say command



