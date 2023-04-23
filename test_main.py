from main import Movie, Runtime, BoxOffice

def test_movie_score():
    test_score = Movie("Titanic", 220, 250)
    summary = test_score.movie_score()
    assert .88 == summary

def test_movie_score2():
    test_score = Movie("Avatar", 274, 335)
    summary = test_score.movie_score()
    assert .81 < summary < .82

def test_movie_run_time():
    test_run_time = Runtime("Titanic", 194)
    summary = test_run_time.calculate_runtime()
    assert '3 hours 14 minutes' in summary

def test_movie_run_time2():
    test_run_time = Runtime("Avatar", 162)
    summary = test_run_time.calculate_runtime()
    assert '2 hours 42 minutes' in summary

def test_movie_box_office():
    test_box_office = BoxOffice("Titanic", 2187463944)
    summary = test_box_office.calculate_box_office()
    assert '2,187,463,944' in summary

def test_movie_box_office2():
    test_box_office = BoxOffice("Avatar", 2923706026)
    summary = test_box_office.calculate_box_office()
    assert '2,923,706,026' in summary

def test_repr():
    test_repr = Movie("Titanic", 220, 250)
    summary = test_repr.__repr__()
    assert 'Movie(Titanic, 220, 250)' in summary

def test_repr2():
    test_repr = Movie("Avatar", 274, 335)
    summary = test_repr.__repr__()
    assert 'Movie(Avatar, 274, 335)' in summary

def test_str():
    test_str = Movie("Titanic", 220, 250)
    summary = test_str.__str__()
    assert 'Titanic (250), having 220 positive reviews' in summary

def test_str2():
    test_str = Movie("Avatar", 274, 335)
    summary = test_str.__str__()
    assert 'Avatar (335), having 274 positive reviews' in summary

def test_eq():
    Titanic = Movie("Titanic", positive_reviews=220, total_reviews=250)
    Avatar = Movie("Avatar", positive_reviews=274, total_reviews=335)
    if Titanic == Avatar:
        return False

def test_lt():
    Titanic = Movie("Titanic", positive_reviews=220, total_reviews=250)
    Avatar = Movie("Avatar", positive_reviews=274, total_reviews=335)
    if Titanic < Avatar:
        return True

def test_gt():
    Titanic = Movie("Titanic", positive_reviews=220, total_reviews=250)
    Avatar = Movie("Avatar", positive_reviews=274, total_reviews=335)
    if Titanic > Avatar:
        return False
