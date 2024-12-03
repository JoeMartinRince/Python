"""
AUTHOR : JOE MARTIN RINCE
DATE :3-12-2024
"""
def stick_game(n):
    print("Welcome to Stick game!")
    print()
    print("There are a total of 16 sticks.Each player may take 1,2 or 3 sticks at a time strategically.The Player who picks the last stick loses!!")
    print()
    print("LET THE GAME START,GOOD LUCK!!")
    print()
    player1=input("Enter name of player one: ")
    print()
    player2=input("Enter name of player two: ")
    print()
    while n>0:
        sticks1=int(input(f"{player1},You may pick 1,2 or 3 sticks: "))
        print()
        print(player1, "took", sticks1, "sticks")
        n = n - sticks1
        print(n, "Sticks remain")
        if sticks1>3 or sticks1==0:
            print("CHEATER BOII")
            print(player1,"HAS BEEN DISQUALIFIED,GAME IS BEING TERMINATED....")
            print(player2, "WINS!!")
            break
        if n<=0:
            print(player1,"Picks the last and loses the game! :(")
            print()
            print(player2,"WINS!!")
            break

        sticks2=int(input(f"{player2},You may pick 1,2 or 3 sticks: "))
        print()
        print(player2, "took", sticks2, "sticks")
        print()
        n = n - sticks2
        print(n, "Sticks remain")
        if sticks2>3 or sticks2==0:
            print("YOU CHEATT")
            print(player2,"HAS BEEN DISQUALIFIED.GAME IS BEING TERMINATED...")
            print(player1, "WINS!!")
            break
        if n<=0:
            print(player2,"Picks the last and loses the game! :(")
            print()
            print(player1,"WINS!!")
            break





stick_game(16)
