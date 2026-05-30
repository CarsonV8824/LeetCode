from typing import List

def generateMatrix(n: int):
    temp_matrix = [[0 for j in range(n)] for i in range(n)]
    numbers = [n for n in range(1, (n**2)+1, 1)]
    row_index = 0
    col_index = 0
    sprial_count = 0
    
    while True:
        try:
            if col_index < n - sprial_count and row_index == 0 + sprial_count:
                print("GOING RIGHT")
                number = numbers.pop(0)
                
                temp_matrix[row_index].pop(col_index)
                
                temp_matrix[row_index].insert(col_index, number)
                col_index += 1
            
            elif col_index == n - sprial_count and row_index < n - sprial_count:
                print("GOING DOWN")
                row_index += 1
                if row_index == n - sprial_count:
                    continue
                number = numbers.pop(0)
                temp_matrix[row_index].pop(col_index  - 1)
                temp_matrix[row_index].insert(col_index  - 1, number)

            elif row_index == n - sprial_count and col_index > 1 + sprial_count:
                print("GOING LEFT")
                col_index -= 1
                number = numbers.pop(0)
                temp_matrix[row_index-1].pop(col_index - 1)
                temp_matrix[row_index-1].insert(col_index -  1, number)
            
            elif col_index == sprial_count + 1 and row_index > sprial_count-1:
                print("GOING UP")
                row_index -= 1
                if row_index == 1 + sprial_count:
                    sprial_count += 1
                    row_index = sprial_count
                    col_index = sprial_count
                    continue

                number = numbers.pop(0)
                temp_matrix[row_index-1].pop(col_index - 1)
                temp_matrix[row_index-1].insert(col_index  - 1, number)
        except Exception:
            break
                

    return temp_matrix

        
    

    

if __name__ == "__main__":
    print(generateMatrix(5))