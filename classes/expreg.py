# operacao = + ou -
#
class Expreg:

    def __init__(self, expreg=None, operacao=None, term=None):
        self.expreg = expreg
        self.operacao = operacao
        self.term = term

    def __str__(self):
        aux = "<EXPREG> \n"

        if self.expreg:
            aux += self.expreg.__repr__()

        if self.operacao:
            aux += self.operacao + "\n"

        if self.term:
             aux += self.term.__repr__()
        
        
        aux += "</EXPREG> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def getValue(self):
        return self.term.getFactor().getNumber()