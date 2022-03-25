import pandas as pd
import numpy as np

def FIFO(df, n):
    processes = df.to_numpy().tolist()

    turnaround = 0
    wait = 0

    processors = []
    for i in range(n):
        processors.append([])

    for i, processor in enumerate(processors):
        process = processes.pop(0)
        processors[i] = process[1]
        turnaround += process[1]

    for process in processes:
        nextOpen = processors.index(min(processors))

        wait+=processors[nextOpen]

        processors[nextOpen] += process[1]

        turnaround += processors[nextOpen]

    return turnaround/df.shape[0], wait/df.shape[0]

def SJF(df, n):
    processes = df.to_numpy().tolist()

    processes.sort(key = lambda x: x[1])

    turnaround = 0
    wait = 0

    processors = []
    for i in range(n):
        processors.append([])

    for i, processor in enumerate(processors):
        process = processes.pop(0)
        processors[i] = process[1]
        turnaround += process[1]

    for process in processes:
        nextOpen = processors.index(min(processors))

        wait+=processors[nextOpen]

        processors[nextOpen] += process[1]

        turnaround += processors[nextOpen]

    return turnaround/df.shape[0], wait/df.shape[0]

if __name__ == "__main__":
    df = pd.read_csv('processes.csv')
    print(FIFO(df,6))
    print(SJF(df,6))
