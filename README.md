# netflix-movies-and-tv-shows
Netflix - TV Shows and Movies
This dataset was created to list all shows and movies available on Netflix. It was collected from JustWatch in March 2023, containing data available in the United States.

Content
This dataset contains two files, one for the titles (titles.csv) and the other for the cast (credits.csv) of each movie and show on the platform.

The titles.csv contains more than 6k titles, witch 15 columns containing:

id: The title ID on JustWatch.
title: The name of the title.
show_type: TV show or movie.
description: A brief description.
release_year: The release year.
age_certification: The age certification.
runtime: The length of the episode (SHOW) or movie.
genres: A list of genres.
production_countries: A list of countries that - produced the title.
seasons: Number of seasons if it's a SHOW.
imdb_id: The title ID on IMDB.
imdb_score: Score on IMDB.
imdb_votes: Votes on IMDB.
tmdb_popularity: Popularity on TMDB.
tmdb_score: Score on TMDB.
The credits.csv contains over 81k credits of actors and directors, with 5 columns containing:

person_ID: The person ID on JustWatch.
id: The title ID on JustWatch.
name: The actor or director's name.
character_name: The character name.
role: ACTOR or DIRECTOR.
