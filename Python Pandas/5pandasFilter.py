import pandas as pd
import numpy as np

data = np.random.randint(0,100,80).reshape(10,8)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5","Column6","Column7","Column8"])

#30 dan büyük değerler

result= df[df>30]

#column1>50
result=df[df["Column1"]>50]["Column1"]

#column1>30 ve column3<65

result=df[(df["Column1"]>30) & (df["Column3"]<65)][["Column1","Column3"]]

#column2>50 veya column3<25

result=df[(df["Column2"]>50) | (df["Column3"]<25)][["Column2","Column3"]]

#column5 2 nin katı ve column8<65

result=df[(df["Column5"] %2==0) & (df["Column8"]<65)][["Column5","Column8"]]

#column1>30 veya column5 3 ün katı
result=df[(df["Column1"]>30) | (df["Column5"]%3==0)][["Column1","Column5"]]

print(df)
print(result)