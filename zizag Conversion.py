def convert(s: str, numRows: int) -> str:
    if len(s) <= numRows:
        print("yep")
        return s
    if numRows == 1:
        return s
    matrix = [[" " for j in range(numRows*2)] for i in range(numRows)]
    new_s = s

    x_coor = 0
    input_string = new_s[0]
    new_s = new_s[1:]
    matrix[0].insert(0, input_string)
    running = True
    
    while running:
        for i in range(1,numRows):
            if not new_s:
                
                running = False
                break
            input_string = new_s[0]
            
            new_s = new_s[1:]
            
            
            matrix[i].insert(x_coor,input_string)
            
            
        
        for i in range(numRows-2, -1, -1):
            if not new_s:
                running = False
                break
            x_coor += 1
            
            input_string = new_s[0]
            new_s = new_s[1:]
            
            
            matrix[i].insert(x_coor,input_string)


    final = ""
    for row in matrix:
        final += " ".join(row).rstrip() + "\n"

    return final
