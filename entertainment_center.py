import media,fresh_tomatoes

from moviedb import movie_sel, title,plot, cover, actors, release_date, length, rating

bl= movie_sel("the blue lagoon",0)
blue_lagoon = media.Movie(title(bl), plot(bl), cover(bl),"https://www.youtube.com/watch?v=OUffh8dkm5M",rating(bl),actors(bl),release_date(bl),length(bl))

m = movie_sel("the matrix", 4)
matrix = media.Movie(title(m),plot(m),cover(m),"https://www.youtube.com/watch?v=m8e-FF8MsqU",rating(m),actors(m),release_date(m),length(m))

g = movie_sel("gravity", 0)
gravity = media.Movie(title(g),plot(g),cover(g),"https://www.youtube.com/watch?v=OiTiKOy59o4",rating(g),actors(g),release_date(g),length(g))

jp = movie_sel("jurassic park", 3)
jurassic_park = media.Movie(title(jp),plot(jp),cover(jp),"https://www.youtube.com/watch?v=lc0UehYemQA",rating(jp),actors(jp),release_date(jp),length(jp))

im = movie_sel("iron man", 3)
iron_man = media.Movie(title(im),plot(im),cover(im),"https://www.youtube.com/watch?v=oYSD2VQagc4",rating(im),actors(im),release_date(im),length(im))

a = movie_sel("the avengers", 0)
avengers = media.Movie(title(a),plot(a),cover(a),"https://www.youtube.com/watch?v=hIR8Ar-Z4hw",rating(a),actors(a),release_date(a),length(a))

t3 = movie_sel("the transporter", 3)
the_transporter_3 = media.Movie(title(t3),plot(t3),cover(t3),"https://www.youtube.com/watch?v=Pbh3CDBNIQA",rating(t3),actors(t3),release_date(t3),length(t3))

h = movie_sel("hatchi",0)
hatchi = media.Movie(title(h),plot(h),cover(h),"https://www.youtube.com/watch?v=Y6U7mAnPtw4",rating(h),actors(h),release_date(h),length(h))

#list that will be passed to fresh_tomatoes function
movies  = [blue_lagoon, matrix, gravity, jurassic_park, iron_man, avengers, the_transporter_3,hatchi ]

#calling the function on the fresh_tomatoes file to create the website
fresh_tomatoes.open_movies_page(movies)
