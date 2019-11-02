a={'name':'ok','数学':92,'语文':12,'英语':2}
def ooook(a):
    b=[i for i,j in a.items() if type(j)==int and j>90]
    return a.update({'评价':'优秀'}) if len(b)>=2 else a.update({'评价':'良好'})
