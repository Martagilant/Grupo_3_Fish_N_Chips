SELECT *
FROM crime_scene_report
where date = "20180115" and type = "murder" and city = "SQL City"

20180115	murder	Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".	SQL City


SELECT *
FROM person
WHERE address_street_name in ("Northwestern Dr")
ORDER BY address_number DESC   
	Morty Schapiro 14887


I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".

SELECT *
FROM person
WHERE address_street_name = "Franklin Ave" and name like "Annabel%"

	Annabel Miller  16371 318771143
I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.
            
SELECT *
FROM interview
WHERE person_id in (14887, 16371)

SELECT *
FROM get_fit_now_member
WHERE id like "48Z%"

48Z7A	28819	Joe Germuska	20160305	gold 48z38
48Z55	67318	Jeremy Bowers	20160101	gold 48z55*

SELECT *
FROM get_fit_now_check_in
WHERE membership_id in ("48Z38", "48Z55") and check_in_date = 20180109

SELECT *
FROM get_fit_now_check_in
WHERE membership_id in ("48Z38", "48Z55") and check_in_date = 20180115


SELECT *
FROM drivers_license
WHERE plate_number like "H42W%"

183779	21	65	blue	blonde	female	H42W0X	Toyota	Prius

SELECT *
FROM person
WHERE license_id = 183779

78193	Maxine Whitely	183779	110	Fisk Rd	137882671

SELECT *
FROM crime_scene_report
WHERE type = "robbery" and date < 20180115 and description like "%car%"


SELECT *
FROM person
WHERE license_id = 183779 

license_id	address_number	address_street_name	ssn
78193	Maxine Whitely	183779	110	Fisk Rd	137882671

SELECT *
FROM interview
WHERE person_id = 78193

no data returned, maxine whitely did not give an interview


SELECT *
FROM facebook_event_checkin
WHERE person_id = 78193

maxine wasnt seen 


SELECT *
FROM person
WHERE name = "Jeremy Bowers"

id	name	license_id	address_number	address_street_name	ssn
67318	Jeremy Bowers	423327	530	Washington Pl, Apt 3A	871539279


SELECT *
FROM drivers_license
WHERE id = 423327

23327	30	70	brown	brown	male	0H42W2	Chevrolet	Spark LS


SELECT *
FROM facebook_event_checkin
WHERE person_id = 67318


67318	4719	The Funky Grooves Tour	20180115
67318	1143	SQL Symphony Concert	20171206

SELECT *
FROM interview
WHERE person_id = 67318

67318	I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017
SELECT COUNT(person_id), person_id
FROM facebook_event_checkin
WHERE date like "201712%" and event_name = "SQL Symphony Concert"
GROUP BY person_id

3	24556 #id persona 



3	99716


SELECT *
FROM person
WHERE id = 24556

24556	Bryan Pardo	101191	703	Machine Ln	816663882

SELECT *
FROM person
WHERE id = 99716

9716	Miranda Priestly	202298	1883	Golden Ave	987756388


SELECT *
FROM drivers_license
WHERE id = 202298

id	age	height	eye_color	hair_color	gender	plate_number	car_make	car_model
202298	68	66	green	red	female	500123	Tesla	Model S


INSERT INTO solution VALUES (1, 'Jeremy Bowers');
        
        SELECT value FROM solution;

INSERT INTO solution VALUES (1, 'Miranda Priestly');
        
        SELECT value FROM solution;