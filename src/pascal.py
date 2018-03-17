rows = [[1], [1, 1]]

def pascal_row(n):
    """
    Get the nth row of Pascal's triangle.
    """
    while len(rows) <= n:
        last_row = rows[-1]
        this_row = [1]
        while len(this_row) <= len(last_row) / 2.0:
            r = len(this_row)
            this_row.append(last_row[r - 1] + last_row[r])

        if len(last_row) % 2:
            this_row.extend(reversed(this_row))
        else:
            this_row.extend(reversed(this_row[:-1]))
        rows.append(this_row)

    return rows[-1]
