#!/usr/bin/env python
# coding: utf-8

# In[203]:


from statistics import mean #for average 
from Data import Data #importing Data class from data module
from extractData import extractData #importing extractData class from extractData module


# In[ ]:





# In[208]:


data=Data('us_avg_tuition.csv')
lis=data.getData()
extData=extractData(lis)#data to lists

inp=5
#main loop
while inp!=0:

    inp=int(input('Enter your choice: 1) State wise 2) County Wise 0) To Exit  '))
    if(int(inp==1)):#if user choice 1        
        statesFees=[list()]*52# 2d array for storing fee state and years wise
        for i in range(1,len(lis)): #getting states
            fees=extData.tokenize(i)
            statesFees[i]=fees
        avg_us_tut=list()    #average US  Fee
        for j in range(0,12): #for years wise
            summ=0 #sum variale
            for k in range(1,50): #for states
                summ=summ+statesFees[k][j]
            avg_us_tut.append(summ/50) #storing averageUS fee
        avg_us_rise=list()
        for i in range(0,len(avg_us_tut)-1):
            avg_us_rise.append(round(avg_us_tut[i+1]-avg_us_tut[i],2)) #average US rise
        print('Average US Tuition Data: ',end=" ")    
        for i in avg_us_tut:
            print('$'+str(i),end=" ")
        print()    
        print('Average US Tuition Rises: ',end=" ")    
        for i in avg_us_rise:
            print('$'+str(i),end=" ")
        print()    
        print('Prediction Recent: ','$'+str(mean(avg_us_rise)*12+mean(avg_us_tut)))
        print('Prediction Overall: ','$'+str(mean(avg_us_rise)*16+mean(avg_us_tut)))    

        #for state wise
    elif inp==2:
        st=input('Enter State: ')
        st=st+','
        fees=extData.tokenize(extData.stateToIndex(st))
        rises=list()
        print('State: ',st)
        print('Tuition Data: ', end=" ")
        for f in range(len(fees)):
            print('$'+str(fees[f]),end=" ")
        for i in range(0,len(fees)-1):
            rises.append(fees[i+1]-fees[i])
        print()  
        print('Tuition Rises: ',end=" ")
        for i in rises:
            print('$'+str(i),end=" ")
        print()    
        print('Average Tuition: '+'$'+str(mean(fees)))
        print('Average Rises: '+'$'+str(mean(rises)))
        print('Prediction Recent: ','$'+str(mean(rises)*12+mean(fees)))
        print('Prediction Overall: ','$'+str(mean(rises)*16+mean(fees)))





    


# In[135]:





# In[ ]:





# In[ ]:




