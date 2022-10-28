import pandas as pd

numbers=[1,2,3,4,5,6]
pandas_series=pd.Series(numbers)
print(pandas_series)

liste=[1,4,7,"a","s","d","c"]

pandas_series=pd.Series(liste)

print(pandas_series)

dict={1:"adana",34:"istanbul",6:"ankara",35:"izmir",38:"kayseri"}

pandas_series=pd.Series(dict)
print(pandas_series)

indexes=["a","b","c","d","e","f"]

pandas_series=pd.Series(1,indexes)
print(pandas_series)

pandas_series=pd.Series(numbers,indexes)
print(pandas_series)