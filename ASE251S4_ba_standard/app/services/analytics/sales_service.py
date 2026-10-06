import pandas as pd
from app.repositories.sqlserver.sales_repository import SalesRepository
from app.schemas.analytics_schema import IndicatorResponse

class SalesService:
    def __init__(self):
        self.repository = SalesRepository()

    def total_sales(self):
        result = self.repository.get_total_sales()
        return IndicatorResponse(
            indicator="sales_total",
            title="Ventas Totales",
            chart_type="card",
            data=result,
            sources=[
                "SQL Server"
            ]
        )

    def get_monthly_sales(self):
        rows = self.repository.get_sales_rows()
        df = pd.DataFrame(rows)
        
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        df['month'] = df['sale_date'].dt.to_period('M').astype(str)
        
        result = (
            df.groupby('month')['total_amount']
            .sum()
            .reset_index()
            .to_dict(orient='records')
        )
        return result

    def get_sales_by_region(self):
        # Según el paso 2, el resultado de Ventas por Región es directo de SQL sin usar Pandas (agrupado en SQL Server)
        return self.repository.get_sales_by_region()
