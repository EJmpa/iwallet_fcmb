# app/routes/loan.py
from flask import Blueprint

loan_bp = Blueprint('loan', __name__)

@loan_bp.route('/create_loan', methods=['POST'])
def create_loan():
    # Code to create a loan
    pass

@loan_bp.route('/approve_loan/<int:loan_id>', methods=['POST'])
def approve_loan(loan_id):
    # Code to approve a loan
    pass
