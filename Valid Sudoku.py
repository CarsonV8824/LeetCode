def test(board:list[list[str]]):
    
    for row in board:
            dict_of_horz_nums = {}
            for col in row:
                if col.isdigit() and col not in dict_of_horz_nums:
                    dict_of_horz_nums[col] = 1
                elif col in dict_of_horz_nums:
                    return False
        
    for i in range(len(board[0])):
            list_of_vert_nums = {}
            for row in board:
                if row[i].isdigit() and row[i] not in list_of_vert_nums:
                    list_of_vert_nums[row[i]] = 1
                elif row[i] in list_of_vert_nums:
                    return False

    row_index = [0,1,2]
    col_index = [0,1,2]

    for i in range(len(row_index) * len(col_index)):
        pass

    return True