from square import *
from random import randint,choice


from sys import setrecursionlimit
setrecursionlimit(10000)

class Grid(object):

    def __init__(self):
        
        #
        self.place = ["first", "second", "third"]
        # build square that keeps adjecent rows, cols
        self.top_left = Square(["1","2"],["3","6"]) #0 obj
        self.top_middle = Square(["0","2"],["4","7"]) #1
        self.top_right = Square(["0","1"],["5","8"])
        self.middle_left = Square(["4","5"],["0","6"])
        self.middle_center = Square(["3","5"],["1","7"])
        self.middle_right = Square(["3","4"],["2","8"])
        self.bottom_left = Square(["7","8"],["0","3"])
        self.bottom_middle = Square(["6","8"],["1","4"])
        self.bottom_right = Square(["7","6"],["2","5"])

        self.layout = { "0":self.top_left,"1":self.top_middle,"2":self.top_right,
                        "3":self.middle_left,"4":self.middle_center,"5":self.middle_right,
                        "6":self.bottom_left,"7":self.bottom_middle,"8":self.bottom_right
                        }

        self.coords =[]
        

    def gen_coords(self):
        for x in range(len(self.place)):
            for y in range(len(self.place)):
                self.coords.append( [ self.place[x], self.place[y] ])
        
    def build(self, start_square="0", num=1):
        
        # try these rows and cols per sqr
        try:
            #print self.coord_index, len(self.coords)
            if len(self.coords) == 0:
                #print "no more choices"
                self.coords =[]
                self.gen_coords()
                return "invalid"            #tried every coord choice
            else:
                cord = choice(self.coords)
                #print cord, self.coords.index(cord)
                
                row = cord[0]
                col = cord[1]

                del self.coords[self.coords.index(cord)]

                #get the number that indicates neighbouring row and col , they are in pairs
                next_rows = self.layout[start_square].same_rows
                next_cols = self.layout[start_square].same_cols
                
                #check self then cell
                if num not in self.layout[start_square].get_all() and self.layout[start_square].get_number(row, col) == 0 and\
                num not in self.layout[next_rows[0]].get_row(row) and\
                num not in self.layout[next_rows[1]].get_row(row) and\
                num not in self.layout[next_cols[0]].get_col(col) and\
                num not in self.layout[next_cols[1]].get_col(col):
                    #add num to valid row col                   
                    self.layout[start_square].add_number(num, row, col)
                    # test print
                    #print start_square, len(self.coords)
                    #self.layout[start_square].print_all()
                    #print "\n"
                    self.coords =[]
                    self.gen_coords()
                    return "valid"
                else:
                    if len(self.coords) > 0:
                        self.build(start_square, num)
                
        except RuntimeError as e:
            print("too deep for me")
            return "invalid"





