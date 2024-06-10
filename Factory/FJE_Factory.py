from abc import ABC, abstractmethod
class FJE_Factory(ABC):
    @abstractmethod
    def createFJE(self,icon_path):
        pass
