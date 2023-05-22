In this example, we have the following components:

- `PaymentStrategy` is an interface that defines the strategy contract. It
  declares the `pay` method that concrete strategies must implement.

- `CreditCardPaymentStrategy` and `PayPalPaymentStrategy` are concrete
  strategies that implement the `PaymentStrategy` interface. They provide their
  own implementations of the `pay` method specific to credit card and PayPal
  payments, respectively.

- `PaymentContext` is the context class that utilizes the selected payment
  strategy to process a payment. It takes a payment strategy object as a
  parameter in its constructor and provides the `process_payment` method to
  initiate the payment process.

In the usage example, we create instances of the concrete payment strategies:
`CreditCardPaymentStrategy` and `PayPalPaymentStrategy`. Each strategy has its
own set of parameters representing the necessary information for that payment
method (e.g., credit card details or PayPal account credentials).

Then, we create an instance of the `PaymentContext` class, passing the desired
payment strategy as an argument to the constructor. We can then use the
`process_payment` method to initiate the payment process.

In the example, we demonstrate two different payment scenarios: paying with a
credit card and paying with PayPal. We create the `PaymentContext` instance
with the corresponding payment strategy and call the `process_payment` method
with the desired payment amount.

The chosen payment strategy's `pay` method is invoked, simulating the actual
payment process. The payment amount and relevant payment information specific
to the selected strategy are printed as part of the payment confirmation
message.

The Strategy pattern allows the client code (in this case, the usage example)
to utilize different payment strategies interchangeably while decoupling the
payment processing logic from the specific payment methods. This flexibility
enables easy extension with new payment strategies and allows the client to
choose the appropriate strategy based on different requirements or preferences.

<img width="571" alt="image" src="https://github.com/jfrerich/oop-design-patterns/assets/7575921/1bf72425-27e8-4bf7-829d-d069889e193a">


```python
class PaymentStrategy:
    """Strategy interface"""

    def pay(self, amount):
        pass


class CreditCardPaymentStrategy(PaymentStrategy):
    """Concrete strategy for credit card payment"""

    def __init__(self, card_number, card_holder, expiration_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paid ${amount} with credit card {self.card_number}")


class PayPalPaymentStrategy(PaymentStrategy):
    """Concrete strategy for PayPal payment"""

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        print(f"Paid ${amount} with PayPal account {self.email}")


class PaymentContext:
    """Context class"""

    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.pay(amount)


# Usage example
credit_card_strategy = CreditCardPaymentStrategy("1234567890", "John Doe", "12/2023", "123")
paypal_strategy = PayPalPaymentStrategy("john.doe@example.com", "password123")

payment_context = PaymentContext(credit_card_strategy)
payment_context.process_payment(100.0)  # Pays $100 with credit card

payment_context = PaymentContext(paypal_strategy)
payment_context.process_payment(50.0)  # Pays $50 with PayPal
```
