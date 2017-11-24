from matricula import matricula

class aluno(object):
    def __init__(self):
        self._sigla_curso = None
        self._matriculas = None
		
    def disciplinas_alunos(self,lista,disciplina,aluno):
        lista.append(disciplina)
        lista.append(aluno)
        return lista
    
    def getSigla(self,sigla):
        self._sigla_curso = sigla
        
    def matricular(self,matricula,lista_matricula):
        lista_matricula.append(matricula)
        return True

    def confirmar_matricula(self,matricula,lista_matricula,disp,lista_disp):
        if disp in lista_matricula:
            return False
        else:
            lista_disp.append(disp)
            if matricula in lista_matricula:
                matricula.data_de_canfirmacao(self)
                return matricula.data_de_canfirmacao(self)
        
    def cancelar_matricula(self,matricula,lista_matricula):
        if matricula in lista_matricula:
            
            matricula.data_de_cancelamento(self)
            
            return matricula.data_de_cancelamento(self)

        





