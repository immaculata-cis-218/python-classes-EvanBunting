"""
Movie class lab
Evan Bunting
"""

class Movie:
    """
    Any movie
    """

    def __init__(self, total_reviews, positive_reviews, name, score):
        self.total_reviews = total_reviews
        self.positive_reviews = positive_reviews
        self.name = name
        self.score = score

    def get_reviews(self):
        '''Tells you what movie picked'''
        return f"You chose the movie {self.name}, which is a score of {self.score} "

    def movie_score(self):
        """Calculates a movies rotten tomatoes score"""
        self.score = self.positive_reviews / self.total_reviews
        return self.score

if __name__ == "__main__":
    Titanic = Movie("Titanic", 250, 220, 88)
    Avatar = Movie("Avatar", 335, 274, 82)
    print(Titanic.movie_score())
    print(Titanic.get_reviews())