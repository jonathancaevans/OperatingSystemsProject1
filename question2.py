import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def heterogenous(df):
    clockSpeeds = [1,1,1,2,2,2]
    turnaround = 0
    wait = 0

    processes = df.to_numpy().tolist()

    processors = []
    for i in range(6):
        processors.append(0)

    queues = []
    for i in range(6):
        queues.append([])

    processes.sort(key = lambda x: x[1])
    
    while len(processes) > 5:
       a,b,c = processes.pop(0),processes.pop(0),processes.pop(0)

       i = 0

       while((i < len(processes) - 3) and (a[1] < processes[i][1]/2)):
           i+=1

       d,e,f = processes.pop(i),processes.pop(i),processes.pop(i)

       queues[0].append(a)
       queues[1].append(b)
       queues[2].append(c)
       queues[3].append(d)
       queues[4].append(e)
       queues[5].append(f)

    i=5
    while len(processes) > 0:
       queues[i].append(processes.pop())
       i-=1

    #Calculate wait and turnaround
    for i in range(6):
       for process in queues[i]:
           if i < 3:
               wait += processors[i]
               processors[i] += process[1]
               turnaround += process[i]
           else:
               wait += processors[i]
               processors[i] += process[1]  
               turnaround += processors[i]

    return turnaround/df.shape[0], wait/df.shape[0]

if __name__ == "__main__":
    df = pd.read_csv('processes.csv')
    print(heterogenous(df))
    
