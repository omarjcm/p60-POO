#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime

class Consulta:
    def __init__(self, fecha_consulta, paciente, especialidad):
        self.__fecha_consulta = fecha_consulta
        self.__valor_descuento = 0.0
        self.__valor_total = 0.0
        self.ref_paciente = paciente
        self.ref_especialidad = especialidad
        self.especialidades = []

    @property
    def fecha_consulta(self):
        return self.__fecha_consulta

    @fecha_consulta.setter
    def fecha_consulta(self, valor):
        self.__fecha_consulta = datetime.strptime(valor, '%d-%m-%Y')

    @property
    def valor_descuento(self):
        return self.__valor_descuento

    @valor_descuento.setter
    def valor_descuento(self, valor):
        self.__valor_descuento = valor

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor):
        self.__valor_total = valor

    def __str__(self):
        return str(self.ref_paciente) + ' - ' + str(self.ref_especialidad)
