from typing import List
from bills import Bill
from operators import Operator

class Customer:
    # Клас Customer представляє клієнта

    def __init__(self, id: int, first_name: str, last_name: str, age: int, operators: List[Operator], bills: List[Bill]) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.operators = operators
        self.bills = bills

    def talk(self, minutes: float, customer, operator_id: int) -> None:
        # Виконує дзвінок та додає вартість до рахунку
        operator = self.operators[operator_id]
        cost = operator.calc_talking_cost(minutes, self)
        bill = self.bills[operator_id]
        if not bill.check():
            bill.add_debt(cost)
            print(f"{self.first_name} говорив з {customer.first_name} протягом {minutes} хвилин.")
        else:
            print(f"{self.first_name} не може здійснити дзвінок - перевищено ліміт.")

    def message(self, quantity: int, customer, operator_id: int) -> None:
        # Відправляє повідомлення
        operator = self.operators[operator_id]
        cost = operator.calc_message_cost(quantity, self, customer)
        bill = self.bills[operator_id]
        if not bill.check():
            bill.add_debt(cost)
            print(f"{self.first_name} відправив {quantity} повідомлень до {customer.first_name}.")
        else:
            print(f"{self.first_name} не може відправити повідомлення - перевищено ліміт.")

    def connection(self, data_usage: float, operator_id: int) -> None:
        # Використовує інтернет
        operator = self.operators[operator_id]
        cost = operator.calc_network_cost(data_usage)
        bill = self.bills[operator_id]
        if not bill.check():
            bill.add_debt(cost)
            print(f"{self.first_name} використав {data_usage} MB інтернету.")
        else:
            print(f"{self.first_name} не може використовувати інтернет - перевищено ліміт.")

    def get_bill(self, operator_id: int) -> Bill:
        return self.bills[operator_id]
