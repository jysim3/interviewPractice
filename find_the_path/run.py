



from Map import Map
from Car import Car


m = Map()
print(m)
c = Car(m)
c.find_path(m.start, m.end)


