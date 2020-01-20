class User(UserMixin):

    def to_dict(self):
        data = {'name': 'fillmore'}

        return data

    # def from_dict(self, data):
    #     for field in ['username', 'email', 'about_me']:
    #         if field in data:
    #             setattr(self, field, data[field])
    #     if new_user and 'password' in data:
    #         self.set_password(data['password'])
