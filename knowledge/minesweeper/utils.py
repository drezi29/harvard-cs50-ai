def get_ranges(cell, height, width):
    previous_row = cell[0] - 1
    next_row = cell[0] + 1
    row_range_start = previous_row if previous_row >=0 else cell[0]
    row_range_end = (next_row if next_row < height else cell[0]) + 1

    previous_column = cell[1] - 1
    next_column = cell[1] + 1
    column_range_start = previous_column if previous_column >=0 else cell[1]
    column_range_end = (next_column if next_column < width else cell[1]) + 1

    return [range(row_range_start, row_range_end), range(column_range_start, column_range_end)]