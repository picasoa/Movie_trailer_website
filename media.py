# the in-build library file "webbrowser"
import webbrowser


# main class with common attributes shared by  subclasses
class Main_class():
    def __init__(self, movie_title, movie_trailer, movie_story, movie_poster):
        self.movie_title = movie_title
        self.trailer_youtube_url = movie_trailer
        self.movie_story = movie_story
        self.poster_image_url = movie_poster


# class for creating new movies
class New_movie(Main_class):
    def __init__(self, movie_title, movie_trailer, movie_story, movie_poster):  # cunstructor
        Main_class.__init__(self, movie_title, movie_trailer, movie_story, movie_poster)


# class for creating new series
class New_series(Main_class):
    def __init__(self, movie_title, movie_trailer, movie_story, movie_poster):  # cunstructor
        Main_class.__init__(self, movie_title, movie_trailer, movie_story, movie_poster)
