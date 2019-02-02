from decimal import getcontext, Decimal
import time
import mylog

class log:
    fo = None
    filename=None

    def __init__(self,filepath=None):
        if filepath == None:
            self.filename = 'F:\\boceruninfo.txt'
        else:
            self.filename = filepath

    def logspendtime(self,pages,spend):
        site = mylog.JudSiteByHost()
        self.fo = open(self.filename, "a+")
        strcurtime = time.strftime("%D%H%M%S", time.localtime())
        strspend = str(Decimal(str(spend)).quantize(Decimal('0.00')))
        message = str(strcurtime) + " " + site + " " + pages + " "+ strspend + '\n'
        self.fo.write(message)
        self.fo.close()

