import datetime,time

class matricula(object):
    def __inti__(self):
        self._aluno = None
        self.disciplina = None
        self._data_matricula = None
        self._data_confirmacao=None
        self._data_cancelamento = None

    def altera_aluno(self,aluno):
        self._aluno=aluno
        return True
 
    def altera_disciplina(self,disciplina):
        self._disciplina = disciplina
        return True
       
    def data_confirmacao(self):
        self._data_confirmacao = datetime.datetime.now()
        return self._data_confirmacao
		
    def data_cancelamento(self):
        self._data_cancelamento=datetime.datetime.now()
        return self._data_cancelamento
    
    





