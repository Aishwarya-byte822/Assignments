USE DataBank;
SELECT * FROM regions;
SELECT * FROM customer_nodes;

SELECT * FROM customer_transactions;

-- A(a) How many unique nodes are there on the Data Bank system ?
SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;

/*output
unique_nodes
------------
5*/


--A(b) What is the number of nodes per region? 
SELECT region_id,
       COUNT(DISTINCT node_id) AS node_count
FROM customer_nodes
GROUP BY region_id;

/*output
region_id node_count
--------- -----------
1         5
2         5
3         5
4         5
5         5 */


--A(c) How many customers are allocated to each region?
SELECT region_id,
      COUNT(DISTINCT customer_id) AS customer_count
FROM customer_nodes
GROUP BY region_id;

/*output
region_id customer_count
--------- --------------
1         110
2         105
3         102
4         95
5         88*/


--A(d) How many days on average are customers reallocated to a different node?
WITH node_duration AS
(
    SELECT
        customer_id,
        node_id,
        start_date,
        end_date,
        DATEDIFF(day, start_date, end_date) AS days_on_node
    FROM customer_nodes
    WHERE end_date <> '9999-12-31'
)

SELECT
    AVG(days_on_node) AS avg_days
FROM node_duration;

/*output 
avg_days
-----------
14*/

--A(e) What is the median, 80th and 95th percentile for this same reallocation days metric for each region?
WITH node_duration AS
(
    SELECT
        r.region_name,
        DATEDIFF(day, cn.start_date, cn.end_date) AS days_on_node
    FROM customer_nodes cn
    JOIN regions r
        ON cn.region_id = r.region_id
    WHERE cn.end_date <> '9999-12-31'
)

SELECT DISTINCT
    region_name,

    PERCENTILE_CONT(0.50)
    WITHIN GROUP (ORDER BY days_on_node)
    OVER (PARTITION BY region_name) AS median_days,

    PERCENTILE_CONT(0.80)
    WITHIN GROUP (ORDER BY days_on_node)
    OVER (PARTITION BY region_name) AS percentile_80_days,

    PERCENTILE_CONT(0.95)
    WITHIN GROUP (ORDER BY days_on_node)
    OVER (PARTITION BY region_name) AS percentile_95_days

FROM node_duration
ORDER BY region_name;

/*output 

region_name                                        median_days            percentile_80_days     percentile_95_days
-------------------------------------------------- ---------------------- ---------------------- ----------------------
Africa                                             15                     24                     28
America                                            15                     23                     28
Asia                                               15                     23                     28
Australia                                          15                     23                     28
Europe                                             15                     24                     28 
*/



--B Customer Transactions (a) What is the unique count and total amount for each transaction type?

SELECT
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type;

/*output 
txn_type                                           transaction_count total_amount
-------------------------------------------------- ----------------- ------------
purchase                                           1617              806537
withdrawal                                         1580              793003
deposit                                            2671              1359168
*/


--B(b) What is the average total historical deposit counts and amounts for all customers?

WITH customer_deposits AS
(
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS total_deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)

SELECT
    AVG(deposit_count) AS avg_deposit_count,
    AVG(total_deposit_amount) AS avg_deposit_amount
FROM customer_deposits;

/*output
avg_deposit_count avg_deposit_amount
----------------- ------------------
5                 2718
*/


--B(c) For each month - how many Data Bank customers make more than 1 deposit and either 1 purchase or 1 withdrawal in a single month?
WITH monthly_transactions AS
(
    SELECT
        customer_id,
        MONTH(txn_date) AS month_no,

        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,

        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,

        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count

    FROM customer_transactions
    GROUP BY customer_id, MONTH(txn_date)
)

SELECT
    month_no,
    COUNT(customer_id) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month_no
ORDER BY month_no;

/*output
month_no    customer_count
----------- --------------
1           168
2           181
3           192
4           70
/*
