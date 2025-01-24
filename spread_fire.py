import numpy as np

EMPTY = 0  # תא ריק ("אדמה")
TREE = 1   # תא עם עץ
BURNING = 2  # תא עם עץ בוער

def initialize_forest(size):
    """ אתחול מערך דו-ממדי עם עצים """
    forest = np.zeros((size, size), dtype=int)
    forest[size // 2, size // 2] = BURNING  # התא המרכזי בוער
    return forest

def spread_fire(forest):
    """ עדכון מצב המערך לפי כללי ההתפשטות """
    new_forest = forest.copy()
    size = forest.shape[0]

    for i in range(size):
        for j in range(size):
            if forest[i, j] == TREE:
                # בדיקה אם אחד השכנים בוער
                if (i > 0 and forest[i-1, j] == BURNING) or \
                   (i < size-1 and forest[i+1, j] == BURNING) or \
                   (j > 0 and forest[i, j-1] == BURNING) or \
                   (j < size-1 and forest[i, j+1] == BURNING):
                    new_forest[i, j] = BURNING
            elif forest[i, j] == BURNING:
                new_forest[i, j] = EMPTY  # תא בוער הופך לריק

    return new_forest

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size-1):
        for j in range(grid_size-1):
            if grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid





