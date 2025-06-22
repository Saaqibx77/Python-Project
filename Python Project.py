import random
import time


nm=input("\nEnter your Name :")

print("\n",nm," You have 7 chances to guess my number")

print("\nI have in My mind 1 number between 1 and 100")

print("\nAfter every chance i will give you a clue...")

print("\nStart Now.....")


time.sleep(2)

print("****************Number Guessing Game**************")

x=random.randint(1,100) #Computer randomly think a number


c=1

i=1
while c<=7:
    y=int(input("Guess A number :"))
    if x==y:
        print("You won the game in Chance :",c)
        break
    elif x<y:
        print("i have chosen a smaller number ")
    elif x>y:
        print("i have chosen a bigger number ")

    c=c+1

if c>7:
    print("you lose the game.. the number was :",x)
    


