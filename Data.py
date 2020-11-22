#For Reading CSV
import csv
class Data:
    def __init__(self, filename):
        self.file=filename
    def getData(self):
        items=list()
        with open(self.file, 'r') as file:
            r = csv.reader(file, delimiter = '\t')
            for x in r:
                items.append(x)
            return items    


# In[ ]:




