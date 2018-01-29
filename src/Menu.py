'''
Created on 28/5/2016

@author: Marcos F. Vilaboa
'''
import re
from src.tools.PreProcess import PreProcess
from src.tools.CsvArchive import CsvArchive
from src.classifiers.Knn import Knn
from pip._vendor.distlib.compat import raw_input

class Menu:
    trainFilePath = "Data/trainFinal.csv"
    testFilePath = "Data/testFive.csv"

    def __init__(self, filePath={}):
        self.fileObj = filePath        
        self.preProc = PreProcess()
        self.csvFile = CsvArchive()
        self.knn = Knn()

    
    def drawMain (self):
        print("\n CLASSIFIERS:")
        self.line()
        print("\n    1.- File creation")
        print("    2.- Simple kNN")
        print("    3.- Weighted kNN")
        print("    4.- Help")
        print("    5.- EXIT")
    
    def fileCreationOpt(self):
        self.points()
        print(" Attention, you are about to create (or overwrite) the test files")
        print(" The file with the 10 random sample test raws will be recalculated")
        self.points()
        while True:
            opt1 = raw_input("\n Are you sure to continue? (Y/N): ")
            if opt1 == 'y' or opt1 == 'Y':
                self.preProc.createNoHeadFiles()
                self.preProc.createTest()
                break 
            elif opt1 == 'n' or opt1 == 'N':
                break
            else:
                self.points()
                print(" Invalid option!")
                self.points() 
    
    def simpleKnnOpt(self):
        print("\n\n   SIMPLE KNN")
        self.line()
        print("\n    The test file will be classified by the simple kNN method\n")
        self.points()
        k = self.chooseKValue()
        trainSet = self.csvFile.readCSV(self.trainFilePath)
        testSet = self.csvFile.readCSV(self.testFilePath)   
        self.knn.simpleKNN(k, trainSet, testSet) 
         
    def weightedKnnOpt(self):
        print("\n\n   WEIGHTED KNN")
        self.line()
        print("\n    The test file will be classified by the weighted kNN method")
        self.points()
        k = self.chooseKValue()
        trainSet = self.csvFile.readCSV(self.trainFilePath)
        testSet = self.csvFile.readCSV(self.testFilePath)   
        self.knn.weightedKNN(k, trainSet, testSet)

    def chooseKValue(self):
        while True:
            k = raw_input("\n    Choose a value for k: ")
            matchNum = re.match(r'\d', k)
            if matchNum:
                if (int(k) < 56):
                    return k
                else:
                    print("\n The calculation process for {} could take too much time.".format(k))
                    while True:
                        opt = raw_input(" Are you sure to continue? (Y/N): ")
                        if opt == 'y' or opt == 'Y':
                            return k 
                        elif opt == 'n' or opt == 'N':
                            break
                        else:
                            self.points()
                            print(" Invalid option!")
                            self.points() 
            else:
                self.points()
                print(" Invalid option!")
                self.points() 
                
    def help(self):
        while True:
            self.drawHelp()
            opt4 = raw_input("\n Insert a letter: ")
            if opt4 == 'a' or opt4 =='A':
                self.points()
                self.aboutApp()
                self.wait()
            elif opt4 == 'b' or opt4 == 'B':
                self.points()
                self.instructions()
                self.wait()
            elif opt4 == 'c' or opt4 == 'C':
                break
            else:
                self.points()
                print(" Invalid option!")
                self.points()
    
    def drawHelp(self):
        print("\n HELP")
        self.line()
        print("\n    a) About this app")
        print("    b) Instructions")
        print("    c) Go back")
    
    def aboutApp(self):        
        print("\n\n Author: Marcos F. Vilaboa")
        self.line()
        print(" for -Open University of Catalonia-")
        print("    Practice of the Computational Learning course")
        print("    2nd Semester")
        self.points()
        print("\n App version: 1.3\n")

    def instructions(self):
        print("\n\n Option 1 -- File creation")
        print("           The appropriate test and training files will be created.  ")
        print("        In order to do it, the program will process the normalized ")
        print("        CSV files named ccTestN.csv and ccTrainN.csv in Data folder.")
        print("        This removes the first titles row and takes five random rows")
        print("        of each class for the test file. The final files will be called")
        print("        trainFinal.csv and testFive.csv\n")
        print("    NOTE:  This random process will produce different analysis files.  ")
        print("        The results will vary from one classification to another.")
        print("\n Option 2 -- Simple kNN:")
        print("           This option will executes the simple kNN classifier. It ")
        print("        needs the 'k' value and uses testFive.csv and trainFinal.csv")
        print("        files from Data folder.")
        print("        Results are:  ")
        print("               · The value of the predicted and current classes ")
        print("               · The number of hits and its accuracy percentage ")
        print("               · The time the classifier tooks to calculate ")
        print("               · The confusion matrix ")
        print("\n Option 3 -- Weighted kNN:")
        print("           This option will executes the simple kNN classifier. This ")
        print("        is to sort the neighbors applying weights. As the simple kNN,")
        print("        it needs the 'k' value and uses testFive.csv and trainFinal.csv")
        print("        files from Data folder.")
        print("        Results are:  ")
        print("               · The calculated weight and its confidence value ")
        print("               · The value of the predicted and current classes ")
        print("               · The number of hits and its accuracy percentage ")
        print("               · The time the classifier tooks to calculate ")
        print("               · The confusion matrix ")

    def wait(self):
        self.points()
        raw_input("\n Press enter to continue...")    
        self.points()
    
    def line(self):
        print("===============================\n")
    
    def points(self):
        print("·······························")
    