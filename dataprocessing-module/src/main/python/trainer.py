import numpy

std_axes = ['ax', 'ay', 'az', 'axa', 'aya']

class DataSet:
    def __init__(self,filename,start = 0,end = 100000000):
        f = open(filename)
        all = f.read()
        lines = all.split(';')
        self.data = {'ax': [],'ay': [],'az': [],'gx': [],'gy': [],'gz': [], 'axa': [], 'aya': [], 'time': []}
        print "Total lines in file: ",len(lines)
        print "Creating dataSet for: ",filename,start,end
        for line in lines:
            values = line.split('\t')
            if(len(values)==11):
                time = (long)(values[8])
                if(time>start and time<end):
                    self.data['ax'].append((float) (values[2]))
                    self.data['ay'].append((float) (values[3]))
                    self.data['az'].append((float) (values[4]))
                    self.data['gx'].append((float) (values[5]))
                    self.data['gy'].append((float) (values[6]))
                    self.data['gz'].append((float) (values[7]))
                    self.data['axa'].append((float) (values[0]))
                    self.data['aya'].append((float) (values[1]))
                    self.data['time'].append(time)
            else:
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


def getDataSetsbySamplingIntervals(filename,start,stop,intervalSize):
    totalTime = stop-start
    curStop = start + intervalSize
    datasets = []
    prevCurStop = start
    while(curStop<=stop):
        data_set = DataSet(filename, prevCurStop, curStop)
        if(len(data_set.data['ax'])) == 0:
            print "zero data"
        else:
            datasets.append(data_set)
        prevCurStop = curStop
        curStop+=intervalSize
    return datasets

def getFeatures(dataset):
    featList = []
    for axis in std_axes:
        featList.append(getAvg(dataset,axis))
        featList.append(getP2PDistance(dataset,axis))
        featList.append(getStdDev(dataset,axis))
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








