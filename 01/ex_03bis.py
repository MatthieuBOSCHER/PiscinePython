import json
import os

class Budget:
    def __init__(self, path):
        self.path = path
        self.data = self.open_json()
        self.transactions = self.get_transaction()
        self.categories = self.get_categories()


    def open_json(self):
        f = open(self.path)
        data = json.load(f)
        print(data)
        return data

    # get dict of transaction
    def get_transaction(self):
        dict_transactions = {}
        for categories in self.data.values():
            for category in categories:
                dict_transactions[category.get(" category ")] = category.get(" value ")
        return dict_transactions

    # print a list of all transaction
    def print_list_transaction(self, transactions_amounts):

        for transation_amount in transactions_amounts:
            # print(transation_amount)
            if transation_amount != 0:
                if transation_amount > 0:
                    print(f"You received {transation_amount} euros")
                else:
                    print(f"You spent {-1 * transation_amount} euros")

    # return a list with the amounts of all transactions
    def get_list_transactions(self, category=""):
        transactions_amounts = []
        if category == "":
            for transaction_amount in self.transactions.values():
                for amount in transaction_amount:
                    transactions_amounts.append(amount)
        else:
            for amount in self.transactions.get(category):
                transactions_amounts.append(amount)
        # print(f"transactions_amounts {transactions_amounts}")
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

    def add_transactions(self, added_transactions, category):
        self.transactions[category] = added_transactions
        self.convert_transactions_to_json()
        self.write_to_json()

    def convert_transactions_to_json(self):
        list_of_dict = []
        for category in self.transactions:

            list_of_dict.append({" value ": self.transactions.get(category), " category ": category})
        self.data[" transactions "] = list_of_dict

    def write_to_json(self):
        os.remove(self.path)
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)


