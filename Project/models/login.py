# class naming is wrong . Update it to something sensible 
class MongoData:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def to_dict(self):
        return {
            'username': self.field1,
            'password': self.field2,
        }
        
        # use camelCase 
