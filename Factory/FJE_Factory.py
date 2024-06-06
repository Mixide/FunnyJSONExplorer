from abc import ABC, abstractmethod
import json
class FJE_Factory(ABC):
    def __init__(self,icon_config):
        self.leaf_icon = " "
        self.norm_icon = " "
        self.load_icon(icon_config)

    def load_icon(self,icon_config):
        with open(icon_config,'r',encoding='utf-8') as icon_file:
            icon_data = json.load(icon_file)
            self.leaf_icon = icon_data['leaf']
            self.norm_icon = icon_data['non-leaf']

    @abstractmethod
    def create_FJE(self):
        pass
