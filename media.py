import webbrowser

class Video():
    """This class defines what a video and also provides a method for playing a trailer of the video."""
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    """This is a child class of the Video class, it inherits all of the parent's class attributes with the addition of the attributes
        CAST, RELEASE DATE AND DURATION"""
    def __init__(self, title, storyline, poster_image, trailer_youtube, rating, cast, release_date, lenght):
        Video.__init__(self, title, storyline, poster_image, trailer_youtube)
        self.rating = rating
        self.actors = cast
        self.release_date = release_date
        self.duration = lenght
    
