from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database
db = SQLAlchemy()


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)

    # Load configuration from config.py
    # app.config.from_object('config.config') # This buggy and unnecessary from the original code but I wont remove it
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev_test:DevLog#1@localhost/iwallet_fcmb_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    # Initialize the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Import and register blueprints for each feature
    from .routes.loan import loan_bp
    from .routes.messaging import messaging_bp
    from .routes.feedback import feedback_bp
    from .routes.referral import referral_bp
    from .routes.location import location_bp
    from .routes.authentication import auth_bp
    from .routes.dispute import dispute_bp
    from .routes.review import review_bp
    from .routes.transaction import transaction_bp
    from .routes.chatbot import chatbot_bp
    from .routes.faq import faq_bp
    from .routes.support import support_bp
    from .routes.notifications import notifications_bp

    # Register blueprints
    app.register_blueprint(loan_bp, url_prefix='/loan')
    app.register_blueprint(messaging_bp, url_prefix='/messaging')
    app.register_blueprint(feedback_bp, url_prefix='/feedback')
    app.register_blueprint(referral_bp, url_prefix='/referral')
    app.register_blueprint(location_bp, url_prefix='/location')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dispute_bp, url_prefix='/dispute')
    app.register_blueprint(review_bp, url_prefix='/review')
    app.register_blueprint(transaction_bp, url_prefix='/transaction')
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')
    app.register_blueprint(faq_bp, url_prefix='/faq')
    app.register_blueprint(support_bp, url_prefix='/support')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')

    return app
