from controlador.Gestionar_Objeto import Gestionar_Objeto

class Gestionar_Consulta(Gestionar_Objeto):
	def __init__(self):
		self.ref_consultas = []

	def insertar(self, objeto):
		self.ref_consultas.append( objeto )

	def modificar(self, objeto):
		for consulta in self.ref_consultas:
			if consulta.codigo == objeto.codigo:
				consulta.fecha_consulta = objeto.fecha_consulta
				consulta.valor_total = objeto.valor_total
				consulta.valor_descuento = objeto.valor_descuento
				consulta.ref_paciente = objeto.ref_paciente
				consulta.ref_especialidad = objeto.ref_especialidad

	def eliminar(self, objeto):
		for consulta in self.ref_consultas:
			if consulta.codigo == objeto.codigo:
				self.ref_consultas.remove(consulta)

	def listar(self, objeto):
		if objeto is None:
			for consulta in self.ref_consultas:
				print(consulta)
		else:
			for consulta in self.ref_consultas:
				if consulta.codigo == objeto.codigo:
					return consulta

