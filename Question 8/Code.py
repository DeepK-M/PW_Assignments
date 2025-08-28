# Fitness Club Management System using OOPs

class Member:
    def __init__(self, member_id, name, age, membership_type):
        self.__member_id = member_id       # Encapsulated (Private)
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.membership_status = "Active"

    # Getter for private attribute
    def get_member_id(self):
        return self.__member_id

    # Register a new member
    def register(self):
        print(f"Member {self.name} (ID: {self.__member_id}) has been registered with {self.membership_type} membership.")

    # Renew membership
    def renew_membership(self):
        if self.membership_status == "Cancelled":
            print(f"Cannot renew. Membership for {self.name} (ID: {self.__member_id}) is cancelled.")
        else:
            self.membership_status = "Active"
            print(f"Membership for {self.name} (ID: {self.__member_id}) has been renewed.")

    # Cancel membership
    def cancel_membership(self):
        self.membership_status = "Cancelled"
        print(f"Membership for {self.name} (ID: {self.__member_id}) has been cancelled.")


# Inherited class for Family Member
class FamilyMember(Member):
    def __init__(self, member_id, name, age, membership_type, family_size):
        super().__init__(member_id, name, age, membership_type)
        self.family_size = family_size

    def family_details(self):
        print(f"Family Member {self.name} (ID: {self.get_member_id()}) has a family package covering {self.family_size} members.")


# Inherited class for Individual Member
class IndividualMember(Member):
    def __init__(self, member_id, name, age, membership_type, personal_trainer=False):
        super().__init__(member_id, name, age, membership_type)
        self.personal_trainer = personal_trainer

    def individual_details(self):
        trainer_info = "with Personal Trainer" if self.personal_trainer else "without Personal Trainer"
        print(f"Individual Member {self.name} (ID: {self.get_member_id()}) has membership {trainer_info}.")


# --------- Example Usage ---------
if __name__ == "__main__":
    # Creating members
    family_member1 = FamilyMember(101, "Amar", 35, "Family Plan", family_size=4)
    individual_member1 = IndividualMember(201, "Bulbul", 28, "Gold", personal_trainer=True)

    # Register members
    family_member1.register()
    individual_member1.register()

    # Show details
    family_member1.family_details()
    individual_member1.individual_details()

    # Membership operations
    family_member1.renew_membership()
    individual_member1.cancel_membership()
    individual_member1.renew_membership()




#Sample Output:
# Member Amar (ID: 101) has been registered with Family Plan membership.
# Member Bulbul (ID: 201) has been registered with Gold membership.
# Family Member Amar (ID: 101) has a family package covering 4 members.
# Individual Member Bulbul (ID: 201) has membership with Personal Trainer.
# Membership for Amar (ID: 101) has been renewed.
# Membership for Bulbul (ID: 201) has been cancelled.
# Cannot renew. Membership for Bulbul (ID: 201) is cancelled.