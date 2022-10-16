import random


def stock_market():
    stocks_1 = 0
    stocks_2 = 0
    stocks_3 = 0
    stocks_4 = 0
    firm1 = "Amazon"
    firm2 = "Facebook"
    firm3 = "Allegro"
    firm4 = "Netflix"
    value_1 = round(random.uniform(10.00, 100.00), 2)
    value_2 = round(random.uniform(10.00, 100.00), 2)
    value_3 = round(random.uniform(10.00, 100.00), 2)
    value_4 = round(random.uniform(10.00, 100.00), 2)
    firm_list = {firm1: [value_1, stocks_1, 1], firm2: [value_2, stocks_2, 2], firm3: [
        value_3, stocks_3, 3], firm4: [value_4, stocks_4, 4]}
    firm_number_dict = {1: firm1, 2: firm2, 3: firm3, 4: firm4}
    return firm_list, firm_number_dict


def possible_firm_presentation(firm_list, possible_firms):
    for firm in possible_firms:
        print(firm_list[firm][2], " %9s" % firm)


def show_firm_list(firm_list=dict):
    print("=" * 48)
    print("L.p.|", "  Name of firm", "| Amount of stocks|", " Value|")
    print("=" * 48)
    for firm in firm_list:
        print(firm_list[firm][2], "  |"+" "*3, "%11s" % firm, "| %15d" %
              firm_list[firm][1], "| %6.2f|" % firm_list[firm][0])
    print("=" * 48)


def new_day(firm_list=dict):
    n = 0
    print("Here is the new state of stock market: ")
    while n < len(firm_list):
        firm = list(firm_list.keys())[n]
        percent = random.randint(0, 30)
        tend = random.choice([-1, 1])
        value = firm_list[firm][0]
        value += (percent * 0.01 * tend * value)
        firm_list[firm][0] = round(value, 2)
        n += 1
    return firm_list


def transaction_process(transaction, impossible_transaction_communicate, possible_firms, which_firm_communicate, transaction_account_sign, state_of_account, firm_list, firm_number_dict):
    if len(possible_firms) != 0:
        print(which_firm_communicate)
        possible_firm_presentation(firm_list, possible_firms)
        choice = input().lower().capitalize()
        while choice not in possible_firms:
            try:
                choice = int(choice)
                choice = firm_number_dict[choice]
            except:
                if choice in possible_firms:
                    None
                else:
                    choice = (
                        input("Write correct name or number of the firm: ").lower()).capitalize()
        price_of_one_stock = firm_list[choice][0]
        if transaction == "b":
            possible_amount = state_of_account // price_of_one_stock
            amount_communicate = f"How many stocks do you want to buy? [max {possible_amount}] "
        elif transaction == "s":
            possible_amount = firm_list[choice][1]
            amount_communicate = f"How many stocks do you want to sell [max {possible_amount}] "
        amount = (input(amount_communicate))
        try:
            amount = int(amount)
        except:
            None
        while amount > possible_amount or amount < 0 or type(amount) != int:
            amount = input("Write correct amount: ")
        state_of_account += amount * price_of_one_stock * transaction_account_sign
        firm_list[choice][1] += amount * transaction_account_sign * (-1)
        show_firm_list(firm_list)
        print("Your state of account is:", round(state_of_account, 2))
    else:
        print(impossible_transaction_communicate)
    decision = input(
        "Do you want to do something more? \n If yes - write 'y' \n If no - write 'n' : ").lower()
    return decision, state_of_account, firm_list


def shopping(state_of_account, firm_list, firm_number_dict):
    decision = input(
        "Do you want to buy some stocks? \n If yes - write 'y' \n If no - write 'n' : ").lower()
    while decision != "n":
        if decision == "y":
            possible_firms = []
            transaction = input(
                "What do you want to do? \n If buy - write 'b' \n If sell - write 's' : ")
            if transaction == "b":
                for firm in list(firm_list.keys()):
                    if state_of_account >= firm_list[firm][0]:
                        possible_firms.append(firm)
                which_firm_communicate = "Which stocks do you want to buy? Write down the number or the name of the firm:"
                impossible_transaction_communicate = "You do not have enough money to buy anything"
                transaction_account_sign = -1
                decision, state_of_account, firm_list = transaction_process(
                    transaction, impossible_transaction_communicate, possible_firms, which_firm_communicate, transaction_account_sign, state_of_account, firm_list, firm_number_dict)
            elif transaction == "s":
                for firm in list(firm_list.keys()):
                    if firm_list[firm][1] > 0:
                        possible_firms.append(firm)
                which_firm_communicate = "Which stock do you want to sell? Write the number of firm:"
                impossible_transaction_communicate = "Unfortunately you don't have any stocks to sell"
                transaction_account_sign = 1
                decision, state_of_account, firm_list = transaction_process(transaction, impossible_transaction_communicate, possible_firms,
                                                                            which_firm_communicate, transaction_account_sign, state_of_account, firm_list,
                                                                            firm_number_dict)
            else:
                decision = input(
                    "Do you still want to buy or sell? \n If yes - write 'y' \n If no - write 'n' : ")
        else:
            decision = input("'y' or 'n'?")
    return state_of_account, firm_list


def bussines_game():
    state_of_account = 200
    firm_list, firm_number_dict = stock_market()
    while True:
        show_firm_list(firm_list)
        print("Your state of account is:", round(state_of_account, 2))
        state_of_account, firm_list = shopping(
            state_of_account, firm_list, firm_number_dict)
        firm_list = new_day(firm_list)


bussines_game()
