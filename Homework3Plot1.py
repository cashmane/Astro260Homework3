import numpy as np
import matplotlib.pyplot as plt

f = open('problem_1_1_data.txt','r')
lines = f.readlines()
data = []
for line in lines:
    if line[0]=='#':
        continue
    else:
        line = line[:-2]
        data.append(line.split(','))
f.close()

x = []
y_exact = []
y_forward = []
y_central = []
for i in range(len(data)):
    x.append(float(data[i][0]))
    y_exact.append(float(data[i][1]))
    y_forward.append(float(data[i][2]))
    y_central.append(float(data[i][3]))


plt.figure(figsize=(15,10))
plt.scatter(x, y_exact, marker='.', color='blue',label='Analytic')
plt.scatter(x, y_forward, marker='.',color='red',label='Forward')
plt.scatter(x, y_central, marker='.',color='orange',label='Central')
plt.xticks([min(x),max(x)])
plt.yticks([min(y_exact),max(y_central)])
plt.title('Analytic vs Forward vs Central Derivatives')
plt.xlabel('Value of X')
plt.ylabel('Value of Derivative of f(x)')
plt.legend()

plt.show()
    
        
