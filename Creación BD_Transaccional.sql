-- =============================================
-- BASE TRANSACCIONAL ASIA MARKET
-- Backend Analítico
-- =============================================

CREATE DATABASE AsiaMarket_Transactional;
GO

USE AsiaMarket_Transactional;
GO


-- =============================================
-- TABLA CABECERA DE VENTAS
-- =============================================

CREATE TABLE sales
(
    sale_id VARCHAR(10) PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_id VARCHAR(10) NOT NULL,
    channel VARCHAR(30),
    region VARCHAR(30),
    payment_method VARCHAR(30),
    total_amount DECIMAL(10,2) NOT NULL
);

GO


-- =============================================
-- TABLA DETALLE DE VENTAS
-- =============================================

CREATE TABLE sales_detail
(
    detail_id INT IDENTITY(1,1) PRIMARY KEY,
    sale_id VARCHAR(10) NOT NULL,
    product_id VARCHAR(10) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2),
    subtotal DECIMAL(10,2),

    CONSTRAINT FK_sales_detail_sales
    FOREIGN KEY (sale_id)
    REFERENCES sales(sale_id)
);

GO