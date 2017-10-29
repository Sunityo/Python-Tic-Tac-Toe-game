import tkinter 
from sys import exit
from tkinter import messagebox
from gameboard import GameBoard
from player import HumanPlayer
from player import ComputerPlayer

class GameGUI:
                
        def __init__(self):
                
                self.mw = tkinter.Tk()
                
                self.size = 3
                self.buttons_2d_list =  []
                for i in range (self.size):
                        self.row = [' ']*self.size
                        self.buttons_2d_list.append(self.row)
                
                # place players 1 and 2 in tuple for turn based game. 
                self.gboard = GameBoard(3)
                p1 = HumanPlayer("X")   
                p2 = ComputerPlayer("O", self.buttons_2d_list)
                
                self.players_lst = (p1, p2)
                self.currnt_player_index = 0
                self.winner = False

    
        def clicked_btn(self,x, y):
        
                p = self.players_lst[self.currnt_player_index]
                
                button = self.buttons_2d_list[x][y] # get the button instance from the list
                if button["text"] == " ":
                                
                        button["text"] = p.get_player_symbol()
                        
                        self.gboard.make_move(x, y, p.get_player_symbol())
                        
                        #self.gboard.show_board_dynamic()
                        
                        winner = self.gboard.check_winner() # The board will check after each move, if any player has won the game
                        
                        is_full = self.gboard.is_board_full()
                        
                        if winner == True:
                                # Show current player's symbol as Winner, 
                                        # and terminate the game
                                win_messge = ("Player %s is the Winner!" % p.get_player_symbol())
                                messagebox.showinfo("Winner Info ",win_messge)
                                self.mw.destroy()
                                exit()
                
                        elif is_full == True:
                                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                                self.mw.destroy()
                                exit()
                        else:
                                pass
                 
                
                        # change player index to allow the next player to play. 
                        if self.currnt_player_index == 1:
                                self.currnt_player_index = 0
                        else:
                                self.currnt_player_index+=1 # increment index by 1

                        p = self.players_lst[self.currnt_player_index]
                        p.play()
        
        
        def intialise_dynamic(self):
                for x in range(3):
                        for y in range(3):

                                self.button = tkinter.Button(self.mw, text = " ", font = ('Arial 30 bold'), command = lambda i = x, j = y: self.clicked_btn(i,j), height = 5, width = 10)
                                self.button.grid(row=x,column=y)
                                self.buttons_2d_list[x][y] = self.button
                
def main():
        b_gui = GameGUI()
        b_gui.intialise_dynamic()
        gui = b_gui             
                
main()  
