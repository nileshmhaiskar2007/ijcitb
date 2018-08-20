import os


class Article:
	""" Paper with all essentials must be stored
	class with all methods """

	def __init__(self,title,abstract,keywords,docfile):
		""" Initialize all paper attributes """

		self._id = id
		self._title = title 
		self._abstract = abstract
		self._keywords = keywords 
		self._docfile = docfile 

	def get_title(self):
		""" Return title of the paper """
		return self._title 

	def get_abstract(self):
		""" Return abstract of the paper """
		return self._abstract

	def get_keywords(self):
		""" Return keywords of the paper """
		return self._keywords 

	def get_docfile(self):
		""" Return docfile of the paper """
		return self._docfile 

	def get_bytes(self):
		""" How many bytes of space required to store paper """
		return os.path.getsize(self._docfile)# a path to file is provided



def main():
	pass


if __name__ == "__main__":
	main()
	


