import os
import math
class Player:
  board = ['-']*9
  draw = False
  def __init__(self,name,choice,turn):
    self.name = name
    self.choice = choice
    self.turn = turn
    self.won = False
  
  def dispGrid(self,board):
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('___________')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('___________')
    print(f' {board[6]} | {board[7]} | {board[8]}')
  
  def checkChoice(self,ch):
    if(self.board[ch] == 'X' or self.board[ch] == 'O'):
      return False
    return True
  
  def play(self):
    print(f'({self.name}):')
    ch = int(input())
    while(self.checkChoice(ch-1) != True):
      print('Invalid choice . Please Enter again :')
      ch = int(input())
    self.board[ch-1] = self.choice
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')
    self.dispGrid(self.board)
    self.status(ch-1)
    self.checkDraw()
  
  def checkDiagonals(self,ch):
    if(ch%2 == 0):
      # print(f'{ch} is diagonal')
      d1 = 0
      d2 = 0
      for i in range(0,9,4):
        if(self.board[i] == self.choice):
          d1 += 1
      for i in range(2,7,2):
        if(self.board[i] == self.choice):
          d2 += 1
      if(d1 == 3 or d2 == 3):
        return True
    return False

  def status(self,ch):
    row = math.floor(ch/3)
    col = ch % 3
    # print(f'{row} {col}')
    if(self.checkRow(row) == True or self.checkCol(col) == True):
      print(f'{self.name} wins !!')
      self.won = True
    
    if(self.checkDiagonals(ch) == True):
      print(f'{self.name} wins !!')
      self.won = True

  def checkRow(self,row):
    count = 0
    for i in range(9):
      if(math.floor(i/3) == row):
        if(self.board[i] == self.choice):
          count += 1
    if(count == 3):
      return True
    return False

  def checkCol(self,col):
    count = 0
    for i in range(9):
      if(i%3 == col):
        if(self.board[i] == self.choice):
          count += 1
    if(count == 3):
      return True
    return False
  
  def checkDraw(self):
    if '-' not in self.board:
      print('--- Match Draw --- ')
      self.draw = True

player1 = Player('Player - 1','X',True)
player2 = Player('Player - 2','O',False)
player1.dispGrid(player1.board)


while(True):
  if(player1.turn == True):
    player1.turn = False
    player2.turn = True
    player1.play()
    if(player1.won == True or player1.draw == True):
      break
  if(player2.turn == True):
    player2.turn = False
    player1.turn = True
    player2.play()
    if(player2.won == True or player2.draw == True):
      break

# player1.board[2] = 1

# player2.dispGrid(player2.board)




