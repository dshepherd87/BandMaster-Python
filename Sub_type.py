class Sub_type:
    def __init__(self, id, sub_type):
        self.__id = id
        self.__sub_type = sub_type

    def __str__(self):
        return f"sub_type"
    
    def __repr__(self):
        return self.__str__()
    
    def set_sub_type(self, sub_type):
        self.__sub_type = sub_type

    def get_sub_type(self):
        return self.__sub_type