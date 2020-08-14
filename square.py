#make sudo grid first wayne w 1016



#shuffle(nums)
##[ 0, 0, 0
##  0, 0, 0
##  0, 0, 0]
class Square(object):

    def __init__(self, match_rows, match_cols):
        
        #keep where matching rows and columns are in other squares
        self.same_rows = match_rows
        self.same_cols = match_cols
        #rows
        self.first_row = [0,0,0]
        self.second_row= [0,0,0]
        self.third_row = [0,0,0]
        
        
    def add_number(self, value, row, col):
        # add by row col place
        if row == "first":
            if col == "first":
                self.first_row[0] = value
            if col == "second":
                self.first_row[1] = value
            if col == "third":
                self.first_row[2] = value

        if row == "second":
            if col == "first":
                self.second_row[0] = value
            if col == "second":
                self.second_row[1] = value
            if col == "third":
                self.second_row[2] = value

        if row == "third":
            if col == "first":
                self.third_row[0] = value
            if col == "second":
                self.third_row[1] = value
            if col == "third":
                self.third_row[2] = value


    def get_number(self, row, col):
        # return cell by row col place
        
        if row == "first":
            if col == "first":
                return self.first_row[0]
            if col == "second":
                return self.first_row[1] 
            if col == "third":
                return self.first_row[2] 

        if row == "second":
            if col == "first":
                return self.second_row[0] 
            if col == "second":
                return self.second_row[1] 
            if col == "third":
                return self.second_row[2] 

        if row == "third":
            if col == "first":
                return self.third_row[0] 
            if col == "second":
                return self.third_row[1] 
            if col == "third":
                return self.third_row[2] 

    def get_row(self, row):
        if row == "first":
            return self.first_row
            
        if row == "second":
            return self.second_row
            
        if row == "third":
            return self.third_row

    def get_col(self, col):
        """[0 1 2
            0 1 2
            0 1 2]"""
        if col == "first":
            return [self.first_row[0], self.second_row[0], self.third_row[0]]
            
        if col == "second":
            return [self.first_row[1], self.second_row[1], self.third_row[1]]
            
        if col == "third":
            return [self.first_row[2], self.second_row[2], self.third_row[2]]
            
            
    def print_all(self):
        print(self.first_row)
        print(self.second_row)
        print(self.third_row)
    
    def get_all(self):
        return self.first_row+self.second_row+self.third_row
    

