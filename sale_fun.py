def sale_fun(
    product_id,
    unit_price,
    product_amount,
    saldo,
    check,
    logs,
    storehouse,
    dataDest,
):
    if product_amount < 0:
        dataDest.write(
            "Błąd. Ujemna ilość zakupionego towaru {} w ilości {}".format(
                product_id, product_amount
            )
        )
        check = False
        return
    elif unit_price * product_amount < 0:
        dataDest.write(
            "Błąd. Ujemna kwota zakupu {} w ilości {}".format(
                product_id, product_amount
            )
        )
        check = False
        return
    logs.append(("sprzedaż", product_id, unit_price, product_amount))
    if product_id in storehouse:
        storehouse[product_id] -= product_amount
    else:
        dataDest.write(
            "Błąd. Brak produktu {} na magazynie".format(product_id)
        )
        check = False
        return
    saldo += unit_price * product_amount
