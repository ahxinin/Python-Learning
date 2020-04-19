try:
    print(1/0)
except ZeroDivisionError as e:
    print("error occurs.", e)