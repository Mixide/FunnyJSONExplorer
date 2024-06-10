import json
from entry.entryBuilder import EntryBuilder
class Analyzer:#json结构分析器，被FJE组合使用
    def clean(self):
        self.list = []
        self.idx = 0

    def __init__(self):
        self.clean()

    def preOrder_analyze(self,item, idx, siz, level,parents):
        key,value = item
        firstFlag = idx == 0
        lastFlag = idx == siz - 1
        leafFlag = not isinstance(value, dict)
        builder = EntryBuilder()
        entry = builder.setfirst(firstFlag).setlast(lastFlag).setleaf(leafFlag)\
            .setkey(key).setvalue(value).setlevel(level).setparents(parents).build()
        self.list.append(entry)
        parents.append(len(self.list)-1)
        sons = []
        if(isinstance(value, dict)):
            for new_idx,new_item in enumerate(value.items()):
                sons.append(len(self.list))
                self.preOrder_analyze(new_item,new_idx,len(value),level+1,parents)
        builder.setsons(sons)
        parents.pop()

    def analyze(self,json_path):
        with open(json_path,'r') as json_file:
            root = json.load(json_file)
        self.clean()
        for idx, item in enumerate(root.items()):
            self.preOrder_analyze(item,idx,len(root),0,[])

    def isroot(self,idx):
        return idx == 0
    
    def istail(self,idx):
        return idx + 1 == len(self.list)
    
    def isleaf(self,idx):
        return self.list[idx].isleaf
    
    def isfirst(self,idx):
        return self.list[idx].isfirst
    
    def islast(self,idx):
        return self.list[idx].islast
    
    def getValue(self,idx):
        return self.list[idx].value
    
    def getKey(self,idx):
        return self.list[idx].key
    
    def getLevel(self,idx):
        return self.list[idx].level
    
    def getParents(self,idx):
        return self.list[idx].parents
    
    def getSons(self,idx):
        return self.list[idx].sons
    
    def next(self):
        self.idx += 1

    def isend(self):
        return self.idx == len(self.list)