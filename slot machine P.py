import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 7
        elif row[0] == "🍉":
            return bet * 6
        elif row[0] == "🍋":
            return bet * 6
        else:
            return bet * 5
    return 0

def main():
    balance = 100

    print("-----------------------")
    print("welcome to python slots\n")

    print("symbols: 🍒🍉🍋🔔⭐")
    print("-----------------------")

    while balance > 0:
        print(f"\ncurrent balance: {balance}")

        bet = input("place your bet amount: \n")

        if not bet.isdigit():
            print("\ninvalid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("\ninsufficient funds")
            continue

        if bet <=0:
            print("\nbet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("\nspinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        
        if payout>0:
            print(f"\nyou won {payout}\n")
        else:
            print("\nsorry you lost this round\n")

        balance += payout

        play_again = input("do you want to spin again? (y/n)").lower()

        if not play_again == "y":
            break

    print("-----------------------------")
    print(f"your final balance is {balance}\n")

if __name__ == "__main__":
    main()