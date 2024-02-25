from ..modelManager import MemberSerializer


class Member:
    def __init__(self, email, username, password, DateOfBirth, CITIZENSHIP_NO, Address, Phone_No, E1):
        self.memberId = MemberSerializer(email, username, password, DateOfBirth, CITIZENSHIP_NO, Address, Phone_No)

    def getMemberId(self):
        return self.memberId