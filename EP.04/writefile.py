# writefile.py program name
def writedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('5888')

def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        #file.write(text)
        file.write(text + '\n')

def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        data = file.readlines()
        #data = file.read()
        print(data)

#readdata()
adddata('00000')
#writedata()
