class Game():
    def __init__(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,}
        
    def play_game(self):
            print("Shall we play a game?")
            while(not self.winner or not self.tie):
                self.render()
                self.get_move()
                self.checkForWinner()
                self.checkForTie()
                self.switch_turn()
            
            self.render()
    # While there is no winner or tie
        # render
        # get player input
        # check for a winner
        # check for a tie
        # switch turns
        # ...repeat until there is a winner or tie
    # Outside the loop, render state at the end of a game


    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else: print(f"It's player {self.turn}'s turn!")
    

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while(True):
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move.lower() in self.board.keys() and self.board[move.lower()] == None:
                break
        self.board[move.lower()] = self.turn

    
    def checkForWinner(self):
        return self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])
    
    def checkForTie(self):
        for key in self.board:
            if self.board[key] == None:
                return False
        if self.winner:
            return False
        
        return True
    
    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"



game_instance = Game()
game_instance.play_game()
# game_instance.print_board()

