from core.api.api import core

exec("from content.not_physical import *")
exec("from content.tower import *")
exec("from content.tree import *")
exec("from content.TNT import *")

for x in range(25): core.spawn(not_physical, x * core.meter, 0)

tower().poke(4 * core.meter, -core.meter)

sapling = sapling()
sapling.x = 19 * core.meter
sapling.y = -core.meter
sapling.poke()

core.spawn(TNT, 11 * core.meter, -core.meter)
core.spawn(TNT, 11.45 * core.meter, -2 * core.meter)
core.spawn(TNT, 12 * core.meter, -core.meter)
  
scene = 0