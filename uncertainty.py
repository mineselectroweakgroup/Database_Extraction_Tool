import math as m



def adduncert(da,db):
    error = m.sqrt(da**2 + db**2)
    return(error)


def multuncert(a,b,da,db):
    error = m.sqrt((a*db)**2+(b*da)**2)
    return(error)
