import ex_03bis
import argparse


parser = argparse.ArgumentParser(description='Payment system of the future')


def show_user_inputs():
    prompts = ["1 - consult my balance", "2 - add new transaction" , "3 - consult your transactions history"
               , "4 - quit"]
    for prompt in prompts:
        print(prompt)


def calculate_balance():
    amounts_list = userBudjet.get_list_transactions()
    balance = 0
    for amount in amounts_list:
        balance += amount
    return round(balance, 2)


def get_transaction_to_add():
    category_input = f" {input('Enter the category of the transaction :')} "
    amount_input = [int(input('Enter the amount of the transaction :'))]
    # print(f"amount_input {amount_input}")
    userBudjet.add_transactions(added_transactions=amount_input, category=category_input)
    userBudjet.print_transactions(category=category_input)


def get_user_inputs():
    user_input = input("Enter you input:")

    if user_input == "1":
        print(f"{calculate_balance()} €")
        get_user_inputs()
    elif user_input == "2":
        get_transaction_to_add()
        get_user_inputs()
    elif user_input == "3":
        userBudjet.print_transactions()
        get_user_inputs()
    elif user_input == "4":
        userBudjet.convert_transactions_to_json()
        userBudjet.write_to_json()
        quit()


if __name__ == "__main__":
    userBudjet = ex_03bis.Budget("../data/transaction.json")
    show_user_inputs()
    get_user_inputs()
