from abc import ABC, abstractmethod


class PipelineStage(ABC):

    @abstractmethod
    def run(self, repository):
        pass