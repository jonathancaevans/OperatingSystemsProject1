import pandas as pd

def heterogenous(df: pd.DataFrame) -> tuple[float, float]:
    """
    Implementation of the SJF scheduling algorithm with high-efficiency cores.

    Parameters: 
        df (pandas dataframe): Dataframe containing process information.

    Returns:
        tuple[float, float]: The average turnaround time and wait time.
    """

    # sort the process list by burst time, ascending
    processes = sorted(df.to_numpy().tolist(), key=lambda x: x[1])
    queues = [[] for _ in range(6)]

    for i, process in enumerate(processes):
        queues[i % 6].append(process)

    # Calculate wait and turnaround
    wait = 0
    turnaround = 0
    processors = [0] * 6
    for i in range(6):
        for process in queues[i]:
            if i < 3:
                wait += processors[i]
                processors[i] += process[1]
                turnaround += processors[i]
            else:
                wait += processors[i]
                processors[i] += process[1] / 2 # high-efficiency cores complete twice as fast
                turnaround += processors[i]

    return turnaround/df.shape[0], wait/df.shape[0]

def main():
    df = pd.read_csv('processes.csv')
    print(heterogenous(df))

if __name__ == "__main__":
    main()
