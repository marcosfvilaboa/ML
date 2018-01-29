'''
Created on 27/5/2016

@author: Marcos F. Vilaboa
'''

import operator
from cmath import sqrt
import time


class Knn:

    def __init__(self, filePath={}):
        self.trainSet = filePath
        self.length = len(self.trainSet)-1
        
    # KNN with test set and k parameter
    def simpleKNN (self, k, trainSet, testSet):        
        predicted = []
        actual = []
        
        timeVar = self.startClock()
        for rows in testSet:
            neighbors = self.neighbors(k, rows, trainSet)
            votes = self.votes(neighbors)            
            predicted.append(votes)
            actual.append(rows[-1])       
        self.precision(actual, predicted)            
        self.stopClock(timeVar)
    
    # Weighted KNN with test set  and k parameter
    def weightedKNN (self, k, trainSet, testSet):  
        predicted = []
        actual = []
        
        timeVar = self.startClock()
        for rows in testSet:
            neighbors = self.weightedNeighbors(k, rows, trainSet)
            votes = self.votes(neighbors)        
            predicted.append(votes)
            actual.append(rows[-1])      
        precise = self.precision(actual, predicted)
        self.stopClock(timeVar)    
    
    # vote for the best class attribute
    def votes (self, neighbors):
        votes = {}
        
        neigh = [x[0] for x in neighbors] # Extract distances column from neighbors
        
        for col in neigh: # Extract distances column from neighbors
            vote = col[-1]
            if vote in votes:
                votes[vote] += 1
            else:
                votes[vote] = 1
        sortVotes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
        
        return sortVotes[0][0]
    
    # Returns a list with the k lowest distances
    def neighbors (self, k, testInstance, trainSet):
        neighbors = []
        distances = []
        
        [distances.append((rows,float(self.euclideanDistance(rows, testInstance)))) for rows in trainSet]
        
        # sort the elements. Key don't modify the list and
        # is called as int(x) before the comparison
        distances.sort(key=operator.itemgetter(1)) 
           
        [neighbors.append(distances[i]) for i in range(int(k))]
        return neighbors

    # Similar to neighbors function but applying weights to sort them
    def weightedNeighbors (self, k, testInstance, trainSet):
        neighbors = []
        weightedDist = []
        confValue = 0
        
        for rows in trainSet: 
            dist=self.euclideanDistance(rows, testInstance)
            # To control zero divisions
            dist = 1 / 1 + float(dist)            
            weightedDist.append((rows,dist))
        # sort the elements. 'k' don't modify the list and 
        # is called as int(x) before the comparison    
        weightedDist.sort(key=operator.itemgetter(1), reverse=True)                                          
        for x in range(int(k)):
            neighbors.append(weightedDist[x])
            confValue += weightedDist[x][1]
        confianceValue = weightedDist[0][1]/confValue     
        print("\n Weight: ",weightedDist[0][1])        
        print(" Confidence value: {:.6f}".format(confianceValue))
        
        return neighbors  
    
    # Calculate the Euclidean distance between two instances
    def euclideanDistance (self, trainInstance, testInstance):
       
        dist = sum([pow((float(trainInstance[col]) - float(testInstance[col])), 2) for col in range(0,len(testInstance)-1)])
        
        # Reparse to return       
        distance = sqrt(dist)
        dist = str(distance)                    
        dist = "{:.6f}".format(distance.real) 
        
        return dist

    # Calculates the precision percentage of belongs to a class
    # and prints the confusion matrix
    def precision(self, actual, predictions):
        correct = 0
        zeroZero = 0
        zeroOne = 0
        oneZero = 0
        oneOne = 0 
        length = len(actual)

        print("\n\n Current lenght: ",length)
        for i in range(0,length):    
                if actual[i] is predictions[i]:                    
                    correct+=1
                if actual[i] == '0' and predictions[i] =='0':
                    zeroZero += 1
                elif actual[i] == '0' and predictions[i] =='1':
                    zeroOne +=1
                elif actual[i] == '1' and predictions[i] =='0':
                    oneZero +=1
                else:
                    oneOne +=1
        print("\n Prediction: \n",predictions)
        print(" Current values: \n",actual)        
        print("\n Corrects: ",correct)        
        print("\n --With {}% of accuracy".format(round((correct/float(len(predictions)))*100,2)))
            
        zeroPred = zeroZero+zeroOne
        onePred = oneZero+oneOne
        zeroActual = zeroZero+oneZero
        oneActual = zeroOne+oneOne        
        print("\n CONFUSION MATRIX")
        print("==================")
        print(" __________________________________________________ ")
        print("|          \ CURRENT  |                  |         |")
        print("| PREDICTED \         |  [ ,0]    [ ,1]  |   ALL   |")
        print("|____________\________|__________________|_________|")
        print("|        [0, ]        |   -{}-       {}    |    {}    |".format(zeroZero, zeroOne, zeroPred))
        print("|        [1, ]        |    {}       -{}-   |    {}    |".format(oneZero, oneOne, onePred))
        print("|_____________________|__________________|_________|")
        print("|         ALL         |    {}        {}    |    {}   |".format(zeroActual, oneActual, length))
        print("|_____________________|__________________|_________|")
    
    def startClock(self):
        return time.clock()
    
    def stopClock (self,timeVar):
        print("\nThe process lasted {} seconds\n\n\n".format(round(time.clock()-timeVar,2)))
    
    