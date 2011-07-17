#coding:utf-8

class Paciente(object):
    quadro_pacientes = []
    def __init__(self,nome,codigoSeguroSocial,idade):
        self.nome = nome
        self.codigoSeguroSocial = codigoSeguroSocial
        self.idade = idade
        self.adicionar_paciente(self)

    def adicionar_paciente(self, paciente):
        Paciente.quadro_pacientes.append(paciente)



class Medico(object):
    quadro_medicos = []
    def __init__(self, nome,matricula,especialidade,vinculo):
        self.nome = nome
        self.matricula = matricula
        self.especialidade = especialidade
        self.vinculo = vinculo
        self.adicionar_medico(self)

    def adicionar_medico(self, medico):
        Medico.quadro_medicos.append(medico)

    def lista_hospitais_vinculados_medico(self):
        hospitais_vinculados_medico = []
        for codigo_hospital_vinculado in self.vinculo:
            for hospital in Hospital.quadro_hospitais:
                if hospital.codigo == codigo_hospital_vinculado:
                    dados_hospital = (hospital.nome, hospital.codigo, hospital.endereco)
                    hospitais_vinculados_medico.append(dados_hospital)
        return hospitais_vinculados_medico



class Enfermeira(object):
    quadro_enfermeiras = []   
    def __init__(self, nome,matricula,cargo,vinculo):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.vinculo = vinculo 
        self.adicionar_enfermeira(self)

    def adicionar_enfermeira(self,enfermeira):
        Enfermeira.quadro_enfermeiras.append(Enfermeira)

    def lista_hospitais_vinculados_enfermeira(self):
        hospitais_vinculados_enfermeira = []
        for codigo_hospital_vinculado in self.vinculo:
            for hospital in Hospital.quadro_hospitais:
                if hospital.codigo == codigo_hospital_vinculado:
                    dados_hospital = (hospital.nome, hospital.codigo, hospital.endereco)
                    hospitais_vinculados_enfermeira.append(dados_hospital)
        return hospitais_vinculados_enfermeira



class Hospital(object):
    quadro_hospitais = []
    def __init__(self,nome,codigo,endereco):
        self.nome = nome
        self.codigo = codigo
        self.endereco = endereco
        self.internacoes = []
        self.adicionar_hospital(self)

    def adicionar_hospital(self, hospital):
        Hospital.quadro_hospitais.append(hospital)

    def buscar_hospital(self, codigo):
        for hospital in quadro_hospitais:
            if hospital.codigo == codigo:
                Medico.quadro_medicos[hospital].nome
                Enfermeira.quadro_enfermeiras.nome

    def lista_medicos_vinculado_a_um_hospital(self):
        medicos_vinculados_a_um_hospital = []
        for medico in Medico.quadro_medicos:
            for codigo_hospital in medico.vinculo:
                if self.codigo == codigo_hospital:
                    dados_dos_medicos = (medico.nome, medico.matricula)
                    medicos_vinculados_a_um_hospital.append(dados_dos_medicos)
        return medicos_vinculados_a_um_hospital

    def internar_paciente(self,paciente,medico,periodo_internacao):
        self.internacoes.append((paciente,medico,periodo_internacao))

    def lista_internacao_pacientes_medico_periodo(self):
        lista_paciente_medico_periodo = []
        for lista_paciente in self.internacoes:
            lista = []
            for item in lista_paciente:
                lista.append((item))
            lista_paciente_medico_periodo.append(lista)
        return lista_paciente_medico_periodo


class Internacao(object):
    quadro_internacoes = []
    def __init__(self, codigo, periodo, medico, paciente, hospital):
        self.codigo = codigo
        self.periodo = periodo
        self.medico = medico
        self.paciente = paciente
        self.hospital = hospital

    def adicionar_internacoes(self, internacoes):
        Hospital.quadro_internacoes.append(internacoes)



