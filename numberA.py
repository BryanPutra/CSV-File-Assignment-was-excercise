import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt
with open('activity.csv','r') as file:
    datas = csv.reader(file)
    sum_of_steps = {}
    for i in datas:
        if i[0] != "NA" and i[0] != "steps":
            if i[1] not in sum_of_steps:
                sum_of_steps[i[1]] = [int(i[0])] # if the date from the i[1] is not in the dictionary then the dictionary will get the date to its keys and get the value from the first index of the i
            else:
                sum_of_steps[i[1]].append(int(i[0]))

total_per_day = {}
mean_total_per_day = {}

for key, value in sum_of_steps.items():
    total_per_day[key] = sum(value)
    mean_total_per_day [key] = statistics.mean(value)

print(total_per_day)
print(mean_total_per_day)

N = len(sum_of_steps)
meantotalperday = tuple(mean_total_per_day.values())
ind = np.arange(N)
width = 1

p1 = plt.bar(ind, meantotalperday, width)

plt.ylabel('Average Steps')
plt.title('Mean Total per Day')
plt.xticks(ind, mean_total_per_day.keys())
plt.yticks(np.arange(0,101,10))

plt.show()








