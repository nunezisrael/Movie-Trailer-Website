Movie package

Main file is called, entertainment_center.py, it contains intances of the Movie class and it dynamially creates the website. The website displays several movies and it allows their trailers to be previewed.

This packagemMakes use the IMDbPy API to download data for the site.
http://imdbpy.sourceforge.net/support.html

********* However please note that the IMDB webservers are SLOW and so when running entertainment_center.py the site may load in 25 - 35 seconds to load the first time. Nonetheless once everything is compiled the data fetch take only about 10-15 seconds  ****************


Here is breakdown of the files attached and their use:

1. media - defines a Video class (Parent) and the Movie class (child). The Movie class is used to create movie objects that are displayed on the website.

2. moviedb.py - imports the IMDbPY API and makes use if functions to gather different data types of a specific movie. i.e. movie title, plot, ratings, etc.

-movie_search_manual - creates a method for the user to search the IMDB DB and select a specific movie. This information was used when creating the movie instances in entertainment_center.py. This program is for reference only.

3. entertainment_center.py - instantiates Movie instance from media.py and uses functions from the module moviedb.py to call the IMDB webservers to gather movie data.

4. fresh_tomatoes.py -  creates the HTML, CSS and Java Script for the website. It calls the Movie instances from entertainment_center.py to populate data for each movie.



