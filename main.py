from customers import Customer
from operators import Operator
from bills import Bill

def main():
    # Ініціалізація операторів з новими параметрами
    operators = [Operator(0, 0.5, 0.15, 0.2, 8), Operator(1, 0.7, 0.25, 0.3, 10)]

    # Ініціалізація рахунків з новими лімітами
    bills = [Bill(800), Bill(400)]

    # Створюємо клієнтів з новими даними
    customers = [Customer(0, 'Олексій', 'Ковальчук', 30, operators, bills),
                 Customer(1, 'Іван', 'Мельник', 25, operators, bills)]

    # Дії клієнтів
    customers[0].talk(5, customers[1], 0)  # Олексій говорить з Іваном
    customers[1].message(10, customers[0], 1)  # Іван відправляє повідомлення Олексію
    customers[0].connection(200, 0)  # Олексій використовує інтернет

    # Оплата та зміна ліміту
    customers[0].get_bill(0).pay(50)
    customers[0].get_bill(0).change_limit(20)

if __name__ == "__main__":
    main()
