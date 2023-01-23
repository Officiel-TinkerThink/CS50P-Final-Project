from project import game_setup, assessment, level_verification

def test_game_setup():
    assert len(game_setup(1)) < 7
    assert len(game_setup(2)) < 10
    assert len(game_setup(3)) < 13

def test_assessment():
    assert assessment('7+4=11','7+3=10') == (False, '220220')
    assert assessment('9=13-4','9=13-4') == (True, '222222')

def test_level_verification():
    try:
        assert level_verification(0) == False
        assert level_verification(1) == True
        assert level_verification('Easy') == True
    except ValueError:
        pass