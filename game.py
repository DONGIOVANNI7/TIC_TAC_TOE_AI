class TicTacToeAI:
    def __init__(self):
        self.ai = "X"
        self.human = "O"

    def best_move(self, board):
        best_score = -float('inf')
        best_move = (-1, -1)
        
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = self.ai
                    score = self.minimax_alpha_beta(board, 0, -float('inf'), float('inf'), False)
                    board[row][col] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax_alpha_beta(self, board, depth, alpha, beta, is_maximizing):
        winner = self.get_winner(board)
        
        # Base cases
        if winner == self.ai:
            return 10 - depth
        if winner == self.human:
            return depth - 10
        if self.is_board_full(board):
            return 0

        # Recursive case with pruning
        if is_maximizing:
            max_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "":
                        board[row][col] = self.ai
                        score = self.minimax_alpha_beta(board, depth+1, alpha, beta, False)
                        board[row][col] = ""
                        max_score = max(max_score, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break  # Prune remaining branches
            return max_score
        else:
            min_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "":
                        board[row][col] = self.human
                        score = self.minimax_alpha_beta(board, depth+1, alpha, beta, True)
                        board[row][col] = ""
                        min_score = min(min_score, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break  # Prune remaining branches
            return min_score

    def get_winner(self, board):
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]

        return None

    def is_board_full(self, board):
        return all(all(cell != "" for cell in row) for row in board)