# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код
class BankAccount:

    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        if amount > self.initial_balance:
            raise ValueError("You don't have the amount on your account")
        else:
            self.initial_balance -= amount

try:
    ba = BankAccount(222, 3000)
    ba.deposit(500)
    print(ba.initial_balance)
    ba.withdraw(1000)
    ba.deposit(1000)
    print(ba.initial_balance)
    # ba.withdraw(5000)
    print(ba.initial_balance)
except ValueError as e:
    print(e)
