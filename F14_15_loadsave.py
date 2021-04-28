# Mario Jeiba - 16520280
# Table handler library 3 for IF1210-TB1

# ====================================================
# FUNCTION DIRECTORY

# INTERNAL USE
# _tablefromtext(<text>)
#   - Converts raw csv text to array.
#   - used in loadcsv()
# _tabletotext(<array>)
#   - Converts array to raw csv text
#   - used in savecsv()
# _completerow(<array>, <width>)
#   - Fills empty columns, makes every row
#     no shorter than the header (whose width is specified).
#   - used in loadcsv()

# PUBLIC
# loadcsv(<file>)
#   - Loads array from file.
#   Input:  file  : string
#   Output:         list of list
# savecsv(<file>, <array>)
#   - Saves array to file.
#   Input:  file  : string
#           array : list of list

# ===============================================
# INTERNAL FUNCTIONS

# :: Text-array conversion

def _tablefromtext(text: str, *, delimiter=";"):
    # used in: loadcsv()
    # -------------------------------------------

    # Base values
    array = []
    line = []
    i_start = 0

    # Add final line delimiter
    text += "\n"

    # Scan for each character in <text>
    for i in range(len(text)):
        # Check if scanned character is a delimiter (meaning new cell)
        if text[i] in (delimiter, "\n"):
            # Retrieve cell
            i_end = i                               # Acquire last scan
            cell = text[i_start:i_end]              # Retrieve cell from position <i_start> to <i_end>-1
            line.append(cell.strip())               # Append new cell with leading/trailing whitespaces removed
            i_start = i + 1                         # New retrieval start position

            # Retrieve row when scanned newline
            if text[i] == "\n":
                array.append(line)
                line = []

    # Return converted array
    return array

def _tabletotext(array: list, *, delimiter=";"):
    # used in: savefile()
    # -------------------------------------------

    # Base values
    lines = []

    # Loop for each row in nested array
    for row in array:
        cells = ["" for i in range(len(row))]
        for i in range(len(row)):
            cells[i] = str(row[i])
        lines.append(delimiter.join(cells))

    return "\n".join(lines)

# :: Filling blank entries

def _completerow(array: list, width: int):
    # used in: loadcsv()
    # -------------------------------------------

    arrayout = list.copy(array)     # output array
    for row in arrayout:
        if len(row) < width:        # if row has less entries than header (specified by <width>)
            for i in range(width - len(row)):
                row.append("")      # append blank
    return arrayout

# ===============================================
# PUBLIC FUNCTIONS

# :: Load from/save to file

def loadcsv(file: str, *, delimiter=";", complete_rows=True):
    # uses: _tablefromtext(), _completerow()
    # -------------------------------------------

    with open(file, newline="\n") as f:
        raw = f.read()
        array = _tablefromtext(raw, delimiter=delimiter)

    # option to fill blank entries in columns
    if complete_rows:
        array = _completerow(array, len(array[0]))

    return array

def savecsv(file: str, array: list, *, delimiter=";"):
    # uses: _tabletotext()
    # -------------------------------------------

    with open(file, newline="\n", mode='w') as f:
        f.write(
            _tabletotext(array, delimiter=delimiter)
        )
