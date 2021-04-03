import csv
#from modules.getime import getTime
#from modules import const

def getData(f):
    with open("QT1_1210-15.csv",'r') as csv_file:
        f_dicts=csv.DictReader(csv_file,delimiter=';')

        #将有效数据读入x1,x2,y1,y2；
        x1,y1,x2,y2=[],[],[],[]
        d=next(f_dicts)
        while float(d[rotation_value])<10:
            d=next(f_dicts)
        while float(d[rotation_value])>=10:
            x1.append(d[sp_time_1_3])
            y1.append(d[sp_value_1_3])
            x2.append(d[av_time_1_3])
            y2.append(d[av_value_1_3])
            d=next(f_dicts)
    x1,x2=getTime(x1),getTime(x2)
    return x1,x2,y1,y2