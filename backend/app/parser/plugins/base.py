from abc import ABC
from abc import abstractmethod

from app.parser.models import ParsedFile


class BaseLanguagePlugin(ABC):

    @abstractmethod
    def extract(
        self,
        tree,
        source: str,
        path: str,
    ) -> ParsedFile:
        ...