def saldo_fun(temp_saldo, comment, saldo, logs):
    saldo += temp_saldo
    logs.append(("saldo", temp_saldo, comment))
    return saldo
