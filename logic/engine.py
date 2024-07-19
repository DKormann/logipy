#%%
from functools import lru_cache
from typing import Any, List, Callable, Tuple, Optional, Dict
from helpers import DEBUG


class Node:
  name= "Node"
  def __init__(self,inputs, fn:Callable , outsize:int=1):
    self.fn = fn
    self.inputs = inputs
    self.outsize = outsize
  def __repr__(self) -> str:
    return f"{self.name}[{len(self.inputs)}->{self.outsize}]"

class Input(Node):
  name = "Input"
  def __init__(self, value:bool = False):
    self.value: bool = value
    super().__init__([], fn=lambda: (self.value,))
  def set(self, value:bool): self.value = value

def Gate(fn:Callable, n:Optional[int]=None, name=None, outsize=1, cached=True):
  if cached: fn = lru_cache(8)(fn)
  class _Gate(Node):
    def __init__(self, *inputs:Node):
      assert isinstance(inputs[0], Node), f"{inputs}"
      if n is not None: assert n == sum([i.outsize for i in inputs])
      super().__init__(inputs, fn=fn, outsize = outsize)
      self.name = name
  return _Gate

cache: Dict[Node, Tuple[bool, ...]] = {}
old_cache = cache.copy()
visited = set()

def ceval(gate: Gate):
  if gate in visited:
    if gate in cache: return cache[gate]
    if gate in old_cache: return old_cache[gate]
    return tuple((False,)*gate.outsize)
  visited.add(gate)
  data = sum((ceval(i) for i in gate.inputs), tuple())
  res = gate.fn(*data)
  if DEBUG.value > 0: print(f"{gate.name}: {data} -> {res}")
  cache[gate] = res
  return res

def update():
  global cache, old_cache
  old_cache.clear()
  old_cache = cache
  cache = {}
  visited.clear()


def run(*gate: Gate): return tuple(sum((ceval(g) for g in gate), tuple()))


def Composite(inputs:List[Input], sinks: List[Gate], name=None):

  replace = {i:Input() for i in inputs}

  @lru_cache
  def deepcopy(node:Node):
    if node in replace: return replace[node]
    args = [deepcopy(i) for i in node.inputs]
    res = type(node)(*args)
    return res

  sinks = [deepcopy(s) for s in sinks]
  inputs = [replace[i] for i in inputs]

  def fn(*data:bool):
    for i,d in zip(inputs,data): i.set(d)
    return tuple(sum((ceval(g) for g in sinks), tuple()))  

  
  g = Gate(fn, len(inputs), name)
  g.sinks = sinks
  return g

