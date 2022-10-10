class Budget():
    def __init__(self, transactions):
        self.transactions = transactions

    def print_list_transaction(self, list_transaction):
        for transaction in list_transaction:
            if transaction != 0:
                if transaction > 0:
                    print(f"You received {transaction} euros")
                else:
                    print(f"You spent {-1 * transaction} euros")

    def print_transactions(self):
        self.print_list_transaction(self.transactions)

    def print_sorted_transactions(self):
        self.print_list_transaction(sorted(self.transactions))

    def add_transaction(self, added_transactions):
        for transaction in added_transactions:
            self.transactions.append(transaction)




transactions = Budget([-5, 5, -123, 1234, -6, 89])


# transactions.print_transactions()
# transactions.print_sorted_transactions()
transactions.add_transaction([69])
# transactions.print_transactions()
transactions.print_sorted_transactions()