from selsort import huh3
from quickSort import quickSort
from insertionSort import insertionSort
import time
import matplotlib.pyplot as plt
import sys

marr = []
for i in range(8):
    f = open('readydata8' + str(i + 1) + '.txt', "r", encoding="utf-8")
    arr = []
    for j in f.readlines():
        tikit = j.split()
        if(len(tikit) == 6 and tikit[4].isnumeric()):
            arr.append(j.split())
    marr.append(arr)
    f.close()

class ticket:
    def __init__(self, owner_name:list, cabin_number:int, cabin_type:int, dest_point:str):
        self.owner_name = owner_name
        self.cabin_number = cabin_number
        self.cabin_type = cabin_type
        self.dest_point = dest_point

    def __gt__(self, other): # >
        if self.cabin_number > other.cabin_number:            
            return True
        else:
            return False
        
    def __ge__(self, other): # >=
        if self.cabin_number >= other.cabin_number:
            return True
        else:
            return False

    def __lt__(self, other): # <
        if self.cabin_number < other.cabin_number:
            return True
        else:
            return False

    def __le__(self, other): # <=
        if self.cabin_number <= other.cabin_number:
            return True
        else:
            return False

ticketmarr = []
for j in range(len(marr)):
    ticketarr = []
    for i in range(len(marr[j])):
        ticketarr.append(ticket(marr[j][i][:3], int(marr[j][i][3]), int(marr[j][i][4]), marr[j][i][5]))
    ticketmarr.append(ticketarr)
    
oarr = []
tm = []
tmtmp = []

for i in range(8):
    start = time.time()
    oarr.append(huh3(ticketmarr[i]))
    tmtmp.append(time.time() - start)
    f = open('selsorted' + str(i + 1) + '.txt', "w", encoding="utf-8")
    for j in range(len(oarr[i])):
        print(i, j)
        f.write(oarr[i][j].owner_name[0] + " " + oarr[i][j].owner_name[1] + " " + oarr[i][j].owner_name[2] + " " + str(oarr[i][j].cabin_number) + " " + str(oarr[i][j].cabin_type) + " " + oarr[i][j].dest_point + "\n")
    f.close()
    
oarr = []
tm.append(tmtmp)
tmtmp = []

for i in range(8):
    start = time.time()
    oarr.append(insertionSort(ticketmarr[i]))
    tmtmp.append(time.time() - start)
    f = open('inssorted' + str(i + 1) + '.txt', "w", encoding="utf-8")
    for j in range(len(oarr[i])):
        f.write(oarr[i][j].owner_name[0] + " " + oarr[i][j].owner_name[1] + " " + oarr[i][j].owner_name[2] + " " + str(oarr[i][j].cabin_number) + " " + str(oarr[i][j].cabin_type) + " " + oarr[i][j].dest_point + "\n")
    f.close()
    
oarr = []
tm.append(tmtmp)
tmtmp = []

sys.setrecursionlimit(100000)

for i in range(8):
    start = time.time()
    oarr.append(quickSort(ticketmarr[i]))
    tmtmp.append(time.time() - start)
    f = open('quicksorted' + str(i + 1) + '.txt', "w", encoding="utf-8")
    for j in range(len(oarr[i])):
        f.write(oarr[i][j].owner_name[0] + " " + oarr[i][j].owner_name[1] + " " + oarr[i][j].owner_name[2] + " " + str(oarr[i][j].cabin_number) + " " + str(oarr[i][j].cabin_type) + " " + oarr[i][j].dest_point + "\n")
    f.close()
    
oarr = []
tm.append(tmtmp)
tmtmp = []

print(tm[0])
print(tm[1])
print(tm[2])

plt.plot([12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[0], [12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[1], [12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000], tm[2])
plt.legend(["Selection sort", "Insertion sort", "Quick sort"])
plt.show()
