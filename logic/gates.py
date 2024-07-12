#%%
from logipy.engine import Gate, Input, run, update, Composite

i1, i2 = Input(), Input()
Nand = Gate(lambda *x: (not all(x),), name="Nand")
Not = Composite([i1], [Nand(i1,i1)], name="Not")
And = Composite([i1,i2], [Not(Nand(i1,i2))], name="And")
Or = Composite([i1,i2], [Nand(Not(i1), Not(i2))], name="Or")
Nor = Composite([i1,i2], [Not(Or(i1,i2))], name="Nor")
Xor = Composite([i1,i2], [And(Or(i1,i2), Nand(i1,i2))], name="Xor")
Xnor = Composite([i1,i2], [Not(Xor(i1,i2))], name="Xnor")
