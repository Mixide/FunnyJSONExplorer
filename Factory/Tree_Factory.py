from Factory import AB_FJE
from Factory import FJE_Factory

class TreeFJE(AB_FJE):#具体产品2
    def __init__(self, icon_path):
        super().__init__(icon_path)

    def setPrefix(self):
        super().setPrefix()
        for p_idx in self.getParents():
            if not self.islast(p_idx):
                self.prefix += '|  '
            else:
                self.prefix += '   '
        if self.islast():
            self.prefix += '└─'
        else:
            self.prefix += '├─'
    
    def setSuffix(self):
        super().setSuffix()

class Tree_Factory(FJE_Factory):#具体工厂2
    def createFJE(self,icon_path):
        return TreeFJE(icon_path)   
        