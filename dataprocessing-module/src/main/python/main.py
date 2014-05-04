__author__ = "devashish.shankar"

from trainer import *
import random
from sklearn import svm

def getDatasets(labelToFileDict, intervalSize):
    walkTypeToDataSets = {}
    for label in labelToFileDict.keys():
        walkTypeToDataSets[label] = []
        #print "Getting data for label: ",label
        for file in labelToFileDict.get(label):
            #print "Getting data from file: ",file
            datasets = getDataSetsbySamplingIntervals(file,0,180000,intervalSize)
            #print "Got datasets: ",len(datasets), "from file: ",file
            walkTypeToDataSets[label].extend(datasets)
    return walkTypeToDataSets

def splitIntoTrainTest(labelToDataSets, ratio):
    totalSet = []
    for walkType in labelToDataSets.keys():
        for dataset in labelToDataSets[walkType]:
            features = getFeatures(dataset)
            #freq_features = getFreqDomainFeatures(dataset)
            freq_features = []
            #print "feat",features
            #print "freq_feat",freq_features
            totalSet.append((walkType, features+freq_features))
    random.shuffle(totalSet)
    #print("Total sets: ",len(totalSet))
    trainLen = (int) (len(totalSet)*ratio)
    #print "Train len: ",trainLen
    trainSet = totalSet[:trainLen-1]
    testSet = totalSet[trainLen:]
    return trainSet,testSet

def plotGraph(labelToDataSets):
    timeBasedFeatures = {}
    timeBasedFeatures['avg'] = []
    timeBasedFeatures['p2p'] = []
    timeBasedFeatures['stdDev'] = []
    timeBasedFeatures['median'] = []
    timeBasedFeatures['max'] = []
    timeBasedFeatures['min'] = []
    timeBasedFeatures['rms'] = []
    timeBasedFeatures['cor1'] = []
    walkTypeToNumOfSamples = {}
    for walkType in labelToDataSets.keys():
        walkTypeToNumOfSamples[walkType]=0
        for dataset in labelToDataSets[walkType]:
            walkTypeToNumOfSamples[walkType]+=1
            features = getFeatures(dataset)
            timeBasedFeatures['avg'].append(features[0])
            timeBasedFeatures['p2p'].append(features[1])
            timeBasedFeatures['stdDev'].append(features[2])
            timeBasedFeatures['median'].append(features[3])
            timeBasedFeatures['max'].append(features[4])
            timeBasedFeatures['min'].append(features[5])
            timeBasedFeatures['rms'].append(features[6])
            timeBasedFeatures['cor1'].append(features[7])

    #print walkTypeToNumOfSamples
    import numpy as np
    import matplotlib.pyplot as plt
    plt.plot(range(len(timeBasedFeatures['avg'])),timeBasedFeatures['avg'],'r')
    plt.plot(range(len(timeBasedFeatures['p2p'])),timeBasedFeatures['p2p'],'b')
    plt.show()


def splitIntoTrainTestOld(labelToDataSets, ratio):
    totalSet = []
    for walkType in labelToDataSets.keys():
        for dataset in labelToDataSets[walkType]:
            features = getFeaturesOld(dataset)
            #freq_features = getFreqDomainFeatures(dataset)
            freq_features = []
            #print "feat",features
            #print "freq_feat",freq_features
            totalSet.append((walkType, features+freq_features))
    random.shuffle(totalSet)
    #print("Total sets: ",len(totalSet))
    trainLen = (int) (len(totalSet)*ratio)
    #print "Train len: ",trainLen
    trainSet = totalSet[:trainLen-1]
    testSet = totalSet[trainLen:]
    return trainSet,testSet

def train(trainingDataSet,clf):
    trainX = []
    trainy = []
    for train in trainingDataSet:
        trainX.append(train[1])
        trainy.append(train[0])
    clf_fit = clf.fit(trainX, trainy)
    return clf_fit

def evaluate(clf_fit, testingDataSet):
    testX = []
    testy = []
    for test in testingDataSet:
        testX.append(test[1])
        testy.append(test[0])
    return clf_fit.score(testX,testy)


labelToFileDict = {
    'sitting':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/final_sit.txt'],
     'slowWalk':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/final_walk.txt'],
     #'fastWalk':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/fastWalk.txt'],
     'lying':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/final_lying.txt'],
 'stand':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/final_stand.txt'],
 #'climbingUp':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/climbingUp.txt'],
 #'slowRun':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/stand.txt'],
 'fastRun':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/final_run.txt'],
# 'comp':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/new/comp.txt']
}

#Step 2: Set interval size
clfs = []
rbfSVM = svm.SVC();
linearSVM = svm.SVC(1.0,'linear');
polySVM = svm.SVC(1.0,'poly');
sigmoidSVM = svm.SVC(1.0,'sigmoid');
from sklearn.linear_model import SGDClassifier
sgdHinge = SGDClassifier(loss="hinge", penalty="l2")
sgdLog = SGDClassifier(loss="log", penalty="l2")

from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
gnb = GaussianNB()
mnb = MultinomialNB()
bnb = BernoulliNB()

def getRBF():
    return svm.SVC();

def getLinear():
    return svm.SVC(1.0,'linear');

def getPoly():
    return svm.SVC(1.0,'poly');



clfs.append(rbfSVM)
for intervalSize in [250,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000]:

    #Step 3: Get data sets from labels
    labelToDataSets = getDatasets(labelToFileDict,intervalSize)

    #plotGraph(labelToDataSets)
    print "labels are: ",labelToDataSets.keys()
    for label in labelToDataSets.keys():
        print "label: ",label, "; datasets: ",len(labelToDataSets.get(label))

    for clf in clfs:
        newModelScore = []
        oldModelScore = []
        for i in range(20):
            #Step 4: divide into training testing
            trainingDataSet,testingDataSet = splitIntoTrainTest(labelToDataSets,0.8)

            trainingDataSetOld,testingDataSetOld = splitIntoTrainTestOld(labelToDataSets,0.8)

            #Step 5:
            clf = SGDClassifier(loss="hinge", penalty="l2");
            model = train(trainingDataSet,clf)
            clf = SGDClassifier(loss="hinge", penalty="l2");
            modelOld = train(trainingDataSetOld,clf)

            newModelScore.append(evaluate(model,testingDataSet))
            oldModelScore.append(evaluate(modelOld,testingDataSetOld))

        import numpy
        print "Interval Size:",intervalSize
        print "CLF: ",clf
        print newModelScore
        print oldModelScore
        print "new",numpy.mean(newModelScore)
        print "old",numpy.mean(oldModelScore)
