class Consulta:
	def __init__(self, codigo, fecha_consulta, valor_descuento, valor_total, paciente, especialidad):
		self.__codigo = codigo
		self.__fecha_consulta = fecha_consulta
		self.__valor_descuento = valor_descuento
		self.__valor_total = valor_total
		self.ref_paciente = paciente
		self.ref_especialidad = especialidad

	@property
	def codigo(self):
		return self.__codigo

	@codigo.setter
	def codigo(self, nuevo_valor):
		self.__codigo = nuevo_valor

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

	def __str__(self):
		return 'Codigo: {}. Fecha de consulta: {}. Valor a Pagar: ${} (Descuento: ${}).\nPaciente: {}, Especialidad: {}'.format(
			self.codigo, self.fecha_consulta, self.valor_total, self.valor_descuento, self.ref_paciente, self.ref_especialidad
		)
