from abc import ABC, abstractmethod

class LlmModel(ABC):

    @abstractmethod
    def getEmbeddingModel(self,engine):
        pass

    @abstractmethod
    def getChatModel(self,engine):
        pass

    @abstractmethod
    def getCodeModel(self,engine):
        pass