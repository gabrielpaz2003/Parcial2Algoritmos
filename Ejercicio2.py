import time

def largest_cross_size(grid):

    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])


    # Se inicializan en 0
    left   = [[0]*cols for _ in range(rows)]
    right  = [[0]*cols for _ in range(rows)]
    top    = [[0]*cols for _ in range(rows)]
    bottom = [[0]*cols for _ in range(rows)]

    # (A) left[i][j]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1
            else:
                left[i][j] = 0

    # (B) right[i][j]
    for i in range(rows):
        for j in range(cols - 1, -1, -1):
            if grid[i][j] == 1:
                if j == cols - 1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j + 1] + 1
            else:
                right[i][j] = 0

    # (C) top[i][j]
    for j in range(cols):
        for i in range(rows):
            if grid[i][j] == 1:
                if i == 0:
                    top[i][j] = 1
                else:
                    top[i][j] = top[i - 1][j] + 1
            else:
                top[i][j] = 0

    # (D) bottom[i][j]
    for j in range(cols):
        for i in range(rows - 1, -1, -1):
            if grid[i][j] == 1:
                if i == rows - 1:
                    bottom[i][j] = 1
                else:
                    bottom[i][j] = bottom[i + 1][j] + 1
            else:
                bottom[i][j] = 0

    max_cross_size = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                r = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                current_size = 1 + 4*(r - 1)  # tamaño de la cruz con centro en (i,j)
                if current_size > max_cross_size:
                    max_cross_size = current_size

    return max_cross_size


if __name__ == "__main__":

    grid_ejemplo = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]

    start_time = time.time()
    result = largest_cross_size(grid_ejemplo)
    end_time = time.time()

    print("Tamaño de la cruz más grande en la matriz de ejemplo:", result)
    print(f"Tiempo real transcurrido (para este input): {end_time - start_time:.5f} segundos")

