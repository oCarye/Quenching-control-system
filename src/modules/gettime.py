from datetime import datetime

def getTime(pre_times,step=1):
    #把时间字符串列表转化成数字，并以times[0]为第0秒；
    #时间字符串形如"12/10/2020 9:02:51 AM"
    new_times=[]
    new_times.append(datetime.strptime(pre_times[0],"%m/%d/%Y %I:%M:%S %p"))
    for i in range(step,len(pre_times),step):
        new_times.append(datetime.strptime(pre_times[i],"%m/%d/%Y %I:%M:%S %p")-new_times[0])
    new_times[0]=new_times[0]-new_times[0]
    new_times=[int(t.total_seconds()) for t in new_times]
    return new_times