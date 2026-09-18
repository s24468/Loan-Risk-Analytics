DROP VIEW IF EXISTS vw_loan_summary;

CREATE VIEW vw_loan_summary AS
SELECT
    "ID" AS loan_id,
    age AS age,
    income AS income,
    loan_amount AS loan_amount,
    "Credit_Score" AS credit_score,
    rate_of_interest AS interest_rate,
    term AS loan_term,
    dtir1 AS dti_ratio,
    "Status" AS default_status,

    CASE
        WHEN income IS NULL THEN 'Unknown'
        WHEN income < 30000 THEN 'Low Income'
        WHEN income < 75000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_category,

    CASE
        WHEN "Credit_Score" IS NULL THEN 'Unknown'
        WHEN "Credit_Score" < 580 THEN 'Very High Risk'
        WHEN "Credit_Score" < 670 THEN 'High Risk'
        WHEN "Credit_Score" < 740 THEN 'Medium Risk'
        WHEN "Credit_Score" < 800 THEN 'Low Risk'
        ELSE 'Very Low Risk'
    END AS credit_risk_group,

    CASE
        WHEN "Credit_Score" IS NULL THEN 'Unknown'
        WHEN "Credit_Score" < 580 THEN 'Below 580'
        WHEN "Credit_Score" < 670 THEN '580-669'
        WHEN "Credit_Score" < 740 THEN '670-739'
        WHEN "Credit_Score" < 800 THEN '740-799'
        ELSE '800+'
    END AS credit_score_bucket,

    CASE
        WHEN loan_amount IS NULL THEN 'Unknown'
        WHEN loan_amount < 100000 THEN 'Small Loan'
        WHEN loan_amount < 300000 THEN 'Medium Loan'
        ELSE 'Large Loan'
    END AS loan_amount_category,

    CASE
        WHEN dtir1 IS NULL THEN 'Unknown'
        WHEN dtir1 < 20 THEN 'Low DTI'
        WHEN dtir1 < 40 THEN 'Medium DTI'
        ELSE 'High DTI'
    END AS dti_category,

    CASE
        WHEN rate_of_interest IS NULL THEN 'Unknown'
        WHEN rate_of_interest < 4 THEN 'Low Rate'
        WHEN rate_of_interest < 6 THEN 'Medium Rate'
        ELSE 'High Rate'
    END AS interest_rate_category,

    CASE
        WHEN "Status" IS NULL THEN NULL
        ELSE CAST("Status" AS INTEGER)
    END AS default_flag,

    1 AS loan_count

FROM raw_loans;