#!/usr/bin/python
#-*- coding: utf-8 -*-

class Paciente:
	def __init__(self, cedula, nombre, apellido, sexo, anio_nacimiento):
		self.__cedula = cedula
		self.__nombre = nombre
		self.__apellido = apellido
		self.__sexo = sexo
		self.__anio_nacimiento = anio_nacimiento

	@property
	def cedula(self):
		return self.__cedula

	@cedula.setter
	def cedula(self, nuevo_valor):
		self.__cedula = nuevo_valor

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, nuevo_valor):
		self.__nombre = nuevo_valor

	@property
	def apellido(self):
		return self.__apellido

	@apellido.setter
	def apellido(self, nuevo_valor):
		self.__apellido = nuevo_valor

	@property
	def sexo(self):
		return self.__sexo

	@sexo.setter
	def sexo(self, nuevo_valor):
		self.__sexo = nuevo_valor

	@property
	def anio_nacimiento(self):
		return self.__anio_nacimiento

	@anio_nacimiento.setter
	def anio_nacimiento(self, nuevo_valor):
		self.__anio_nacimiento = nuevo_valor
