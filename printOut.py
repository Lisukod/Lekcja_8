def printOut(logs):
    for log in logs:
        if log == "stop":
            print("{}".format(log))
        else:
            for log_element in log:
                print("{}".format(log_element))
