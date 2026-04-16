class Solution:
    def isValidSudoku(self, board):

        # step1 row should be valid
        set_row = set()
        for i in range(9):
            for j in range(9):
                current_element = board[i][j]

                if current_element == ".":
                    continue

                if current_element not in set_row:
                    set_row.add(current_element)
                else:
                    return False

            set_row.clear()


        # step2 columns should be valid
        set_col = set()
        for j in range(9):
            for i in range(9):
                current_element = board[i][j]

                if current_element == ".":
                    continue

                if current_element not in set_col:
                    set_col.add(current_element)
                else:
                    return False

            set_col.clear()


        # step3 3*3 box should be valid
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                set_box = set()

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        current_element = board[i][j]

                        if current_element == ".":
                            continue

                        if current_element not in set_box:
                            set_box.add(current_element)
                        else:
                            return False

        return True