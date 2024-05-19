from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                'id': self._generateId(),
                'first_name': 'john',
                'last_name': last_name,
                'age': '33',
                'lucky_numbers': [7, 13, 22]
            },
            {
                'id': self._generateId(),
                'first_name': 'jane',
                'last_name': last_name,
                'age': '35',
                'lucky_numbers': [10, 14, 3]
            },
            {
                'id': self._generateId(),
                'first_name': 'Jimmy ',
                'last_name': last_name,
                'age': '5',
                'lucky_numbers': [1]
            },
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for i, member in enumerate(self._members):
            if member["id"] == id:
                deleted_member = self._members.pop(i)
                return deleted_member
        return None

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
