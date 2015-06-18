class ClassMethod(object):
	class_name = cls.__name__

	def __init__(self):
		pass

	def do(self):
		print("%s: %s" % ("class_name", class_name))

class_method = ClassMethod()
class_name.do()
