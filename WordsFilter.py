def StopWords(str):
  import re
  alphabet = re.compile("[A-Za-z,-.?]+")
  strList = str.split()
  strRes = []
  for i in strList:
    if alphabet.fullmatch(i) is not None:
      strRes.append(i)
  return strRes

str1 = "Saat meng*ecat tembok, Agung dib_antu oleh Raihan"
str2 = "Berapa u(mur minimal[ untuk !mengurus ktp?"
str3 = "Masing-masing anak mendap(atkan uang jajan ya=ng be&rbeda"

str1List = StopWords(str1)
str2List = StopWords(str2)
str3List = StopWords(str3)

print(str1List, "Total Kata = ",len(str1List))
print(str2List, "Total Kata = ",len(str2List))
print(str3List, "Total Kata = ",len(str3List))