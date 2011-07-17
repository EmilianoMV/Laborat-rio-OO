#coding:utf-8

import unittest
from should_dsl import should
from hospital import Paciente, Medico, Enfermeira, Hospital

class Test_paciente(unittest.TestCase):
    def test_criar_paciente(self):
        paciente4 = Paciente("Pedro","5823","51")
        paciente4.nome |should| equal_to("Pedro")
        paciente4.codigoSeguroSocial |should| equal_to("5823")
        paciente4.idade |should| equal_to ("51")
        paciente1 = Paciente("Gleicy","09876","18") 
        paciente1.nome |should| equal_to("Gleicy")
        paciente1.codigoSeguroSocial |should| equal_to("09876")
        paciente1.idade |should| equal_to("18")
        paciente2 = Paciente("Marcolino","1234","31")
        paciente2.nome |should| equal_to("Marcolino")
        paciente2.codigoSeguroSocial |should| equal_to("1234")
        paciente2.idade |should| equal_to("31")
        paciente3 = Paciente("João","56780","13")
        paciente3.nome |should| equal_to("João")
        paciente3.codigoSeguroSocial |should| equal_to("56780")
        paciente3.idade |should| equal_to("13")
        paciente1.adicionar_paciente("paciente1") 
        paciente2.adicionar_paciente("paciente2") 
        paciente3.adicionar_paciente("paciente3")  

class Test_medico(unittest.TestCase):
    def test_criar_medico(self):
        Medico.quadro_medicos = []
        medico1 = Medico("Emiliano","1234567","pediatra",["01","02","03"])
        medico1.nome |should| equal_to("Emiliano")
        medico1.matricula |should| equal_to("1234567")
        medico1.especialidade |should| equal_to("pediatra")
        medico1.vinculo |should| equal_to(["01","02","03"])
        medico2 = Medico("Lucas","987654","geriatra",["01","02","05"])
        medico2.nome |should| equal_to("Lucas")
        medico2.matricula |should| equal_to("987654")
        medico2.especialidade |should| equal_to("geriatra")
        medico2.vinculo |should| equal_to(["01","02","05"])
        medico3 = Medico("Luciano","4321","ortopedista",["05","02","06"])
        medico3.nome |should| equal_to("Luciano")
        medico3.matricula |should| equal_to("4321")
        medico3.especialidade |should| equal_to("ortopedista")
        medico3.vinculo |should| equal_to(["05","02","06"])
        Medico.quadro_medicos |should| have(3).itens #verifico se tenho 3 médicos cadastrado  na lista quadro_medicos

# Relação dos hospitais(nome, código e endereço ) que um médico ou enfermeira mantém vínculo
    def test_lista_hospitais_vinculados_medico(self):
        Hospital.quadro_hospitais = []        
        hospital1 = Hospital("Ferreira","01","Seila")
        hospital2 = Hospital("Unimed","02","Ruadoleao")
        hospital3 = Hospital("HGG","23","Guarus")
        hospital4 = Hospital("Benzocriol","03","Rua Ricks")
        medico1 = Medico("Emiliano","1234567","pediatra",["01","02","03"])
        medico1.adicionar_medico(medico1)
        medico1.lista_hospitais_vinculados_medico() |should| equal_to([("Ferreira","01","Seila"),("Unimed","02","Ruadoleao"),("Benzocriol","03","Rua Ricks")])
        
#____________________________________________________________________
# Relação dos hospitais(nome, código e endereço ) que um médico ou enfermeira mantém cínculo

    def test_lista_hospitais_vinculados_enfermeira(self):
        Hospital.quadro_hospitais = []
        hospital1 = Hospital("Ferreira","01","Seila")
        hospital2 = Hospital("Unimed","02","Ruadoleao")
        hospital3 = Hospital("HGG","23","Guarus")
        hospital4 = Hospital("Benzocriol","03","Rua Ricks")
        enfermeira1 = Enfermeira("Maria","02","Chefe",["01","02","03"])
        enfermeira1.adicionar_enfermeira(enfermeira1)  
        enfermeira1.lista_hospitais_vinculados_enfermeira() |should| equal_to([("Ferreira","01","Seila"),("Unimed","02","Ruadoleao"),("Benzocriol","03","Rua Ricks")])     

 #____________________________________________________________________
# Relação dos médicos e enfermeiras (nome, matricula) que trabalham em determinado hospital

    def test_lista_medicos_vinculado_a_um_hospital(self):
        Hospital.quadro_hospitais = []
        Medico.quadro_medicos = []
        hospital1 = Hospital("Ferreira","01","Seila")
        hospital2 = Hospital("Unimed","02","Ruadoleao")
        hospital3 = Hospital("Benzocriol","03","Rua Ricks")
        hospital4 = Hospital("ola","04","Rua Ricks")
        hospital5 = Hospital("oi","05","Rua Ricks")
        medico1 = Medico("Emiliano","1234567","pediatra",["01","02","03"])
        medico2 = Medico("Lucas","987654","geriatra",["01","02","05"])
        medico3 = Medico("Luciano","4321","ortopedista",["05","02","01"])
        hospital1.lista_medicos_vinculado_a_um_hospital() |should| equal_to([("Emiliano","1234567"),("Lucas","987654"),("Luciano","4321")])  



 #____________________________________________________________________
class Test_Enfermeira(unittest.TestCase):
    def test_criar_Enfermeira(self):
        enfermeira1 = Enfermeira("Maria","02","Chefe",["01","02","03"])
        enfermeira1.nome |should| equal_to("Maria")
        enfermeira1.matricula |should| equal_to("02")
        enfermeira1.cargo |should| equal_to("Chefe")
        enfermeira1.vinculo |should| equal_to(["01","02","03"])
        enfermeira2 = Enfermeira("Samara","03","Auxiliar",["03","01","02"])
        enfermeira2.nome |should| equal_to("Samara")
        enfermeira2.matricula |should| equal_to("03")
        enfermeira2.cargo |should| equal_to("Auxiliar")
        enfermeira2.vinculo |should| equal_to(["03","01","02"])
        enfermeira3 = Enfermeira("Luciana","04","Auxiliar",["01","02","03"])
        enfermeira3.nome |should| equal_to("Luciana")
        enfermeira3.matricula |should| equal_to("04")
        enfermeira3.cargo |should| equal_to("Auxiliar")
        enfermeira3.vinculo |should| equal_to(["01","02","03"])
      
        #não precisa tem a parametro que faz esta verificação no hostital.py que é (def adicionar_enfermeira(self,enfermeira):) esta na linha 49
        #enfermeira1.adicionar_enfermeira("enfermeira1") 
        #enfermeira2.adicionar_enfermeira("enfermeira2")
        #enfermeira3.adicionar_enfermeira("enfermeira3")

class Test_hospital(unittest.TestCase):
    def test_criar_hospital(self):
        Hospital.quadro_hospitais = []
        hospital1 = Hospital("Ferreira","01","Seila")
        hospital1.nome |should| equal_to("Ferreira")
        hospital1.codigo |should| equal_to("01")
        hospital1.endereco |should| equal_to("Seila")
        hospital2 = Hospital("Unimed","02","Ruadoleao")
        hospital2.nome |should| equal_to("Unimed")
        hospital2.codigo |should| equal_to("02")
        hospital2.endereco |should| equal_to("Ruadoleao")
        hospital3 = Hospital("HGG","03","Guarus")
        hospital3.nome |should| equal_to("HGG")
        hospital3.codigo |should| equal_to("03")
        hospital3.endereco |should| equal_to("Guarus")
        #hospital1.adicionar_enfermeira("enfermeira1") 
        Hospital.quadro_hospitais |should| have(3).itens
        

    def test_buscar_hospital(self):
        hospital1 = Hospital("Ferreira","01","Seila")
        hospital1.codigo |should| equal_to("01")
        #hospital1.buscar_hospital(01)

        # def test_buscar_hospital(self):

    def test_internar_paciente(self):
        Hospital.quadro_hospitais = []
        hospital = Hospital("Ferreira","01","Seila")
        paciente1 = Paciente("Gleicy","09876","18")
        paciente2 = Paciente("Marcolino","1234","31")
        medico1 = Medico("Emiliano","1234567","pediatra",["01","02","03"])
        hospital.internar_paciente(paciente1,medico1,"10")
        hospital.internacoes |should| equal_to ([(paciente1,medico1,"10")])

    def test_lista_internacao_pacientes_medico_periodo(self):
        Hospital.quadro_hospitais = []
        hospital = Hospital("Ferreira","01","Seila")
        paciente1 = Paciente("Gleicy","09876","18")
        paciente2 = Paciente("Marcolino","09876","18")
        medico1 = Medico("Emiliano","1234567","pediatra",["01","02","03"])
        hospital.internar_paciente(paciente1,medico1,"10")
        hospital.internar_paciente(paciente2,medico1,"15")
        hospital.lista_internacao_pacientes_medico_periodo() |should| equal_to ([ [(paciente1),(medico1),("10")] , [(paciente2),(medico1),("15")] ]) 
        
87

if __name__== "__main__":
    unittest.main()
