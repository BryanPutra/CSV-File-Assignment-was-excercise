import csv
import matplotlib.pyplot as plt
import statistics
import numpy as np

with open('activity.csv','r') as file:
    datas = csv.reader(file)
    mydict = {}
    for i in datas:
        if i[0] != "NA" and i[0] != 'steps':
            if i[2] not in mydict:
                mydict[i[2]] = [int(i[0])]
            else:
                mydict[i[2]].append(int(i[0]))

totalpertime = {}
mean_totaltime = {}
median_pertime = {}
for key, value in mydict.items():
    totalpertime[key] = sum(value)
    mean_totaltime[key] = statistics.mean(value)

print(totalpertime)
print(mean_totaltime)


