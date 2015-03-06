import imdb

#instantiating Movie object
moviedb = imdb.IMDb(accessSystem='web')

#Creating a list of movie searched
def movie_search(title):
    #Get movie from IMDB
    movie_list = moviedb.search_movie(title)
    return movie_list

#Function that will provide the movie selected
def movie_sel(title, number):
    movie_list = movie_search(title)
    selected_movie = movie_list[number]
    moviedb.update(selected_movie)
    return selected_movie

#Function that return the selected movie title
def title(selected_movie):
    movie_title = selected_movie['long imdb title']
    return movie_title

#Function that return the selected movie plot
def plot(selected_movie):
    movie_plot = selected_movie['plot']
    return movie_plot[1]

#Function that return the selected movie cover url
def cover(selected_movie):
    movie_cover = selected_movie['cover url']
    return movie_cover

#Function that return the selected movie actors
def actors(selected_movie):
    movie_actors = selected_movie['cast']
    cast = str(movie_actors[0])
    for index in range(1,len(movie_actors)):
        cast = cast +', '+str(movie_actors[index])
    return cast

#Function that return the selected movie release date
def release_date(selected_movie):
    movie_release_date = selected_movie['year']
    return movie_release_date

#Function that return the selected movie duration
def length(selected_movie):
    movie_length = selected_movie['runtimes']
    return movie_length[0] + ' minutes'

#Function that return the selected movie rating
def rating(selected_movie):
    movie_rating = selected_movie['rating']
    return 'Rating: '+str(movie_rating) + ' of 10'

