# app/models.py
# Import necessary modules
from app import db

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80, collation='utf8_general_ci'), unique=True, nullable=False)
    password = db.Column(db.String(120, collation='utf8_general_ci'), nullable=False)
    bvn = db.Column(db.String(10, collation='utf8_general_ci'))  # BVN field
    live_picture = db.Column(db.Text(collation='utf8_general_ci'))  # Store as TEXT
    fingerprint = db.Column(db.Text(collation='utf8_general_ci'))  # Stor
    email = db.Column(db.String(120, collation='utf8_general_ci'), unique=True, nullable=False)
    allow_transaction_notifications = db.Column(db.Boolean, default=True)
    allow_dispute_notifications = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Loan model
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    term = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Float, nullable=False)
    approved = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Loan {self.id} - {self.borrower}>'

# Lender model
class Lender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    available_funds = db.Column(db.Float, nullable=False)
    preferred_rate = db.Column(db.Float, nullable=False)
    max_loan_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Lender {self.id} - {self.name}>'

# Dispute model
class Dispute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<Dispute {self.id} - {self.user_id}>'
