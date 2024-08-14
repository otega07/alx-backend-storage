-- lists all bands with Glam rock as their main style, ranked by their longevity
-- IFNULL: USE 2022 if split culumn is null
-- to get the longevity: split minus formed
-- from metal_bands table
-- select only glam rock from style culume
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
