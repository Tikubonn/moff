
from abc import ABC, abstractmethod

class Unit (ABC):
  
  @abstractmethod
  def write (self, stream):
    pass
