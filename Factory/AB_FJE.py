from abc import ABC, abstractmethod
from analyzer import Analyzer

class AB_FJE(ABC):
    analyzer = Analyzer()
    def __init__(self,leafpre,normalpre):
        self.leafpre = leafpre
        self.norpre = normalpre

    def load(self,json_path):
        self.json_path = json_path
        
    def isroot(self):
        return self.analyzer.isroot()    
    
    def isfirst(self):
        return self.analyzer.isroot()  
    
    def islast(self):
        return self.analyzer.isroot()  
    
    def isleaf(self):
        return self.analyzer.isroot()  
    
    def show(self):
        self.analyzer.analyze(self.json_path)
        while not self.analyzer.isend():
            self.showSingle()
            self.analyzer.next()

    @abstractmethod
    def showSingle(self):
        pass

    