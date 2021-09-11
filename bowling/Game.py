




class Game():

    def __str__(self):
        return str(self.games) + '\n' + str(self.totals) + '\n' + str(self.total)

    def __init__(self):
        self.games = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 10]] 


    def new_bowl(self, pin):
        pin = int(pin)
        if len(self.games) == 9:
            if pin == 10:
                self.games.append([10])
        elif len(self.games) == 10:

            if len(self.games[-1]) == 1:
                self.games[-1].append(pin)

                if sum(self.games[-1]) < 10:
                    return True
            elif len(self.games[-1]) == 2 and sum(self.games[-1]) > 10:
                self.games[-1].append(pin)
                return True


        elif pin == 10:
            self.games.append([10, 0])
        elif len(self.games) == 0:
            self.games.append([pin])
        elif len(self.games[-1]) == 1:
            self.games[-1].append(pin)
        else:
            self.games.append([pin])



    @property
    def total(self):
        return sum(self.totals)

    @property
    def totals(self):
        return [self.get_round_total(x) for x in range(len(self.games))]

    def get_round_total(self, r):
        if r >= len(self.games):
            return 0
        game = self.games[r]
        subtotal = sum(game)

        if r + 1 < len(self.games):
            # spare
            if subtotal == 10:
                subtotal += self.games[r+1][0]

            # strike
            if game[0] == 10:

                # get 2 from next game
                if r + 1 == 9 or self.games[r+1][0] != 10:
                    if len(self.games[r+1]) > 1:
                        subtotal += self.games[r+1][1]
                else: # get 1 from next game and 1 from the one after
                    if r + 2 < len(self.games):
                        subtotal += self.games[r+2][0]

        return subtotal





