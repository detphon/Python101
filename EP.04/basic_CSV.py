import csv

def writecsv(datalist):
    with open('basic_CSV.csv','a',encoding='utf-8',newline='') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(datalist)

def readcsv():
    with open('basic_CSV.csv',encoding='utf-8',newline='') as file:
        filereader = csv.reader(file)
        data = list(filereader)
    return data

data = ['ดังโงะ',20,'7.00']
writecsv(data )
#data = readcsv()
#print(data)

