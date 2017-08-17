import fresh_tomatoes
import media

avengers = media.Movie("Avengers", "https://images-na.ssl-images-amazon.com/"
                       "images/I/61bINjWK62L.jpg", "https://www.youtube.com/"
                       "watch?v=eOrNdBpGMv8")

captain_america = media.Movie("Captain America", "http://nuggettheatre.com/"
                              "wp-content/uploads/2016/05/Captain-America-"
                              "Civil-War-movie-poster.jpg", "https://www."
                              "youtube.com/watch?v=dKrVegVI0Us")

justice_league = media.Movie("Justice League",
                             "https://pbs.twimg.com/media/C7tkfeoVwAAEyNX.jpg",
                             "https://www.youtube.com/watch?v=DblEwHkde8U")

thor_ragnarok = media.Movie("Thor Ragnarok",
                            "https://img14.deviantart.net/4304/i/2016/115/6/6"
                            "/thor___ragnarok_movie_poster_by_jackjack671120-"
                            "da07c33.jpg", "https://www.youtube.com/watch?v="
                            "ue80QwXMRHg")

iron_man = media.Movie("Iron Man",
                       "http://www.freemovieposters.net/posters/iron_man_2_"
                       "2010_3219_poster.jpg", "https://www.youtube.com/watch"
                       "?v=8hYlB38asDY")

spider_man = media.Movie("Spider-Man Homecoming",
                         "https://i.redd.it/pslzf509nb1z.jpg",
                         "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

movies = [avengers, captain_america, justice_league, thor_ragnarok,
          iron_man, spider_man]
fresh_tomatoes.open_movies_page(movies)
