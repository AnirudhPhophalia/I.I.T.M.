# def index_of_first_occurance(row:list,elem):
#     '''
#     Given a list find the index of first occurance of 1 in it
#     '''
#     ...
# def index_of_last_occurance(row:list,elem):
#     '''
#     Given a list find the index of last occurance of 1 in it.
#     Hint: use index_of_first_one with reversal.
#     '''
#     ...

# def is_valid_coordinate(x:int,y:int, M):
#     '''
#     Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
#     '''
#     ...
# def valid_adjacent_coordinates(x:int,y:int, M):
#     '''
#     Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
#     '''
#     ...
#     return {
#       (x1,y1)
#       for x1,y1 in ... # all the possible adjacent coordinates
#       if is_valid_coordinate(x1,y1, M)
#     }

# def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
#     '''
#     Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
#     '''
#     ...

# def get_path_coordinates(M):
#     '''
#     Given the matrix m, find the path formed by 1 from the last row to the first row.
#     '''
#     ...

# def print_path(M):
#     path = get_path_coordinates(M)
#     ...

# def alternate_path(M):
#     path = get_path_coordinates(M)
#     ...

# def count_path(M):
#     path = get_path_coordinates(M)
#     ...

# def mirror_horizontally(M):
#     path = get_path_coordinates(M)
#     ...

# def mirror_vertically(M):
#     path = get_path_coordinates(M)
#     ...







def index_of_first_occurance(row:list,elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    for index, value in enumerate(row):
        if value == elem:
            return index
    return -1

def index_of_last_occurance(row:list,elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    reversed_row = row[::-1]
    index = index_of_first_occurance(reversed_row, elem)
    return len(row) - 1 - index if index != -1 else -1

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''
    return 0 <= x < len(M) and 0 <= y < len(M[0]) if M else False

def valid_adjacent_coordinates(x:int,y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    adjacent_coords = {
        (x - 1, y), (x + 1, y),   # Up and Down
        (x, y - 1), (x, y + 1)    # Left and Right
    }
    return {
      (x1,y1)
      for x1,y1 in ... # all the possible adjacent coordinates
      if is_valid_coordinate(x1,y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    x, y = curr_coords
    adjacent_coords = valid_adjacent_coordinates(x, y, M)
    
    for coord in adjacent_coords:
        if coord != prev_coords and M[coord[0]][coord[1]] == value:
            return coord
    return None

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)
    ...

def print_path(M):
    path = get_path_coordinates(M)
    ...

def alternate_path(M):
    path = get_path_coordinates(M)
    ...

def count_path(M):
    path = get_path_coordinates(M)
    ...

def mirror_horizontally(M):
    path = get_path_coordinates(M)
    return M[::-1]

def mirror_vertically(M):
    path = get_path_coordinates(M)
    return [row[::-1] for row in M]
