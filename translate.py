from googletrans import Translator
translator = Translator()
translation = translator.translate("Anh yêu em", dest='en')
print(translation.text)
#output: 'The sky is blue and I like bananas'