from flask import Blueprint, jsonify
from app.services.analytics.sales_service import SalesService

sales_bp = Blueprint(
    "sales",
    __name__
)

service = SalesService()

@sales_bp.route(
    "/analytics/sql/sales-total",
    methods=["GET"]
)
def sales_total():
    result = service.total_sales()
    return jsonify(
        result.__dict__
    )

@sales_bp.route(
    "/analytics/pandas/monthly-sales",
    methods=["GET"]
)
def monthly_sales():
    result = service.get_monthly_sales()
    return jsonify(result)

@sales_bp.route(
    "/analytics/sql/sales-by-region",
    methods=["GET"]
)
def sales_by_region():
    result = service.get_sales_by_region()
    return jsonify(result)
