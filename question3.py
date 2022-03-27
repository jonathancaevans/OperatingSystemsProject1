import pandas as pd


def heterogenous_mem(df: pd.DataFrame) -> tuple[float, float]:
    """
    Implementation of the SJF scheduling algorithm with high-efficiency cores
    and memory requirements.

    Parameters:
        df (pandas dataframe): Dataframe containing process information.

    Returns:
        tuple[float, float]: The average turnaround time and wait time.
    """

    # sort the process list by burst time, ascending
    processes = sorted(df.to_numpy().tolist(), key=lambda x: x[1])
    queues = [[] for _ in range(6)]

    low_req = [p for p in processes if p[2] <= 8e9]
    high_req = [p for p in processes if p[2] > 8e9]

    i, j = 0, 0
    while low_req or high_req:
        if high_req:
            # assign processes which require > 8gb to only processors 3-6
            queues[3 + j % 3].append(high_req.pop(0))
            j += 1

        if low_req:
            # assign processes which require <= 8gb to any processor
            queues[i % 6].append(low_req.pop(0))
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
                elapsed[i] += (
                    process[1] / 2
                )  # high-efficiency cores complete twice as fast
                turnaround += elapsed[i]

    return turnaround / df.shape[0], wait / df.shape[0]


def main():
    df = pd.read_csv("processes.csv")
    print(heterogenous_mem(df))


if __name__ == "__main__":
    main()
