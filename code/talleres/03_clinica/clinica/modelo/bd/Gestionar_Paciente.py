from controlador.Gestionar_Objeto import Gestionar_Objeto
from modelo.dominio.Paciente import Paciente

class Gestionar_Paciente(Gestionar_Objeto):
	def __init__(self):
		self.ref_pacientes = [
			Paciente('0938475639', 'Pablo', 'Banderas', 'M', 1996),
			Paciente('0938345639', 'Angie', 'Santos', 'F', 2001),
			Paciente('0938475621', 'Julian', 'Tamayo', 'M', 2002),
			Paciente('0924475639', 'Marcelo', 'Bolaños', 'M', 2001),
			Paciente('0934975639', 'Samantha', 'Iglesias', 'F', 2003),
			Paciente('0938411111', 'Marco' ,'Guevara', 'M', 2003),
			Paciente('0938123639', 'Julia', 'Child', 'F', 1948),
			Paciente('0912375639', 'Luis', 'Parrales', 'M', 1950)
		]

	def insertar(self, objeto):
		self.ref_pacientes.append(objeto)

	def modificar(self, objeto):
		for paciente in self.ref_pacientes:
			if paciente.cedula == objeto.cedula:
				paciente.nombre = objeto.nombre
				paciente.apellido = objeto.apellido
				paciente.sexo = objeto.sexo
				paciente.anio_nacimiento = objeto.anio_nacimiento

	def eliminar(self, objeto):
		for paciente in self.ref_pacientes:
			if paciente.cedula == objeto.cedula:
				self.ref_pacientes.remove(paciente)

	def listar(self, cedula):
		for paciente in self.ref_pacientes:
			if paciente.cedula == cedula:
				return paciente