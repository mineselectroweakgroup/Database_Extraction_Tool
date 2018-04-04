# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:30:14 2017

@author: Jessica
Websites used:
https://stackoverflow.com/questions/316866/ping-a-site-in-python
http://www.geeksforgeeks.org/downloading-files-web-using-python/
https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-folder-in-python
https://stackoverflow.com/questions/22383218/how-to-replace-all-the-file-extensions-in-a-folder-python
"""

#Import all the things. All of them.
import subprocess
import shlex
import requests
import time
import zipfile
import os


def main():
#Base URL
     
    url="www.nndc.bnl.gov"
    internetAccess=0
#Initialize variable as false
    
    response=os.system("ping -c 1 " +url )
    
    if response==0:
        
        
        internetAccess=1
        #If you can find the website, set variable to true
    else:
        print ("Unable to find website, please check internet access")
        internetAccess=0
        #If cant find the website, dont continue.
    if internetAccess==0:
        #If there isnt internet, dont continue
        print("Cannot Update at this time, check internet access")
        return;
    else:
        #Append URL to be closer to download URL
        urlfix=url+"/ensarchivals/"
        
        print("Download begin:")
        print(time.strftime("%H:%M:%S"))
        print("Estimated time until completion: 15 min")
        #Call download function
        delOld()
        
        
        filename=download(urlfix)
        #Feed each of the file extensions through the download function
            
        print("Time stopped Downloading:")
        print(time.strftime("%H:%M:%S"))
    
        print("Begin Unzipping, time:")
        print(time.strftime("%H:%M:%S"))
       #Delete the Old Files
        
        
        #Unzip Download function
        for j in range(0,len(filename)):
             
            unZip(filename[j])
        #Feed each of the Zip files through the Unzip function?
            
        
        #Turn files into txt files
        print("Finished Unzipping and Converting, time:")
        print(time.strftime("%H:%M:%S"))
        return;
        
def download(url):
    print("Downloading...")
    
    #Get Current Year from computer
    year=time.strftime("%y")    
    secondAdd=["099","199","299"]; #The three folders containing ensdf files
    #firstAdd=["0101","0201","0301","0406","0501","0601","0701","0801","1001"]
        #0-99, 100-199 and 200-299
    rstore=["placeholder","placeholder","placeholder"]
    filename=["placeholder","placeholder","placeholder"]
        #Initializes the filename list
        
    i=secondAdd[0];
    for yr in range(int(year)-1,int(year)+1):    
        for month in range(1,13):
            for day in range(1,32):
                urlnew="http://"+url+"distributions/dist"+str(yr)+"/ensdf_"+str(yr)+str(month).zfill(2)+str(day).zfill(2)+"_"+i+".zip"
       #url for the zip files
                r=requests.get(urlnew)
                if r.status_code==200:
                    mostRecYr=str(yr);
                    mostRecMn=str(month).zfill(2);
                    mostRecDay=str(day).zfill(2);
                    
    counter=0;                
    for j in secondAdd:
        downloadURL="http://"+url+"distributions/dist"+mostRecYr+"/ensdf_"+mostRecYr+mostRecMn+mostRecDay+"_"+j+".zip"
        filename[counter] = "Zipped"+j+".zip" 
        rstore[counter]=requests.get(downloadURL)
        new_path=os.path.join(os.getcwd(),"Data/")
        with open(new_path+filename[counter],"wb") as f:
            f.write(rstore[counter].content)
        counter=counter+1
       
    return filename; #Return the name of the file

#Unzip the files    
def unZip(filename):
    try:
        new_path=os.path.join(os.getcwd(),"Data/")
        os.chdir(new_path)
        zip = zipfile.ZipFile(filename)
        zip.extractall()
    except:
        print("Checking File Path")
    #Extracts all files into current folder
    
    #Convert extracted files into txt files
    
    return;
    
#Converts files into .txt files    
def delOld(path="Data/"):
     #Path is defined to be the current folder that the .py file is in
    new_path = os.path.join(os.getcwd(), path)
    #The path to the folder where the folders exist
    
    os.chdir(new_path)
    
    for f in os.listdir(new_path):
        #For all the files in the folder
        try:
            if "ensdf" or "Zipped" in f:#Check to see if has ensdf in the name
                os.remove(f)
                        #Remove the old file
                        
                    
                
        except StandardError:
            continue;
    return;
    
main()
