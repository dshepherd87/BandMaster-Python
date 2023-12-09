class Instrument:
    def __init__(self, id, type, sub_type, key, make, model, serial):
        self.__id = id
        self.__type = type
        self.__sub_type = sub_type
        self.__key = key
        self.__make = make
        self.__model = model
        self.__serial = serial

    #String for class; if instrument has a subtype, use that. Otherwise, use the key. ex. 'Alto Saxophone' vs 'C Trumpet'
    def __str__(self):
        if self.__sub_type is None:
            return f"{self.__key} {self.__type}"
        else:
            return f"{self.__sub_type} {self.__type}"
        
    def __repr__(self):
        if self.__type is None:
            return f"{self.__key} {self.__type}"
        else:
            return f"{self.__sub_type} {self.__type}"        

    #Setter Methods

    def set_type(self, type):
        self.__type = type

    def set_sub_type(self, sub_type):
        self.__sub_type = sub_type

    def set_key(self, key):
        self.__key = key

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_serial(self, serial):
        self.__serial = serial

    #Getter methods

    def get_type(self):
        return self.__type
    
    def get_sub_type(self):
        return self.__sub_type
    
    def get_key(self):
        return self.__key
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_serial(self):
        return self.__serial
