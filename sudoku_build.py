#sudoku main wayne warren 2016
from sudoku_gen import *

# add uniqueness tests and if solvable after n removals so the gui module only checks if 
# a number matches the missing number

class Sudoku(object):
    """ provides a single sudoku table"""
    
    def __init__(self):
        
        self.su_grid = Grid()
        self.su_grid.gen_coords()
        self.invalid = 0
        self.count = 0
        
    def get_valid_sqrs(self,num):        
        
        square = [str(i) for i in range(0,9)]
        for sq in square:
                self.su_grid.build(sq, num)
                if self.su_grid.build(sq, num) == "invalid":
                    #print "invalid", sq, str(num)
                    # remove num from all of sq and previous 
                
                
                    self.invalid += 1
                    return False
                
    def make_sudoku(self):
        
        for i in range(1,10):
            self.get_valid_sqrs(i)

        # after trying each square and passing each test check for a 0, if none are found a valid board is made anyway
        if self.invalid == 0:
            for i in range(0,9):
                # a valid sqr has no zeros, it's filled
                if 0 in self.su_grid.layout[str(i)].get_all():
                    self.su_grid = Grid()
                    self.su_grid.gen_coords()
                    self.invalid = 0
                    self.make_sudoku()
                    #break
                
                    
        # one or more squares failed, so call this function again
        if self.invalid > 0:
            self.su_grid = Grid()
            self.su_grid.gen_coords()
            self.invalid = 0
            self.make_sudoku()

    def remove_cells(self,num=18):
        #even amount per sqr, of indexes of cells1-9. a reminder a sqr is one list, represented differently in print
        # remove 27, 3 from each

	# remember removals for gui
        
        square = [str(i) for i in range(0,9)]
##        for sq in square:
##            self.su_grid.layout[sq].first_row[ randint(0,2) ] = 0
##            self.su_grid.layout[sq].second_row[ randint(0,2) ] = 0
##            self.su_grid.layout[sq].third_row[ randint(0,2) ] = 0
        for sq in square:
            rand_first = randint(0,2)
            hidden_num_first = self.su_grid.layout[sq].first_row[ rand_first ] # remember num then change it
            self.su_grid.layout[sq].first_row[ rand_first ] = int("99"+str(hidden_num_first))  #using 99 because first 0's will be removed in an int

            rand_second = randint(0,2)
            hidden_num_second = self.su_grid.layout[sq].second_row[ rand_second ]
            self.su_grid.layout[sq].second_row[ rand_second ] = int("99"+str(hidden_num_second))
            
            rand_third = randint(0,2)
            hidden_num_third = self.su_grid.layout[sq].third_row[ rand_third ]
            self.su_grid.layout[sq].third_row[ rand_third ] = int("99" + str(hidden_num_third))
            
    def get_grid(self):
        return self.su_grid
    
    def print_grid(self):
	# actual order for game
        print(self.su_grid.layout["0"].first_row, self.su_grid.layout["1"].first_row, self.su_grid.layout["2"].first_row)
        print(self.su_grid.layout["0"].second_row, self.su_grid.layout["1"].second_row, self.su_grid.layout["2"].second_row)
        print(self.su_grid.layout["0"].third_row, self.su_grid.layout["1"].third_row, self.su_grid.layout["2"].third_row)
        print()
        print(self.su_grid.layout["3"].first_row, self.su_grid.layout["4"].first_row, self.su_grid.layout["5"].first_row)
        print(self.su_grid.layout["3"].second_row, self.su_grid.layout["4"].second_row, self.su_grid.layout["5"].second_row)
        print(self.su_grid.layout["3"].third_row, self.su_grid.layout["4"].third_row, self.su_grid.layout["5"].third_row)
        print()
        print(self.su_grid.layout["6"].first_row, self.su_grid.layout["7"].first_row, self.su_grid.layout["8"].first_row)
        print(self.su_grid.layout["6"].second_row, self.su_grid.layout["7"].second_row, self.su_grid.layout["8"].second_row)
        print(self.su_grid.layout["6"].third_row, self.su_grid.layout["7"].third_row, self.su_grid.layout["8"].third_row)




#sudoku = Sudoku()

##while True:
##    print "######"
##    sudoku.make_sudoku()
##    sudoku.print_grid()
##    print "######"
#sudoku.make_sudoku()
#sudoku.print_grid()

#removal
#sudoku.remove_cells()
#print
#sudoku.print_grid()

