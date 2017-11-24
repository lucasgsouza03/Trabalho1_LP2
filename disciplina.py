class disciplina(object):
    def __init(self):
        self._nome = None
        self._carga = None
        self._teoria = None
        self._pratica = None
        self._ementa = None
        self._competencias = None
        self._conteudo = None
        self._bibliografia_basica = None
        self._bibliografia_complementar = None

    def get_nome(self):
        return self._nome
     
    def altera_nome(self,nome):
        self._nome=nome
    
	def get_carga(self):
        return self._carga
    
	def Altera_carga(self,carga):
        try:
            if carga <= 0 :
                return False
            else:
                self._carga=carga
                return True
        except Exception as e:
            return print(e)
    
	def get_teoria(self):
         return self._teoria

    def altera_teoria(self,teoria):
        try:
            if teoria <= 0 :
                return False
            else:
                self._teoria=teoria
                return True
        except Exception as e:
            return print(e)
       
    def get_pratica(self):
        return self._pratica
        
    def altera_pratica(self,pratica):
        try:
            if pratica <= 0 :
                return False
            else:
                self._pratica=pratica
                return True
        except Exception as e:
            return print(e)

    def get_ementa(self):
        return self._ementa
    
    def set_ementa(self,ementa):
        self._ementa=ementa

    def altera_ementa(self,novo_ementa):
        self._ementa=novo_ementa
        
    def get_competencias(self):
        return self._competencias
    
    def set_competencias(self,competencias):
        self._competencias=competencias

    def altera_competencias(self,novo_competencias):
        self._competencias=novo_competencias
        
    def get_habilidades(self):
        return self._habilidades
    
    def set_habilidades(self,habilidades):
        self._habilidades=habilidades

    def altera_habilidades(self,novo_habilidades):
        self._habilidades=novo_habilidades
        
    def get_conteudo(self):
        return self._conteudo
    
    def set_conteudo(self,conteudo):
        self._conteudo=conteudo

    def altera_conteudo(self,novo_conteudo):
        self._conteudo=novo_conteudo
       
    def get_bibliografia_basica(self):
        return self._bibliografia_basica
    
    def set_bibliografia_basica(self,bibliografia_basica):
        self._bibliografia_basica=bibliografia_basica

    def altera_bibliografia_basica(self,novo_bibliografia_basica):
        self._bibliografia_basica=novo_bibliografia_basica
        
    def get_bibliografia_complementar(self):
        return self._bibliografia_complementar
    
    def set_bibliografia_complementar(self,bibliografia_complementar):
        self._bibliografia_complementar=bibliografia_complementar

    def altera_bibliografia_complementar(self,novo_bibliografia_complementar):
        self._bibliografia_complementar=novo_bibliografia_complementar
    
        



     
