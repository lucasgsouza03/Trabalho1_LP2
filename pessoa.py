class pessoa(object):
    def __init(self):
        self._nome=None
        self._email=None
        self._celular=None
        
    def retorna_nome(self):
        return self._nome
    
    def retorna_email(self):
        return self._email
    
    def retorna_celular(self):
        return self._celular
      
    def alterar_nome(self,nome):
        self._nome=nome
        return True
		
    def alterar_celular(self,celular):
        self._celular=celular
        return True
		
    def alterar_email(self,email):
        self._email=email
        return True
