#辨别毒蘑菇
#mushroom.dat  第一个特征表示有毒或者可食用。如果某样本有毒，则值为2。如果可食用，则值为1。下一
#个特征是蘑菇伞的形状，有六种可能的值，分别用整数3-8来表示。
from time import sleep
from apriori import *
mushDatset=[line.split() for line in open('mushroom.dat').readlines()]
#print(mushDatset)
L,supportData=apriori(mushDatset,0.3)
#
# for item in L[1]:
#     #if item.intersection('2'):
#     if set('2').issubset(item):
#         print(item)
for item in L[3]:
    #if item.intersection('2'):
    if set(['2']).issubset(item):
        print(item)
