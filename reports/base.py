from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def update(self, data): pass

    @abstractmethod
    def display(self): pass
