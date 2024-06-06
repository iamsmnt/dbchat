from abc import ABC, abstractmethod

class LlmEngine(ABC):

    @abstractmethod
    def getOllama(self,engine):
        pass

    @abstractmethod
    def getGoogleEngine(self,engine):
        pass

    @abstractmethod
    def getAWSEngine(self,engine):
        pass

    @abstractmethod
    def getAzureOpenAIEngine(self,engine):
        pass