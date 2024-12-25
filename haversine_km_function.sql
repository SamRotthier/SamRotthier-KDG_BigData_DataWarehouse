CREATE OR REPLACE FUNCTION haversine_km(lat1 numeric, lon1 numeric, lat2 numeric, lon2 numeric)
RETURNS numeric AS $$
DECLARE
   distance numeric;
BEGIN
-- Check if the coordinates are the same
    IF lat1 = lat2 AND lon1 = lon2 THEN
       distance := 0;
    ELSE
        SELECT 6371 * ACOS(
	     COS(radians(lat1))
	     * COS(radians(lat2))
         * COS(radians(lon2) - radians(lon1))
         + SIN(radians(lat1)) * SIN(radians(lat2)))
     INTO distance;
    END IF;
   RETURN distance;
END;
$$ LANGUAGE plpgsql IMMUTABLE;
