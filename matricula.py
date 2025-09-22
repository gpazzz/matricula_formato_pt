matricula_int = "31ggxa"
matricula_med = ""
matricula_final = ""
valido = True

#Passar a matricula introduzida para apenas letras maiuculas e numeros
for i in range(len(matricula_int)):
    if matricula_int[i].isalpha():
      matricula_med += matricula_int[i].upper()
    elif matricula_int[i].isdigit():
      matricula_med += matricula_int[i]

#validar o formato da matricula
if len(matricula_med) != 6:
  valido = False
else:
  for i in range(0,len(matricula_med),2):
    bloco = matricula_med[i:i+2]

    if len(bloco) < 2:
      valido = False
      break
    elif bloco[0].isalpha() and bloco[1].isalpha():
      pass
    elif bloco[0].isdigit() and bloco[1].isdigit():
      pass
    else:
      valido = False
      break


#Formato matricula e output se for válido
if valido:
  for i in range(len(matricula_med)):
    if i in [2, 4]:
      matricula_final += "-"
    matricula_final += matricula_med[i]
  print(matricula_final)
else:
  print("A matricula introduzida é inválida!")
