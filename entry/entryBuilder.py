from entry import Entry
class EntryBuilder:
    def __init__(self):
        self.entry = Entry()

    def setroot(self,rootFlag):
        self.entry.isroot = rootFlag
        return self
    
    def setfirst(self,firstFlag):
        self.entry.isfirst = firstFlag
        return self

    def setleaf(self,leafFlag):
        self.entry.isleaf = leafFlag
        return self

    def setlast(self,lastFlag):
        self.entry.islast = lastFlag
        return self
    
    def setkey(self,key):
        self.entry.key = key
        return self

    def setvalue(self,value):
        self.entry.value = value
        return self
    
    def setlevel(self,level):
        self.entry.level = level
        return self
    
    def setparents(self,parents):
        self.entry.parents = parents.copy()
        return self

    def build(self):
        return self.entry