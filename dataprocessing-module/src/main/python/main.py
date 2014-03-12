__author__ = 'devashish.shankar'

from trainer import *
import random
from sklearn import svm

def getDatasets(labelToFileDict, intervalSize):
    walkTypeToDataSets = {}
    for label in labelToFileDict.keys():
        walkTypeToDataSets[label] = []
        for file in labelToFileDict.get(label):
            datasets = getDataSetsbySamplingIntervals(file,30000,180000,intervalSize)
            walkTypeToDataSets[label].extend(datasets)
    return walkTypeToDataSets

def splitIntoTrainTest(labelToDataSets, ratio):
    totalSet = []
    for walkType in labelToDataSets.keys():
        for dataset in labelToDataSets[walkType]:
            totalSet.append((walkType,getFeatures(dataset)))
    random.shuffle(totalSet)
    print("Total sets: ",len(totalSet))
    trainLen = (int) (len(totalSet)*ratio)
    print "Train len: ",trainLen
    trainSet = totalSet[:trainLen-1]
    testSet = totalSet[trainLen:]
    return trainSet,testSet

def train(trainingDataSet):
    trainX = []
    trainy = []
    for train in trainingDataSet:
        trainX.append(train[1])
        trainy.append(train[0])
    clf = svm.SVC()
    clf_fit = clf.fit(trainX, trainy)
    return clf_fit

def evaluate(clf_fit, testingDataSet):
    testX = []
    testy = []
    for test in testingDataSet:
        testX.append(test[1])
        testy.append(test[0])
    print clf_fit.score(testX,testy)


#Step 1: get files with labels
labelToFileDict = {'walk': ['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/christinawalk.txt',
                            '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/nageshwalk.txt',
                           # '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/rajwalk.txt',
                            '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/sudhamaniwalk.txt'
                            ],
                    'sit':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/christinasitting.txt',
                           '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/nageshsitting.txt',
                    #       '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/rajsitting.txt',
                           '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/sudhamanisitting.txt',
                           ]
                   }

#Step 2: Set interval size
intervalSize = 1000

#Step 3: Get data sets from labels
labelToDataSets = getDatasets(labelToFileDict,intervalSize)

print "labels are: ",labelToDataSets.keys()
for label in labelToDataSets.keys():
    print "label: ",label, "; datasets: ",len(labelToDataSets.get(label))

#Step 4: divide into training testing
trainingDataSet,testingDataSet = splitIntoTrainTest(labelToDataSets,0.8)

#Step 5:
model = train(trainingDataSet)

evaluate(model,testingDataSet)
