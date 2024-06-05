class Entry:
    def __init__(self):
        self.isroot = False
        self.isfirst = False
        self.isleaf = False
        self.islast = False
        self.parents = None
        self.level = None
        self.key = None
        self.value = None