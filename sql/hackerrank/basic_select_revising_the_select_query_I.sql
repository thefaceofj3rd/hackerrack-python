CREATE TABLE CITY
(
    ID NUMBER,
    NAME VARCHAR2 (17),
    COUNTRYCODE VARCHAR2 (3),
    DISTRICT VARCHAR2 (20),
    POPULATION NUMBER
);

SELECT *
FROM CITY
WHERE Population > 100000
  AND CountryCode = 'USA';
