list = [12, 35, 9, 56, 24]
def myfun(list):
     si = len(list)
     
     tmp = list[0]
     list[0]=list[si-1]
     list[si-1]=tmp
     
     return list
print(myfun(list))