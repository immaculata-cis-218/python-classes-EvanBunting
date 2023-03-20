from main import Movie

def test_movie_score():
    test_score = Movie("Titanic", 250, 220, 88)
    summary = test_score.movie_score()
    assert "Titanic" in summary

def test_movie_score2():
    test_score = Movie("Avatar", 335, 274, 82)
    summary = test_score.movie_score()
    assert "Avatar" in summary