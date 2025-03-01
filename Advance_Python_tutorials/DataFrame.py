import pandas as pd
import datetime
import time
'''
This program reads n(DataChunkSize) lines at a time and write to txt files. 
'''
Input_dataFrame = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
DataChunkSize=20
SeekCursorFrom=0
SeekCursorTo=0
folder_name=r"C:\Users\anils\PycharmProjects\pythonProject\files\\"

for SeekCursorFrom in range(0,Input_dataFrame.shape[0],DataChunkSize):
    filename1 = folder_name + datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f") + ".txt"
    with open(filename1, 'a') as f:
                dfAsString = Input_dataFrame[SeekCursorFrom:SeekCursorTo+DataChunkSize].to_string(header=False, index=False)
                ###print(dfAsString)
                f.write(dfAsString)
    SeekCursorTo=SeekCursorFrom + DataChunkSize
    time.sleep(10)

