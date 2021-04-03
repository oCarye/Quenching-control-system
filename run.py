from src import data
from src import graph
x1,x2,y1,y2=data.getData("res\QT1_1210-15.csv")
graph.drawGraph(x1,y1,x2,y2)