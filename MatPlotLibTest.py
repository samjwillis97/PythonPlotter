import matplotlib.pyplot as plt
import csv

file = "testFiles/VPU5LBP_Trend_2020.06.23_19.00.00.csv"

index=[]
y=[]

with open(file, 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    print(plots)
    next(plots)
    next(plots)
    for row in plots:
        index.append(float(row[0]))
        y.append(float(row[1]))


plt.plot(index,y, marker='o')

plt.title('Data from the CSV File: People and Expenses')

plt.xlabel('Number of People')
plt.ylabel('Expenses')

plt.show()

