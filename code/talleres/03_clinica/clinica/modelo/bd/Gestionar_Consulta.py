from controlador.Gestionar_Objeto import Gestionar_Objeto
from modelo.bd.Gestionar_Especialidad import Gestionar_Especialidad

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

	def reporte_total_consultas(self):
		valor_total = 0.0
		for consulta in self.ref_consultas:
			valor_total += consulta.valor_total
		
		print('El valor total recaudado en consultas: ${}'.format(valor_total))

	def reporte_total_x_sexo(self):
		total_h = 0
		total_m = 0

		for consulta in self.ref_consultas:
			if consulta.ref_paciente.sexo == 'M':
				total_h += 1

			if  consulta.ref_paciente.sexo == 'F':
				total_m += 1

		print('El total de mujeres consultadas son: {}'.format(total_m))
		print('El total de varones consultados son: {}'.format(total_h))

	def reporte_cantidad_x_especialidad(self):
		gestionar_especialidades = Gestionar_Especialidad()
		especialidades = gestionar_especialidades.ref_especialidades

		frecuencias = []
		for especialidad in especialidades:
			frecuencias.append( 0 )

		for consulta in self.ref_consultas:
			if consulta.ref_especialidad.nombre == especialidades[0]:
				frecuencias[0] += 1
			if consulta.ref_especialidad.nombre == especialidades[1]:
				frecuencias[1] += 1
			if consulta.ref_especialidad.nombre == especialidades[2]:
				frecuencias[2] += 1
			if consulta.ref_especialidad.nombre == especialidades[3]:
				frecuencias[3] += 1
			if consulta.ref_especialidad.nombre == especialidades[4]:
				frecuencias[4] += 1

		indice = 0
		for especialidad in especialidades:
			print('Especialidad: {} - frecuencia: {}'.format(especialidad, frecuencias[indice]))
			indice += 1

	def reporte_recaudado_x_especialidad(self):
		gestionar_especialidades = Gestionar_Especialidad()
		especialidades = gestionar_especialidades.ref_especialidades

		recaudado = []
		for especialidad in especialidades:
			recaudado.append( 0.0 )

		for consulta in self.ref_consultas:
			if consulta.ref_especialidad.nombre == especialidades[0]:
				recaudado[0] += consulta.valor_total
			if consulta.ref_especialidad.nombre == especialidades[1]:
				recaudado[1] += consulta.valor_total
			if consulta.ref_especialidad.nombre == especialidades[2]:
				recaudado[2] += consulta.valor_total
			if consulta.ref_especialidad.nombre == especialidades[3]:
				recaudado[3] += consulta.valor_total
			if consulta.ref_especialidad.nombre == especialidades[4]:
				recaudado[4] += consulta.valor_total

		indice = 0
		for especialidad in especialidades:
			print('Especialidad: {} - Valor recaudado: ${}'.format(especialidad, recaudado[indice]))
			indice += 1

	def reporte_descuentos_realizados(self):
		pass

	def reportes(self):
		self.reporte_descuentos_realizados()
		self.reporte_total_consultas()
		self.reporte_total_x_sexo()
		self.reporte_cantidad_x_especialidad()
		self.reporte_recaudado_x_especialidad()