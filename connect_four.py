import random

class player:
    def __init__(self, playername, playernum):
        self.playername = playername
        self.playernum = playernum

    def getname(self):
        """This returns my username"""
        return self.playername

    def getnum(self):
        """This returns the number I am that game - 1 or 2"""
        return self.playernum

    def getenemynum(self):
        """This returns the number that my enemy is playing as - 1 or 2"""
        if self.getnum() == 1:
            return 2
        else:
            return 1

    def possible_moves(self, board):
        """
        Loop through the board and check if a column has an empty spot and make sure
        the empty spot does not have an empty spot below it then add it to the possible
        moves.
        """
        moves = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if row == 0 and board[row][col] == 0:
                    moves.append([row, col])
                elif board[row][col] == 0 and (board[row - 1][col] != 0):
                    moves.append([row, col])

        return moves

    def do_i_have_three_vertical(self, board):
        """
        Loop through the board and check if there are three of my tokens in a column and
        there is an open spot above my third token. Make sure that the row is not higher
        than the 2nd row or else we will go out of bounds.
        """
        my_token = self.getnum()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if row < 3:
                    if (board[row][col] == my_token and
                        board[row + 1][col] == my_token and
                        board[row + 2][col] == my_token and
                        board[row + 3][col] == 0):

                        '''
                        return column plus 1 because if the column is number 0
                        then it will fail the if statement used to check if I have
                        three vertically. The one will be subtracted.
                        '''
                        return col + 1

        return False

    def do_i_have_three_horizontal(self, board):
        """
        Loop through the board and check if there are three of my tokens in a row and
        there is an open spot to the left/right of third token.
        Make sure that the column is not higher than the 2nd column
        or else we will go out of bounds.
        """
        my_token = self.getnum()
        moves = self.possible_moves(board)

        '''loop through the board checking from left to right, check for three in a row'''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4:
                    if (board[row][col] == my_token and
                        board[row][col + 1] == my_token and
                        board[row][col + 2] == my_token and
                        [row, col + 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 3]

        '''loop through the board checking from right to left, check for three in a row'''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 2:
                    if (board[row][col] == my_token and
                        board[row][col - 1] == my_token and
                        board[row][col - 2] == my_token and
                        [row, col - 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 3]

        '''
        loop through the board checking from left to right, check for two tokens and then
        an empty spot then a token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4:
                    if (board[row][col] == my_token and
                        board[row][col + 1] == my_token and
                        [row, col + 2] in moves and
                        board[row][col + 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 2]

        '''
        loop through the board checking from right to left, check for two tokens and then
        an empty spot then a token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 2:
                    if (board[row][col] == my_token and
                        board[row][col - 1] == my_token and
                        [row, col - 2] in moves and
                        board[row][col - 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 2]

        '''
        loop through the board checking from left to right, check for one token and then
        an empty spot then two tokens
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4:
                    if (board[row][col] == my_token and
                        [row, col + 1] in moves and
                        board[row][col + 2] == my_token and
                        board[row][col + 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 1]

        '''
        loop through the board checking from right to left, check for one token and then
        an empty spot then two tokens
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 2:
                    if (board[row][col] == my_token and
                        [row, col - 1] in moves and
                        board[row][col - 2] == my_token and
                        board[row][col - 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 1]

        return False

    def do_i_have_three_diagonal(self, board):
        """
        Loop through the board and check if there are three of my tokens in a diagonal and
        there is an open spot to the top-left/right bottom-left/right.
        """
        my_token = self.getnum()
        moves = self.possible_moves(board)

        '''loop through the board checking from left to right, bottom to top'''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4 and row < 3:
                    if (board[row][col] == my_token and
                        board[row + 1][col + 1] == my_token and
                        board[row + 2][col + 2] == my_token and
                        [row + 3, col + 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 3, col + 3]

        '''
        loop through the board checking from left to right, bottom to top for two
        tokens then a blank spot and then a token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4 and row < 3:
                    if (board[row][col] == my_token and
                        board[row + 1][col + 1] == my_token and
                        [row + 2, col + 2] in moves and
                        board[row + 3][col + 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 2, col + 2]

        '''
        loop through the board checking from left to right, bottom to top for one
        token then a blank spot and then two token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4 and row < 3:
                    if (board[row][col] == my_token and
                        [row + 1, col + 1] in moves and
                        board[row + 2][col + 2] == my_token and
                        board[row + 3][col + 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 1, col + 1]

        '''loop through the board checking from right to left, top to bottom'''
        for row in reversed(range(len(board))):
            for col in reversed(range(len(board[row]))):
                if col > 2 and row > 2:
                    if (board[row][col] == my_token and
                        board[row - 1][col - 1] == my_token and
                        board[row - 2][col - 2] == my_token and
                        [row - 3, col - 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 3, col - 3]

        '''
        loop through the board checking from right to left, top to bottom and check for
        two tokens and open spot and then a token
        '''
        for row in reversed(range(len(board))):
            for col in reversed(range(len(board[row]))):
                if col > 2 and row > 2:
                    if (board[row][col] == my_token and
                        board[row - 1][col - 1] == my_token and
                        [row - 2, col - 2] in moves and
                        board[row - 3][col - 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 2, col - 2]

        '''
        loop through the board checking from right to left, top to bottom and check for
        one token and open spot and then two tokens
        '''
        for row in reversed(range(len(board))):
            for col in reversed(range(len(board[row]))):
                if col > 2 and row > 2:
                    if (board[row][col] == my_token and
                        [row - 1, col - 1] in moves and
                        board[row - 2][col - 2] == my_token and
                        board[row - 3][col - 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 1, col - 1]

        '''loop through the board checking from left to right, top to bottom'''
        for row in reversed(range(len(board))):
            for col in range(len(board[row])):
                if col < 4 and row > 2:
                    if (board[row][col] == my_token and
                        board[row - 1][col + 1] == my_token and
                        board[row - 2][col + 2] == my_token and
                        [row - 3, col + 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 3, col + 3]

        '''
        loop through the board checking from left to right, top to bottom look for
        two tokens and open spot and then one token
        '''
        for row in reversed(range(len(board))):
            for col in range(len(board[row])):
                if col < 4 and row > 2:
                    if (board[row][col] == my_token and
                        board[row - 1][col + 1] == my_token and
                        [row - 2, col + 2] in moves and
                        board[row - 3][col + 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 2, col + 2]

        '''
        loop through the board checking from left to right, top to bottom look for
        one token and open spot and then two tokens
        '''
        for row in reversed(range(len(board))):
            for col in range(len(board[row])):
                if col < 4 and row > 2:
                    if (board[row][col] == my_token and
                        [row - 1, col + 1] in moves and
                        board[row - 2][col + 2] == my_token and
                        board[row - 3][col + 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 1, col + 1]

        '''loop through the board checking from right to left, bottom to top'''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 4 and row < 3:
                    if (board[row][col] == my_token and
                        board[row + 1][col - 1] == my_token and
                        board[row + 2][col - 2] == my_token and
                        [row + 3, col - 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 3, col - 3]

        '''
        loop through the board checking from right to left, bottom to top for two
        tokens and then open spot and then one token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 4 and row < 3:
                    if (board[row][col] == my_token and
                        board[row + 1][col - 1] == my_token and
                        [row + 2, col - 2] in moves and
                        board[row + 3][col - 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 2, col - 2]

        '''
        loop through the board checking from right to left, bottom to top for two
        tokens and then open spot and then one token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 4 and row < 3:
                    if (board[row][col] == my_token and
                        [row + 1, col - 1] in moves and
                        board[row + 2][col - 2] == my_token and
                        board[row + 3][col - 3] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 1, col - 1]

        return False

    def do_i_have_two_vertical(self, board):
        """
        Loop through the board and check if there are two of my tokens in a column and
        there is an open spot above my second token. Make sure that the row is not higher
        than the 3rd row because there is no point in placing a token if I cant get 3
        in a row
        """
        my_token = self.getnum()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if row < 3:
                    if (board[row][col] == my_token and
                        board[row + 1][col] == my_token and
                        board[row + 2][col] == 0):

                        '''
                        return column plus 1 because if the column is number 0
                        then it will fail the if statement used to check if I have
                        three vertically. The one will be subtracted.
                        '''
                        return col + 1

        return False

    def do_i_have_two_horizontal(self, board):
        """
        Loop through the board and check if there are two of my tokens in a row and
        there is an open spot to the left/right of 2nd token.
        Make sure that the column is not higher than the 5th column
        or else we will go out of bounds.
        """
        my_token = self.getnum()
        moves = self.possible_moves(board)

        '''loop through the board checking from left to right'''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 5:
                    if (board[row][col] == my_token and
                        board[row][col + 1] == my_token and
                        [row, col + 2] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 2]
        '''loop through the board checking from right to left'''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 1:
                    if (board[row][col] == my_token and
                        board[row][col - 1] == my_token and
                        [row, col - 2] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 2]
        '''
        loop through the board checking from left to right for one token, blank spot,
        then another token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 5:
                    if (board[row][col] == my_token and
                        [row, col + 1] in moves and
                        board[row][col + 2] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 1]

        '''
        loop through the board checking from right to left for one token, blank spot,
        then another token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 1:
                    if (board[row][col] == my_token and
                        [row, col - 1] in moves and
                        board[row][col - 2] == my_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 1]

        return False

    def do_they_have_three_vertical(self, board):
        """
        Loop through the board and check if there are three of my enemy's tokens in a col
        and there is an open spot above their third token. Make sure that the row is not
        higher than the 2nd row or else we will go out of bounds.
        """
        enemy_token = self.getenemynum()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if row < 3:
                    if (board[row][col] == enemy_token and
                        board[row + 1][col] == enemy_token and
                        board[row + 2][col] == enemy_token and
                        board[row + 3][col] == 0):

                        '''
                        return column plus 1 because if the column is number 0
                        then it will fail the if statement used to check if the
                        enemy has three vertically. The one will be subtracted.
                        '''
                        return col + 1

        return False

    def do_they_have_three_horizontal(self, board):
        """
        Loop through the board and check if there are three of my enemies tokens in
        a row and there is an open spot to the left/right of the third token.
        Make sure that the column is not higher than the 2nd column
        or else we will go out of bounds.
        """
        enemy_token = self.getenemynum()
        moves = self.possible_moves(board)

        '''loop through the board checking from left to right'''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4:
                    if (board[row][col] == enemy_token and
                        board[row][col + 1] == enemy_token and
                        board[row][col + 2] == enemy_token and
                        [row, col + 3] in moves):

                        '''
                        return the column and row that will give my enemy four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 3]

        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 2:
                    if (board[row][col] == enemy_token and
                        board[row][col - 1] == enemy_token and
                        board[row][col - 2] == enemy_token and
                        [row, col - 3] in moves):

                        '''
                        return the column and row that will give my enemy four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 3]

        '''
        loop through the board checking from left to right, check for two tokens and then
        an empty spot then a token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4:
                    if (board[row][col] == enemy_token and
                        board[row][col + 1] == enemy_token and
                        [row, col + 2] in moves and
                        board[row][col + 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 2]

        '''
        loop through the board checking from right to left, check for two tokens and then
        an empty spot then a token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 2:
                    if (board[row][col] == enemy_token and
                        board[row][col - 1] == enemy_token and
                        [row, col - 2] in moves and
                        board[row][col - 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 2]

        '''
        loop through the board checking from left to right, check for one token and then
        an empty spot then two tokens
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4:
                    if (board[row][col] == enemy_token and
                        [row, col + 1] in moves and
                        board[row][col + 2] == enemy_token and
                        board[row][col + 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 1]

        '''
        loop through the board checking from right to left, check for one token and then
        an empty spot then two tokens
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 2:
                    if (board[row][col] == enemy_token and
                        [row, col - 1] in moves and
                        board[row][col - 2] == enemy_token and
                        board[row][col - 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 1]

        return False

    def do_they_have_three_diagonal(self, board):
        """
        Loop through the board and check if there are three of my enemy tokens in a
        diagonal and there is an open spot to the top-left/right bottom-left/right.
        """
        enemy_token = self.getenemynum()
        moves = self.possible_moves(board)

        '''loop through the board checking from left to right, bottom to top'''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4 and row < 3:
                    if (board[row][col] == enemy_token and
                        board[row + 1][col + 1] == enemy_token and
                        board[row + 2][col + 2] == enemy_token and
                        [row + 3, col + 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 3, col + 3]

        '''
        loop through the board checking from left to right, bottom to top for two
        tokens then a blank spot and then a token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4 and row < 3:
                    if (board[row][col] == enemy_token and
                        board[row + 1][col + 1] == enemy_token and
                        [row + 2, col + 2] in moves and
                        board[row + 3][col + 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 2, col + 2]

        '''
        loop through the board checking from left to right, bottom to top for one
        token then a blank spot and then two token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 4 and row < 3:
                    if (board[row][col] == enemy_token and
                        [row + 1, col + 1] in moves and
                        board[row + 2][col + 2] == enemy_token and
                        board[row + 3][col + 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 1, col + 1]

        '''loop through the board checking from right to left, top to bottom'''
        for row in reversed(range(len(board))):
            for col in reversed(range(len(board[row]))):
                if col > 2 and row > 2:
                    if (board[row][col] == enemy_token and
                        board[row - 1][col - 1] == enemy_token and
                        board[row - 2][col - 2] == enemy_token and
                        [row - 3, col - 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 3, col - 3]

        '''
        loop through the board checking from right to left, top to bottom and check for
        two tokens and open spot and then a token
        '''
        for row in reversed(range(len(board))):
            for col in reversed(range(len(board[row]))):
                if col > 2 and row > 2:
                    if (board[row][col] == enemy_token and
                        board[row - 1][col - 1] == enemy_token and
                        [row - 2, col - 2] in moves and
                        board[row - 3][col - 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 2, col - 2]

        '''
        loop through the board checking from right to left, top to bottom and check for
        one token and open spot and then two tokens
        '''
        for row in reversed(range(len(board))):
            for col in reversed(range(len(board[row]))):
                if col > 2 and row > 2:
                    if (board[row][col] == enemy_token and
                        [row - 1, col - 1] in moves and
                        board[row - 2][col - 2] == enemy_token and
                        board[row - 3][col - 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 1, col - 1]

        '''loop through the board checking from left to right, top to bottom'''
        for row in reversed(range(len(board))):
            for col in range(len(board[row])):
                if col < 4 and row > 2:
                    if (board[row][col] == enemy_token and
                        board[row - 1][col + 1] == enemy_token and
                        board[row - 2][col + 2] == enemy_token and
                        [row - 3, col + 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 3, col + 3]

        '''
        loop through the board checking from left to right, top to bottom look for
        two tokens and open spot and then one token
        '''
        for row in reversed(range(len(board))):
            for col in range(len(board[row])):
                if col < 4 and row > 2:
                    if (board[row][col] == enemy_token and
                        board[row - 1][col + 1] == enemy_token and
                        [row - 2, col + 2] in moves and
                        board[row - 3][col + 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 2, col + 2]

        '''
        loop through the board checking from left to right, top to bottom look for
        one token and open spot and then two tokens
        '''
        for row in reversed(range(len(board))):
            for col in range(len(board[row])):
                if col < 4 and row > 2:
                    if (board[row][col] == enemy_token and
                        [row - 1, col + 1] in moves and
                        board[row - 2][col + 2] == enemy_token and
                        board[row - 3][col + 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row - 1, col + 1]

        '''loop through the board checking from right to left, bottom to top'''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 4 and row < 3:
                    if (board[row][col] == enemy_token and
                        board[row + 1][col - 1] == enemy_token and
                        board[row + 2][col - 2] == enemy_token and
                        [row + 3, col - 3] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 3, col - 3]

        '''
        loop through the board checking from right to left, bottom to top for two
        tokens and then open spot and then one token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 4 and row < 3:
                    if (board[row][col] == enemy_token and
                        board[row + 1][col - 1] == enemy_token and
                        [row + 2, col - 2] in moves and
                        board[row + 3][col - 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 2, col - 2]

        '''
        loop through the board checking from right to left, bottom to top for two
        tokens and then open spot and then one token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 4 and row < 3:
                    if (board[row][col] == enemy_token and
                        [row + 1, col - 1] in moves and
                        board[row + 2][col - 2] == enemy_token and
                        board[row + 3][col - 3] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row + 1, col - 1]

        return False

    def do_they_have_two_horizontal(self, board):
        """
        Loop through the board and check if there are two of my enemies tokens
        in a row and there is an open spot to the left/right of 2nd token.
        Make sure that the column is not higher than the 5th column
        or else we will go out of bounds.
        """
        enemy_token = self.getenemynum()
        moves = self.possible_moves(board)

        '''loop through the board checking from left to right'''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 5:
                    if (board[row][col] == enemy_token and
                        board[row][col + 1] == enemy_token and
                        [row, col + 2] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 2]

        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 1:
                    if (board[row][col] == enemy_token and
                        board[row][col - 1] == enemy_token and
                        [row, col - 2] in moves):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 2]

        '''
        loop through the board checking from left to right for one token, blank spot,
        then another token
        '''
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col < 5:
                    if (board[row][col] == enemy_token and
                        [row, col + 1] in moves and
                        board[row][col + 2] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col + 1]

        '''
        loop through the board checking from right to left for one token, blank spot,
        then another token
        '''
        for row in range(len(board)):
            for col in reversed(range(len(board[row]))):
                if col > 1:
                    if (board[row][col] == enemy_token and
                        [row, col - 1] in moves and
                        board[row][col - 2] == enemy_token):

                        '''
                        return the column and row that will give me four in a row.
                        This will be compared to the moves I am allowed to make
                        '''
                        return [row, col - 1]

        return False

    def do_they_have_two_vertical(self, board):
        """
        Loop through the board and check if there are two of my enemies tokens in a column
        and there is an open spot above my second token. Make sure that the row is not
        higher than the 3rd row because there is no point in placing a token if I cant
        get 3 in a row
        """
        enemy_token = self.getenemynum()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if row < 3:
                    if (board[row][col] == enemy_token and
                        board[row + 1][col] == enemy_token and
                        board[row + 2][col] == 0):

                        '''
                        return column plus 1 because if the column is number 0
                        then it will fail the if statement used to check if I have
                        three vertically. The one will be subtracted.
                        '''
                        return col + 1

        return False

    def requestmovement(self, board, height):
        """
        This function is the function that returns the column that I am going to place
        my token.
        """

        '''Get all the possible moves'''
        moves = self.possible_moves(board)

        '''If I have three in a col with one open on top then play that spot'''
        if self.do_i_have_three_vertical(board):
            '''
            read the return statement comment form this function to know why we subtract
            one
            '''
            return self.do_i_have_three_vertical(board) - 1

        elif self.do_i_have_three_horizontal(board) in moves:
            return self.do_i_have_three_horizontal(board)[1]

        elif self.do_i_have_three_diagonal(board) in moves:

            return self.do_i_have_three_diagonal(board)[1]

        elif self.do_they_have_three_vertical(board):
            '''
            read the return statement comment form this function to know why we subtract
            one
            '''
            return self.do_they_have_three_vertical(board) - 1

        elif self.do_they_have_three_horizontal(board) in moves:

            return self.do_they_have_three_horizontal(board)[1]

        elif self.do_they_have_three_diagonal(board) in moves:

            return self.do_they_have_three_diagonal(board)[1]

        elif self.do_i_have_two_horizontal(board) in moves:

            return self.do_i_have_two_horizontal(board)[1]

        elif self.do_i_have_two_vertical(board):

            return self.do_i_have_two_vertical(board) - 1

        elif self.do_they_have_two_horizontal(board) in moves:

            return self.do_they_have_two_horizontal(board)[1]

        elif self.do_they_have_two_vertical(board):

            return self.do_they_have_two_vertical(board) - 1

        elif [0, 3] in moves:
            return 3

        elif [1, 3] in moves:
            return 3

        else:
            length = len(moves)
            return moves[random.randrange(0, length)][1]