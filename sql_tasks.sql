/*
task number 1 

# this is wrong
SELECT airport_name, coordinates
FROM airports_data
where coordinates = (SELECT MAX(coordinates) FROM airports_data)
UNION ALL
SELECT airport_name, coordinates
FROM airports_data
WHERE coordinates = (SELECT MIN(coordinates) FROM airports_data);
*/

/*
task number 2
*/

SELECT model, range
FROM bookings.aircrafts_data
ORDER BY range DESC LIMIT 1;

/*
task number 3
*/

SELECT aircraft_code, seat_no, fare_conditions,
       rank() OVER (PARTITION BY aircraft_code ORDER BY fare_conditions DESC)
FROM bookings.seats;