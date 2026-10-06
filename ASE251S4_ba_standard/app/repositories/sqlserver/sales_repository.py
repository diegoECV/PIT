from app.database.sqlserver import get_sqlserver_connection

class SalesRepository:
    def get_total_sales(self):
        connection = get_sqlserver_connection()
        cursor = connection.cursor()
        query = """
        SELECT
            SUM(total_amount)
        FROM sales
        """
        cursor.execute(query)
        result = cursor.fetchone()
        connection.close()
        return result[0]

    def get_sales_rows(self):
        conn = get_sqlserver_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT sale_date, customer_id, region,
                   payment_method, total_amount
            FROM sales
        """)
        columns = [c[0] for c in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return rows

    def get_sales_by_region(self):
        conn = get_sqlserver_connection()
        cursor = conn.cursor()
        query = """
        SELECT
            region,
            SUM(total_amount) AS sales
        FROM sales
        GROUP BY region;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        result = [{"region": row[0], "sales": float(row[1])} for row in rows]
        conn.close()
        return result
