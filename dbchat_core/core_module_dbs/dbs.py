from abc import ABC, abstractmethod

class DBInterface(ABC):

    @abstractmethod
    def getPostgresDB(self,engine):
        pass