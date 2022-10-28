
import numpy as np

# numbers=np.arange(5,25,3)
# print(numbers)

# result=numbers[0]
# result=numbers[5]
# result=numbers[-1]
# result=numbers[-3]
# result=numbers[0:5]
# result=numbers[3:5]
# result=numbers[::]
# result=numbers[::-1]

numbers2=np.arange(1,10).reshape(3,3)
print(numbers2)

result=numbers2[0]
result=numbers2[2]
result=numbers2[1][0]
result=numbers2[0][2]
result=numbers2[0:][1]
result=numbers2[:,1]
result=numbers2[:2,:2]
result=numbers2[-1,:]
result=numbers2[-1,0:2]




print(result)






