from Factory import AB_FJE
from Factory import FJE_Factory
import os

class RectFJE(AB_FJE):
    def __init__(self, leafpre, normalpre,width):
        super().__init__(leafpre,normalpre)
        self.width = width
    
    def showSingle(self):
        pre = ""
        for _ in self.analyzer.getparents():
            if self.analyzer.istail():
                pre += '└──'
            else:
                pre += '|──'
        if self.analyzer.isroot():
            pre += '┌─'
        elif self.analyzer.istail():
            pre += '└─'
        else:
            pre += '├─'
        if self.analyzer.isleaf():
            pre += self.leafpre
        else:
            pre += self.norpre
        if self.analyzer.isleaf() and self.analyzer.getValue() != None:
            pre += self.analyzer.getKey()+':'+self.analyzer.getValue()
        else:
            pre += self.analyzer.getKey()
        if len(pre) < self.width:
            pre += '─' * (self.width-1-len(pre))
        if self.analyzer.isroot():
            pre += '┐'
        elif self.analyzer.istail():
            pre += '┘'
        else:
            pre += '|'
        print(pre)

class Rect_Factory(FJE_Factory):
    def __init__(self):
        super().__init__()

    def create_FJE(self):
        try:
            width = os.environ['WIDTH']
        except:
            width = 50
        return RectFJE(self.leaf_icon,self.norm_icon,width) 
    