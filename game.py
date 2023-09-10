class Game:
    def __init__(self, id):
        self.p1went = False #check if players have made a move or not
        self.p2went = False
        self.ready = False #
        self.id = id # this stands for the current game id. Each game is going to have its own id
        self.moves = [None, None] #currently both player 1 and 2 has not made a movee
        self.wins = [0,0] # tracks the wins, wins[0] initializes player 1 wins and wins[1] is for player 2
        self.ties = 0

    def get_player_move(self, p): # p is for players
        # p: [0,1] holds player 1 and 2 and we are returning their movement
        return self.moves[p]

    def player(self, player, move): #player can either be 0 or 1 which represent player 1 or 2 respectively. move is the movement of each player
        self.moves[player] = move
        if player == 0:
            self.p1went = True # verifies that player made a move
        else:
            self.p2went = True

    def connected(self): # tells if if both players are connect to the game and ready
        return self.ready

    def bothwent(self): # defines if both our players have moved
        return self.p1went and self.p2went

    def winner(self): #checks who won game
        return 1