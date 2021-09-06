import random

comp = random.randint(1,50)
print("----- Guess The Number Game. -----")
print()

print("Rules of the Game :-")
print(" -> You have to guess a number from *1* to *50* which is guessed by computer.")
print(" -> You have only 5 chances to win the game.")
print(" -> Don't worry...!!! Computer will give Hint in every chances.")
print()

i = 5
k = True

while(i):
    i = i - 1
    you = int(input("Enter Your Guess."))

    if(you == comp):
        print()
        print("You Win \_:)_/")
        k = False
    elif(comp > you):
        print()
        print(f"Enter greater Number than {you} ...You are close to that number. :|")
        print(f"You have only {i} chances left.")
    elif(comp < you):
        print()
        print(f"Enter lesser Number than {you} ...You are close to that number. :|")
        print(f"You have only {i} chances left.")

if((i == 0) and (k == True)):
    print()
    print(f"You loose :( Answer is {comp}")