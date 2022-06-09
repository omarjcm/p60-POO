#!/usr/bin/python
#-*- coding: utf-8 -*-

class Consulta:
	def __init__(self, fecha_consulta, valor_descuento, valor_total):
		self.__fecha_consulta = fecha_consulta
		self.__valor_descuento = valor_descuento
		self.__valor_total = valor_total
		self.ref_paciente = None
		self.ref_especialidad = None

