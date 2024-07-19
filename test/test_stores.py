
#%%
from logic.store import clock
from logic.engine import run, update


def test_clock():

  value = run(clock)
  for i in range(10):
    update()
    assert value != (value:=run(clock))
