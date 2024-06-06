from Factory import AB_FJE
from Factory import FJE_Factory

class TreeFJE(AB_FJE):
    def __init__(self, leafpre, normalpre):
        super().__init__(leafpre,normalpre)

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

class Tree_Factory(FJE_Factory):
    def __init__(self,icon_config):
        super().__init__(icon_config)

    def create_FJE(self):
        return TreeFJE(self.leaf_icon,self.norm_icon)   
        