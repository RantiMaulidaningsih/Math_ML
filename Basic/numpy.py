import numpy as np
#find the angle --> also can replace cos by sin tan etc
#example
x = [1,1]
y= [-1,1]
A = ([(2,-1), (-1, 4)])
cos = np.cos(x.T@A@y / sqrt(x.T@A@x * y.T@A@y)**1/2)
Angle = np.arccos(cos)
return Angle
#round for some nomber after . in decimal
retunr np.round(Angle,2)
#array to make matriks, vector, and array
matriks = np.array([[1,1],
                [-3,-3],
                [2,2],
                [0,2],
                [-2,0],
                [1,3],
                [4,4]])
#mean to search mean in data set 
mean_data = np.mean(data, axis=0)
