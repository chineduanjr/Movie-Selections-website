# the following imports the parent class called media.
# it also imports the fresh_tomatoes program which helps
# create my trailor website.
import media
import fresh_tomatoes

# This code stores info in the following order:
# movie title,synopsis, poster image, movie trailor.
belly = media.Movie(
    "Belly",
    "Living a Gangster life",
    "https://lh3.googleusercontent.com/jZB6hWcH87rxdmMu2hclv_dzUxSTzogdNHEYsRfYbIS4LLYDGuvZF_TbEDqU2tPA7YMoJw=w200-h300",  # NOQA
    "https://www.youtube.com/watch?v=VPEVkNCr00M")

sink = media.Movie(
    "Sink",
    "A domestic worker living in Johanesburg",
    "http://www.impawards.com/intl/south_africa/2016/posters/sink.jpg",
    "https://www.youtube.com/watch?v=QqFSK_n7mZc")

baby_driver = media.Movie(
    "Baby Driver",
    "Young teen driving for criminals",
    "http://www.movieposter.com/posters/archive/main/240/MPW-120377",
    "https://www.youtube.com/watch?v=D9YZw_X5UzQ")

# the movie list is needed so the fresh_tomatoes program can
# know what part of my code to read from.
movies = [belly, sink, baby_driver]

# Fresh_tomato is a pre built program to create my website.
# really cool code, thank god for the creators of this code!
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)
