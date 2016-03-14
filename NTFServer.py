import pynma
import setting
from datetime import datetime
import time 
week = 0
listclass = []

def readfile(name):
    global week
    global listclass
    if int(time.strftime('%H')) is 0:
        week = 0
    else:
        pass
    if week <= int(len(setting.user)) - 1:
        cls = open('./classraw/' + name, 'r')
        listcls = cls.readline()
        cals = listcls
        cls.close()
        clsdb = open('./classdb/' + name, 'w')
        clsdb.write(str(cals))
        clsdb.close()
        week = week + 1
        return 0
    else:
        return 0

while 1:
    for x in setting.user:
        readfile(x[0])
        db = open('./classdb/' + x[0], 'r')
        listdb = db.readline()
        listdbl = eval(listdb)
        count = 0
        db.close()
        for xx in listdbl:
            if int(xx[1]) is int(datetime.now().weekday()) + 1:
                if int(xx[2]) is int(time.strftime('%H')):
                    p = pynma.PyNMA(x[1])
                    p.push('下一節課', xx[0], '小時: ' + xx[3] + ',教室: ' + xx[4])
                    print(xx[0])
                    listdbl.pop(count)
                    wdb = open('./classdb/' + x[0], 'w')
                    wdb.write(str(listdbl))
                    wdb.close()
                else:
                    count = count + 1
                    pass
            else:
                count = count + 1
                pass
