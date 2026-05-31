from collections import deque

"""
What I learned:
DO NOT USE INSERT ON LISTS! Use a lookup like a dictionary to replace items in a matrix or list. Also, python has a queue data structure.
"""

"""
def generateMatrix(n: int):
    temp_matrix = [[0 for _ in range(n)] for _ in range(n)]
    numbers = deque(range(1, n*n + 1))

    row_index = 0
    col_index = 0
    sprial_count = 0

    while numbers:

        # GO RIGHT
        if col_index < n - sprial_count and row_index == sprial_count:
            temp_matrix[row_index][col_index] = numbers.popleft()
            col_index += 1
            continue

        # GO DOWN
        if col_index == n - sprial_count and row_index < n - sprial_count:
            row_index += 1
            if row_index < n - sprial_count:
                temp_matrix[row_index][col_index - 1] = numbers.popleft()
            continue

        # GO LEFT
        if row_index == n - sprial_count and col_index > sprial_count + 1:
            col_index -= 1
            temp_matrix[row_index - 1][col_index - 1] = numbers.popleft()
            continue

        # GO UP
        if col_index == sprial_count + 1 and row_index > sprial_count:
            row_index -= 1

            # reached top of this layer → move inward
            if row_index == sprial_count + 1:
                sprial_count += 1
                row_index = sprial_count
                col_index = sprial_count
                continue

            temp_matrix[row_index - 1][col_index - 1] = numbers.popleft()
            continue

    return temp_matrix
"""


def generateMatrix(n: int):
    matrix = [[0] * n for _ in range(n)]
    nums = deque(range(1, n * n + 1))

    r = c = 0
    layer = 0

    while nums:

        # RIGHT
        while c < n - layer and nums:
            matrix[r][c] = nums.popleft()
            c += 1
        c -= 1
        r += 1

        # DOWN
        while r < n - layer and nums:
            matrix[r][c] = nums.popleft()
            r += 1
        r -= 1
        c -= 1

        # LEFT
        while c >= layer and nums:
            matrix[r][c] = nums.popleft()
            c -= 1
        c += 1
        r -= 1

        # UP
        while r > layer and nums:
            matrix[r][c] = nums.popleft()
            r -= 1

        # move to next inner layer
        layer += 1
        r = layer
        c = layer

    return matrix


if __name__ == "__main__":
    print(generateMatrix(6))
