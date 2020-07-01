from pandas import Series,DataFrame
import pandas as pd


obj = Series([1, 2, 3])
print(obj)
print(obj.values)


data = {"name":["jack", "tony"],
        "age":[23, 25]}
frame = DataFrame(data)
print(frame)