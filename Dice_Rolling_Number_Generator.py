import random as rd
import time as tp

def rollingDice(n,Names):
    
    print("\nDice is Rolling",end=" ")
    for i in range(3):
        print("_",end=" ")
        tp.sleep(1)
    print()
    for i in range(n):
        num = rd.randint(1,6)
        print(f"{Names[i]} : {num}")

def names(n):

    name = []
    for i in range(n):
        a = input("Enter player name : ")
        name.append(a)
    return name

def main():

    n = int(input("\nHow many players want to play : "))
    print()
    Names = names(n)
    rollingDice(n,Names)
    while True:
        choice = input("\nDo you want to roll again (y/n) : ")
        if choice == "Y" or choice == "y":
            rollingDice(n,Names)
        else:
            print("\nThank You!")
            break

if __name__ == "__main__":
    main()
