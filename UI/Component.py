from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def draw(self):
        pass