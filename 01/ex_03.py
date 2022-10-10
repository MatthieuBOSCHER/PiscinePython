import json

class Budget:
    def __init__(self, path):
        self.path = path
        self.data = self.open_json()
        self.transactions = self.get_transaction()
        self.categories = self.get_categories()


    def open_json(self):
        f = open(self.path)
        data = json.load(f)
        return data

    def get_transaction(self):
        dict_transactions = {}
        for categories in self.data.values():
            for category in categories:
                dict_transactions[category.get(" category ")] = category.get(" value ")
        return dict_transactions

    def print_list_transaction(self, transactions_amounts):

        for transation_amount in transactions_amounts:
            # print(transation_amount)
            if transation_amount != 0:
                if transation_amount > 0:
                    print(f"You received {transation_amount} euros")
                else:
                    print(f"You spent {-1 * transation_amount} euros")

    def get_list_transactions(self, category=""):
        transactions_amounts = []
        if category == "":
            for transaction_amount in self.transactions.values():
                for amount in transaction_amount:
                    transactions_amounts.append(amount)
        else:
            for amount in self.transactions.get(category):
                 transactions_amounts.append(amount)
        return transactions_amounts

    def print_transactions(self, category=""):
        transactions_amounts = self.get_list_transactions(category)
        self.print_list_transaction(transactions_amounts)

    def print_sorted_transactions(self, category=""):
        transactions_amounts = self.get_list_transactions(category)
        transactions_amounts.sort()
        self.print_list_transaction(transactions_amounts)

    def get_categories(self):
        categories = self.transactions.keys()
        return categories

    def add_transaction(self, added_transactions, category):

        for transaction in added_transactions:
            self.transactions.append(transaction)


json_path = "../data/transaction.json"
wonderfull_transactions = Budget(json_path)
wonderfull_transactions.print_sorted_transactions(category=" transportation ")


