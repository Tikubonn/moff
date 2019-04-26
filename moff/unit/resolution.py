
from .unit import Unit

class Resolution (Unit):
  
  def __init__ (self, num):
    self.num = num
  
  # override
  def __eq__ (self, instance):
    return (
      isinstance(instance, Resolution) and
      self.num == instance.num)
  
  # override
  def write (self, stream):
    stream.write(str(self.num))
    stream.write("x")
  