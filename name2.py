import plotly.express as px
import csv
import numpy as np
def getdatasource(data_path):
    average1=[]
    sizeofTV1=[]
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeofTV1.append(float(row['sizeofTV']))
            average1.append(float(row['average']))
    return{'x':sizeofTV,'y':average}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between sizeofTV vs average:',correlation[0,1])
def setup():
    data_path = './TV.csv'
    datasource = getdatasource(data_path)
    findcorrelation(datasource)
setup()