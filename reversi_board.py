import re


class Board:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.opponent = 'W' if self.player == 'B' else 'B'

    def possibilities(self) -> [str]:
        result = []
        for row in self.board:
            row = self.mark_possibility_right(row)
            row = self.mark_possibility_left(row)
            result.append(row)
        return result

    def mark_possibility_right(self, row: str):
        return re.sub(f'({self.player}{self.opponent}+)\\.', r'\g<1>0', row)

    def mark_possibility_left(self, row):
        return re.sub(f'\\.({self.opponent}+{self.player})', r'0\g<1>', row)
