-- List all bands with `Glam rock` as their main style
-- ranked by their longevity (life span untill 2022)
SELECT band_name, IF(split, split - formed, 2022 - formed) as lifespan
  FROM metal_bands
 WHERE style LIKE '%Glam rock%'
 ORDER BY lifespan DESC;
