def scramble_conversion(scramble):
    "R' U2 R' U' B R U F' L D2 U' B' D2 U2 L2 F2 L2 D F R B L2 B' D' R U' L F2 R2 F"
    """
    This function will take in a scramble
    and convert it into an array of moves
    for the cube to be scrambled in. Negative
    numbers are prime moves, and something like
    U2 will be represented as two moves instead
    of one.
    """

    converted_moves = [] 
    move_map = {
        "L": 1,
        "R": 2,
        "U": 3,
        "D": 4,
        "B": 5,
        "F": 6
    }

    moves = scramble.split(" ")

    for move in moves:
        if(move.endswith("'")):
            converted_moves.append(move_map[move[0]]* -1)
        elif(move.endswith("2")):
            converted_moves.append(move_map[move[0]])
            converted_moves.append(move_map[move[0]])
        else:
            converted_moves.append(move_map[move[0]])
    
    return converted_moves