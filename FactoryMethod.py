from __future__ import annotations
from abc import ABC, abstractmethod 

class Creator (ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        #chama o factory method para criar um objeto
        product = self.factory_method()

        #Agora, use o produto
        result = f"Criado: o codigo do mesmo creator acabou de trabalhar com {product.operation()}"

        return result 
    
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()
    
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()    
    
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct1}"  

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct2}"  

def cliente_code(creator: Creator) -> None:

    print(f"Cliente: Não conheço a classe do creator, mas ainda funciona.\n"
          f"{creator.some_operation()}", end="")
    
if __name__ == "__main__":
   print ("App: Lançado com o ConcreteCreator1.")
   cliente_code(ConcreteCreator1())
   print("\n")

   print ("App: Lançado com o ConcreteCreator2.")
   cliente_code(ConcreteCreator2())



