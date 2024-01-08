import visual

class RubiksCube:
    def __init__(self):
        self.cube = [
                [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[0,2,0],[0,2,1],[0,2,2]], # Top Face (White Core)
                [[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2],[1,2,0],[1,2,1],[1,2,2]], # Left Face (Green Core)
                [[2,0,0],[2,0,1],[2,0,2],[2,1,0],[2,1,1],[2,1,2],[2,2,0],[2,2,1],[2,2,2]], # Front Face (Red Core)
                [[3,0,0],[3,0,1],[3,0,2],[3,1,0],[3,1,1],[3,1,2],[3,2,0],[3,2,1],[3,2,2]], # Right Face (Blue Core)
                [[4,0,0],[4,0,1],[4,0,2],[4,1,0],[4,1,1],[4,1,2],[4,2,0],[4,2,1],[4,2,2]], # Back Face (Orange Core)
                [[5,0,0],[5,0,1],[5,0,2],[5,1,0],[5,1,1],[5,1,2],[5,2,0],[5,2,1],[5,2,2]] # Bottom Face (Yellow Core)
            ] 
        
    def scramble_cube(self,scramble_pattern):
        """ This will handle a scrambling
        pattern. There are 6 different notations
        used for showing which way to turn cube.
        There are also prime varraints of each turn.
        """

        scramble = scramble_pattern.split()

        for s in scramble:
            if(s == "U"):
                self.horizontal_turn(0,False)
            if(s == "U2"):
                self.horizontal_turn(0,False)
                self.horizontal_turn(0,False)
            if(s == "U'"):
                self.horizontal_turn(0,True) 
            if(s == "D"):
                self.horizontal_turn(2,False)
            if(s == "D2"):
                self.horizontal_turn(2,False)
                self.horizontal_turn(2,False)
            if(s == "D'"):
                self.horizontal_turn(2,True) 
    
    def clockwise_face_rotation(self, face):
        """"
        0 1 2   6 3 0
        3 4 5 ->7 4 1
        6 7 8   8 5 2
        """
        new_face = [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

        # Now we have the colors correct but the next two indexes of each new_face entry are wrong as they are the previous pos
        for tiles in new_face:
            for y in range (0,4):
                for x in range (0,4):
                    tiles[1] = x
                    tiles[2] = y
        return new_face
    
    def counter_clockwise_face_rotation(self,face):
        """
        0 1 2     2 5 8
        3 4 5 ->  1 4 7
        6 7 8     0 3 6
        """
        new_face = [face[2],face[5],face[8],face[1],face[4],face[7],face[0],face[3],face[6]]
        for tiles in new_face:
            for y in range (0,4):
                for x in range (0,4):
                    tiles[1] = x
                    tiles[2] = y
        return new_face

    def horizontal_turn(self,row,prime):
        if row == 0: # Top row U or U'
            # Get row information of current rows that will be edited
            left_face_row =[self.cube[1][color] for color in range(3)] # This gets every color for the top row (0-2)
            front_face_row = [self.cube[2][color] for color in range(3)] 
            right_face_row = [self.cube[3][color] for color in range(3)]
            back_face_row = [self.cube[4][color] for color in range(3)]
     
            if prime == False: #U move
                for tile in range (0,3):
                    self.cube[1][tile] = front_face_row[tile]
                    self.cube[2][tile] = right_face_row[tile]
                    self.cube[3][tile] = back_face_row[tile]
                    self.cube[4][tile] = left_face_row[tile]
                self.cube[0] = self.clockwise_face_rotation(self.cube[0])
            else: #U' move
                for tile in range (0,3):
                    self.cube[1][tile] = back_face_row[tile]
                    self.cube[2][tile] = left_face_row[tile]
                    self.cube[3][tile] = front_face_row[tile]
                    self.cube[4][tile] = right_face_row[tile]

        elif row == 2: #Bottom row D or D'
            # Get row information of current rows that will be edited
            left_face_row =[self.cube[1][color] for color in range(6,9)] # This gets every color for the top row (0-2)
            front_face_row = [self.cube[2][color] for color in range(6,9)] 
            right_face_row = [self.cube[3][color] for color in range(6,9)]
            back_face_row = [self.cube[4][color] for color in range(6,9)]

            if prime == False: #D move
                for tile in range (0,3):
                    self.cube[1][tile+6] = back_face_row[tile]
                    self.cube[2][tile+6] = left_face_row[tile]
                    self.cube[3][tile+6] = front_face_row[tile]
                    self.cube[4][tile+6] = right_face_row[tile]
                self.cube[5] = self.clockwise_face_rotation(self.cube[5])
            else: #D' move
                for tile in range (0,3):
                    self.cube[1][tile+6] = front_face_row[tile]
                    self.cube[2][tile+6] = right_face_row[tile]
                    self.cube[3][tile+6] = back_face_row[tile]
                    self.cube[4][tile+6] = left_face_row[tile]
                self.cube[5] = self.counter_clockwise_face_rotation(self.cube[5])
    


"""
    def verticle_turn(self, column, prime):
        This simulates a verticle turn.
        The column is given 0 being left, 1 being middle, and 2
        being the rightmost column.
        A none prime turns the column clockwise, and prime
        turns are counter clockwise.
        
        # Define column indices
        columns = [0, 3, 6] if column == 0 else [1, 4, 7] if column == 1 else [2, 5, 8]

        # Extract columns from each face
        top_face_column = [self.cube[0][i] for i in columns]
        front_face_column = [self.cube[2][i] for i in columns]
        bottom_face_column = [self.cube[5][i] for i in columns]
        back_face_column = [self.cube[4][i] for i in columns]

        # Rotate columns clockwise or counter-clockwise
        if not prime:
            # Clockwise rotation
            for i in columns:
                self.cube[0][i] = front_face_column[2 - columns.index(i)]
                self.cube[2][i] = bottom_face_column[2 - columns.index(i)]
                self.cube[5][i] = back_face_column[2 - columns.index(i)]
                self.cube[4][i] = top_face_column[2 - columns.index(i)]
        else:
            # Counter-clockwise rotation
            for i in columns:
                self.cube[0][i] = back_face_column[2 - columns.index(i)]
                self.cube[2][i] = top_face_column[2 - columns.index(i)]
                self.cube[5][i] = front_face_column[2 - columns.index(i)]
                self.cube[4][i] = bottom_face_column[2 - columns.index(i)]

    def face_turn(self,column,prime):
        print("WOP")
"""                







        

