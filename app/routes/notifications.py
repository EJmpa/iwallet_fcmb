# app/routes/notifications.py
from flask import Blueprint, jsonify, request

notifications_bp = Blueprint('notifications', __name__)

# List to store notifications for users
notifications = []

@notifications_bp.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    # Send a push notification to the user
    notification = {'user_id': user_id, 'message': message}
    notifications.append(notification)
    return jsonify({'message': 'Notification sent successfully'})

@notifications_bp.route('/get_notifications/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    # Return a list of notifications for a specific user
    user_notifications = [n for n in notifications if n['user_id'] == user_id]
    return jsonify({'notifications': user_notifications})
