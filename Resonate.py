import random
import numpy as np
import matplotlib.pyplot as plt

total = 0.0
highest = 0.0
testsize = 1000000
casterlvl = 6
distribution = {}
for x in range(0,int(testsize)):
    count = 0
    for y in range(0,1+(casterlvl/2)):
        flip = True
        while flip:
            count += 1
            if random.randint(0,1) == 0:
                flip = False
    total += count
    if count > highest:
        highest = count
    if count not in distribution:
        distribution[count] = 1
    else:
        distribution[count] += 1

print "In " + str(int(testsize)) + " attemps..."
print "Highest damage: " + str(highest)
print "Average damage: " + str(total/testsize)
for x in range(2,highest+1):
    if x in distribution:
        print str(x) + ": " + str(distribution[x]/testsize)
higherthaninflict = 0
for x in range(14, highest+1):
    if x in distribution:
        higherthaninflict += distribution[x]/testsize
print "Percent greater than the Maximum of ILW: " + str(higherthaninflict)
arr = []
for x in range(0,highest+1):
    arr.append(0)
for key in distribution:
    arr[key] = float(distribution[key])
nparr = np.array(arr)

for x in range(0,len(nparr)):
    nparr[x] = arr[x]/testsize

fig = plt.figure()
ax = plt.subplot(111)
ax.bar(range(0,len(nparr)),nparr, width=1)

ax.set_ylabel('Percentage')
ax.set_title('Damage delt, Average: ' + str(round(total/testsize, 2)))
plt.xticks(np.arange(0, highest+1, 1.0))
plt.show()
