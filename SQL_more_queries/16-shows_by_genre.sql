-- task 16
-- Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- You can use only one SELECT statement
SELECT
    tv_shows.title,
    tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres -- para contemplar los NULL
ON tv_shows.id = tv_show_genres.show_id
-- solo los programas y generos compartidos
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
-- solo los generos de los programas que
-- se encuentran en la tabla de generos
ORDER BY tv_shows.title ASC;