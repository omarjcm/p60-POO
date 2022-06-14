from controlador.Gestionar_Objeto import Gestionar_Objeto
from modelo.dominio.Especialidad import Especialidad

class Gestionar_Especialidad(Gestionar_Objeto):
	def __init__(self):
		self.ref_especialidades = [
			Especialidad('Medicina General', 30),
			Especialidad('Cardiologia', 35),
			Especialidad('Traumatologia', 50),
			Especialidad('Dermatologia', 45),
			Especialidad('Pediatria', 40)
		]

	def insertar(self, objeto):
		self.ref_especialidades.append( objeto )

	def modificar(self, objeto):
		for especialidad in self.ref_especialidades:
			if especialidad.nombre == objeto.nombre:
				especialidad.valor = objeto.valor

	def eliminar(self, objeto):
		for especialidad in self.ref_especialidades:
			if especialidad.nombre == objeto.nombre:
				self.ref_especialidades.remove(especialidad)

	def listar(self, nombre):
		for especialidad in self.ref_especialidades:
			if especialidad.nombre == nombre:
				return especialidad