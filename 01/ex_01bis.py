from ex_01 import print_transactions


def print_sorted_transactions(list_of_transactions):
    sorted_transaction = sorted(list_of_transactions)

    print_transactions(sorted_transaction)


print_sorted_transactions([512, 34, -123, 0, 42.08, -12])
