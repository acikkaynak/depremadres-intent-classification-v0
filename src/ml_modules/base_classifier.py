from abc import ABC, abstractmethod
from typing import List


class BaseClassifier(ABC):

    @abstractmethod
    def classify(self, text: str) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def all_intents(self) -> List[str]:
        raise NotImplementedError
