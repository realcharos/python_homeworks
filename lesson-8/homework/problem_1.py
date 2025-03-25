import json
import random


# Farm Model
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Cow(Animal):
    def moo(self):
        print(f"{self.name} says Moo!")


class Chicken(Animal):
    def cluck(self):
        print(f"{self.name} says Cluck!")


class Horse(Animal):
    def neigh(self):
        print(f"{self.name} says Neigh!")


# Bank Application
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        print(f"Account created! Account Number: {account_number}")
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account {account_number}: Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, f)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                for acc, details in data.items():
                    self.accounts[int(acc)] = Account(int(acc), details['name'], details['balance'])
        except FileNotFoundError:
            pass


# Example Usage
if __name__ == "__main__":
    # Farm Simulation
    cow = Cow("Bessie", 5)
    chicken = Chicken("Clucky", 2)
    horse = Horse("Thunder", 7)

    cow.eat()
    cow.moo()
    chicken.cluck()
    horse.neigh()

    # Bank Simulation
    bank = Bank()
    acc_num = bank.create_account("John Doe", 500)
    bank.view_account(acc_num)
    bank.deposit(acc_num, 200)
    bank.withdraw(acc_num, 100)
    bank.view_account(acc_num)
