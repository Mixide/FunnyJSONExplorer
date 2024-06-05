import json
from entry.entryBuilder import EntryBuilder
class Analyzer:
    def clean(self):
        self.list = []
        self.idx = 0

    def __init__(self):
        self.clean()

    def preanalyze(self,item, idx, siz, level,parents):
        key,value = item
        firstFlag = idx == 0
        lastFlag = idx == siz - 1
        rootFlag = len(self.list) == 0
        leafFlag = not isinstance(value, dict)
        entry = EntryBuilder().setfirst(firstFlag).setlast(lastFlag).setroot(rootFlag)\
        .setleaf(leafFlag).setkey(key).setvalue(value).setlevel(level).setparents(parents).build()
        self.list.append(entry)
        parents.append(len(self.list)-1)
        if(isinstance(value, dict)):
            for new_idx,new_item in enumerate(value.items()):
                self.preanalyze(new_item,new_idx,len(value),level+1,parents)
        parents.pop()

    def analyze(self,json_path):
        with open(json_path,'r') as json_file:
            root = json.load(json_file)
        self.clean()
        for idx, item in enumerate(root.items()):
            self.preanalyze(item,idx,len(root),0,[])

    def isroot(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].isroot
    
    def isleaf(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].isleaf
    
    def isfirst(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].isfirst
    
    def islast(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].islast
    
    def getValue(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].value
    
    def getKey(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].key
    
    def getlevel(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].level
    
    def getparents(self,idx = None):
        if idx == None:
            idx = self.idx
        return self.list[idx].parents
    
    def next(self):
        self.idx += 1

    def isend(self):
        return self.idx == len(self.list)