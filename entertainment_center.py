import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/" +
                     "Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/d1_JBMrrYw8")

inception = media.Movie("Inception",
                        "A contemporary science fiction action thriller set" +
                        "within the architecture of the mind",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/" +
                        "Inception_%282010%29_theatrical_poster.jpg",
                        "https://youtu.be/8hP9D6kZseM")

iron_man = media.Movie("Iron Man",
                       "Suit up for action with Robert Downey Jr. in the" +
                       "ultimate adventure movie you've been waiting for",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/" +
                       "Ironmanposter.JPG",
                       "https://youtu.be/8hYlB38asDY")

forrest_gump = media.Movie("Forrest Gump",
                           "A inspirational story about the life of Forrest" +
                           "Gump who has intellectual deficiency",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/" +
                           "Forrest_Gump_poster.jpg",
                           "https://youtu.be/hMxENmG3Tyw")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "A prominent banker unjustly" +
                                       "convicted of murder spends many" +
                                       "years in the Shawshank prison",
                                       "https://upload.wikimedia.org/" +
                                       "wikipedia/en/8/81/ShawshankRedemp" +
                                       "tionMoviePoster.jpg",
                                       "https://youtu.be/K_tLp7T6U1c")

shutter_island = media.Movie("Shutter Island",
                             "As Marshal Teddy Daniels arrives at the asylum" +
                             " for the criminally insane on Shutter Island " +
                             "what starts as a routine investigation quickly" +
                             " takes a sinister turn",
                             "https://upload.wikimedia.org/wikipedia/en/7/" +
                             "76/Shutterislandposter.jpg",
                             "https://youtu.be/1jERdYDWG8g")

# add movie instance to movies list
movies_list = [
    avatar, inception, iron_man, forrest_gump,
    the_shawshank_redemption, shutter_island
]

# pass the movie instance list to fresh_tomatoes to render the static web page
fresh_tomatoes.open_movies_page(movies_list)
