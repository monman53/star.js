import pandas as pd
import math

data  = pd.read_csv("./HYG-Database/hygdata_v3.csv")
num = 119613
hip = data['hip'].fillna(-1).astype(int)
x = data['x']
y = data['y']
z = data['z']
mag = data['mag']
ci = data['ci'].fillna(0)

print('star_data = {', end='')
print('"table" : { "hip" : 0, "x" : 1, "y" : 2, "z" : 3, "mag" : 4, "ci" : 5, },', end='')
print('"data" : [', end='')
for i in range(num):
	if i==0:
		continue
	print('[', end='')
	print(hip[i], end=',')
	l = math.sqrt(x[i]*x[i]+y[i]*y[i]+z[i]*z[i])
	print(x[i]/l, end=',')
	print(y[i]/l, end=',')
	print(z[i]/l, end=',')
	print(mag[i], end=',')
	print(ci[i], end=',')
	print(']', end='')
	print(',', end='')
print('],', end='')
print('}')