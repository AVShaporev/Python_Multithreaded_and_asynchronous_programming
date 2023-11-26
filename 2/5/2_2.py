from random import randint, choice


with open("my_payment_orders_1.txt", "w") as file_1, open("my_payment_orders_2.txt", "w") as file_2:
    for i in range(200):
        priority = randint(1, 3)
        assignment = choice(("receipt", "withdrawal"))
        amount = randint(1, 200000)
        payment_order = f"{priority} {amount} {assignment}\n"
        if i & 1:
            file_1.write(payment_order)
        else:
            file_2.write(payment_order)