def buy_fun(
    product_id, unit_price, product_amount, saldo, check, logs, storehouse
):
    if saldo - unit_price * product_amount < 0:
        print(
            "Błąd. Ujemne saldo po zakupie {} w ilości {}".format(
                product_id, product_amount
            )
        )
        check = False
        return
    elif product_amount < 0:
        print(
            "Błąd. Ujemna ilość zakupionego towaru {} w ilości {}".format(
                product_id, product_amount
            )
        )
        check = False
        return
    elif unit_price * product_amount < 0:
        print(
            "Błąd. Ujemna kwota zakupu {} w ilości {}".format(
                product_id, product_amount
            )
        )
        check = False
        return
    logs.append(("zakup", product_id, unit_price, product_amount))
    if product_id in storehouse:
        storehouse[product_id] += product_amount
    else:
        storehouse[product_id] = product_amount
    saldo -= unit_price * product_amount
