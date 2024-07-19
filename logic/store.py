#%%
from logic import Not, And, Or, Composite, Nand
from logic.engine import Node, Input, run, update, Gate
from helpers import DEBUG

DEBUG.value = 1

i1 = Input()

clock = Not(i1)
clock.inputs = [clock]

# %%

put = Input()
clear = Input()

def flop(put:Input, clear:Input):
  a = And(Input(), Input())
  flop = Or(put, a)
  a.inputs = [Not(clear), flop]
  return flop

f = flop(put, clear)

put.set(True)

run(f)

# %%

update()
put.set(True)
run(f)

#%%


i1, i2 = Input(), Input()
a = And(i1, i2)
i1.set(True)
i2.set(True)
run(a)
o = Or(i1, i2)
#%%

o.fn(True,True)
