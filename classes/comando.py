class Comando:

    def __init__(self, comando1=None, comando2=None):
        self.comando1 = comando1
        self.comando2 = comando2

    def __str__(self):
        aux = "<COMANDO> \n"

        if self.comando1:
            aux += self.comando1.__repr__()
        
        if self.comando2:
            aux += self.comando2.__repr__()

        aux += "</COMANDO> \n"
        return aux

    def __repr__(self):
        return self.__str__()