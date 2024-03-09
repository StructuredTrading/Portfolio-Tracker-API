from flask import Blueprint

from init import db
from models.transactions import Transaction, transactions_schema


transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


@transactions_bp.route("/")
def retrieve_all_transactions():
    stmt = db.select(Transaction)
    transactions = db.session.execute(stmt).scalars().all()
    return transactions_schema.dump(transactions)