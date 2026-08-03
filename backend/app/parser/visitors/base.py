from abc import ABC, abstractmethod


class BaseVisitor(ABC):

    @abstractmethod
    def visit(self, node, source, result):
        pass