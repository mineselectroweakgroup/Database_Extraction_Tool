import math as m
from decimal import *

HBAR = Decimal('6.582119514e-16') ## [eV sec] from NIST
DHBAR = Decimal('4e-24') ## Standard Uncertainty in hbar [eV sec] from NIST
LN2 = Decimal('6.931471806e-1')

def halfLifeErrorProp(gamma,dgamma):
    error = LN2/gamma * ((HBAR/gamma * dgamma)**2 + DHBAR**2).sqrt()
    return error

def adduncert(da,db):
    error = m.sqrt(da**2 + db**2)
    return(error)


def multuncert(a,b,da,db):
    error = m.sqrt((a*db)**2+(b*da)**2)
    return(error)
