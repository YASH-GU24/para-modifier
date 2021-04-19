from googletrans import Translator


translator=Translator()
fo = open('output.txt', 'w')
fi = open('input.txt','r')
#str2=""

#str="The natural environment or natural world encompasses all living and non-living things occurring naturally, meaning in this case not artificial. The term is most often applied to the Earth or some parts of Earth"
#translator.translate(str,dest='ja')

text1=translator.translate(fi.read(),src= 'en',dest= 'ja')
text2=translator.translate(text1,src= 'ja',dest='ru' )
text3=translator.translate(text2,src= 'ru',dest='german')
text4=translator.translate(text3,src= 'german',dest='es')
text5=translator.translate(text4,src= 'es',dest='en')



fo.write(text5.text)
fo.close()
fi.close()
