from abc import ABC, abstractmethod

class Gestionar_Objeto(ABC):
	def __init__(self):
		pass
	
	@abstractmethod
	def insertar(self, objeto):
		pass

	@abstractmethod
	def modificar(self, objeto):
		pass

	@abstractmethod
	def eliminar(self, objeto):
		pass

	@abstractmethod
	def listar(self, objeto):
		pass

