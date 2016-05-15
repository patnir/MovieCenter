# -*- coding: utf-8 -*-
"""
Created on Sun May 15 15:22:27 2016

@author: Rahul Patni
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", 
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", 
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


the_day_after_tomorrow = media.Movie("The Day After Tomorrow", 
                                     "Climate change is real", 
                                     "https://upload.wikimedia.org/wikipedia/en/5/58/The_Day_After_Tomorrow_movie.jpg", 
                                     "https://www.youtube.com/watch?v=MFLncfCvPeY")

school_of_rock = media.Movie("School of rock", 
                             "People come here to learn riffs", 
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")     

ratatouille = media.Movie("Ratatouille", 
                             "Story of a chef and his cook, a rat", 
                             "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", 
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")                                     

hunger_games = media.Movie("Hunger Games", 
                             "Competition between districts", 
                             "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg", 
                             "https://www.youtube.com/watch?v=4S9a5V9ODuY")   

movies = [toy_story, avatar, the_day_after_tomorrow, school_of_rock, ratatouille, hunger_games]

print media.Movie.__doc__

fresh_tomatoes.open_movies_page(movies)

                                  