import random

#create 4*4 matrix(game board)
class Board:
    def __init__(self):
        self.board=[]
        for i in range(4):
            row = []
            for j in range(4):
                row.append(0)
            self.board.append(row)
            
    # print board
    
    def print_board(self):
        print self.board
        
    # randomly generate index and also(2 or 4 value)
    
    def add_random_2_or_4(self):
        while True:
            random_index_row = random.randint(0,3)
            random_index_col = random.randint(0,3)
            arr = [2,4]
            random_no_from_arr = random.randint(0,1)
            if self.board[random_index_row][random_index_col] == 0:
                self.board[random_index_row][random_index_col] = arr[random_no_from_arr]
                return
            
    # checking is game over- 3 condition apply
    # if any row has 0 element game will continue
    # if previous element of each row different game will over
    # check column wise also
    
    def is_game_over(self):
        for i in range(len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == 0:
                    return False

        for i in range(len(self.board)):
            for j in range(1, len(self.board[i])):
                if j < len(self.board[i]):
                    if self.board[i][j-1] == self.board[i][j]:
                        return False

        i = 1
        for i in range(1, len(self.board)):
            for j in range(0, len(self.board[i])):
                if j < len(self.board[i-1]):
                    if self.board[i-1][j] == self.board[i][j]:
                        return False
                    
        return True
    
    # iterate reverse for moving right
    
    def move_right(self):
        for index in range(len(self.board)):
            sub_list = self.board[index]
            p = len(sub_list)-1
            for i in reversed(range(len(sub_list)-1)):
                if sub_list[i] == 0:
                    continue
                elif sub_list[i] == sub_list[p]:
                    sub_list[p] = sub_list[p] + sub_list[i]
                    sub_list[i] = 0
                    p -= 1
                elif sub_list[p] == 0:
                    sub_list[p] = sub_list[i] + sub_list[p]
                    sub_list[i] = 0
                elif sub_list[p] != 0:
                    if i != p-1:
                        sub_list[p-1] = sub_list[i]
                        sub_list[i] = 0
                    p -= 1
                    
    # iterate over the list of list
    
    def move_left(self):
        for index in range(len(self.board)):
            sub_list = self.board[index]
            p = 0
            for i in range(1, len(sub_list)):
                #print sub_list[i], p
                if sub_list[i] == 0:
                    continue
                elif sub_list[i] == sub_list[p]:
                    sub_list[p] = sub_list[p] + sub_list[i]
                    sub_list[i] = 0
                    p += 1
                elif sub_list[p] == 0:
                    sub_list[p] = sub_list[i]
                    sub_list[i] = 0
                elif sub_list[p] != 0:
                    if i != p+1:
                        sub_list[p+1] = sub_list[i]
                        sub_list[i] = 0
                    p += 1
                
    def move_up(self):
        for c in range(len(self.board)):
            p = 0
            for r in range(1, len(self.board[c])):
                if self.board[r][c] == 0:
                    continue
                elif self.board[r][c] == self.board[p][c]:
                    self.board[p][c] = self.board[r][c] + self.board[p][c]
                    self.board[r][c] = 0
                    p += 1
                elif self.board[p][c] == 0:
                    self.board[p][c] = self.board[r][c]
                    self.board[r][c] = 0
                elif self.board[p][c] != 0:
                    if r != p+1:
                        self.board[p+1][c] = self.board[r][c]
                        self.board[r][c] = 0
                    p +=1
                    
    # iterate column wise
    
    def move_down(self):
        for c in range(len(self.board)):
            p = 3
            for r in reversed(range(len(self.board[c])-1)):
        #rint("p", A[r][c])
                if self.board[r][c] == 0:
                    continue
                elif self.board[r][c] == self.board[p][c]:
                    self.board[p][c] = self.board[r][c] + self.board[p][c]
                    self.board[r][c] = 0
                    p -= 1
                elif self.board[p][c] == 0:
                    self.board[p][c] = self.board[r][c]
                    self.board[r][c] = 0
                elif self.board[p][c] != 0:
                    if r != p-1:
                        self.board[p-1][c] = self.board[r][c]
                        self.board[r][c] = 0
                    p -=1
              
class Game:
    def __init__(self):
        self.board = Board()
        self.board.add_random_2_or_4()
        self.board.add_random_2_or_4()
        
    # iterate reversed as column wise
    def process_input(self,keyword):
        if keyword == 'a' or keyword == 'A':   #left
            self.board.move_left()          

        if keyword == 'd' or keyword == 'D':    #right
            self.board.move_right()            

        if keyword == 'w' or keyword == 'W':    #up
            self.board.move_up()
                    
        if keyword == 's' or keyword == 'S':   #down
            self.board.move_down()
        self.board.add_random_2_or_4()
            
    def check_is_game_over(self):
        return self.board.is_game_over()

        
    def display_board(self):
        self.board.print_board()
        
def main():       
    obj_game = Game()
    obj_game.display_board()
    while not obj_game.check_is_game_over():
        select = raw_input("press any key a/s/d/w: ")
        print select
        obj_game.process_input(select)
        obj_game.display_board()
    print "Game is over"
        
if __name__ == "__main__":
    main()

