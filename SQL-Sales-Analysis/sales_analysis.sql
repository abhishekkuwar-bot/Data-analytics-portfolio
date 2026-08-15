-- SQL Sales & Business Analysis
CREATE TABLE sales (
 order_id VARCHAR(20) PRIMARY KEY, order_date DATE, customer_id VARCHAR(20),
 state VARCHAR(50), region VARCHAR(20), product VARCHAR(50),
 quantity INT, unit_price DECIMAL(12,2), discount DECIMAL(5,2), revenue DECIMAL(14,2)
);

-- Overall KPIs
SELECT COUNT(DISTINCT order_id) total_orders, COUNT(DISTINCT customer_id) total_customers,
SUM(quantity) total_quantity, ROUND(SUM(revenue),2) total_revenue,
ROUND(AVG(revenue),2) avg_order_value FROM sales;

-- Revenue by region
SELECT region, ROUND(SUM(revenue),2) revenue FROM sales GROUP BY region ORDER BY revenue DESC;

-- State performance
SELECT state, SUM(quantity) total_quantity, ROUND(SUM(revenue),2) revenue
FROM sales GROUP BY state ORDER BY revenue DESC;

-- Product performance
SELECT product, SUM(quantity) units_sold, ROUND(SUM(revenue),2) revenue
FROM sales GROUP BY product ORDER BY revenue DESC;

-- Monthly trend
SELECT EXTRACT(YEAR FROM order_date) year, EXTRACT(MONTH FROM order_date) month,
ROUND(SUM(revenue),2) revenue FROM sales
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY year, month;

-- Top 10 customers
SELECT customer_id, COUNT(DISTINCT order_id) orders, ROUND(SUM(revenue),2) revenue
FROM sales GROUP BY customer_id ORDER BY revenue DESC LIMIT 10;

-- Discount analysis
SELECT CASE WHEN discount=0 THEN 'No Discount' WHEN discount<=0.05 THEN 'Low'
WHEN discount<=0.08 THEN 'Medium' ELSE 'High' END discount_band,
COUNT(*) orders, ROUND(SUM(revenue),2) revenue
FROM sales GROUP BY discount_band ORDER BY revenue DESC;

-- State ranking with window function
SELECT state, ROUND(SUM(revenue),2) revenue,
DENSE_RANK() OVER (ORDER BY SUM(revenue) DESC) revenue_rank
FROM sales GROUP BY state ORDER BY revenue_rank;

-- Top product in each region
WITH x AS (
 SELECT region,product,SUM(revenue) revenue,
 ROW_NUMBER() OVER(PARTITION BY region ORDER BY SUM(revenue) DESC) rn
 FROM sales GROUP BY region,product
)
SELECT region,product,ROUND(revenue,2) revenue FROM x WHERE rn=1 ORDER BY region;
