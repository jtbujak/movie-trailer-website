import webbrowser


class Movie():
    """Class for each of my favorite movies"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Initialize movie name, poster and trailer attributes"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Plays movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
