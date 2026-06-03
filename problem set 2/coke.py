

import sys

def main():
    print("Amount due: 50")
    check()

def check():
    due = 50
    while True:
        inserted = int(input("Insert coin: "))
        if inserted in [25, 10, 5]:
           due -= inserted 
           if due > 0:
               print("Amount due: ", due)
           else:
               print("Change owed: ", -due)
               break
        else:
            print("Invalid coin")


main()
