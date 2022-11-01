from random import randint
import pandas as pd
import numpy as np

array=np.random.randint(1,30,16).reshape(4,4)
df=pd.DataFrame(array,index=["a","b","c","d"],columns=["column1","column2","column3","column4"])

#head()
result=df.head(2)


#tail()
result=df.tail(2)


#info()
#print(df.info())

#shape
result=df.shape


#loc [row,column]

result=df.loc["a"]
result=df.loc[["a","c"]]
result=df.loc[["a","c"],["column1"]]
result=df.loc[:,["column1","column3"]]

#iloc

result=df.iloc[["0","3"]]
result=df.iloc[[0,3],[0,3]]

#drop()

result=df.drop("column1",axis=1,inplace=True)

print(df)
print(result)