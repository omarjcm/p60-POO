#!/usr/bin/python
#-*- coding: utf-8 -*-

class Paciente:
    def __init__(self, nombre, apellido, sexo, anio_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__anio_nacimiento = anio_nacimiento

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, valor):
        self.__sexo = valor

    @property
    def anio_nacimiento(self):
        return self.__anio_nacimiento

    @anio_nacimiento.setter
    def anio_nacimiento(self, valor):
        self.__anio_nacimiento = valor