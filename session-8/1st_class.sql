SELECT DISTINCT author_id FROM requisitions;
# Using distinct value
SELECT DISTINCT delivery_status FROM requisitions;
# Find max and min Date
SELECT MIN(requisition_date), MAX(requisition_date)
FROM requisitions;

#Find how many proposal create with an proposal
SELECT rp.reference_no, rp.request_date, r.reference_no as "requistion_no", r.author_id,
    COUNT(rpr.request_proposal_id) as "total_proposal_no"
FROM requisitions r
    INNER JOIN request_proposal_requisitions rpr ON rpr.requisition_id = r.id
    INNER JOIN request_proposals rp on rpr.request_proposal_id = rp.id
GROUP BY rp.reference_no, rp.request_date, requistion_no,  r.author_id
ORDER BY total_proposal_no DESC;

#Find total requisition by an user
SELECT r.author_id, u.name,
    COUNT(r.author_id) as "total_requisition"
FROM requisitions r
    INNER JOIN users u ON u.id = r.author_id
WHERE r.requisition_date BETWEEN '2022-07-06' AND '2022-09-30'
GROUP BY  r.author_id, u.name
HAVING COUNT(r.author_id) > 3
ORDER BY total_requisition DESC;

#Split column query
#EST-22-CEIL-059
SELECT reference_no,
       SUBSTRING_INDEX(reference_no,'-',1) as 'code',
       SUBSTRING_INDEX(SUBSTRING_INDEX(reference_no,'-',2),'-',-1) as 'year',
       SUBSTRING_INDEX(SUBSTRING_INDEX(reference_no,'-',-2),'-',1) as 'unit'
FROM quotations;

#CASE
SELECT temp.*,
       CASE
          WHEN GET_YEAR = 22
        THEN 'PREVIOUS_YEAR'
        ELSE 'CURRENT_YEAR'
        END AS YEAR
FROM(
        SELECT reference_no,
           SUBSTRING_INDEX(reference_no,'-',1) CODE,
           SUBSTRING_INDEX(SUBSTRING_INDEX(reference_no,'-',2),'-',-1)  GET_YEAR,
           SUBSTRING_INDEX(SUBSTRING_INDEX(reference_no,'-',-2),'-',1) UNIT_NAME
        FROM quotations
    ) temp;

# Yearly Sum gross total as TOTAL_AMOUNT
SELECT temp.*,
       CASE
          WHEN GET_YEAR = 22
        THEN 'PREVIOUS_YEAR'
        ELSE 'CURRENT_YEAR'
        END AS YEAR
FROM(
        SELECT
           SUBSTRING_INDEX(SUBSTRING_INDEX(reference_no,'-',2),'-',-1)  GET_YEAR,
           SUM(gross_price) TOTAL_PRICE

        FROM quotations
        GROUP BY GET_YEAR
    ) temp;


# Yearly gross total as TOTAL_AMOUNT with custing
SELECT temp.*,
       CASE
          WHEN GET_YEAR = 22
        THEN 'PREVIOUS_YEAR'
        ELSE 'CURRENT_YEAR'
        END AS YEAR
FROM(
        SELECT
           SUBSTRING_INDEX(SUBSTRING_INDEX(reference_no,'-',2),'-',-1)  GET_YEAR,
           SUM(gross_price) TOTAL_PRICE,
           CAST(TOTAL_PRICE AS DECIMAL(10,2)) CUSTING_PRICE

        FROM quotations
        GROUP BY GET_YEAR, CUSTING_PRICE
    ) temp;
#Variable & Casting in SQL




