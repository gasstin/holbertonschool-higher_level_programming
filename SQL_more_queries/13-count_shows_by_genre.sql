-- task 13
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
SELECT
    tv_genres.name AS genre,
    COUNT(tv_genres.name) AS number_of_shows -- cuenta la cantidad de generos.
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre                                  -- ordeno por genero, no por cantidad.
ORDER BY number_of_shows DESC;