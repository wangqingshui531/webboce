from decimal import getcontext, Decimal
import time

class log:
    fo = None
    filename=None

    def __init__(self,filepath=None):
        if filepath == None:
            self.filename = 'F:\\boceruninfo.txt'
        else:
            self.filename = filepath

    def open(self):
        self.fo = open(self.filename, "a+")
        return self.fo

    def logspendtime(self,site,spend):
        strcurtime = time.strftime("%H%M%S", time.localtime())
        strspend = str(Decimal(str(spend)).quantize(Decimal('0.00')))
        message = str(strcurtime) + " " + site + " " + strspend + '\n'
        self.fo.write(message)

    def close(self):
        if self.fo == None:
            return
        self.fo.close()
