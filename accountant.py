from sys import argv
from saldo_fun import saldo_fun
from buy_fun import buy_fun
from sale_fun import sale_fun
from printOut import printOut
import codecs

saldo = 0
check = True
logs = []
storehouse = {}
sourceLines = []
count = 0

with open(argv[-2]) as sourceFile:
    for line in sourceFile:
        sourceLines.append(line)

dataDest = codecs.open(argv[-1], "w", "utf-8")
switchCase = {"sprzedaż": sale_fun, "zakup": buy_fun}
while check:
    action = sourceLines[count].strip()
    if action == "saldo":
        saldo = saldo_fun(
            int(sourceLines[count + 1]), sourceLines[count + 2].strip(), saldo, logs
        )
        count += 3
    elif action == "zakup" or action == "sprzedaż":
        switchCase[action](
            sourceLines[count + 1].strip(),
            int(sourceLines[count + 2]),
            int(sourceLines[count + 3]),
            saldo,
            check,
            logs,
            storehouse,
            dataDest,
        )
        count += 4
    elif action == "stop":
        if len(argv) == 1:
            printOut(logs, dataDest)
        elif argv[1] == "saldo":
            saldo = saldo_fun(int(argv[2]), argv[3], saldo, logs)
            dataDest.write(str(saldo))
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
                dataDest,
            )
            printOut(logs, dataDest)
        elif argv[1] == "sprzedaż":
            sale_fun(
                argv[2],
                int(argv[3]),
                int(argv[4]),
                saldo,
                check,
                logs,
                storehouse,
                dataDest,
            )
            printOut(logs, dataDest)
        elif argv[1] == "konto":
            dataDest.write(str(saldo))
            break
        elif argv[1] == "magazyn":
            for name in argv[2:-2]:
                if name in storehouse:
                    dataDest.write("{}: {}\n".format(name, storehouse[name]))
                else:
                    dataDest.write("{}: 0\n".format(name))
        elif argv[1] == "przegląd":
            for index, log in enumerate(logs):
                if index >= int(argv[2]) and index <= int(argv[3]):
                    if log == "stop":
                        dataDest.write("{}\n".format(log))
                        break
                    else:
                        for log_element in log:
                            dataDest.write("{}\n".format(log_element))
        else:
            printOut(logs, dataDest)
        logs.append("stop")
        dataDest.write(logs[-1])
        break
    else:
        dataDest.write("Błędna nazwa operacji. Podano {}".format(action))
        break
