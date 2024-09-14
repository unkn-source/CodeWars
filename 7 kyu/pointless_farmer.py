def buy_or_sell(pairs, harvested_fruit):
    current_fruit = harvested_fruit
    actions = []

    for offer in pairs:
        fruit1, fruit2 = offer

        if current_fruit == fruit1:
            actions.append("buy")
            current_fruit = fruit2
        elif current_fruit == fruit2:
            actions.append("sell")
            current_fruit = fruit1
        else:
            return "ERROR"

    if current_fruit == harvested_fruit:
        return actions
    else:
        return "ERROR"