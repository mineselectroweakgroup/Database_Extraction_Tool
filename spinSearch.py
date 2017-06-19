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
        for value in tempList: ##FIXME
            if ('TO' in value or ':' in value):
                toIndex = tempList.index(value)
        ## if a range is given, len(tempList) = 1 ALWAYS
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
    print(tempList)
    if (matchVal in tempList):
        return True

    ## AP LE GE handling.
    elif any('GE' in value or 'LE' in value or 'AP' in value for value in tempList):
        print(tempList)
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
            ## FIXME add loop for whatever AP means
                
    else:
        ## Spin not found
        return False
