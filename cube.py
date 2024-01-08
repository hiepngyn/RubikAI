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
                self.cube[0] = self.counter_clockwise_face_rotation(self.cube[0])

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
    
    def vertical_turn(self, column, prime):
        if(column == 0):  # Left column
            columns = [0, 3, 6]
            back_columns = [8, 5, 2]
        elif(column == 1):  # Middle column
            columns = [1, 4, 7]
            back_columns = [7, 4, 1]
        elif(column == 2):  # Right column
            columns = [2, 5, 8]
            back_columns = [6, 3, 0]

        # Storing current configuration in temporary variables
        top_face_column = [self.cube[0][i] for i in columns]
        front_face_column = [self.cube[2][i] for i in columns]
        bottom_face_column = [self.cube[5][i] for i in columns]
        back_face_column = [self.cube[4][i] for i in back_columns]

        if column == 0:
            if not prime:  # L move
                for i, col in enumerate(columns):
                    self.cube[0][col] = back_face_column[i]
                    self.cube[2][col] = top_face_column[i]
                    self.cube[5][col] = front_face_column[i]
                    self.cube[4][back_columns[i]] = bottom_face_column[i]
                # Rotate left face clockwise
                self.cube[1] = self.clockwise_face_rotation(self.cube[1])
            else:  # L' move
                for i, col in enumerate(columns):
                    self.cube[0][col] = front_face_column[i]
                    self.cube[2][col] = bottom_face_column[i]
                    self.cube[5][col] = back_face_column[i]
                    self.cube[4][back_columns[i]] = top_face_column[i]
                # Rotate left face counter-clockwise
                self.cube[1] = self.counter_clockwise_face_rotation(self.cube[1])
        if column == 1:
            if not prime:  # M move
                for i, col in enumerate(columns):
                    self.cube[0][col] = back_face_column[i]
                    self.cube[2][col] = top_face_column[i]
                    self.cube[5][col] = front_face_column[i]
                    self.cube[4][back_columns[i]] = bottom_face_column[i]
            else:  # M' move
                for i, col in enumerate(columns):
                    self.cube[0][col] = front_face_column[i]
                    self.cube[2][col] = bottom_face_column[i]
                    self.cube[5][col] = back_face_column[i]
                    self.cube[4][back_columns[i]] = top_face_column[i]
        if column == 2:
            if not prime:  # R move
                for i, col in enumerate(columns):
                    self.cube[0][col] = front_face_column[i]
                    self.cube[2][col] = bottom_face_column[i]
                    self.cube[5][col] = back_face_column[i]
                    self.cube[4][back_columns[i]] = top_face_column[i]
                # Rotate right face clockwise
                self.cube[3] = self.clockwise_face_rotation(self.cube[3])
            else:  # R' move
                for i, col in enumerate(columns):
                    self.cube[0][col] = back_face_column[i]
                    self.cube[2][col] = top_face_column[i]
                    self.cube[5][col] = front_face_column[i]
                    self.cube[4][back_columns[i]] = bottom_face_column[i]
                # Rotate right face counter-clockwise
                self.cube[3] = self.counter_clockwise_face_rotation(self.cube[3])
    
    def face_turn(self, face, prime):
        """
        top_face_row = [self.cube[0][tile] for tile in range(6,9)] if face == 0 else [self.cube[0][tile] for tile in range (0,3)]
        right_face_row = [self.cube[3][tile*3] for tile in range(3)] if face == 0 else [self.cube[0][tile] for tile in range (2,9,3)]
        left_face_row = [self.cube[1][tile] for tile in range(2,9,3)] if face == 0 else [self.cube[0][tile*3] for tile in range (0,3)]
        bottom_face_row = [self.cube[5][tile] for tile in range(3)] if face == 0 else [self.cube[0][tile] for tile in range (6,9)]
        """
        if (face == 0):
            top_face_row = [self.cube[0][tile] for tile in range(6,9)]
            right_face_row = [self.cube[3][tile*3] for tile in range(3)]
            left_face_row = [self.cube[1][tile] for tile in range(2,9,3)]
            bottom_face_row = [self.cube[5][tile] for tile in range(3)]
        elif(face == 1):
            top_face_row = [self.cube[0][tile] for tile in range (0,3)]
            right_face_row = [self.cube[3][tile] for tile in range (2,9,3)]
            left_face_row = [self.cube[1][tile*3] for tile in range (0,3)]
            bottom_face_row = [self.cube[5][tile] for tile in range (6,9)]

        if(face == 0):
            if(not prime): #F
                left_face_row = left_face_row[::-1]
                right_face_row = right_face_row[::-1]
                #Need to reverse to account for mirror on bottom
                for tile in range(3):
                    self.cube[0][tile+6] = left_face_row[tile] #6,7,8
                    self.cube[3][tile*3] = top_face_row[tile] #0,3,6
                    self.cube[5][tile] = right_face_row[tile] #0,1,2
                    self.cube[1][(tile*3) + 2] = bottom_face_row[tile] #2,5,8
                self.cube[2] = self.clockwise_face_rotation(self.cube[2])
            else: #F'
                top_face_row = top_face_row[::-1]
                bottom_face_row = bottom_face_row[::-1]
                for tile in range(3):
                    self.cube[0][tile+6] = right_face_row[tile] #6,7,8
                    self.cube[3][tile*3] = bottom_face_row[tile] #0,3,6
                    self.cube[5][tile] = left_face_row[tile] #0,1,2
                    self.cube[1][(tile*3) + 2] = top_face_row[tile] #2,5,8
                self.cube[2] = self.counter_clockwise_face_rotation(self.cube[2])
        elif(face == 1):
            if(not prime): #B
                print('b')
                bottom_face_row = bottom_face_row[::-1]
                top_face_row = top_face_row[::-1]
                for tile in range(3):
                    self.cube[0][tile] = right_face_row[tile] #0,1,2
                    self.cube[3][(tile*3) + 2] = bottom_face_row[tile] #2,5,8
                    self.cube[5][tile+6] = left_face_row[tile] #6,7,8
                    self.cube[1][tile*3] = top_face_row[tile] #0,3,6
                self.cube[4] = self.clockwise_face_rotation(self.cube[4])
            else: #B'
                right_face_row = right_face_row[::-1]
                left_face_row = left_face_row[::-1]
                for tile in range(3):
                    self.cube[0][tile] = left_face_row[tile] #0,1,2
                    self.cube[3][(tile*3) + 2] = top_face_row[tile] #2,5,8
                    self.cube[5][tile+6] = right_face_row[tile] #6,7,8
                    self.cube[1][tile*3] = bottom_face_row[tile] #0,3,6
                self.cube[4] = self.counter_clockwise_face_rotation(self.cube[4])
        











        

