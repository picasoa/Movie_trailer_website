# importing the file which will render us the Main_class
import media
# importing the file which will hel us render our website on the web browser
import fresh_tomatoes


# following are the instances of the "New_movie" and "New_series" class
# with the same shared attributes inherited by the Main_class
cap = media.New_movie("Captian America", "https://www.youtube.com/watch?v=Je"
                      "rVrbLldXw", "An experimental super soldier", "images\\"
                      "2.jpg")

irmn = media.New_movie("Iron_man", "https://www.youtube.com/watch?v=8hYlB38asDY",  # noqa 
                       "A multidollar billionaire makes a suit to save himself", "images\\3.jpg")  # noqa

hulk = media.New_movie("Hulk", "https://www.youtube.com/watch?v=pfd5Sw4_LSc"
                       "LldXw", "An experimental green maniac", "images\\4.j"
                       "pg")

irmn2 = media.New_movie("Iron_Man_2", "https://www.youtube.com/watch?v=wKtcm"
                        "iifycUbLldXw", "tony stak makes a new element for h"
                        "is suit", "images\\5.jpg")

thor = media.New_movie("Thor", "https://www.youtube.com/watch?v=lKoN-dTaepA",
                       "the god of thunder redeem his power", "images\\6.jpg")

avngs = media.New_movie("Avengers", "https://www.youtube.com/watch?v=eOrNdBp"
                        "GMv8", "An experimental super soldier", "images\\7."
                        "jpg")

irmn3 = media.New_movie("Iron_Man_3", "https://www.youtube.com/watch?v=Ke1Y3"
                        "P9D0Bc", "destroys his tech looking it as a threat",
                        "images\\8.jpg")

thor2 = media.New_movie("Thor2", "https://www.youtube.com/watch?v=npvJ9FTgZbM",
                        "saving his world form the dark elve", "images\\9.jpg")

# list of all the instances which will be passed to the function below
movies = [cap, irmn, hulk, thor, avngs, irmn3, thor2]

# function open_movies_page called which will help us built our site
fresh_tomatoes.open_movies_page(movies)
