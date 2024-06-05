from Factory import AB_FJE
from Factory import FJE_Factory

class TreeFJE(AB_FJE):
    def __init__(self, leafpre, normalpre):
        super().__init__(leafpre,normalpre)
    
    def showSingle(self):
        pre = ""
        for p_idx in self.analyzer.getparents():
            if not self.analyzer.islast(p_idx):
                pre += '|  '
            else:
                pre += '   '
        if self.analyzer.islast():
            pre += '└─'
        else:
            pre += '├─'
        if self.analyzer.isleaf():
            pre += self.leafpre
        else:
            pre += self.norpre
        if self.analyzer.isleaf() and self.analyzer.getValue() != None:
            print(pre + self.analyzer.getKey()+':'+self.analyzer.getValue())
        else:
            print(pre + self.analyzer.getKey())

class Tree_Factory(FJE_Factory):
    def __init__(self):
        super().__init__()

    def create_FJE(self):
        return TreeFJE(self.leaf_icon,self.norm_icon)   
        