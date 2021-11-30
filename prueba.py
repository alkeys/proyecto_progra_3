import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
a3=1
b3=-6
c3=8
d3=0
y=[]
x=[]
for i in range(-5,6):
    x.append(i)
    y.append((a3*(pow(i,3)))+(b3*(pow(i,2)))+(i*c3)+d3)
plt.plot(x,y, 'g')
plt.show()
