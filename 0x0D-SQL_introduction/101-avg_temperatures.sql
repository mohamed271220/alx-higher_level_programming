-- This script computes the average temperature by city and orders the result by temperature in descending order
SELECT city, AVG(temperature) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
