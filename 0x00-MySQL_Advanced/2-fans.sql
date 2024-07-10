-- ranks the origin of bands by the most (non-unique) fans
-- group all the origins and calulate the sum of Fans while grouping
SELECT origin, SUM(fans) as nb_fans
  FROM metal_bands
 GROUP BY origin
 ORDER BY nb_fans DESC;
