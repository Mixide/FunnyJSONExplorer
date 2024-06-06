from Factory import AB_FJE
from Factory import FJE_Factory
import os

class RectFJE(AB_FJE):
    def __init__(self, leafpre, normalpre,width):
        super().__init__(leafpre,normalpre)
        self.width = width
    
    def setPrefix(self):
        super().setPrefix()
        for _ in self.getParents():
            if self.istail():
                self.prefix += '└──'
            else:
                self.prefix += '|──'
        if self.isroot():
            self.prefix += '┌─'
        elif self.istail():
            self.prefix += '└─'
        else:
            self.prefix += '├─'

    def setSuffix(self):
        super().setSuffix()
        length = len(self.getPrefix()+self.getEntryView())
        if length < self.width:
            self.suffix += '─' * (self.width-1-length)
        if self.isroot():
            self.suffix  += '┐'
        elif self.istail():
            self.suffix  += '┘'
        else:
            self.suffix  += '|'

class Rect_Factory(FJE_Factory):
    def __init__(self,icon_config):
        super().__init__(icon_config)

    def create_FJE(self):
        try:
            width = int(os.getenv('WIDTH'))#从环境变量中读取矩形的宽度
        except Exception as e:
            width = 50#无有效设置时，默认宽度为50
        return RectFJE(self.leaf_icon,self.norm_icon,width) 
    