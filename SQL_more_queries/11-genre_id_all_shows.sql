-- task 11
-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres 
-- Uno los genres a los tv_show y los que no coinciden toman el valor NULL
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;