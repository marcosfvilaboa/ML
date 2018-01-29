'''
Created on 26/5/2016

@author: Marcos F. Vilaboa
'''
import csv

class CsvArchive:

    def __init__(self, filePath={}):
        self.fileObj = filePath
    
    # Read archive from fileObj using reader()
    def readCSV (self,filePath):      
        data = []
        
        with open(filePath, "r") as self.fileObj:
            reader = csv.reader(self.fileObj)                       
            for x in reader:
                data.append(x)                         
        return data

    
    # Write archive from reader
    def writeCSV (self, reader, outFilePath):  
        with open(outFilePath,"w", newline='') as self.fileObj:
            writer = csv.writer(self.fileObj)
            writer.writerows(reader)
    
    # Reads archive 
    # print and count archive rows
    def printCSV (self,filePath):
        self.fileObj  = open(filePath, "r")
        reader = csv.reader(self.fileObj)
        rowNum = 0
        
        for row in reader:
            print(row)
            rowNum += 1
        self.fileObj.close()
        print("L'arxiu conté ",rowNum, " files")
    