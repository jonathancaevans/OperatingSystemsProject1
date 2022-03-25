import pandas as pd 

def heterogenous_mem(df):
    turnaround = 0
    wait = 0

    processes = sorted(df.to_numpy().tolist(), key=lambda x: x[1])
    elapsed = [0] * 6
    queues = [[] for _ in range(6)]

    low_req = [p for p in processes if p[2] <= 8e9]
    high_req = [p for p in processes if p[2] > 8e9]

    i, j = 0, 0
    while low_req or high_req:
        if high_req:
            queues[3 + j % 3].append(high_req.pop(0))
            j += 1

        if low_req:
            queues[i % 6].append(low_req.pop(0))
            i += 1

    # Calculate wait and turnaround
    for i in range(6):
        for process in queues[i]:
            if i < 3:
                wait += elapsed[i]
                elapsed[i] += process[1]
                turnaround += elapsed[i]
            else:
                wait += elapsed[i]
                elapsed[i] += process[1] / 2 # high-efficiency cores complete twice as fast
                turnaround += elapsed[i]

    return turnaround/df.shape[0], wait/df.shape[0]

if __name__ == "__main__":
    df = pd.read_csv('processes.csv')
    print(heterogenous_mem(df))
