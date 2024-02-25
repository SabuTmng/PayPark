from ..modelManager import PaymentSerializer


class Payment:
    def __init__(self, bill, paymentMethod, employee):
        PaymentSerializer(bill, paymentMethod, employee)