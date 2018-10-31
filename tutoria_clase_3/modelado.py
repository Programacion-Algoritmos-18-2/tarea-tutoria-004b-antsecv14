class Persona(object):
	def __init__(self):
		self.nombre = ""
		self.edad = 0
	def agregar_nombres(self,n):
		self.nombres = n
	def agregar_edad(self,n):
		self.edad = n
	def obtener_nombres(self):
		return self.nombre
	def obtener_edad(self):
		return self.edad
	def presentar_datos(self):
		c = "%s - %s" %(self.obtener_edad(),self.obtener_nombres())
		return c
class Estudiante(Persona):
	def __init__(self):

		super(Estudiante,self).__init__()
		self.nota = 0
	def presentar_datos(self):
		c = "%s - %s" %(super(Estudiante,self).presentar_datos(),self.nota)
#c = "%s - %s - %s" %(self.nombre,self.edad,self.nota)
		return c