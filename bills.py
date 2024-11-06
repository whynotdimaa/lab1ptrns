class Bill:
    # Клас Bill представляє рахунок клієнта

    def __init__(self, limit: float):
        self.limit = limit
        self.debt = 0.0

    def check(self) -> bool:
        # Перевірка ліміту боргу
        return self.debt >= self.limit

    def add_debt(self, amount: float) -> None:
        # Додає борг до рахунку
        self.debt += amount
        if self.debt > self.limit:
            print(f"Перевищено ліміт! Ваш борг: {self.debt}")

    def pay(self, amount: float) -> None:
        # Оплата рахунку
        self.debt -= amount
        if self.debt < 0:
            self.limit += abs(self.debt)
            self.debt = 0
        print(f"Оплачено {amount}. Залишок боргу: {self.debt}")

    def change_limit(self, amount: float) -> None:
        # Зміна ліміту боргу
        self.limit += amount
        print(f"Новий ліміт: {self.limit}")
