# -*- coding: utf-8 -*-
"""
Created on Sun May 15 15:19:16 2016

@author: Rahul Patni
"""
import webbrowser

class Movie(object):

    """This class provides to store information related to movies"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]    
    
    def __init__(self, movie_title, movie_storyline, movie_poster_image_url, 
                 movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        