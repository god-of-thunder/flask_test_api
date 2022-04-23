from flask import Blueprint
from flask import request
from datetime import datetime
from app.models.order import Order
from app.models.order_item import OrderItem
order_page = Blueprint('Order', __name__)

@order_page.route('/add', methods=['POST'])
def orderData():
    if request.method == "POST":
        order_id = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        received_json = request.get_json()
        o = Order(order_id=order_id,customer_name=received_json["customer_name"],customer_id=received_json["customer_id"])
        o.add()
        i = OrderItem(order_id=order_id,product_id=received_json["product_id"],product_name=received_json["product_name"],amount=received_json["amount"],price=received_json["price"])
        i.add()
        return {"msg":"{} transction success".format(received_json["product_name"])},201


@order_page.route('/modify', methods=['PUT'])
def modifyOrderData():
    if request.method == "PUT":
        received_json = request.get_json()
        m = OrderItem.get_by_order_id_and_product_id(received_json["product_id"],received_json["order_id"])
        m.amount = received_json["amount"]
        m.update()      
        return {"msg":"modify amount : {}  success".format(received_json["amount"])},201