## This file contains functions that are used by newDataClass.py to read and filter data from the ensdf files

from fractions import Fraction
from decimal import Decimal
from uncertainty import halfLifeErrorProp

HBAR = Decimal('6.582119514e-16') ## [eV sec] from NIST
LN2 = Decimal('6.931471806e-1')

def convertToSec(hl,dhl):
    [val,units]=hl.split(' ')
    if 'EV' in units:
        if units == 'EV':
            conversion = '1'
        elif units == 'KEV':
            conversion = '1e3'
        elif units == 'MEV':
            conversion = '1e6'
        width = Decimal(val) * Decimal(conversion)
        dwidth = [Decimal(num) * Decimal(conversion) for num in dhl]
        hl = HBAR * LN2 / width
        dhl = [halfLifeErrorProp(width,num) for num in dwidth]
        
    else:
        if units == 'Y':
            conversion = '3.1536e7'
        elif units == 'D':
            conversion = '8.64e4'
        elif units == 'H':
            conversion = '3.6e3'
        elif units == 'M':
            conversion = '60' 
        elif units == 'S':
            conversion = '1'
        elif units == 'MS':
            conversion = '1e-3'
        elif units == 'US':
            conversion = '1e-6'
        elif units == 'NS':
            conversion = '1e-9'
        elif units == 'PS':
            conversion = '1e-12'
        elif units == 'FS':
            conversion = '1e-15'
        elif units == 'AS':
            conversion = '1e-18'
        hl = Decimal(val) * Decimal(conversion)
        dhl = [Decimal(it) * Decimal(conversion) for it in dhl]
    
    return [hl, dhl]

def getPI(JPI): ## Extract parity
        if '+' in JPI:
            return '+'
        elif '-' in JPI:
            return '-'
        else:
            return ''
def getJ(JPI): ## Extract spin w/o parity

    return Fraction(JPI.replace('+','').replace('-',''))

def getJrange(lowval,highval): ## Creates range of spins
    jRange = [lowval]
    while (jRange[-1] < highval):
        jRange.append(jRange[-1]+1)
    for jIndex in range(len(jRange)):
        jRange[jIndex] = str(jRange[jIndex])
    return jRange
        

def spinMatchFinder(matchVal,checkVal):
    ## matchVal is the desired spin, checkVal is the spin to be checked for matchVal      
    tempList = checkVal.replace('**','').replace('&',',').replace('[','').replace(']','') 
    tempList = tempList.split(',')
          
    ## Look for parities that need to be distributed.
    if any((')+' in value or ')-' in value) for value in tempList):
        addPlus = False
        addMinus = False
        for j in range(len(tempList)): 
            if ')+' in tempList[j]:
                addPlus = True
                tempList[j] = tempList[j].replace('+','')
                closePar = j 
                for k in range(j+1):
                    if '(' in tempList[j-k]:
                        openPar = j-k
                        break
                
            elif ')-' in tempList[j]: 
                addMinus = True
                tempList[j] = tempList[j].replace('-','')
                closePar = j 
                for k in range(j+1):
                    if '(' in tempList[j-k]:
                        openPar = j-k
                        break
         ## Distribute the parities to each term
        for j in range(openPar,closePar+1):
            if addPlus:
                tempList[j] = tempList[j] + '+'
            if addMinus:
                tempList[j] = tempList[j] + '-'

    ## Remove () and whitespace so that spins can be identified with ==
    for j in range(len(tempList)):
        tempList[j] = tempList[j].replace('(','')
        tempList[j] = tempList[j].replace(')','')
        tempList[j] = tempList[j].strip()
    ## Handing of ranges of spins (eg. JPI to J'PI', see ensdf manual pg. 46 for more info)
    if any(('TO' in value or ':' in value) for value in tempList):
        for value in tempList: 
            if ('TO' in value or ':' in value):
                toIndex = tempList.index(value)
        tempList[toIndex] = tempList[toIndex].replace('TO',':')
        [lhs,rhs] = tempList[toIndex].split(':')
        
        ## JPI TO J'PI'
        if (('+' in lhs) or ('-' in lhs)) and (('+' in rhs) or ('-' in rhs)): 
            ## Note that lowJ and highJ are Fraction objects
            lowJ = getJ(lhs)
            lowPI = getPI(lhs)
            highJ = getJ(rhs)
            highPI = getPI(rhs) 
            ## jRange is a list of strings
            jRange = getJrange(lowJ,highJ)
            
            jRange[0] = jRange[0]+lowPI
            jRange[-1] = jRange[-1]+highPI
            insertList = jRange

        ## J TO J'PI
        elif ('+' in rhs) or ('-' in rhs):
            lowJ = getJ(lhs)
            highJ = getJ(rhs)
            highPI = getPI(rhs) 
            jRange = getJrange(lowJ,highJ)
                
            for jIndex in range(len(jRange)):
                jRange[jIndex] = jRange[jIndex]+highPI
            insertList = jRange

        ## JPI TO J'
        elif ('+' in lhs) or ('-' in lhs):
            lowJ = getJ(lhs)
            lowPI = getPI(lhs)
            highJ = getJ(rhs) 
            jRange = getJrange(lowJ,highJ)
            
            jRange[0] = jRange[0]+lowPI
            insertList = jRange

        else: ## J TO J'
            lowJ = getJ(lhs)
            highJ = getJ(rhs) 
            jRange = getJrange(lowJ,highJ)
            insertList = jRange 

        tempList[toIndex:toIndex+1] = insertList

     ## assign + and - to states with no indicated pairity
    if (not tempList == ['']) and any(('+' not in value and '-' not in value) for value in tempList):
        j=0
        while (j < len(tempList)):
            if ('+' not in tempList[j] and '-' not in tempList[j]):
                tempList.insert(j,tempList[j]+'-')
                tempList[j+1] = tempList[j+1]+'+'
            j+=1

    if (matchVal in tempList):
        return True

    ## AP LE GE handling.
    elif any('GE' in value or 'LE' in value or 'AP' in value for value in tempList):
        
        for value in tempList:
            ## Greater than or equal
            if 'GE' in value:
                value = value.replace('GE','').strip()
                ## Check if correct parity
                if (getPI(matchVal)==getPI(value)):
                    if (getJ(matchVal) >= getJ(value)) and (getJ(matchVal).denominator == getJ(value).denominator):
                        return True
            ## Less than or equal
            elif 'LE' in value:
                value = value.replace('LE','').strip()
                ## Check if correct parity
                if (getPI(matchVal)==getPI(value)):
                    if (getJ(matchVal) <= getJ(value)) and (getJ(matchVal).denominator == getJ(value).denominator):
                        return True
            ## Approximate
            elif 'AP' in value:
                value = value.replace('AP','').strip()
                if (value == matchVal):
                    return true
    else:
        ## Spin not found
        return False
