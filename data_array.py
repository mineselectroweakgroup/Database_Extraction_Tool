# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:19:52 2016

@author: hblair
"""
import re


a = open('mass.AME12.txt','r')
data =''.join(a.readlines())
find = re.compile('\n.+\n').findall(data)
'''
Here, I searched the long string data, and seperated it into a list of strings,
each of which represents one row of the data
'''


final = []
for i in find:
    final.append(re.compile('\n?\S+').findall(i))

'''
This for loop takes each string that is an element of the list find, and seperates
it into another list whose entries are the specific columns of the data set. Now,
final is an array where final[i] represents the ith row of the data set and where
final[i][j] represents the jth column of the ith row of the data set.

When called, final[i][j] will return a single string that represents the information
contained in that position of the array.
'''

for i in final:
    if i[0] == '\n0':
        i.remove('\n0')

'''
Some rows have a leading 0 attached to them in the data set. The code treats this
as a column of data, which means that different rows have different column values,
i.e. final[0][6] returns the mass excess for a neutron, but final[1][6] returns 
the error in mass excess for hydrogen. We want the array to have uniform column
values so that the program can isolate the information within the array that it
needs depending on user inputs.

So, to create the uniform column assignment, I used a for loop to delete the 
entries that started with the \n0 (the leading 0)
'''


for i in final:
    if not re.search('[\.#]',i[5]):
        del(i[5])

'''
This for loop removes the entries in a column that flags certain rows in the
data set for orgonizational purposes. There are not entries in this column at
every row, so it will lead to unaligned columns, just like the leading 0 case.
'''

for i in final:
    if i[10] == '*':
        i.insert(11, '*')
        
'''
For certain columns, the entry in the beta decay energy column is just an '*'.
This means that the nucleus is stable and has no value for beta decay. Unfortunately,
The columns that do have a value also have an error in the value as a seperate 
column. The stable nuclie do not have this column and so they are unaligned. I added
another '*' to the stable nuclie rows after the first '*' to symbolize that there
is no error due to stability, and to make sure that the columns stay aligned.
'''

for i in final:
    i.insert(12,i[12]+i[13])
    del(i[13],i[13])
    
'''
The atomic mass unit column is split up in the data file. The number in the
column before the actual atomic mass column represents the number of atmoic 
mass units for the row. The muber in the atomic mass column is the deviation 
from the number of atomic mass units in micro-units. Here, I add the 2 columns
into 1 new column, and get rid of the old ones. This way, the 12th column of 
the array represents each row's exact atomic mass in micro-units.
'''

for i in final:
    for j in range(0,len(final[0])):
        if  j == len(i)-1 and re.search('#',i[j]):
            i.insert(len(i),'#')
        i[j] = re.sub('#','',i[j])

'''
Here i remove the # from all of the theoretical values. This way, i can turn them into floats and then
use them in the searching function later. I denote the theoretical values by adding an extra column to
each theoretical row that only contains a #. This way, if a row has a string containing only # in the
last column, all of the numeric values in that row are theoretical.
'''





        
    
