from flask import Blueprint

from init import db
from models.transactions import Transaction, transactions_schema, transaction_schema


transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")


@transactions_bp.route("/")
def retrieve_all_transactions():
    stmt = db.select(Transaction)
    transactions = db.session.execute(stmt).scalars().all()
    return transactions_schema.dump(transactions)


@transactions_bp.route("/search/<int:transaction_id>")
def search_transactions_by_id(transaction_id):
    stmt = db.select(Transaction).filter_by(transactionID=transaction_id)
    transaction = db.session.execute(stmt).scalars().all()
    return transactions_schema.dump(transaction)