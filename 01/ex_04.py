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


def get_user_inputs():
    user_input = input()
    switch={
        "1": print(f"{calculate_balance()} €")
    }
    return switch.get(user_input, "Invalid input")


if __name__=="__main__":
    userBudjet = ex_03bis.Budget("../data/transaction.json")
    show_user_inputs()
    get_user_inputs()