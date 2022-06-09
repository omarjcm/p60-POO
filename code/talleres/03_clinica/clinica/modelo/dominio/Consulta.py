class Consulta:
	def __init__(self, fecha_consulta, valor_descuento, valor_total):
		self.__fecha_consulta = fecha_consulta
		self.__valor_descuento = valor_descuento
		self.__valor_total = valor_total
		self.ref_paciente = None
		self.ref_especialidad = None

	@property
	def fecha_consulta(self):
		return self.__fecha_consulta

	@fecha_consulta.setter
	def fecha_consulta(self, nuevo_valor):
		self.__fecha_consulta = nuevo_valor

	@property
	def valor_descuento(self):
		return self.__valor_descuento

	@valor_descuento.setter
	def valor_descuento(self, nuevo_valor):
		self.__valor_descuento = nuevo_valor

	@property
	def valor_total(self):
		return self.__valor_total

	@valor_total.setter
	def valor_total(self, nuevo_valor):
		self.__valor_total = nuevo_valor