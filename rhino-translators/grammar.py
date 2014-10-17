#	grammar.py

import rule
import shape

class Grammar(object):
	def __init__(self, initial_shapes, rules):
		try:
			if not (
				type(initial_shapes) == list and
				type(rules) == list
			):
				raise TypeError
			for item in initial_shapes:
				if not type(item) == shape.Shape:
					raise TypeError
			for item in rules:
				if not type(item) == rule.Rule:
					raise TypeError
		except TypeError:
			message = 'The arguments must be a list of shapes and a list of rules'
			print(message)
		else:
			self.initial_shapes = initial_shapes
			self.rules = rules

	@classmethod
	def new_from_drv_text_lines(cls, drv_text_lines):
		"""Receives the text lines of a derivation file:
			[str, ...]
		Returns:
			Grammar
		"""
		try:
			if not type(drv_text_lines) == list:
				raise TypeError
			for item in drv_text_lines:
				if not type(item) == str:
					raise TypeError
		except TypeError:
			message = 'The argument must be a list of strings'
			print(message)
		else:
			initial_shapes = []
			rules = []
			for text_line in drv_text_lines:
				pass
			new_grammar = Grammar(initial_shapes, rules)
			return new_grammar

	def __str__(self):
		"""Returns a string in the drv format:
			str
		"""
		string = '<string place holder>'
		return string

	def __repr__(self):
		"""Returns an (unformatted) string in the form:
			(	<initial shape>,
				[<rule>, ...]
			)
		"""
		string = '<repr place holder>'
		return string

if __name__ == '__main__':
	import doctest
	doctest.testfile('tests/grammar_test.txt')