# app/routes/support.py
from flask import Blueprint, jsonify, request

support_bp = Blueprint('support', __name__)

# List to store customer support tickets
support_tickets = []

@support_bp.route('/create_ticket', methods=['POST'])
def create_support_ticket():
    data = request.get_json()
    user_id = data.get('user_id')
    issue_description = data.get('issue_description')
    # Create a new support ticket
    ticket = {'user_id': user_id, 'issue_description': issue_description, 'status': 'Open'}
    support_tickets.append(ticket)
    return jsonify({'message': 'Support ticket created successfully'})

@support_bp.route('/get_tickets', methods=['GET'])
def get_support_tickets():
    # Return a list of all support tickets
    return jsonify({'tickets': support_tickets})
