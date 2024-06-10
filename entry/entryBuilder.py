from entry import Entry
class EntryBuilder:#建造者模式的Builder，生成entry
    def __init__(self):
        self.entry = Entry()
    
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
        self.entry.key = str(key)
        return self

    def setvalue(self,value):
        if value == None:
            self.entry.value = ''
        else:
            self.entry.value = str(value)
        return self
    
    def setlevel(self,level):
        self.entry.level = level
        return self
    
    def setparents(self,parents):
        self.entry.parents = parents.copy()
        return self

    def setsons(self,sons):
        self.entry.sons = sons
        return self
    
    def build(self):
        return self.entry