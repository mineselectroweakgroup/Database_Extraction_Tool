#Created by Will McDonald
#for use in dataClass.py
#created 6/5/17

#This file can be used to define functions that are used in other files


from decimal import *
#called as addUncert(filtDataSet,line) in dataClass.py where 'line' is the current line in the ensdf file
def addUncert(datalist, currentLine): 
#    print(datalist[-1])
#    print(currentLine)
#    print('\n')
    #Ground state has 0 uncertainty
    if (currentLine[2]=='0.0'):
        uncert = '0'
    #the elif statements will remove the spin from currentLine[3], leaving only the unscaled uncertainty behind
    #if line[3] contains '('
    elif ('(' in currentLine[3]):
        uncert = currentLine[3][:currentLine[3].find('(')]
    #if line[3] contains no parentheses but does have a '+' or '-'
    elif (('+' in currentLine[3]) or ('-' in currentLine[3])):
        uncert = currentLine[3][:currentLine[3].find(datalist[-1][1])]
    #if there are no spin values in line[3]
    else:
        uncert = currentLine[3]
    
    #Will only append an uncertainty if there isn't already an uncertainty for a given line
    if len(datalist) == 0:
        pass
    elif (len(datalist[-1])<3): 
        #empty uncert value
        if (uncert==''):
            datalist[-1].append(0) 
        else:
            #some lines include 'AP' as the uncertainty. This sets these cases to uncert=0
            if(not uncert.isnumeric()):
                uncert = "0"
            elif ('.' in currentLine[2]):    #this block converts uncert to the appropriate magnitude
                #numberino is the energy value
                numberino=currentLine[2] 
                topLimit = 0
                
                for i in range(len(numberino)-1):
                    if (numberino[-1-i]=='.'):
                        decIndex = i
                        numberino = numberino[:-i-1] + numberino[-i:]
     
                    if (i<len(uncert)):
                        digit = int(numberino[-1-i])+int(uncert[-1-i])
                    else:
                        digit = int(numberino[-1-i])
                    topLimit=digit*(10**i)+topLimit
                
                if ('.' in currentLine[2]):
                    topLimitFloat = str(topLimit)[:-decIndex]+'.'+str(topLimit)[-decIndex:]
                else:
                    topLimitFloat = topLimit
                uncert = str(Decimal(topLimitFloat)-Decimal(currentLine[2]))
#            else: #no '.' in currentLine[2] and uncert != 0
            
            #append the value of uncert to be read as the uncertainty to be plotted    
            datalist[-1].append(float(uncert))
