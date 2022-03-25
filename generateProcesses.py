import pandas as pd
import numpy as np
import random


def create_processes(n):

    """Creates a dataframe of processes with associated burst time and memory requirements.

    Parameters: 
        n (int): Number of processes to be generated. 

    Returns: 
        df (pandas dataframe): Dataframe containing process information. 

    """

    # Create an empty list to store process information in the form of dictionaries.  
    process_list = []    

    for i in range(n):   # Iterate through each process, creating a dictionary for each one and appending it to the list. 

        # Create a dictionary for each process, with keys 'process number', 'burst time', and 'memory requirement'.  
        d = {'process number': i + 1, 'burst time': random.randint(10**7, 10**13), 'memory requirement': random.randint(1000000, 16000000000)}     # Generate burst times between 10^7 - 10^13 cycles and memory requirements between 1MB - 16GB at random using randint().  
        
        process_list.append(d)   # Append the dictionary to the list. 

    df = pd.DataFrame(process_list)   # Convert the list of dictionaries into a pandas dataframe. 

    return df

if __name__ == "__main__":
    processes = create_processes(250)
    processes.to_csv("processes.csv", index=False)
