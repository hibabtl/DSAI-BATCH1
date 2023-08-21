USE online_retail;
show tables;
SELECT * FROM online_retail.`online-retail`; 

# ---distribution of order values across all customers---
SELECT CustomerID,
       SUM(quantity*unitprice) AS total_order_value
FROM `online-retail`
GROUP BY CustomerID
ORDER BY total_order_value;

# ---No of unique products has each customer purchased---
SELECT customerID, COUNT(DISTINCT StockCode) AS unique_products
FROM `online-retail`
group by customerID
ORDER BY unique_products desc;


# ---customers who have only made a single purchase from the company--
Select customerID, quantity 
from  `online-retail`
where quantity = 1
group by customerID;

-- Find the most commonly purchased product pairs
SELECT a.Stockcode AS Product1,
       b.StockCode AS Product2,
       COUNT(*) AS PurchaseCount,
       a.Description, b.description
FROM `online-retail` a
JOIN `online-retail` b ON a.InvoiceNo = b.InvoiceNo AND a.stockcode<b.stockcode
GROUP BY Product1, Product2, a.Description, b.Description
ORDER BY PurchaseCount;

#####ADVANCE QUERIES####
# ----CUSTOMER SEGMENTATION BY PURCHASE FREQUENCY----
SELECT CustomerID,
       COUNT(DISTINCT InvoiceNo) AS PurchaseFrequency
FROM `online-retail`
GROUP BY CustomerID
ORDER BY PurchaseFrequency desc;

# ----AVERAGE ORDER VALUE BY COUNTRY----
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

# calculates products are often purchased together by calculating the correlation between product purchases.
SELECT a.StockCode AS Product1, b.StockCode AS Product2, COUNT(DISTINCT a.InvoiceNo) AS CoOccurrenceCount,
    COUNT(DISTINCT a.InvoiceNo) / (p1.QuantityCount * p2.QuantityCount) AS Correlation
FROM `online-retail` a
JOIN `online-retail` b ON a.InvoiceNo = b.InvoiceNo AND a.StockCode < b.StockCode
JOIN (
    SELECT StockCode, COUNT(DISTINCT InvoiceNo) AS QuantityCount
    FROM `online-retail`
    GROUP BY StockCode
) p1 ON a.StockCode = p1.StockCode
JOIN (
    SELECT StockCode, COUNT(DISTINCT InvoiceNo) AS QuantityCount
    FROM `online-retail`
    GROUP BY StockCode
) p2 ON b.StockCode = p2.StockCode
GROUP BY Product1, Product2 ORDER BY Correlation DESC

# calculates customers who haven't made a purchase in a specific period (last 6months) to assess churn.
SELECT DISTINCT
    a.CustomerID
FROM `online-retail` a
LEFT JOIN (
    SELECT DISTINCT CustomerID
    FROM `online-retail`
    WHERE InvoiceDate >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
) b ON a.CustomerID = b.CustomerID
WHERE b.CustomerID IS NULL;
