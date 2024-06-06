from abc import ABC, abstractmethod
from analyzer import Analyzer

class AB_FJE(ABC):
    def __init__(self,leafpre,normalpre):
        self.analyzer = Analyzer()
        self.leafpre = leafpre
        self.norpre = normalpre

    def _load(self,json_path):
        self.json_path = json_path
        
    def getIndex(self):
        return self.analyzer.idx
    
    def isroot(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.isroot(idx)    
    
    def isfirst(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.isfirst(idx)  
    
    def islast(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.islast(idx)  
    
    def isleaf(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.isleaf(idx)  
    
    def istail(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.istail(idx)
    
    def getKey(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.getKey(idx)
    
    def getValue(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.getValue(idx)

    def getParents(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.getParents(idx)
    
    def getSons(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.getSons(idx)
    
    def getLevel(self,idx = None):
        if idx == None:
            idx = self.getIndex()
        return self.analyzer.getLevel(idx)
    
    def isend(self):
        return self.analyzer.isend()
    
    def next(self):
        return self.analyzer.next()
    
    def show(self,json_path):
        self._load(json_path)
        self.analyzer.analyze(self.json_path)
        while not self.isend():
            self.setPrefix()
            self.setSuffix()
            self.showSingle()
            self.next()
    
    def showSingle(self):
        print(self.getPrefix()+self.getEntryView()+self.getSuffix())
    
    def getEntryView(self):
        if self.isleaf():
            icon = self.leafpre
        else:
            icon = self.norpre
        if self.isleaf() and self.getValue() != None:
            return icon + self.getKey()+':'+self.getValue()
        return icon + self.getKey()
    
    def getPrefix(self):
        return self.prefix
    
    def getSuffix(self):
        return self.suffix
    
    @abstractmethod
    def setPrefix(self):
        self.prefix = ""
    
    @abstractmethod
    def setSuffix(self):
        self.suffix = ""
