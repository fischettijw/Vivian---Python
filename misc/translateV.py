#  pip install googletrans
#  pip install googletrans==4.0.0rc1
#  pip show googletrans
#  https://py-googletrans.readthedocs.io/en/latest/
#  https://zetcode.com/python/googletrans/

from googletrans import Translator

translator = Translator()
input = "Hello, my name is Vivian."
print("INPUT:", input)
# print(translator.detect(input))
output = translator.translate(input, src="en", dest="es")
print("OUTPUT: ", output.text)
print()

translator = Translator()
input = "Hola, mi nombre es Vivian."
print("INPUT:", input)
# print(translator.detect(input))
output = translator.translate(input, src="es", dest="en")
print("OUTPUT: ", output.text)
print()
