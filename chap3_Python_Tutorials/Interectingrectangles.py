def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    # Calculate the max x and y coordinates of each rectangle
    x1_max = x1 + w1
    y1_max = y1 + h1
    x2_max = x2 + w2
    y2_max = y2 + h2

    # Rectangles do NOT intersect if one is completely left/right or above/below the other
    if x1_max <= x2 or x1 >= x2_max:
        return False
    if y1_max <= y2 or y1 >= y2_max:
        return False

    # If none of the non-intersecting conditions are met, they intersect
    return True
