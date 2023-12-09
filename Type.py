class Type:
    def __init__(self, id, type):
        self.__id = id
        self.__type = type

    def __str__(self):
        return f"{self.__type}"
    
    def __repr__(self):
         return self.__str__()       

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type
    