#!/usr/bin/env python

# sudoku gtk version by wayne warren 2016 

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from sudoku_build import * 

# used entry.set_max_length(1)
#entry.set_max_width_chars(1)
#entry.set_width_chars(1)
# to stop entry expanding

class SudokuGUI(object):

    def __init__(self):
        # for game answers
        # for entries which should have the right answer
        self.answers={}
        self.keyentry = 0
        self.print_checked = True
        

        # WINDOW
        #self.width = 100
        #self.height = 100
        self.win = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.win.set_title("Sudoku") 
        self.win.set_border_width(5)
        #self.win.set_size_request(400,400)
        #self.win.set_size_request(self.width, self.height)
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", self.die)

        ## Game info, computer player label
        self.computer_lable= Gtk.Label(label="Test game: By wayneww")

        ## Top box
        self.top_box = Gtk.HBox(homogeneous=False)
        self.top_box.pack_start(self.computer_lable, padding=5, expand=False,fill=False)

        ## Mid box, board
        
        self.mid_box = Gtk.VBox(homogeneous=False)
        self.build_grid()
    
        ## Low box, new game etc
        self.lower_box = Gtk.HBox(homogeneous=False)
        self.check_button = Gtk.Button("Check")
        self.check_button.connect("clicked", self.check_game)
        self.lower_box.pack_start(self.check_button,expand=False,fill=False, padding=1)

        #final box to pack all others
        self.big_box = Gtk.VBox(homogeneous=False)
        self.big_box.pack_start(self.top_box,expand=False,fill=False, padding=1)
        self.big_box.pack_start(self.mid_box,expand=False,fill=False, padding=1)
        # ADD BACK
        self.big_box.pack_start(self.lower_box,expand=False,fill=False, padding=1)
        self.win.add(self.big_box)
        self.win.show_all()

    ### Window methods
    def check_game(self, widget, data=None):
        print() 
        print(data)

        for key_num in self.answers:
            # - 0 the object, 1 - the answer
            
            
            #print type(self.answers[key_num][0].get_text()),  type(self.answers[key_num][1] )
            if self.answers[key_num][0].get_text() ==  self.answers[key_num][1]:
                pass
            else:
                print(self.answers[key_num][0].set_text(""))

        # temp to show answers
        if self.print_checked:
            for key_num in self.answers:
                # - 0 the object, 1 - the answer
                entry_txt = self.answers[key_num][0].get_text()
                if len(entry_txt) <1:
                    print("0" + " : "+ self.answers[key_num][1]) 
                else:
                    print(entry_txt + " : "+ self.answers[key_num][1]) 

    def new_game(self):
        #clear answers and build grid again
        self.answers = []
        
    def build_grid(self):
        # a new sudoku grid is local to this method, call make sudoku agian to buid new grid
        game = Sudoku()
        game.make_sudoku()
        #game.print_grid()

        #removal of cells, this part is basic at the moment, no checks for uniqueness
        game.remove_cells()
        #game.print_grid()

        # pack entrys
        square = [str(i) for i in range(0,9)] # each dict element is indexed by str(n)
        board = game.get_grid()

        # packing
        count = 0 # for hhbox
        
        big_row_one = Gtk.HBox(homogeneous=False) # 3 of them containing 3 squares
        big_row_two = Gtk.HBox(homogeneous=False)
        big_row_three = Gtk.HBox(homogeneous=False)

        
        
        for sq in square:
            # each is reassigned and added per larger square
            entry_firstrow = Gtk.HBox(homogeneous=False) #one for each sqr
            entry_secondrow = Gtk.HBox(homogeneous=False) #one for each sqr
            entry_thirdrow = Gtk.HBox(homogeneous=False) #one for each sqr
            # sqr, a vertical box to hold these rows
            sqr_frame = Gtk.Frame()
            sqr_frame.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("pink"))
            sqr_box = Gtk.VBox(homogeneous=False)
            
            # but each vbox of sqr should also be in a row for tidyness

            for num in board.layout[sq].first_row:
                if str(num)[:2] == "99": # not 0 as before because 99 will be kept in a cast to int
                    entry = Gtk.Entry()
                    
                    entry.props.valign = Gtk.Align.CENTER
                    entry.set_max_length(1)
                    entry.set_max_width_chars(1)
                    entry.set_width_chars(1)
                    
                    self.answers[self.keyentry] = [ entry,  str(num)[2:] ]
                    self.keyentry += 1
                else:
                    entry = Gtk.Entry()
                    entry.props.valign = Gtk.Align.CENTER
                    entry.set_max_length(1)
                    entry.set_max_width_chars(1)
                    entry.set_width_chars(1)
                    
                    entry.set_text(str(num))
                    entry.set_editable(False)
                    
                entry_firstrow.pack_start(entry,expand=False,fill=False, padding=1)
                
            sqr_box.pack_start(entry_firstrow, expand=False,fill=False, padding=1)
            
            for num in board.layout[sq].second_row:
                if str(num)[:2] == "99":
                    entry = Gtk.Entry()
                    
                    entry.props.valign = Gtk.Align.CENTER
                    entry.set_max_length(1)
                    entry.set_max_width_chars(1)
                    entry.set_width_chars(1)
                    
                    self.answers[self.keyentry] = [ entry,  str(num)[2:] ]
                    self.keyentry += 1
                else:
                    entry = Gtk.Entry()
                    entry.props.valign = Gtk.Align.CENTER
                    entry.set_max_length(1)
                    entry.set_max_width_chars(1)
                    entry.set_width_chars(1)
        
                    entry.set_text(str(num))
                    entry.set_editable(False)
                    
                entry_secondrow.pack_start(entry, expand=False,fill=False, padding=1)
                
            sqr_box.pack_start(entry_secondrow, expand=False,fill=False, padding=1)
            
            for num in board.layout[sq].third_row:
                if str(num)[:2] == "99":
                    entry = Gtk.Entry()
                    
                    entry.props.valign = Gtk.Align.CENTER
                    entry.set_max_length(1)
                    entry.set_max_width_chars(1)
                    entry.set_width_chars(1)
                    
                    self.answers[self.keyentry] = [ entry,  str(num)[2:] ]
                    self.keyentry += 1
                    
                else:
                    entry = Gtk.Entry()
                    entry.props.valign = Gtk.Align.CENTER
                    entry.set_max_length(1)
                    entry.set_max_width_chars(1)
                    entry.set_width_chars(1)
                    
                    entry.set_text(str(num))
                    entry.set_editable(False)
                    
                entry_thirdrow.pack_start(entry,expand=False,fill=False, padding=1)

            sqr_box.pack_start(entry_thirdrow,expand=False,fill=False, padding=1)
            sqr_frame.add(sqr_box)
            
            #sorting big rows 
            if int(sq) <= 2:
                big_row_one.pack_start(sqr_frame, expand=False,fill=False, padding=5)
            if int(sq) > 2 and int(sq) <=5:
                big_row_two.pack_start(sqr_frame, expand=False,fill=False, padding=5)
            else:
                big_row_three.pack_start(sqr_frame,expand=False,fill=False, padding=5)
        #lastly pack the big rows into the main mid box

        self.mid_box.pack_start(big_row_one,expand=False,fill=False,padding=5)
        self.mid_box.pack_start(big_row_two,expand=False,fill=False,padding=5)
        self.mid_box.pack_start(big_row_three,expand=False,fill=False,padding=5)
        
        #self.mid_box.set_hexpand(False)
        #print self.answers
        self.keyentry = 0
                    
    def die(self, widget, data=None):
        """close"""
        Gtk.main_quit()

    def main(self):
        Gtk.main()


    

if __name__ == "__main__":
    root_window = SudokuGUI()
    root_window.main()
