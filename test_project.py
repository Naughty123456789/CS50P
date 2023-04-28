from project import  has_been_picked, track_turn, tracking_turn
import pytest


def main():
    test_has_been_picked()
    test_track_turn()
    test_tracking_turn()

def test_has_been_picked():
    assert has_been_picked(1 , 1) == "Dude it has already been picked"
    assert has_been_picked(2 , 2) == "Dude it has already been picked"

def test_track_turn():
    assert track_turn(5) == 'X'
    assert track_turn(4) == '0'
    assert track_turn(3) == 'X'

def test_tracking_turn():
    assert tracking_turn(5) == "Player 1 wins"
    assert tracking_turn(4) == "Player 2 wins"
    assert tracking_turn(1) == "Player 1 wins"
    
if __name__ == "__main__":
    main()
