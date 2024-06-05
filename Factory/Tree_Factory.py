from Factory import AB_FJE
from Factory import FJE_Factory
import json
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

class TreeFJE_Factory(FJE_Factory):
    def __init__(self):
        super().__init__()
        
    def load_icon(self,icon_config):
        with open(icon_config,'r',encoding='utf-8') as icon_file:
            icon_data = json.load(icon_file)
            self.leaf_icon = icon_data['leaf']
            self.norm_icon = icon_data['non-leaf']

    def create_FJE(self):
        return TreeFJE(self.leaf_icon,self.norm_icon)   
        