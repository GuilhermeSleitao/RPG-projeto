class Funcionario:
    def __init__ (self,nome,email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora (self, mes, horas):
        if ( mes not in self.horas) or (mes not in self.salario_hora ):
            print("mes inexistente"  )
        else: self.horas[mes]* self.salario_hora [mes]
    
    def __repr__ (self ):

        return f"funcionarios: {self.nome}, \nEmail:{self.email},horas/mes: {self.horas}, \n salario-hora:{self.salario_hora}"