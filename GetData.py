import pandas as pd


def ProgressData(day):
    file = "./GcsjData/"+str(day)+".csv"
    data=pd.read_csv(file)
    return data 
