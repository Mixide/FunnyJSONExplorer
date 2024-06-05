from abc import ABC, abstractmethod

class FJE_Factory(ABC):
    def __init__(self):
        self.leaf_icon = " "
        self.norm_icon = " "
    @abstractmethod
    def create_FJE(self):
        pass
