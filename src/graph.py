import matplotlib.pyplot as plt
from modules.config import *
def drawGraph(x1,y1,x2,y2):
    plt.figure(figsize=(10,8))  #画布大小
    plt.subplot(2,1,1)  #创建2*1的区域内的第一个子图
    plt.bar(x1,y1)  #绘制条状图
    plt.xlabel(sp_time_1_3)  #横坐标名称
    plt.ylabel(sp_value_1_3)
    plt.xticks(range(0,len(x1),20))  #横坐标间距

    plt.subplot(2,1,2)
    plt.bar(x2,y2)
    plt.xlabel(av_time_1_3)
    plt.ylabel(av_value_1_3)
    plt.xticks(range(0,len(x2),20))
    plt.show()  #显示图像