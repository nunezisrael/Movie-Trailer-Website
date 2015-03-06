from moviedb import movie_search
'''Function used to search for a movie and select the index when
creating the movie list to display on the site. This function makes used
of the module moviedb'''

#Sorting throught the movie list to make manual selection
def movies():
    #When running the program it will ask the user to enter the movie title
    print ('Please enter movie title:')
    title = input()

    movie_list = movie_search(title)
    #Printing the movie list gathered form the imdb web service and printing
    #it in a familiar format with the index
    for index in range(len(movie_list)):
        movie_title = movie_list[index]
        print  (str(index) +" "+ movie_title['long imdb title'])
    '''
    Used to test the module and gather all the necessary infomation
    about the selected movie.
    
    #asking user to select movie
    print ('\n select a movie, enter number:')
    movie_selection = input()
    selected_movie = movie_list[movie_selection]
    #gathering all relevant details about the selected movie
    moviedb.update(selected_movie)
    return selected_movie
    '''

movies()
