#for extracting data into its useable form
import csv
class extractData:
    def __init__(self, data):
        self.data=data
        self.state=[]
     #convert whole state string to money tokens    
    def tokenize(self,ind):
        self.state=self.data[ind][0].split('"')
        moneys=list()
        
        for i in range(1,len(self.state)-1):
            if self.state[i]!=',':
                numb=self.state[i].replace('$','')
                numb=numb.replace(',','')
                moneys.append(int(numb))
        return moneys
    #convert state name to its index in file
    def stateToIndex(self,st):
        for i in range(0,len(self.data)):
            self.state=self.data[i][0].split('"')
            sta=list()
            for j in range(0,len(self.state)):
                if self.state[j]==st:
                    return i
