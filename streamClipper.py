from chat_downloader import ChatDownloader
import statistics as s
import time as t
import datetime
import numpy as np



def chat_downloader(start = None, end = None):   
    data = ChatDownloader().get_chat(url, start_time = start, end_time = end)
    i = 0
    for message in data:
        i+=1
    return i


def maxIndex(l):
    return l.index(max(l))

def convert(n):
    return str(datetime.timedelta(seconds = n))

def getPerciseMinute(start, end, interval):
    testList = []
    for i in range (start, end, interval):
        testList.append(chat_downloader(i, i+interval))
    return start+maxIndex(testList)*interval
    
def getMaxCommentClip(amount, inputList, interval, perciseInterval):
    timeList = inputList
    outputList = []
    for i in range (0, amount):
        time = maxIndex(timeList)*interval
        standardTime = getPerciseMinute(time, time+interval, perciseInterval)
        outputList.append(standardTime)
        timeList[maxIndex(timeList)] = 1
    return outputList

def getSTDCommentClip(amount, inputList, interval, perciseInterval, stdNum):
    outputList = []
    timeList = inputList
    for i in range(0, amount):
        std = np.std(timeList)
        mean = np.mean(timeList)
        anomaly_cut_off = std*stdNum

        lower_limit  = mean - anomaly_cut_off 
        upper_limit = mean + anomaly_cut_off
    
        for outlier in timeList:
            if outlier > upper_limit:
                time = timeList.index(outlier)*interval
                standardTime = getPerciseMinute(time, time+interval, perciseInterval)
                outputList.append(standardTime)            
                timeList[timeList.index(outlier)] = mean
    return outputList

if __name__ == "__main__":
    global url
    
    start = t.time()
    
    protentialClipTime = []
    
    url = 'https://www.youtube.com/watch?v=W7gUkrx2KPk'
    interval = 300
    perciseInterval = 30
    timeList = []
    
    comment = 1
    count = 0
    while comment != 0:
        comment = chat_downloader(start = count, end = count+interval)
        timeList.append(comment)
        count += interval
        
        
    protentialClipTime1 = getMaxCommentClip(5, timeList, 300, 30)
    protentialClipTime2 = getSTDCommentClip(1, timeList, 300, 30, 2)
    
        
    for time in protentialClipTime1:
        print("good max time:",convert(time))
    print("")
        
    for time in protentialClipTime2:
        print("good std time:",convert(time))        
    
    print("")
    print("total time took:", int(t.time()-start))
    
        
    
        