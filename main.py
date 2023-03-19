"""
Movie class lab
Evan Bunting
"""

class Movie:
    """
    Any movie
    """

    def __init__(self, total_reviews, positive_reviews):
        self.total_reviews = total_reviews
        self.positive_reviews = positive_reviews

    def get_reviews(self):
        '''Function to gets the total reviews'''
        return self.total_reviews

    def movie_score(self):
        """Calculates a movies rotten tomatoes score"""
        score = self.positive_reviews / self.total_reviews
        return score

if __name__ == "__main__":
    Titanic = Movie("Titanic", 1)
    print(Titanic.movie_score())
    print(Titanic.get_reviews())