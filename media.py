import webbrowser


# This class called movied is the DNA of the 3 movie instances in
# the entertainment_center.py file. Each intance will have a
# title, a story line, a image, and short trailer.
class Movie():
    """CHINEDU SHORT MOVIE TRAILER LIBRARY"""

# This function creates memory to store descriptions of my instances.
    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

# This functon opens a webbroswer to display my trailers.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
