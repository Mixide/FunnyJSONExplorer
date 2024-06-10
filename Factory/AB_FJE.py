from abc import ABC, abstractmethod
from Factory.analyzer import Analyzer
import json
class AB_FJE(ABC):#抽象FJE类，实现了一系列模板方法，并提供具体类接口
    def __init__(self,icon_path):
        self.analyzer = Analyzer()
        self._loadicon(icon_path)

    def _loadicon(self,icon_path):
        with open(icon_path,'r',encoding='utf-8') as icon_file:
            icon_data = json.load(icon_file)
            self.leaf_icon = icon_data['leaf']
            self.norm_icon = icon_data['non-leaf']

    def _loadfile(self,json_path):
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
    
    def show(self,json_path=None):
        if json_path != None:
            self._loadfile(json_path)
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
            icon = self.leaf_icon
        else:
            icon = self.norm_icon
        if self.isleaf() and self.getValue() != '':
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
