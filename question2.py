import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def main():
    n = 250
    #create list with all core speeds
    speeds = [2,2,2,4,4,4]
    #create list with all core names
    names = ["PA", "PB", "PC", "PD", "PE", "PF"]
    #create dataframe with core speeds and names
    df = pd.DataFrame({"Speed": speeds, "Name": names})
    #create list of runtimes
    df["Burst Times"] = np.random.randint(10000000,100000000000, size = 6)
    #create list of memory requirements
    df["Memory"] = np.random.randint(1,16000, size = 6)
    print(df)
    #sort dataframe by increasing speed
    df.sort_values(by = "Speed", inplace = True)
    print(df)
    #initalize total runtime and total memory
    total_runtime = 0
    total_memory = 0
