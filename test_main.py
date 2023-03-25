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
