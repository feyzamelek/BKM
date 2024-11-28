programlama_diller= ["python" , "C#" , "Java", "Javascript"]

#güncelleme
#programlama_diller[2] = "c++"
#print(programlama_diller)

sonuc = len(programlama_diller)
sonuc = programlama_diller + ["Go" , "Delphi"]

sonuc = "Python" in programlama_diller
sonuc = "React" in programlama_diller           #koşul ifadeleri

del programlama_diller[0]

print(programlama_diller)
