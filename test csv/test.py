from operator import length_hint
import pandas

val = pandas.read_csv('test1.csv')

#print(val)
# i=0
# j=1
# info = val.loc[0,'code']
# total = val.loc[:,'code']
# print(length_hint(total))
# if info in total:
#     print (info)
# elif info is not total:
#     info=total
#     print(info) 

# print (info)

total = val.loc[:,'code']
info = {}
j=0
for i in total : 
    if i not in info: 
        info["cathegorie_"+i]=i
print(info)
    