from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
db = SQLAlchemy()
from app.models.order import Order
from app.models.order_item import OrderItem
app = Flask(__name__)
api = Api(app)
# app.config['DEBUG'] = True
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
from .blueprints.example import api_page as api_blueprint
from .blueprints.order import order_page as order_blueprint
app.register_blueprint(api_blueprint, url_prefix='/example')
app.register_blueprint(order_blueprint, url_prefix='/order')
