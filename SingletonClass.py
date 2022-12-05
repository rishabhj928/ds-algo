
class SingletonClass:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("creating object")
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance

s1 = SingletonClass()
print(s1)

s2 = SingletonClass()
print(s2)
