from collections import deque
import pandas as pd
import numpy as np

def FIFO(df, n):
    processes = df.to_numpy().tolist()

    processors = [processes.pop(0)[1] for _ in range(n)]
    turnaround = sum(burst_time for burst_time in processors)
    wait = 0

    for process in processes:
        nextOpen = processors.index(min(processors))

        wait+=processors[nextOpen]

        processors[nextOpen] += process[1]

        turnaround += processors[nextOpen]

    return turnaround/df.shape[0], wait/df.shape[0]

def SJF(df, n):
    processes = sorted(df.to_numpy().tolist(), key = lambda x: x[1])

    processors = [processes.pop(0)[1] for _ in range(n)]
    turnaround = sum(burst_time for burst_time in processors)
    wait = 0

    for process in processes:
        nextOpen = processors.index(min(processors))

        wait+=processors[nextOpen]

        processors[nextOpen] += process[1]

        turnaround += processors[nextOpen]

    return turnaround/df.shape[0], wait/df.shape[0]

def RR(df, n, quantum):
    # list of burst times & remaining times
    ready = deque([rec[1], rec[1]] for rec in df.to_numpy().tolist())

    turnaround = 0
    wait = 0

    # contains currently executing processes
    processors = deque(ready.popleft() for _ in range(n))
    elapsed = [0] * n # total elapsed time per processor

    while len(processors) > 0:
        # visit each current process
        for i in range(len(processors)):
            process = processors.popleft()
            p_burst, p_rem = process

            if p_rem > quantum:
                process[1] -= quantum
                elapsed[i] += quantum
                ready.append(process)
            else:
                elapsed[i] += p_rem
                turnaround += elapsed[i]
                wait += elapsed[i] - p_burst

            if len(ready) > 0:
                processors.append(ready.popleft())
    
    return turnaround/df.shape[0], wait/df.shape[0]


if __name__ == "__main__":
    df = pd.read_csv('processes.csv')
    print(FIFO(df,6))
    print(SJF(df,6))
    print(RR(df, 6, 10**13))
