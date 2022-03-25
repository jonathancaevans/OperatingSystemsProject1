import pandas as pd 

def heterogenous_mem(df):
    turnaround = 0
    wait = 0

    processes = sorted(df.to_numpy().tolist(), key=lambda x: x[1])
    elapsed = [0] * 6
    queues = [[] for _ in range(6)]

    low_req = [p for p in processes if p[2] <= 8e9]
    high_req = [p for p in processes if p[2] > 8e9]

    for i, process in enumerate(high_req):
        queues[3 + i % 3].append(process)

    for i, process in enumerate(low_req):
        queues[i % 3].append(process)

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
