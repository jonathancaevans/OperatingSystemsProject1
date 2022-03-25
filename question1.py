from collections import deque
import pandas as pd

def FIFO(df: pd.DataFrame, n: int) -> tuple[float, float]:
    """
    Implementation of the FIFO scheduling algorithm.

    Parameters: 
        df (pandas dataframe): Dataframe containing process information.
        n (int): Number of processors available.

    Returns:
        tuple[float, float]: The average turnaround time and wait time.
    """

    processes = df.to_numpy().tolist()

    # pop the first N processes and add them to the turnaround
    processors = [processes.pop(0)[1] for _ in range(n)]
    turnaround = sum(burst_time for burst_time in processors)
    wait = 0

    for process in processes:
        # get the processor with the smallest remaining time,
        # and add it to the sum
        nextOpen = processors.index(min(processors))

        wait+=processors[nextOpen]

        processors[nextOpen] += process[1]

        turnaround += processors[nextOpen]

    return turnaround/df.shape[0], wait/df.shape[0]

def SJF(df: pd.DataFrame, n: int) -> tuple[float, float]:
    """
    Implementation of the Shortest Job First scheduling algorithm.

    Parameters: 
        df (pandas dataframe): Dataframe containing process information.
        n (int): Number of processors available.

    Returns:
        tuple[float, float]: The average turnaround time and wait time.
    """

    # sort the process list by burst time, ascending
    processes = sorted(df.to_numpy().tolist(), key=lambda x: x[1])

    # pop the first N processes and add them to the turnaround
    processors = [processes.pop(0)[1] for _ in range(n)]
    turnaround = sum(burst_time for burst_time in processors)
    wait = 0

    for process in processes:
        # get the processor with the smallest remaining time,
        # and add it to the sum
        nextOpen = processors.index(min(processors))

        wait+=processors[nextOpen]

        processors[nextOpen] += process[1]

        turnaround += processors[nextOpen]

    return turnaround/df.shape[0], wait/df.shape[0]

def RR(df: pd.DataFrame, n: int, quantum: int) -> tuple[float, float]:
    """
    Implementation of the Round Robin scheduling algorithm.

    Parameters: 
        df (pandas dataframe): Dataframe containing process information.
        n (int): Number of processors available.
        quantum (int): The time quantum to use.

    Returns:
        tuple[float, float]: The average turnaround time and wait time.
    """

    # list of [total burst time, remaining time] for each process
    # represents the ready queue
    ready = deque([rec[1], rec[1]] for rec in df.to_numpy().tolist())

    turnaround = 0
    wait = 0

    processors = deque(ready.popleft() for _ in range(n)) # contains currently executing processes
    elapsed = [0] * n # total elapsed time per processor

    while len(processors) > 0:
        # visit each current process
        for i in range(len(processors)):
            process = processors.popleft()

            # p_burst = burst time of the process
            # p_rem = remaining execution time of the process
            p_burst, p_rem = process

            if p_rem > quantum:
                # if the remaining time is greater than the quantum,
                # the process should be inserted at the end of the ready queue
                process[1] -= quantum
                elapsed[i] += quantum
                ready.append(process)
            else:
                # if the remaining time is less than or equal to the quantum,
                # the process is done executing and can be added to the sum
                elapsed[i] += p_rem
                turnaround += elapsed[i]
                wait += elapsed[i] - p_burst

            # add the next process in the ready queue
            if len(ready) > 0:
                processors.append(ready.popleft())

    return turnaround/df.shape[0], wait/df.shape[0]

def main():
    df = pd.read_csv('processes.csv')
    print('FIFO:', FIFO(df,6))
    print('SJF :', SJF(df,6))
    print('RR  :', RR(df, 6, 10**13))

if __name__ == "__main__":
    main()
