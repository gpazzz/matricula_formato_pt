matricula_int = input("Introduza a matricula do veiculo: ")
matricula_med = ""
matricula_final = ""
valido = True
count_alfa = 0
count_digi = 0

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

    if bloco.isalpha():
      count_alfa += 1
    elif bloco.isdigit():
      count_digi += 1
    else:
      valido = False
      break

  if count_alfa == 0 or count_digi == 0:
    valido = False

#Formato matricula e output se for válido
if valido:
  for i in range(len(matricula_med)):
    if i in [2, 4]:
      matricula_final += "-"
    matricula_final += matricula_med[i]
  print(matricula_final)
else:
  print("A matricula introduzida é inválida!")
