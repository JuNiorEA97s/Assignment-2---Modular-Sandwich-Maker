class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.10
        total += int(input("how many nickels?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
