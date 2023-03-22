"""
Movie class lab
Evan Bunting
"""

class Movie:
    """
    Any movie
    """

    def __init__(self, name, positive_reviews, total_reviews):
        self.name = name
        self.positive_reviews = positive_reviews
        self.total_reviews = total_reviews

    def movie_score(self):
        """Calculates a movies rotten tomatoes score"""
        score = self.positive_reviews / self.total_reviews
        return score
    
    def get_reviews(self):
        '''Tells you what movie picked'''
        return f"You chose the movie {self.name}, which is a score of {self.movie_score()} "

if __name__ == "__main__":
    Titanic = Movie("Titanic", 220, 250)
    Avatar = Movie("Avatar", 247, 335)
    print(Titanic.movie_score())
    print(Titanic.get_reviews())