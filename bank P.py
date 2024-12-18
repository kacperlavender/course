# Python bank aplication

def showbalance(balance):
    print(f"your balance is {balance:.2f}\n")

def depo():
    amount = float(input("\nenter an amount to be deposited: \n"))

    if amount < 0:
        print("\nthats not a valid amount\n")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("\nenter an amount to be deposited: \n"))

    
    if amount > balance:
        print("\ninsufficient funds")
        return 0
    elif amount < 0:
        print("\nthats not a valid amount\n")
        return 0
    else:
        return amount

def main():
    balance = 0
    runnning = True

    while runnning:
        print("---banking program---\n")
        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")

        choice = input("\nenter your choice: (1-4)\n")

        if choice == "1":
            showbalance(balance)
        elif choice == "2":
            balance += depo()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            runnning = False
        else: 
            print("\ninvalid choice")

    print("\nthank you. have a nice day")

if __name__ == "__main__":
    main()