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
                neighbors = []
                if i > 0:
                    neighbors.append(forest[i-1, j])  # עליון
                if i < size-1:
                    neighbors.append(forest[i+1, j])  # תחתון
                if j > 0:
                    neighbors.append(forest[i, j-1])  # שמאלי
                if j < size-1:
                    neighbors.append(forest[i, j+1])  # ימני

                if BURNING in neighbors:
                    new_forest[i, j] = BURNING
            elif forest[i, j] == BURNING:
                new_forest[i, j] = EMPTY  # תא בוער הופך לריק

    return new_forest



