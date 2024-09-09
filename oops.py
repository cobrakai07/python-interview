class S:
    name="Anonymus" #class attribute
    def __init__(self):
        pass
    
    def __init__(self,name,password):
        self.name=name #boject attribute
        self.__password=password #private data
        
    def __str__(self):
        return f" NAME: {self.name}";
        
    def isHuman():
        return True
    
    #Dunder Function --Operator overloading        
    def __add__(self,obj):
        return S(self.name+obj.name)
        
    # def changeClassAttribute(self):
    #     self.__class__.name="changed"
    @classmethod
    def changeClassAttribute(cls,name):
        cls.name=name
        
    @staticmethod
    def staticFunction():
        return "This is a Static function"
        
    @property
    def nameStartWithD(self):
        if(self.name[0]=="D"):
            return True
        else:
            return False
        
        
    def emptyFunction(self): # used in empty functions and classes
        pass
    
    def __privateFun():
        return "this is a private function"

s1= S("Deepak",123)
print(s1.name)
print(S.staticFunction())
print(s1.emptyFunction())
print(s1.nameStartWithD)
# print(s1.__password)
# del s1

class A:
    def __init__(self,parent):
        self.parent=parent
class B:
    def __init__(self,parent):
        self.parent=parent
class C(A,B):
    def __init__(self,parent):
        super().__init__(parent)
        
c1=C("Parent")
print(f" {c1.parent} ")