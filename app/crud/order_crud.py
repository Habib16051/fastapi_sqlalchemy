from sqlalchemy.orm import Session
from app.db.models import Order, OrderItem
from app.schemas.order import OrderCreate


def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        user_id=order.user_id,
        total_amount=order.total_amount,
        status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_item = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_purchase=item.price_at_purchase
        )
        db.add(db_item)

    db.commit()
    return db_order