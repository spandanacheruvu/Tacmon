import math
import numpy
from numpy import fft

std_axes = ['ax', 'ay', 'az', 'axa', 'aya']

class DataSet:
    def __init__(self,lines,start = 0,end = 100000000):
        self.data = {'ax': [],'ay': [],'az': [],'gx': [],'gy': [],'gz': [], 'axa': [], 'aya': [], 'time': []}
        #print "Total lines in file: ",len(lines)
        #print "Creating dataSet for: "  ,start,end
        # Get time of first line
        firstLine = lines[0]
        firstTimeS = firstLine.split('\t')[8]
        firstTime =  math.floor((float)(firstTimeS))

        for line in lines:
            values = line.split('\t')
            if(len(values)==11):
                time = math.floor((float)(values[8]))
                time = time-firstTime
                #print "time: ",time," start: ",start, " end: ",end
                if(time>start and time<end):
                    gxValue = values[5]
                    if(len(gxValue)==0):
                        gxValue = '0'
                    self.data['ax'].append((float) (values[2]))
                    self.data['ay'].append((float) (values[3]))
                    self.data['az'].append((float) (values[4]))
                    self.data['gx'].append((float) (gxValue))
                    self.data['gy'].append((float) (values[6]))
                    self.data['gz'].append((float) (values[7]))
                    self.data['axa'].append((float) (values[0]))
                    self.data['aya'].append((float) (values[1]))
                    self.data['time'].append(time)
            else:
                if(len(values)!=1):
                    print
                    print "error in line:",line,"values are: ",len(values)


def getAvg(dataset, axis):
    singleAxis = dataset.data[axis]
    return sum(singleAxis) / float(len(singleAxis))

def getP2PDistance(dataset,axis):
    singleAxis = dataset.data[axis]
    return max(singleAxis) - min(singleAxis)

def getStdDev(dataset,axis):
    singleAxis = dataset.data[axis]
    return numpy.std(singleAxis)

def getMedian(dataset,axis):
    singleAxis = dataset.data[axis]
    return numpy.median(singleAxis)

def getMax(dataset,axis):
    singleAxis = dataset.data[axis]
    return numpy.max(singleAxis)

def getMin(dataset,axis):
    singleAxis = dataset.data[axis]
    return numpy.min(singleAxis)

def getRMS(dataset,axis):
    singleAxis = dataset.data[axis]
    return numpy.sqrt(numpy.mean(numpy.array(singleAxis)**2))

def getCorrelation(dataset,axisA,axisB):
    axisAData = dataset.data[axisA]
    azisBData = dataset.data[axisB]
    return numpy.correlate(axisAData,azisBData)

def getDifference(dataset, A, B):
    axisAData = dataset.data[A]
    axisBData = dataset.data[B]
    diffArray = numpy.array(axisAData) - numpy.array(axisBData)
    return max(diffArray)

def getDataSetsbySamplingIntervals(filename,start,stop,intervalSize):
    totalTime = stop-start
    curStop = start + intervalSize
    datasets = []
    prevCurStop = start
    f = open(filename)
    all = f.read()
    lines = all.split('\n')
    preProcessedLines = []
    #print(" Raw lines in file: ",filename," = ",len(lines))
    errorCount=0
    for line in lines :
        values = line.split('\t')
        if(len(values)==11):
            preProcessedLines.append(line)
        else:
            #print "Error in line: "+line+" values are: ",len(values)
            errorCount+=1

    #print "Errors found",errorCount
    #print "After preprocessing: lines: ",len(preProcessedLines)
    miss = 0
    hit =0
    while(curStop<=stop):
        data_set = DataSet(preProcessedLines, prevCurStop, curStop)

        if(len(data_set.data['ax'])) == 0:
            miss+=1
            pass
            # print "zero data for: ",filename,prevCurStop,curStop
        else:
            hit+=1
            datasets.append(data_set)
        prevCurStop = curStop
        curStop+=intervalSize
        #print "miss: ",miss," hit: ",hit
    return datasets

def getFeatures(dataset):
    featList = []
    for axis in std_axes:
        featList.append(getAvg(dataset,axis))
        featList.append(getP2PDistance(dataset,axis))
        featList.append(getStdDev(dataset,axis))
        featList.append(getMedian(dataset,axis))
        featList.append(getMax(dataset,axis))
        featList.append(getMin(dataset,axis))
        featList.append(getRMS(dataset,axis))
    featList.append(getCorrelation(dataset,'ax','ay'))
    featList.append(getCorrelation(dataset,'ax','az'))
    featList.append(getCorrelation(dataset,'ay','az'))
    featList.append(getDifference(dataset,'ay','az'))
    featList.append(getDifference(dataset,'ax','az'))
    featList.append(getDifference(dataset,'ay','ax'))
    return featList

def getFeaturesOld(dataset):
    featList = []
    for axis in std_axes:
        featList.append(getAvg(dataset,axis))
        featList.append(getP2PDistance(dataset,axis))
        featList.append(getStdDev(dataset,axis))
    return featList

def getFreqDomainFeatures(dataset):
    featList = []
    for axis in std_axes:
        arr = dataset.data[axis]
        arrF = fft.fft(arr)
        arrFreq = fft.fftfreq(len(arr))
        featList.append(numpy.real(arrF[0])) #DC Component
    return featList


# fileName1 = '/Users/devashish.shankar/Downloads/walk1.txt'
# fileName2 = '/Users/devashish.shankar/Downloads/walk2.txt'
# fileName3 = '/Users/devashish.shankar/Downloads/walk3.txt'


# labelToFileDict = {'walk': ['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/christinawalk.txt',
#                             '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/nageshwalk.txt',
#                             '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/rajwalk.txt',
#                             '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/sudhamaniwalk.txt'
#                             ],
#                     'sit':['/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/christinasitting.txt',
#                            '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/nageshsitting.txt',
#                     #       '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/rajsitting.txt',
#                            '/Users/devashish.shankar/Work/Tacmon/dataprocessing-module/resources/sudhamanisitting.txt',
#                            ]
#                    }
# defaultIntervalSize = 10000
#
# walkTypeToDataSets = {}
# for label in labelToFileDict.keys():
#     walkTypeToDataSets[label] = []
#     for file in labelToFileDict.get(label):
#         #dataset = DataSet(file,30000,180000)
#         datasets = getDataSetsbySamplingIntervals(file,30000,180000,defaultIntervalSize)
#         walkTypeToDataSets[label].extend(datasets)
#
# #files = [fileName1,fileName2,fileName3]
#
#
#     #Print (useless to computation)
#
# X = []
# y = []
#
# totalSet = []
# for walkType in walkTypeToDataSets.keys():
#     for dataset in walkTypeToDataSets[walkType]:
#         X.append(getFeatures(dataset))
#         y.append(walkType)
#         totalSet.append((walkType,getFeatures(dataset)))
#
# import random
# random.shuffle(totalSet)
#
# print("Total sets: ",len(totalSet))
#
# trainToTestRatio = 0.8
# walkTypeToDataSets
# trainLen = (int) (len(totalSet)*trainToTestRatio)
#
# print "train len: ",trainLen
# trainSet = totalSet[:trainLen-1]
# testSet = totalSet[trainLen:]
#
# trainX = []
# trainy = []
#
# testX = []
# testy = []
#
# for train in trainSet:
#     print train
#     print "dsad",train[1]
#     trainX.append(train[1])
#     trainy.append(train[0])
#
# for test in testSet:
#     testX.append(test[1])
#     testy.append(test[0])
#
#
#
# from sklearn import svm
#
# print len(trainX),len(trainy)
# print trainX,trainy
# print "xtr",X,trainX
#
# clf = svm.SVC()
# clf_fit = clf.fit(trainX, trainy)
# print clf_fit
#
#
# for i in range(len(testX)):
#     stX = testX[i]
#     sty = testy[i]
#     y = clf_fit.predict(stX)
#     print y,sty
#
# #random.shuffle(testy)
# print clf_fit.score(testX,testy)
#








