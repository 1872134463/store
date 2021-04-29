list=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
com={}
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for i in range(len(List)):
#      print( i ,"出现的次数为:",List.count(i),"次")
# print("----------------------------------")
for i in list:
    if i not in com:
        com[i]=1
    else:
        com[i]=com[i]+1
print(com)