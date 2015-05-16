def cat_dog(str):
  c = 0 
  d = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "cat":
      c = c + 1
    if str[i:i+3] == "dog":
      d += 1
  if d == c: 
    return True
  else:
    return False

cat_dog("catxxdogxxxdog")

