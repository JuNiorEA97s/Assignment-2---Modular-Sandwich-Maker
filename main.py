import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()

        if choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid option. Please choose again.")

        should_continue = input("Would you like another sandwich? (yes/no): ").lower()
        if should_continue == 'no':
            is_on = False

if __name__ == "__main__":
    main()

