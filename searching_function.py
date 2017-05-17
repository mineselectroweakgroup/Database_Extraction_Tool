# -*- coding: utf-8 -*-
"""
Hayden Blair
Electro Weak Interactions Group

Searching Function
"""

from data_array import final

def acquire(Q_low,Q_high,A_low,A_high,Theory=False,Sym=False):
    '''
    This is going to be the complete searching function that will take
    in user inputs from the GUI, and return the desired values from the 
    data array.
    '''

    '''
    Here I am going to make it so that the acquire function can handle the inputs as strings. That way, the code
    will interface with GUI.
    '''
    
    args=[Q_low,Q_high,A_low,A_high]
    args_str=['Qlow','Qhigh','Alow','Ahigh']
    
    for i in range(0,len(args)):
        if args[i] == "":
            globals()[args_str[i]] = False
        else:
            globals()[args_str[i]] = float(args[i])
        
    
    pdat = []
    if Theory == False:
        for i in final:
            if len(i) == 14:
                pdat.append(i)
    elif Theory == True:
        for i in final:
            if len(i) == 15:
                del(i[14])
                pdat.append(i)
            else:
                pdat.append(i)
    '''
    Creates a psuedo array that can contain the theoretical values if the user wants them
    The rest of the function then removes all of the different nucleons that do not
    satisfy the user's specifications
    '''

    '''
    This next section uses each one of the user specifications to search through the'
    database, and flags each one of the rows that does not match the desired parameters.
    Once the proper entries have all been flagged, they will be removed before the pseudo
    array is returned to the user.
    '''


#Q value range
    if Qhigh == False and Qlow == False:
        pass
    elif Qhigh == False and Qlow != False:
        for i in range(0,len(pdat)):
            if float(pdat[i][5]) < Qlow:
                pdat[i].append('r')
    elif Qhigh!= False and Qlow == False:
        for i in range(0,len(pdat)):
            if float(pdat[i][5]) > Qhigh:
                pdat[i].append('r')
    elif Qhigh != False and Qlow != False:
        for i in range(0,len(pdat)):
            if float(pdat[i][5]) < Qlow or float(pdat[i][5]) > Qhigh:
                pdat[i].append('r')

#Nucleon range                
    if Ahigh == False and Alow == False:
        pass
    elif Ahigh == False and Alow != False:
        for i in range(0,len(pdat)):
            if eval(pdat[i][3]) < Alow:
                pdat[i].append('r')
    elif Ahigh!= False and Alow == False:
        for i in range(0,len(pdat)):
            if eval(pdat[i][3]) > Ahigh:
                pdat[i].append('r')
    elif Ahigh != False and Alow != False:
        for i in range(0,len(pdat)):
            if eval(pdat[i][3]) < Alow or eval(pdat[i][3]) > Ahigh:
                pdat[i].append('r')

#Chemical Symbol
    if Sym == False:
        pass
    elif Sym != False:
        for i in range(0,len(pdat)):
            if pdat[i][4] != Sym:
                pdat[i].append('r')

    '''
    Now the program runs back through the entire pseudo data array and looks at the
    last column in every row. If the last column is the flag 'r', that row is removed.
    The removal starts at the back of the array and moves forward, so that the array's
    entries do not get their placeholders mixed up as the flagged entries are removed.
    '''

#Removal of flagged entries
    for i in reversed(range(0,len(pdat))):
        if pdat[i][len(pdat[i])-1] == 'r':
            del(pdat[i])

    return pdat
           

    
        
            

