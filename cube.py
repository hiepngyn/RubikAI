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



    def horizontal_turn(self,layer,prime):
        """ This simulates a horizontal turn.
        The layer is given 0 being top, 1 being middle, and 2
        being the lowest layer.
        A none prime turns the layer clockwise, and prime
        turns are counter clockwise.
        """
        if not prime: #Clock wise rotation
            layer_offset = layer * 3
            front_face_row = [self.cube[2][layer_offset],self.cube[2][layer_offset+1],self.cube[2][layer_offset+2]]
            left_face_row = [self.cube[1][layer_offset],self.cube[1][layer_offset+1],self.cube[1][layer_offset+2]]
            right_face_row = [self.cube[3][layer_offset],self.cube[3][layer_offset+1],self.cube[3][layer_offset+2]]
            back_face_row = [self.cube[4][layer_offset],self.cube[4][layer_offset+1],self.cube[4][layer_offset+2]]

            for x in range (1,5):
                for y in range(0,3):
                    if(x == 1): # Sets left face with previous back face row
                        self.cube[x][layer_offset+y] = back_face_row[y] 
                    elif(x == 2): # Sets front face with previous left row
                        self.cube[x][layer_offset+y] = left_face_row[y]
                    elif(x == 3): # Sets right face with previous front row
                        self.cube[x][layer_offset+y] = front_face_row[y]
                    elif(x == 4): # Sets back face with previous right row
                        self.cube[x][layer_offset+y] = right_face_row[y]

        if prime: #Counter clock wise rotation
            layer_offset = layer * 3
            front_face_row = [self.cube[2][layer_offset],self.cube[2][layer_offset+1],self.cube[2][layer_offset+2]]
            left_face_row = [self.cube[1][layer_offset],self.cube[1][layer_offset+1],self.cube[1][layer_offset+2]]
            right_face_row = [self.cube[3][layer_offset],self.cube[3][layer_offset+1],self.cube[3][layer_offset+2]]
            back_face_row = [self.cube[4][layer_offset],self.cube[4][layer_offset+1],self.cube[4][layer_offset+2]]

            for x in range (1,5):
                for y in range(0,3):
                    if(x == 1): # Sets left face with previous front face row
                        self.cube[x][layer_offset+y] = front_face_row[y] 
                    elif(x == 2): # Sets front face with previous right row
                        self.cube[x][layer_offset+y] = right_face_row[y]
                    elif(x == 3): # Sets right face with previous back row
                        self.cube[x][layer_offset+y] = back_face_row[y]
                    elif(x == 4): # Sets back face with previous left row
                        self.cube[x][layer_offset+y] = left_face_row[y]
        
    def verticle_turn(self, column, prime):
        """ This simulates a verticle turn.
        The column is given 0 being left, 1 being middle, and 2
        being the rightmost column.
        A none prime turns the column clockwise, and prime
        turns are counter clockwise.
        """

        left_column = [0,3,6]
        middle_column = [1,4,7]
        right_column = [2,5,8]
        if not prime:
            if column == 0:
                top_face_column = [self.cube[0][left_column[0]],self.cube[0][left_column[1]],self.cube[2][left_column[2]]]
                front_face_column = [self.cube[2][left_column[0]],self.cube[2][left_column[1]],self.cube[2][left_column[2]]]
                bottom_face_column = [self.cube[5][left_column[0]],self.cube[5][left_column[1]],self.cube[5][left_column[2]]]
                back_face_column = [self.cube[4][left_column[0]],self.cube[4][left_column[1]],self.cube[4][left_column[2]]]

                for x in range (0,6):
                    if x != 1 or 3:
                        for y in range (0,3):
                            if x == 0: # Sets Top Face to be prev front column
                                self.cube[0][left_column[y]] = front_face_column[y]
                            if x == 2: # Sets Front Face to be prev bottom column
                                self.cube[2][left_column[y]] = bottom_face_column[y]
                            if x == 4: # Sets Bottom Face to be prev back column
                                self.cube[4][left_column[y]] = back_face_column[y]
                            if x == 5: # Sets Back Face to be prev top column
                                self.cube[5][left_column[y]] = top_face_column[y]

            elif column == 1:
                top_face_column = [self.cube[0][middle_column[0]],self.cube[0][middle_column[1]],self.cube[2][middle_column[2]]]
                front_face_column = [self.cube[2][middle_column[0]],self.cube[2][middle_column[1]],self.cube[2][middle_column[2]]]
                bottom_face_column = [self.cube[5][middle_column[0]],self.cube[5][middle_column[1]],self.cube[5][middle_column[2]]]
                back_face_column = [self.cube[4][middle_column[0]],self.cube[4][middle_column[1]],self.cube[4][middle_column[2]]]

                for x in range (0,6):
                    if x != 1 or 3:
                        for y in range (0,3):
                            if x == 0: # Sets Top Face to be prev front column
                                self.cube[0][middle_column[y]] = front_face_column[y]
                            if x == 2: # Sets Front Face to be prev bottom column
                                self.cube[2][middle_column[y]] = bottom_face_column[y]
                            if x == 4: # Sets Bottom Face to be prev back column
                                self.cube[4][middle_column[y]] = back_face_column[y]
                            if x == 5: # Sets Back Face to be prev top column
                                self.cube[5][middle_column[y]] = top_face_column[y]
            elif column == 2:
                top_face_column = [self.cube[0][right_column[0]],self.cube[0][right_column[1]],self.cube[2][right_column[2]]]
                front_face_column = [self.cube[2][right_column[0]],self.cube[2][right_column[1]],self.cube[2][right_column[2]]]
                bottom_face_column = [self.cube[5][right_column[0]],self.cube[5][right_column[1]],self.cube[5][right_column[2]]]
                back_face_column = [self.cube[4][right_column[0]],self.cube[4][right_column[1]],self.cube[4][right_column[2]]]     

                for x in range (0,6):
                    if x != 1 or 3:
                        for y in range (0,3):
                            if x == 0: # Sets Top Face to be prev front column
                                self.cube[0][right_column[y]] = front_face_column[y]
                            if x == 2: # Sets Front Face to be prev bottom column
                                self.cube[2][right_column[y]] = bottom_face_column[y]
                            if x == 4: # Sets Bottom Face to be prev back column
                                self.cube[4][right_column[y]] = back_face_column[y]
                            if x == 5: # Sets Back Face to be prev top column
                                self.cube[5][right_column[y]] = top_face_column[y]






cube = RubiksCube()
cube.verticle_turn(0,False)


print(cube.cube)