#%%

from os import getenv

class Var:
  def __init__(self, name, default=None):
    self.name = name
    self.value = getenv(name, default)
    if type(default) in (int, float, bool): self.value = type(default)(self.value)

DEBUG = Var("DEBUG", 0)
