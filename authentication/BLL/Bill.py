from ..modelManager import BillSerializer


class Bill:
    def __init__(self,membership, amount, type):
        BillSerializer(membership, amount, type)