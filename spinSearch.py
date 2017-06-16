from fractions import Fraction

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
    tempList = checkVal.replace('**','').replace('&',',') 
    tempList = tempList.split(',')
          
    ## Look for parities that need to be distributed.
    if any((')+' in value or ')-' in value) for value in tempList):
        addPlus = False
        addMinus = False
        for j in range(len(tempList)): 
            if ')+' in tempList[j]:
                addPlus = True
                tempList[j] = tempList[j].replace('+','') 
            if ')-' in tempList[j]:  
                addMinus = True
                tempList[j] = tempList[j].replace('-','')
         ## Distribute the parities to each term
        for j in range(len(tempList)):
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
        ## if a range is given, len(tempList) = 1 ALWAYS
        tempList[0] = tempList[0].replace('TO',':')
        [lhs,rhs] = tempList[0].split(':')
        
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
            tempList = jRange

        ## J TO J'PI
        elif ('+' in rhs) or ('-' in rhs):
            lowJ = getJ(lhs)
            highJ = getJ(rhs)
            highPI = getPI(rhs) 
            jRange = getJrange(lowJ,highJ)
                
            for jIndex in range(len(jRange)):
                jRange[jIndex] = jRange[jIndex]+highPI
            tempList = jRange

        ## JPI TO J'
        elif ('+' in lhs) or ('-' in lhs):
            lowJ = getJ(lhs)
            lowPI = getPI(lhs)
            highJ = getJ(rhs) 
            jRange = getJrange(lowJ,highJ)
            
            jRange[0] = jRange[0]+lowPI
            tempList = jRange

        else: ## J TO J'
            lowJ = getJ(lhs)
            highJ = getJ(rhs) 
            jRange = getJrange(lowJ,highJ)
            tempList = jRange   
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
    else:
        ## Spin not found
        return False
