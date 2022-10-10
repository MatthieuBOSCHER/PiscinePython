def print_transactions(list_of_transactions):
    for transaction in list_of_transactions:
        if transaction >= 0:
            print (f"You received {transaction} euros")
        else :
            print(f"You spent {-1 * transaction} euros")

print_transactions([512, -12, 42.08])

