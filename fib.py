import matplotlib.pyplot as plt

#Define variables
x = 0
y = 1
z= x+y

a = x
b = -y
count = 0

x_list = [0, 0]
y_list = [0, 1]

#Set a limit to stop the function eventually
while z <=100:
    #Perform fibinocci sequence
    z = x+y
    x = y
    y = z

    #Make Coordinates
    count +=1
    if ((count%4 == 1)):
        a = x
        b = y
    elif ((count%4 == 2)):
        a = -x
        b = y
    elif ((count%4 == 3)):
        a = -x
        b = -y
    elif ((count%4 == 0)):
        a = x
        b = -y

    #Add coordinates to list
    x_list.append(a)
    y_list.append(b)




#Plot Coordinates
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x_list,y_list, 'g')
plt.show()

