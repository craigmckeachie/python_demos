from abc import ABCMeta, ABC, abstractmethod

# class Logger(metaclass=ABCMeta):


class Logger(ABC):
    @abstractmethod
    def log(self, entry):
        pass
