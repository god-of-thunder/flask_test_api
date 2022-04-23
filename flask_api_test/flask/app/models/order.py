from app import db
import datetime
from sqlalchemy.orm import relationship


class Order(db.Model):
    order_id = db.Column(db.String(), primary_key=True)
    customer_name = db.Column(db.String())
    customer_id = db.Column(db.String())
    puechase_time = db.Column(db.DateTime,default=datetime.utcnow)
    order_item = relationship('OrderItem')


    def add(self):
        db.session.add(self)
        db.session.commit()
