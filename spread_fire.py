import copy

EMPTY = 0  # תא ריק ("אדמה")
TREE = 1   # תא עם עץ
BURNING = 2  # תא עם עץ בוער

def initialize_forest(size):
    """ אתחול מערך דו-ממדי עם עצים """
    forest = [[EMPTY for _ in range(size)] for _ in range(size)]
    forest[size // 2][size // 2] = BURNING  # התא המרכזי בוער
    return forest

def spread_fire(grid):
    """ עדכון מצב המערך לפי כללי ההתפשטות """
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == TREE:
                neighbors = []
                if i > 0:
                    neighbors.append(grid[i-1][j])  # עליון
                if i < grid_size - 1:
                    neighbors.append(grid[i+1][j])  # תחתון
                if j > 0:
                    neighbors.append(grid[i][j-1])  # שמאלי
                if j < grid_size - 1:
                    neighbors.append(grid[i][j+1])  # ימני

                if BURNING in neighbors:
                    update_grid[i][j] = BURNING
            elif grid[i][j] == BURNING:
                update_grid[i][j] = EMPTY  # תא בוער הופך לריק

    return update_grid

# פונקציית עזר להרצת הסימולציה
def run_simulation(size, steps):
    forest = initialize_forest(size)
    for _ in range(steps):
        forest = spread_fire(forest)

    return forest

# הרצה לדוגמה
final_forest = run_simulation(10, 5)
for row in final_forest:
    print(row)



