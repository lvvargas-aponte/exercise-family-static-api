
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:
    def __init__(self,last_name):
        self.last_name = last_name
  
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_number": [7,13,22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_number": [10,14,3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_number": 1
        }]



    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        
        if "id" in member:
            print(member["first_name"]+ str(member["id"]))
        else:
            member_id = self._generateId()
            member["id"] = member_id
        
        self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        self._members = [member for member in self._members if member["id"] != id]
        pass

    def get_member(self, id):
        # fill this method and update the return
        for member in self.get_all_members():
            
            if member["id"] == id:
                return {
                    "first_name": member["first_name"],
                    "id": int(id),
                    "age": int(member["age"]),
                    "lucky_numbers": member["lucky_number"]
                    }
            print("get_member func member:")
            print(member)
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
