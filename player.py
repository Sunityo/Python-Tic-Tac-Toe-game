import random


class Player:
        def __init__(self, letter):
                self.symbol = letter
        
        def get_player_symbol(self):
                return self.symbol


class HumanPlayer(Player):
    
        def __init__(self, letter):
                Player.__init__(self, letter)      
    
        def play(self):
                # do nothing as the play is done at the Button_GUI
                pass 
        
    
 
class ComputerPlayer(Player):
    
        def __init__(self, letter, buttons_list):
                Player.__init__(self, letter)
                self.buttons_2d_list = buttons_list
        
        
        def play(self):
                is_space_free = False
                while (is_space_free == False):
                        print("Player %s turn" %self.get_player_symbol())
                        r = random.randint(0,2)
                        c = random.randint(0,2)
                        self.button = self.buttons_2d_list[r][c]
                        is_space_free = self.button["text"] == " "
                        self.button.invoke()


