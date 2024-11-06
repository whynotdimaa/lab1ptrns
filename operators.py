class Operator:
    # Клас Operator представляє оператора зв'язку

    def __init__(self, id: int, talking_charge: float, message_cost: float, network_charge: float, discount_rate: int) -> None:
        self.id = id
        self.talking_charge = talking_charge
        self.message_cost = message_cost
        self.network_charge = network_charge
        self.discount_rate = discount_rate

    def calc_talking_cost(self, minutes: float, customer) -> float:
        # Розрахунок вартості дзвінка
        cost = self.talking_charge * minutes
        if customer.age < 18 or customer.age > 65:
            cost -= cost * (self.discount_rate / 100)
        return cost

    def calc_message_cost(self, quantity: int, customer, other) -> float:
        # Розрахунок вартості повідомлень
        cost = self.message_cost * quantity
        if self.id == other.operators[self.id].id:
            cost -= cost * (self.discount_rate / 100)
        return cost

    def calc_network_cost(self, amount: float) -> float:
        # Розрахунок вартості інтернету
        return self.network_charge * amount
