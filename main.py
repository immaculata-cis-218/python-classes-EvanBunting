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

    def give_summary(self):
        '''Tells you what movie picked'''
        return f"You chose the movie {self.name}, which has a score of {self.movie_score()} "

    def __repr__(self):
        return f"Movie({self.name}, {self.positive_reviews}, {self.total_reviews})"

    def __str__(self):
        return f"{self.name} ({self.total_reviews}), having {self.positive_reviews} positive reviews"

    def __eq__(self, other):
        return self.positive_reviews == other.positive_reviews

    def __lt__(self, other):
        return self.positive_reviews < other.positive_reviews

    def __gt__(self, other):
        return self.positive_reviews > other.positive_reviews

class Runtime(Movie):
    """The runtime of any movie"""
    def __init__(self, name, runtime):
        super().__init__(name, positive_reviews=0, total_reviews=250)
        self.runtime = runtime

    def calculate_runtime(self):
        """Calculates the movie's runtime"""
        hours = self.runtime // 60
        minutes = self.runtime % 60
        return f"{hours} hours {minutes} minutes"

    def give_summary(self):
        """Gives summary for run time"""
        summary = super().give_summary()
        summary = f"{summary}, it is {self.runtime} long"
        return summary

class BoxOffice(Movie):
    """The box office of any movie"""
    def __init__(self, name, box_office):
        super().__init__(name, positive_reviews=220, total_reviews=250)
        self.box_office = box_office

    def calculate_box_office(self):
        """Calculates the movie's box office"""
        return f"${self.box_office:,}"

    def give_summary(self):
        """Gives summary for box office"""
        summary = super().give_summary()
        summary = f"{summary}, and it made {self.box_office} "
        return summary

if __name__ == "__main__":
    Titanic = Movie("Titanic", 220, 250)
    Avatar = Movie("Avatar", 274, 335)
    print(Titanic.movie_score())
    print(Titanic.give_summary())

    Titanic = Runtime("Titanic", 194)
    print(Titanic.calculate_runtime())
    print(Titanic.give_summary())

    Titanic = BoxOffice("Titanic", 2187463944)
    print(Titanic.calculate_box_office())
    print(Titanic.give_summary())

    print(Avatar.movie_score())
    print(Avatar.give_summary())

    Avatar = Runtime("Avatar", 162)
    print(Avatar.calculate_runtime())
    print(Avatar.give_summary())

    Avatar = BoxOffice("Avatar", 2923706026)
    print(Avatar.calculate_box_office())
    print(Avatar.give_summary())

    print(repr(Titanic))

    print(str(Titanic))

    print(repr(Avatar))

    print(str(Avatar))

    print(Titanic == Avatar)
    print(Titanic < Avatar)
    print(Titanic > Avatar)
