
class SyntaxNode:
  
  def __init__ (self, character=None, function=None):
    self.character = character
    self.function = function
    self.nodes = list()
  
  def has_character (self, character):
    for node in self.nodes:
      if node.character == character:
        return True
    return False
  
  def get (self, character):
    for node in self.nodes:
      if node.character == character:
        return node
    return None 
  
  def dig (self, character):
    if not self.has_character(character):
      self.nodes.append(
        self.make_node(character))
    return self.get(character)
  
  def make_node (self, character):
    return SyntaxNode(character)
  
  def set_function (self, function):
    self.function = function
  
  def get_function (self):
    return self.function
  