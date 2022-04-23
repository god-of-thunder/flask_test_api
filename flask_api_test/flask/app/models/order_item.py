from sqlalchemy import ForeignKey, func
from app import db

class OrderItem(db.Model):

    product_id = db.Column(db.String(), primary_key=True)
    order_id = db.Column(db.String(), ForeignKey('order.order_id'))
    product_name = db.Column(db.String(),unique=True)
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()    
        
    @staticmethod
    def get_by_order_id_and_product_id(product_id,order_id):
        return db.session.query(OrderItem).filter(
            (OrderItem.product_id == product_id)&(OrderItem.order_id == order_id)
        ).first()
