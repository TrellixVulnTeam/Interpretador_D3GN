from util import Util

class Atribuicao:

    def __init__(self, id=None, expreg=None, string=None, explog=None):    
        self.expreg = expreg
        self.id = id
        self.string = string
        self.explog = explog     
        #self.semantico()   

    def __str__(self):
        aux = "<ATRIBUICAO> \n"

        if self.id:
            aux += self.id.__repr__()

        aux += ":= \n"

        if self.expreg:
            aux += self.expreg.__repr__()
        elif self.string:
            aux += self.string + "\n"
        else:
            aux += self.explog.__repr__()


        aux += "; \n"
        aux += "</ATRIBUICAO> \n"
        return aux

    def __repr__(self):
        return self.__str__()

    def semantico(self):        
        util = Util()

        if not util.getSimble('VAR'+self.id.getValue()):
            util.setSemanticFile('<ATRIBUICAO>A variavel ' + str(self.id.getValue()) + ' não foi previamente declarada </ATRIBUICAO>')
        else:
            if self.expreg:
                if (not isinstance(self.expreg.getValue() , self.id.getType())):
                    util.setSemanticFile('<ATRIBUICAO>A variavel ' + str(self.id.getValue()) + ' espera um valor '+util.getLabelTypes(str(self.id.getType()))+' mas o recebido foi '+util.getLabelTypes(str(type(self.expreg.getValue())))+' </ATRIBUICAO>')
            elif self.explog:
                if (not type(self.explog.getValue()) == self.id.getType()):
                    util.setSemanticFile('<ATRIBUICAO>A variavel ' + str(self.id.getValue()) + ' espera um valor '+util.getLabelTypes(str(self.id.getType()))+' mas o recebido foi '+util.getLabelTypes(str(type(self.expreg.getValue())))+' </ATRIBUICAO>')
            else:
                if (not isinstance(self.string, self.id.getType())):                                
                    util.setSemanticFile('<ATRIBUICAO>A variavel '+ str(self.id.getValue()) + ' espera um valor '+ util.getLabelTypes(str(self.id.getType()))+' mas o recebido foi ' +util.getLabelTypes(str(type(self.string)))+' </ATRIBUICAO>')