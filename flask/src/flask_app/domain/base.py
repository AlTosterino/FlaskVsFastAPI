from abc import ABC as Abstract
from abc import abstractmethod


class Entity(Abstract):
    @abstractmethod
    def as_dict(self) -> dict:
        pass
