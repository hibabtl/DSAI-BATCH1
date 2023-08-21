USE online_retail;
show tables;
SELECT * FROM online_retail.`online-retail`; 
SELECT CustomerID,
       SUM(quantity*unitprice) AS total_order_value
FROM `online-retail`
GROUP BY CustomerID
ORDER BY total_order_value;

SELECT customerID, COUNT(DISTINCT StockCode) AS unique_products
FROM `online-retail`
group by customerID
ORDER BY unique_products desc;


-- Find the most commonly purchased product pairs
SELECT a.Stockcode AS Product1,
       b.StockCode AS Product2,
       COUNT(*) AS PurchaseCount,
       a.Description, b.description
FROM `online-retail` a
JOIN `online-retail` b ON a.InvoiceNo = b.InvoiceNo AND a.stockcode<b.stockcode
GROUP BY Product1, Product2, a.Description, b.Description
ORDER BY PurchaseCount DESC


Select customerID, quantity 
from  `online-retail`
where quantity = 1
group by customerID;

#####ADVANCE QUERIES####
# ----CUSTOMER SEGMENTATION BY PURCHASE FREQUENCY----
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS PurchaseFrequency
FROM `online-retail`
GROUP BY CustomerID
ORDER BY PurchaseFrequency desc;

# ----AVERAGE ORDER VALUE BY COUNTRY----
SELECT customerID, AVG (quantity*unitprice) AS average_order_value_by_country,country
from `online-retail`
group by country,customerID
order by  average_order_value_by_country;

SELECT
    country,
    AVG(total_order_value) AS average_order_value_by_country
FROM (
    SELECT
        country,
        SUM(quantity * unitprice) AS total_order_value
    FROM `online-retail`
    GROUP BY country, InvoiceNo
) subquery
GROUP BY country
ORDER BY average_order_value_by_country DESC;
