'''
Created on 26/5/2016

@author: Marcos F. Vilaboa
'''

import csv
import random

from src.tools.CsvArchive import CsvArchive

class PreProcess:

    def __init__(self, filePath={}):   
        filePath = filePath
        self.csvFile = CsvArchive()
        
    # Read test and train sets and create
    # other csv's without the titles row
    def createNoHeadFiles(self):   
        testPath = "Data/ccTestN.csv"    
        testNoHeadPath = "Data/ccTestNoHead.csv"   
        trainPath = "Data/ccTrainN.csv"    
        trainNoHeadPath = "Data/trainFinal.csv"
           
        self.delFirstColCSV(trainPath, trainNoHeadPath)
        self.delFirstColCSV(testPath, testNoHeadPath)
    
    # Create testset randomly by shuffle
    def createTest(self):    
        testPath = "Data/ccTestNoHead.csv"
        testFivePath = "Data/testFive.csv"
        tFRows = [] #for count the number of rows in testFivePath
        reader = self.csvFile.readCSV(testPath) #read all test set   
        shuffled = self.shuffle(reader)    # shuffle the test set
        newTest = self.selectFive(shuffled) #select five rows
        self.csvFile.writeCSV(newTest, testFivePath) 
        print("\n Test file {} created with 5 rows of each class.".format(testFivePath))
        tFRows = self.csvFile.readCSV(testFivePath)
        rows = sum(1 for row in tFRows)
        print(" {} rows added to it\n\n".format(rows))
    
    # Read file from path, extract header
    # write the out file 
    def delFirstColCSV (self,inFilePath,outFilePath):
        data = []   
        oFRows = [] #for count the number of rows in outFilePath
        print("\n Reading file...")    
        with open(inFilePath, "r") as self.fileObj:
            reader = csv.reader(self.fileObj)           
            next(reader)# Skip header row
            rows = 1
            for x in reader:
                data.append(x) 
                rows += 1    
        print("    {} rows readed.".format(rows))
        print("    Titles row from file {} extracted".format(inFilePath))        
        print("\n Writing file...")
        self.csvFile.writeCSV(data,outFilePath)
        #to know number of rows added
        oFRows = self.csvFile.readCSV(outFilePath)
        rows = sum(1 for row in oFRows)
        print("    {} rows added".format(rows))
        print("    File {} created!".format(outFilePath))
    
    # Read file, shuffle the rows with the specified
    # seed number, finally write the out file  
    def shuffle (self,reader):
        random.shuffle(reader)
        
        return reader
        
    # Select 5 instance randomly of each class 
    # from a reader, then return it.
    # This functions presupose that we have enough
    # rows of every class
    def selectFive(self,reader):      
        rand = random.sample(reader,1)[0]  # Select a random row
        fiveClass1 = []   # Init two lists for each class. 
        fiveClass2 = []         
        for i in reader:
            if (len(fiveClass1)<5 or len(fiveClass2)<5):
                if i[-1] is rand[-1]:                
                    if len(fiveClass1)<5:
                        fiveClass1.append(i)
                else:
                    if len(fiveClass2)<5:
                        fiveClass2.append(i)
            else:
                break
        newTestSet = self.shuffle(fiveClass1+fiveClass2)       
        return newTestSet

    # Read file, split the file in two files(train & test) 
    # with the percentage parameter, finally write the new file
    def split (self,inFilePath,outTrainPath, outTestPath2, percentage):
        'TODO'
    
    # Read train file, applies normalize 
    # with mean and sqr, finally write out file
    def normalizeTrain (self,inTrainPath,outFilePath):
        'TODO'
        
    # Read test file, applies normalize to it with 
    # train mean and sqr parameters, then write out file   
    def normalizeTest (self,inTestPath,mean,sqr,outFilePath):
        'TODO'