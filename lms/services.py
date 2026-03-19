import stripe
from django.conf import settings
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_payment(course, user=None):
    """Создаёт продукт, цену и сессию в Stripe и сохраняет платёж"""
    product = stripe.Product.create(
        name=course.name,
        description=course.description,
    )

    price = stripe.Price.create(
        unit_amount=course.price * 100,
        currency='rub',
        product=product.id,
    )

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price.id,
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )

    payment = Payment.objects.create(
        user=user,
        course=course,
        stripe_product_id=product.id,
        stripe_price_id=price.id,
        stripe_session_id=session.id,
        payment_url=session.url,
        status='created'
    )

    return payment