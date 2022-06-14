from modelo.bd.Gestionar_Consulta import Gestionar_Consulta
from modelo.bd.Gestionar_Paciente import Gestionar_Paciente
from modelo.bd.Gestionar_Especialidad import Gestionar_Especialidad
from modelo.dominio.Consulta import Consulta

from datetime import datetime

class Menu_Principal:
	def __init__(self):
		self.ref_gestionar_consulta = Gestionar_Consulta()
		self.ref_gestionar_paciente = Gestionar_Paciente()
		self.ref_gestionar_especialidad = Gestionar_Especialidad()

		self.opciones = ['Consulta', 'Paciente', 'Especialidad']

	def menu_principal(self):
		print('*'*50)
		print('UNIVERSIDAD')
		print('*'*50)

		indice = 1
		for opcion in self.opciones:
			print('[{}].- {}'.format(indice, opcion))
			indice += 1

		print('[{}].- {}'.format(0, 'Salir'))

	def menu_opcion(self, opcion):
		opcion -= 1

		print('--Gestionar {}--'.format(self.opciones[opcion]))
		print('[1].- Registrar {}'.format(self.opciones[opcion]))
		print('[2].- Modificar {}'.format(self.opciones[opcion]))
		print('[3].- Eliminar {}'.format(self.opciones[opcion]))
		print('[4].- Buscar {}'.format(self.opciones[opcion]))

	def opcion_seleccionada(self, opcion, subopcion):
		if opcion == 1 and subopcion == 1:
			print('REGISTRAR CONSULTA')

			fecha_actual = datetime.now()
			codigo = len(self.ref_gestionar_consulta.ref_consultas) + 1
			print('Codigo: {} - Fecha Consulta: {}'.format(codigo, fecha_actual))

			cedula = input('Ingresar cedula del paciente: ')
			# Buscar al paciente
			paciente = self.ref_gestionar_paciente.listar(cedula)
			# Buscar a la especialidad
			especialidad_nombre = input('Ingresar la especialidad: ')
			especialidad = self.ref_gestionar_especialidad.listar(especialidad_nombre)

			if paciente is not None and especialidad is not None:
				valor_total = especialidad.valor

				anio_actual = fecha_actual.strftime('%Y')
				anio_actual = int(anio_actual)
				anio_nacimiento = paciente.anio_nacimiento

				if (anio_actual - anio_nacimiento) >= 65:
					valor_descuento = especialidad.valor*0.1
				else:
					valor_descuento = 0

				valor_total = especialidad.valor - valor_descuento

				objeto = Consulta(codigo, fecha_actual, valor_descuento, valor_total, paciente, especialidad)

				self.ref_gestionar_consulta.insertar(objeto)
			else:
				print('Debe ingresar el paciente o la especialidad.')

		elif opcion == 1 and subopcion == 2:
			print('MODIFICAR CONSULTA')
			self.ref_gestionar_consulta.modificar(objeto)
		elif opcion == 1 and subopcion == 3:
			print('ELIMINAR CONSULTA')
			self.ref_gestionar_consulta.eliminar(objeto)
		elif opcion == 1 and subopcion == 4:
			self.ref_gestionar_consulta.listar(None)
		elif opcion == 2 and subopcion == 1:
			pass
		elif opcion == 2 and subopcion == 2:
			pass
		elif opcion == 2 and subopcion == 3:
			pass
		elif opcion == 2 and subopcion == 4:
			pass
		elif opcion == 3 and subopcion == 1:
			pass
		elif opcion == 3 and subopcion == 2:
			pass
		elif opcion == 3 and subopcion == 3:
			pass
		elif opcion == 3 and subopcion == 4:
			pass


