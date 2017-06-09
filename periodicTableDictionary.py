massfile = open("mass16.txt","r+")
data=massfile.readlines()

elementFile = open("ElementList.txt","r+")
elementName = elementFile.readline()
elementName = elementName.strip()
elementName = elementName.split(',')


class periodicTable(object):
    def __init__(self,name,N,A,stability):
        self.name = name
        self.N = N
        self.A = A
        self.stability = stability

count = 0
thing = {}
writetofile = ""
for element in elementName:
    for i in range(1,300):
         k=39
         stabilityvalue = 0
         while k <= len(data)-1:
             if len(data[k]) >= 80:
                 mass = data[k][16:19].replace(" ","")
                 mass = int(mass)
                 if mass == i:
                     eName = str(data[k][20:22].replace(" ",""))
                     if eName==element:
                         stabilityvalue = mass
                         break
                 if mass > i:
                     break
             k=k+1
         thing[count,i] = periodicTable(element,count,i,stabilityvalue)
         if thing[count,i].stability != 0:
             writetofile = writetofile+str(thing[count,i].name)+','+str(thing[count,i].N)+','+str(thing[count,i].A)+','+str(thing[count,i].stability)+'\n'
         
    count = count + 1

WriteFile = open("IsotopeList.txt","wb")
WriteFile.write(str.encode(writetofile))
