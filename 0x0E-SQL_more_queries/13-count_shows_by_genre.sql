-- This script lists all genres from tv_genres and displays the number of shows linked to each from tv_shows through tv_show_genres. Each record displays: <TV Show genre> - <Number of shows linked to this genre>. The first column is called genre and the second column is called number_of_shows. Don’t display a genre that doesn’t have any shows linked. Results are sorted in descending order by the number of shows linked.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
