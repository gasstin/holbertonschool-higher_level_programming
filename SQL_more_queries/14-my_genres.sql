-- task 14
-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
SELECT
    tv_genres.name
FROM tv_shows, tv_genres -- can be various tables
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter' -- solo los Dexter
AND tv_shows.id = tv_show_genres.show_id
-- comparten el id del tv_show con el id del tv_show_genres
ORDER BY tv_shows.title ASC;
                                   