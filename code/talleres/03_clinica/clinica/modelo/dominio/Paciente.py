#!/usr/bin/python
#-*- coding: utf-8 -*-

class Paciente:
	def __init__(self, cedula, nombre, apellido, sexo, anio_nacimiento):
		self.__cedula = cedula
		self.__nombre = nombre
		self.__apellido = apellido
		self.__sexo = sexo
		self.__anio_nacimiento = anio_nacimiento