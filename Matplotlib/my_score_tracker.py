import matplotlib.pyplot as plt

days   =['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [65, 77 , 90, 35, 10]

plt.plot(days,scores)
plt.show()

plt.plot(days, scores)
plt.title('My quiz score tracker')
plt.xlabel('Day of the week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0,100)
plt.show()

plt.plot(days, scores, color='Blue', marker='o', linestyle='dashed',linewidth=2)
plt.title('My quiz score tracker')
plt.xlabel('Day of the week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0,100)
plt.show()

plt.bar(days, scores, color='Orange')
plt.title('My quiz score bar Chart')
plt.xlabel('Day of the week')
plt.ylabel('score')
plt.ylim(0, 100)
plt.show()


