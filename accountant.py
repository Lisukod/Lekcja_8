from sys import argv
from saldo_fun import saldo_fun
from buy_fun import buy_fun
from sale_fun import sale_fun
from printOut import printOut

saldo = 0
check = True
logs = []
storehouse = {}

switchCase = {"sprzedaż": sale_fun, "zakup": buy_fun}
while check:
    action = input().strip()
    if action == "saldo":
        x = int(input())
        y = input()
        saldo = saldo_fun(x, y, saldo, logs)
    elif action == "zakup" or action == "sprzedaż":
        x = input()
        y = int(input())
        z = int(input())
        switchCase[action](x, y, z, saldo, check, logs, storehouse)
    elif action == "stop":
        if len(argv) == 1:
            printOut(logs)
        elif argv[1] == "saldo":
            saldo = saldo_fun(int(argv[2]), argv[3], saldo, logs)
            print(saldo)
            break
        elif argv[1] == "zakup":
            buy_fun(
                argv[2],
                int(argv[3]),
                int(argv[4]),
                saldo,
                check,
                logs,
                storehouse,
            )
            printOut(logs)
        elif argv[1] == "sprzedaż":
            sale_fun(
                argv[2],
                int(argv[3]),
                int(argv[4]),
                saldo,
                check,
                logs,
                storehouse,
            )
            printOut(logs)
        elif argv[1] == "konto":
            print(saldo)
            break
        elif argv[1] == "magazyn":
            for name in argv[2:]:
                if name in storehouse:
                    print("{}: {}".format(name, storehouse[name]))
                else:
                    print("{}: 0".format(name))
        elif argv[1] == "przegląd":
            for index, log in enumerate(logs):
                if index >= int(argv[2]) and index <= int(argv[3]):
                    if log == "stop":
                        print("{}".format(log))
                        break
                    else:
                        for log_element in log:
                            print("{}".format(log_element))
        else:
            printOut(logs)
        logs.append("stop")
        print(logs[-1])
        break
    else:
        print("Błędna nazwa operacji. Podano {}".format(action))
        break
