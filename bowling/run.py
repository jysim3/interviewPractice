from Game import Game

g = Game()
print(g)
while True:
    bowl = input('Bowl: ')
    if g.new_bowl(bowl):
        print(g)
        break
    print(g)
