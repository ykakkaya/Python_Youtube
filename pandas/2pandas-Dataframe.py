
import numpy as np

import pandas as pd

numbers=np.random.randint(1,50,10)
df=pd.DataFrame(numbers,columns=["numbers"])



liste=[["a",1],["b",2],["c",3],["d",4]]
df=pd.DataFrame(liste, columns=["harf","sıra"])


dict={"plakalar":[1,6,34,35,38],"şehirler":["adana","ankara","istanbul","izmir","kayseri"]}

df=pd.DataFrame(dict,index=[1,6,34,35,38])


print(df)