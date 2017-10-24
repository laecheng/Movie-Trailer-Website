# import the webbrowser module from Python library
import webbrowser


class Movie():
    """ This class provides a way to store movie related information
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ The constructor for Movie class
            Args:
                movie_title (str): the title of movie
                movie_storyline (str): the story line of movie
                poster_image (str): url to the poster image
                trailer_youtube (str): url to the trailer
            Returns:
                movie instance
        """
        self.title = movie_title
        self.stroyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
