from abc import ABC
from abc import abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    def generate(self, repository):
        pass