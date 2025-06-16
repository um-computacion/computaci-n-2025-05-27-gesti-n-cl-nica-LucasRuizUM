import unittest
from datetime import datetime
from typing import List, Dict

class ErrorPacienteNoExiste(Exception):
    pass
class ErrorPacienteExistente(Exception):
    pass
class ErrorMedicoNoExiste(Exception):
    pass
class ErrorMedicoExistente(Exception):
    pass
class ErrorTurnoDuplicado(Exception):
    pass

class Paciente:
    def __init__(
            self,
            dni_paciente:str,
            nombre_paciente: str,
            fecha_nacimiento: str,
    ):
        
        self.__dni_=dni_paciente
        self.__nombre__=nombre_paciente
        self.__fecha_nacimiento__=fecha_nacimiento

    def obtener_dni(self):
        return f'El nombre del paciente es: {self.__nombre__}'
    
    def set_dni(self, dni_paciente):
        self.__dni__ = str(dni_paciente)
    
    def set_nombre(self, nombre_paciente):
        self.__nombre__ = nombre_paciente
    
    def set_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento__ = fecha_nacimiento
        
    def obtener_nombre(self):
        return f'El nombre del paciente es: {self.__nombre__}'
    
    def obtener_nacimiento(self):
        return f'La fecha de nacimiento del paciente {self.__nombre__} es: {self.__fecha_nacimiento__}'
    
    def obtener_paciente(self) -> str:
        return f"Paciente: {self.__nombre__} (DNI: {self.__dni__}) - Nacimiento: {self.__fecha_nacimiento__}"

    def __str__(self) -> str:
        return f"Paciente: {self.__nombre__} (DNI: {self.__dni__}) - Nacimiento: {self.__fecha_nacimiento__}"

class Especialidad:
    def __init__(
            self,
            tipo: str,
            dias: list[str] = None,
    ):
        self.__tipo__ = tipo
        self.__dias__ = dias if dias is not None else []
        
    def obtener_especialidad(self) -> str:
        return f"La especialidad es: {self.__tipo__}"
    
    def set_especialidad(self, especialidad):
        self.__tipo__ = especialidad
    
    def set_dias(self, dia):
        if self.__dias__ is None:
            self.__dias__ = []
        self.__dias__.append(dia)
    
    def verificar_dia(self, dia: str) -> bool:
        if not self.__dias__:
            return False
            
        for d in self.__dias__:
            if d.lower() == dia.lower():
                return True
        return False

    def __str__(self) -> str:
        if self.__dias__:
            dias_str = ", ".join(self.__dias__)
            return f"Especialidad: {self.__tipo__} - Días disponibles: {dias_str}"
        else:
            return f"Especialidad: {self.__tipo__} - Sin días asignados"

class Medico:
    def __init__(self, matricula_medico: str, nombre_medico: str, especialidad: list[Especialidad]):
        
        self.__matricula__ = matricula_medico
        self.__nombre__ = nombre_medico
        self.__especialidades__ = especialidad  # Objeto de tipo Especialidad

    def obtener_matricula(self):
        return f'La matrícula del Médico {self.__nombre__} es: {self.__matricula__}'
    
    def set_matricula(self, matricula):
        self.__matricula__ = str(matricula)
    
    def set_nombreM(self, nombre_medico):
        self.__nombre__ = nombre_medico
    
    def get_nombre(self):
        return f'El nombre del Médico es: {self.__nombre__}'
    
    def get_especialidad(self, especialidad: Especialidad):
        """Retorna información de la especialidad del médico"""
        return f'La especialidad del Médico {self.__nombre__} es: {especialidad.obtener_especialidad()}'
    
    def get_especialidad_completa(self):
        """Retorna información completa de la especialidad incluyendo días"""
        return f'El Médico {self.__nombre__} - {self.__especialidades__}'
    
    def obtener_especialidad_para_dia(self, dia, especialidad: Especialidad)-> str | None:
        for especialidad in self.__especialidades__:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self) -> str:
        return f"Dr. {self.__nombre__} - {self.__especialidades__} (Matrícula: {self.__matricula__})"

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: Especialidad):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad
    
    def obtener_medico(self) -> Medico:
        return self.__medico__
    
    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora__
    
    def __str__(self) -> str:
        fecha_formateada = self.__fecha_hora__.strftime("%d/%m/%Y %H:%M")
        return (f"Turno - Paciente: {self.__paciente__}, "
                f"Médico: {self.__medico__}, "
                f"Fecha y Hora: {fecha_formateada}, "
                f"Especialidad: {self.__especialidad__}")

class Receta:
    
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: List[str], fecha: datetime = None):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = fecha if fecha else datetime.now()
    
    def agregar_medicamentos (self, medicamento):
        self.__medicamentos__.append(medicamento)

    def __str__(self) -> str:
        fecha_str = self.__fecha__.strftime("%d/%m/%Y")
        medicamentos_str = ", ".join(self.__medicamentos__)
        return f"Receta [{fecha_str}]: {medicamentos_str} - Prescrita por {self.__medico__.__nombre__} para {self.__paciente__.__nombre__}"

class HistoriaClinica():
    def __init__(
        self,
        paciente: Paciente,
    ):
        self.__paciente__ = paciente
        self.__turnos__: List[Turno] = []
        self.__recetas__: List[Receta] = []

    def agregar_turno_a_lista(self, turno : Turno):
        self.__turnos__.append(turno)
    
    def agregar_receta_hist(self, receta : Receta):
        self.__recetas__.append(receta)
    
    def obtener_turnos(self):
        return f'Los Turnos son: {[str(turno) for turno in self.__turnos__]}'
    
    def obtener_receta(self):
        return f'Las Recetas son: {[str(receta) for receta in self.__recetas__]}'
    
    def __str__(self) -> str:
        turnos_info = f"{len(self.__turnos__)} turno(s)" if self.__turnos__ else "Sin turnos"
        recetas_info = f"{len(self.__recetas__)} receta(s)" if self.__recetas__ else "Sin recetas"
    
        return f"Historia Clínica de {self.__paciente__.__nombre__} - {turnos_info}, {recetas_info}"


