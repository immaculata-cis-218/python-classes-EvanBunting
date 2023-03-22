from main import Movie

def test_movie_score():
    test_score = Movie("Titanic", 220, 250)
    summary = test_score.movie_score()
    assert .88 == summary

def test_movie_score2():
    test_score = Movie("Avatar", 274, 335)
    summary = test_score.movie_score()
    assert .81 < summary < .82