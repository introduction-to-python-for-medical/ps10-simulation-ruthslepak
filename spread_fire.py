import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# הגדרות ראשוניות
EMPTY = 0  # תא ריק ("אדמה")
TREE = 1   # תא עם עץ
BURNING = 2  # תא עם עץ בוער

def initialize_forest(size, p_tree):
    """ אתחול מערך דו-ממדי עם עצים לפי הסתברות נתונה """
    forest = np.random.choice([EMPTY, TREE], size=(size, size), p=[1-p_tree, p_tree])
    center = size // 2  # תא מרכזי
    forest[center, center] = BURNING  # התא המרכזי בוער
    return forest

def update_forest(forest):
    """ עדכון מצב המערך לפי כללי ההתפשטות """
    new_forest = forest.copy()
    size = forest.shape[0]

    for i in range(size):
        for j in range(size):
            if forest[i, j] == TREE:
                # בדיקה אם אחד השכנים בוער
                neighbors = [
                    forest[i-1, j] if i > 0 else EMPTY,           # תא עליון
                    forest[i+1, j] if i < size-1 else EMPTY,      # תא תחתון
                    forest[i, j-1] if j > 0 else EMPTY,           # תא שמאלי
                    forest[i, j+1] if j < size-1 else EMPTY        # תא ימני
                ]
                if BURNING in neighbors:
                    new_forest[i, j] = BURNING
            elif forest[i, j] == BURNING:
                new_forest[i, j] = EMPTY  # תא בוער הופך לריק

    return new_forest

def display_forest(forest):
    """ הצגת המערך באמצעות תמונה """
    plt.imshow(forest, cmap='hot', interpolation='nearest')
    plt.show()

def simulate_fire(size, p_tree, steps):
    """ סימולציית התפשטות אש עם הצגה של כל שלב """
    forest = initialize_forest(size, p_tree)
    
    fig, ax = plt.subplots()
    ims = []

    for _ in range(steps):
        im = ax.imshow(forest, cmap='hot', animated=True)
        ims.append([im])
        forest = update_forest(forest)

    ani = animation.ArtistAnimation(fig, ims, interval=500, blit=True)
    plt.show()

# הפעלת הסימולציה
simulate_fire(size=20, p_tree=0.6, steps=20)


