# An insurance company analyzes the risk for an  individual applicant User before issuing the policy, Depending  on the risk the insured amount  for the user is different. You are
# provided with the user id, type of insurance and the risk for a user. Calculate the amount insured for every user based on the insurance type and risk.
# Monthly premiums paid by users are:
#  $100 for Term Life and Whole Life
#  $400 for Health
#  $500 for Endowment

# Term Life and Whole Life -  10%, 8.5% and 7% of the total amount collected in a year  for Low, Medium and High risk users respectively
# Health   2%, 1.5% and 1% of the total amount collected in a year for Low, Medium and High risk users respectively
# Endowment - 15%, 12% and 10% of the total amount collected in a year for Low, Medium and High risk users respectively

# ------------------------- Solution -------------------------------------------------------------

# If a user takes the TermLife package and the risk is Low Then he should pay ($100*10)/$100 = 10$.
# Then in a year, he should pay 10$*12 = $120 to the insurance company.

# Sql Query for that.

`    SELECT temp.*,
        CASE
            WHEN insurance_type = "TERMLIFE" AND risk= "LOW" THEN ROUND((100 * 10 / (100))*12, 2)
            WHEN insurance_type = "TERMLIFE" AND risk= "MEDIUM" THEN ROUND((8.5 * 100.0 / (100))*12, 2)
            WHEN insurance_type = "TERMLIFE" AND risk= "HIGH" THEN ROUND((7 * 100.0 / (100))*12, 2)

            WHEN insurance_type = "HEALTH" AND risk= "LOW" THEN ROUND((2 * 400.0 / (100))*12, 2)
            WHEN insurance_type = "HEALTH" AND risk= "MEDIUM" THEN ROUND((1.5 * 400.0 / (100))*12, 2)
            WHEN insurance_type = "HEALTH" AND risk= "HIGH" THEN ROUND((1 * 400.0 / (100))*12, 2)

            WHEN insurance_type = "ENDOWMENT" AND risk= "LOW" THEN ROUND((15 * 500.0 / (100))*12, 2)
            WHEN insurance_type = "ENDOWMENT" AND risk= "MEDIUM" THEN ROUND((12 * 500.0 / (100))*12, 2)
            WHEN insurance_type = "ENDOWMENT" AND risk= "HIGH" THEN ROUND((10 * 500.0 / (100))*12, 2)
            ELSE 0
        END AS amount
    FROM(
        SELECT user_id, insurance_type,risk
        FROM users
        ORDER BY user_id ASC
    ) temp;`

# Suppose a user have multiple insurance, calculate the sum of insured amount of every users.

    WITH insurance_user_tb AS (
            SELECT temp.*,
            CASE
                WHEN insurance_type = "TERMLIFE" AND risk= "LOW" THEN ROUND((100 * 10 / (100))*12, 2)
                WHEN insurance_type = "TERMLIFE" AND risk= "MEDIUM" THEN ROUND((8.5 * 100.0 / (100))*12, 2)
                WHEN insurance_type = "TERMLIFE" AND risk= "HIGH" THEN ROUND((7 * 100.0 / (100))*12, 2)

                WHEN insurance_type = "HEALTH" AND risk= "LOW" THEN ROUND((2 * 400.0 / (100))*12, 2)
                WHEN insurance_type = "HEALTH" AND risk= "MEDIUM" THEN ROUND((1.5 * 400.0 / (100))*12, 2)
                WHEN insurance_type = "HEALTH" AND risk= "HIGH" THEN ROUND((1 * 400.0 / (100))*12, 2)

                WHEN insurance_type = "ENDOWMENT" AND risk= "LOW" THEN ROUND((15 * 500.0 / (100))*12, 2)
                WHEN insurance_type = "ENDOWMENT" AND risk= "MEDIUM" THEN ROUND((12 * 500.0 / (100))*12, 2)
                WHEN insurance_type = "ENDOWMENT" AND risk= "HIGH" THEN ROUND((10 * 500.0 / (100))*12, 2)
                ELSE 0
            END AS amount
        FROM(
            SELECT user_id, insurance_type,risk
            FROM users
            ORDER BY user_id ASC
        ) temp
        )
    select insurance_user_tb.user_id as usersId,
        SUM(insurance_user_tb.amount) as totalAmount
    FROM insurance_user_tb
    GROUP BY usersId
    ORDER BY totalAmount ASC