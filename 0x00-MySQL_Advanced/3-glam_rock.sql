-- List all bands with `Glam rock` as their main style
-- ranked by their longevity (life span untill 2022)
SELECT band_name, split - formed as lifespan
  FROM metal_bands
 WHERE style = 'Glam rock'
 ORDER BY lifespan DESC;
