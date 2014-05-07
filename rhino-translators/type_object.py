#	type_object.py

class TypeObject(object):
	def __init__(self):
		pass

	@classmethod
	def test(cls, string_in):
		print 'Kilroy is here'
		return string_in

if __name__ == '__main__':
	# import doctest
	# doctest.testfile('tests/type_object_test.txt')
	out = TypeObject.test('hello')
	print 'out: %s' % out
