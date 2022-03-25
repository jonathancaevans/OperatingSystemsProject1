import pandas as pd 

def heterogenous_seq(df):
    queues = [[] for _ in range(6)]

    i, j = 0, 0
    for process in df.to_numpy().tolist():
        # high memory req; must run with high capacity memory
        if process[2] > 8e9:
            queues[3 + j % 3].append(process)
            j += 1
            continue

        queues[i % 6].append(process)
        i += 1

    # Calculate wait and turnaround
    wait = 0
    turnaround = 0
    elapsed = [0] * 6
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
    print(heterogenous_seq(df))
