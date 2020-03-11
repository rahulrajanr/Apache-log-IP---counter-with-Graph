import sys
import os
import collections
import matplotlib.pyplot as plt
ipcounter = collections.Counter()
x = []
y = []
if len(sys.argv) == 3:

  file = sys.argv[1] 
  count = sys.argv[2]
 
  if os.path.isfile(file) and count.isdigit():
    fh = open(file)

    for line in fh:
      ipcounter.update([line.split()[0]])

for ip in ipcounter:
  if ipcounter[ip] > int(count):
    print('{}-{}'.format(ip,ipcounter[ip]))    
    x.append(ip)
    y.append(ipcounter[ip])

plt.bar(x,y)
plt.show()
