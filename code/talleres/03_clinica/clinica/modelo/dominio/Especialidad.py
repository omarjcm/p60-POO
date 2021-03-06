#!/usr/bin/python
#-*- coding: utf-8 -*-

class Especialidad:
	def __init__(self, nombre, valor):
		self.__nombre = nombre
		self.__valor = valor

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, nuevo_valor):
		self.__nombre = nuevo_valor

	@property
	def valor(self):
		return self.__valor

	@valor.setter
	def valor(self, nuevo_valor):
		self.__valor = nuevo_valor

	def __str__(self):
		return '{}. Valor: ${}.'.format(self.nombre, self.valor)
