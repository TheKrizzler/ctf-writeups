import base64

flag = "yljIyRÅAÆåÅgUrDgUrfZÆWÅPUWFICåøåzOpgyåfØBtjAyRP="  
customChars = "hqOVkntvaFdUæzEDXHiSøfWrKyÆQCBMbuIYwsglJoAeNZÅØmcjGxPpåRTLçéû295"  
base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"  

substitutedFlag = ""
for i in flag:
  for j in range(len(customChars)):
    if i == customChars[j]:
      substitutedFlag += base64Chars[j]
      break
    elif i == "=":
      substitutedFlag += i
      break

print(base64.b64decode(substitutedFlag).decode('charmap'))