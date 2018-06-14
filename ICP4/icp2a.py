import numpy as ny
#x = ny.random.random((10,10))
x=ny.random.randint(1,10,size=(10,10))
print(x)
count=0
print("Minimum Value is:",x.min(axis=1))
print("Maximum Value is:",x.max(axis=1))
#for i in x:
 #  xmin=i.min()
  # xmax=i.max()
   #count=count+1
   #print("Minimum Value in " + str(count)+"th row:"+ str(xmin))
   #print("Maximum Value in "+  str(count)+"th row:"+ str(xmax))

