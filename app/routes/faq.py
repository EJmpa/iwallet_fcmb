# app/routes/faq.py
from flask import Blueprint, jsonify

faq_bp = Blueprint('faq', __name__)

# Define a dictionary of frequently asked questions
faq_data = {
    'question1': 'Answer to question 1',
    'question2': 'Answer to question 2',
    # Add more FAQ entries
}

@faq_bp.route('/faq', methods=['GET'])
def get_faq():
    # Return the list of frequently asked questions
    return jsonify({'faq': faq_data})
