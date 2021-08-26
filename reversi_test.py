from reversi_board import Board


def test_right_position_is_detected():
    board = Board([".BW."], "B")
    assert board.possibilities() == [".BW0"]


def test_right_position_is_detected_with_more_in_between():
    board = Board([".BWW."], "B")
    assert board.possibilities() == [".BWW0"]


def test_left_position_is_detected():
    board = Board([".WB."], "B")
    assert board.possibilities() == ["0WB."]


def test_left_position_is_detected_with_more_in_between():
    board = Board([".WWB."], "B")
    assert board.possibilities() == ["0WWB."]


def test_right_position_is_detected_with_white():
    board = Board([".WB."], "W")
    assert board.possibilities() == [".WB0"]


def test_both_sides_are_detected():
    board = Board([".WBW."], "B")
    assert board.possibilities() == ["0WBW0"]


def test_detect_possibilities_for_first_row():
    board = Board([".WBW", "WBW."], "B")
    assert board.possibilities()[0] == "0WBW"


def test_detect_possibilities_for_all_rows():
    board = Board([".WBW", "WBW."], "B")
    assert board.possibilities() == ["0WBW", "WBW0"]
