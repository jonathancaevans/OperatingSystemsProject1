import pandas as pd
import matplotlib.pyplot as plt

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

    for i, process in enumerate(processes[len(processes)//2:]):
        queues[(i % 3)+3].append(process)

    for i, process in enumerate(processes[:len(processes)//2]):
        queues[(i % 3)].append(process)

    #graph processes in queues
    queueName=["LS1","LS2","LS3","HS4","HS5","HS6"]
    avgBurstPerQueue = []
    for i in range(6):
        avgBurst = 0
        for process in queues[i]:
            avgBurst += process[1]

        avgBurstPerQueue.append(avgBurst/len(queues[i]))

    fig, ax = plt.subplots()
    ax.bar(queueName, avgBurstPerQueue, color ='green',width = 0.5)

    ax.set_ylabel('Cycles')
    ax.set_title('Average burst time per processor')

    plt.savefig('Question2AverageBurstTimePerProcessor.png',dpi=400)


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
