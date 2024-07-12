#%%
from engine import Input, update, run
from factory.gates import Nand, And, Or, Not, Nor, Xor, Xnor
from typing import Callable
import itertools


def test_gate(gate: type, fn:Callable[[bool], bool] , n=2):
  inputs = [Input() for _ in range(n)]
  g = gate(*inputs)
  for data in itertools.product([True,False],repeat=len(inputs)):
    update()
    for d, input in zip(data,inputs): input.set(d)
    resp = run(g)
    assert resp == fn(*data), f'{g.name}: {data} -> {resp} != {fn(*data)}'

test_gate( Nand, lambda *x: (not all(x),), 2)

test_gate( Not, lambda x: (not x,), 1)

test_gate( And, lambda *x: (all(x),), 2)

test_gate( Or, lambda *x: (any(x),), 2)

test_gate( Nor, lambda *x: (not any(x),), 2)

test_gate( Xor, lambda x,y: (x != y,), 2)

test_gate( Xnor, lambda x,y: (x == y,), 2)
