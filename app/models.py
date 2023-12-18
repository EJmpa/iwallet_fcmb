# app/models.py
# Import necessary modules
from app import db
from datetime import datetime


# User model for authentication
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80 collation='utf8_general_ci'), nullable=False)
    last_name = db.Column(db.String(80 collation='utf8_general_ci'), nullable=False)
    other_name = db.Column(db.String(80 collation='utf8_general_ci'))
    username = db.Column(db.String(80, collation='utf8_general_ci'), unique=True, nullable=False)
    email = db.Column(db.String(120, collation='utf8_general_ci'), unique=True, nullable=False)
    password = db.Column(db.String(120, collation='utf8_general_ci'), nullable=False)
    phone = db.Column(db.String(20, collation='utf8_general_ci'))
    address = db.Column(db.String(120, collation='utf8_general_ci'))
    balance = db.Column(db.Float, nullable=False)
    bvn = db.Column(db.String(10, collation='utf8_general_ci'))  # BVN field
    live_picture = db.Column(db.Text(collation='utf8_general_ci'))  # To remove this field for optimization
    fingerprint = db.Column(db.Text(collation='utf8_general_ci'))  # To remove this field for optimization
    loan = db.Column(db.Boolean, default=False)
    allow_transaction_notifications = db.Column(db.Boolean, default=True)
    allow_dispute_notifications = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'


# Transaction History
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Transaction {self.id} - {self.user_id}>'


# Loan model
class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    borrower = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    term = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    approved = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Loan {self.id} - {self.borrower}>'


# Lender model
class Lender(db.Model):
    __tablename__ = 'lenders'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    available_funds = db.Column(db.Float, nullable=False)
    preferred_rate = db.Column(db.Float, nullable=False)
    max_loan_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Lender {self.id} - {self.name}>'

# Dispute model
class Dispute(db.Model):
    __tablename__ = 'disputes'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<Dispute {self.id}>'
