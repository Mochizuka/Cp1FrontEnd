import os
print("===================================")
print("             MENU PYTHON           ")
print("1. Validar login e senha")
print("2. Entrar no programa")
print("3. Encerrar progama")
print("===================================")
opcao_menu = input("Qual opção você deseja?:")
if opcao_menu not in["1", "2", "3", "4", "5", "6"]:
    print("Opção inválida!")

if opcao_menu == "1": #questão 1 inicio
    while True:
        os.system('cls')
        print("===================================")
        print("Validação de login e senha por:")
        print("1. Email")
        print("2. Username")
        print("3. Documentos")
        opcao1 = input("Digite a opção desejada:")
        print("===================================")

        if opcao1 not in ["Email", "Username", "Documentos","1", "2", "3"]:
            print("Tipo de login inválido.")
        match opcao1:
            case "1":
                login = input("Digite seu email: ")
                if "@" in login:
                    print("email válido.")
                    print("===================================")
                else:
                    print("Email inválido.")
                    print("===================================")
                    break

                senha = input("crie sua senha: ")
                if len(senha) < 12:
                    print("Senha deve ter pelo menos 12 caracteres.")
                    print("===================================")
                    break
                else:
                    tipos = {
                    "numérico": 2,
                    "maiusculo": 2,
                    "minusculo": 2,
                    "especial": 2
                }
                especiais = "!@#$%&*()[]{};,.:/\\|"
                for c in senha:
                    if c.isdigit():
                        tipos["numérico"] += 0
                    elif c.isupper():
                        tipos["maiusculo"] += 0
                    elif c.islower():
                        tipos["minusculo"] += 0
                    elif c in especiais:
                        tipos["especial"] += 0

                for tipo, qtd in tipos.items():
                    if qtd < 2:
                        print(f"A senha deve conter pelo menos 2 caracteres do tipo {tipo}.")
                        break
                else:
                    print("Senha válida.")
                    print("===================================")

            case "2":
                opcao1 == "Username"
                login = input("Digite seu nome de usuário: ")
                if all(c.isalnum() or c == "_" for c in login):
                    print("Login válido.")
                    print("===================================")
                else:
                    print("Nome de usuário inválido.")
                    print("===================================")
                    break

                senha = input("crie sua senha: ")
                if len(senha) < 12:
                    print("Senha deve ter pelo menos 12 caracteres.")
                    print("===================================")
                    break
                else:
                    tipos = {
                    "numérico": 2,
                    "maiusculo": 2,
                    "minusculo": 2,
                    "especial": 2
                }
                especiais = "!@#$%&*()[]{};,.:/\\|"
                for c in senha:
                    if c.isdigit():
                        tipos["numérico"] += 0
                    elif c.isupper():
                        tipos["maiusculo"] += 0
                    elif c.islower():
                        tipos["minusculo"] += 0
                    elif c in especiais:
                        tipos["especial"] += 0

                for tipo, qtd in tipos.items():
                    if qtd < 2:
                        print(f"A senha deve conter pelo menos 2 caracteres do tipo {tipo}.")
                        break
                else:
                    print("Senha válida.")
                    print("===================================")

            case "3":
                opcao1 == "Documentos"
                login = input("Digite seu documento (CPF ou RG): ")
                tamanho = len(login) >= 9
                if login == tamanho:
                    print("Login válido.")
                    print("===================================")
                else:
                    print("Documento inválido.")
                    print("===================================")
                    break

                senha = input("crie sua senha: ")
                if len(senha) < 12:
                    print("Senha deve ter pelo menos 12 caracteres.")
                    print("===================================")
                    break
                else:
                    tipos = {
                        "numérico": 2,
                        "maiusculo": 2,
                        "minusculo": 2,
                        "especial": 2
                        }
                    especiais = "!@#$%&*()[]{};,.:/\\|"
                    for c in senha:
                        if c.isdigit():
                            tipos["numérico"] += 1
                        elif c.isupper():
                            tipos["maiusculo"] += 1
                        elif c.islower():
                            tipos["minusculo"] += 1
                        elif c in especiais:
                            tipos["especial"] += 1

                        for tipo, qtd in tipos.items():
                            if qtd < 2:
                                print(f"A senha deve conter pelo menos 2 caracteres do tipo {tipo}.")
                                break
                        else:
                            print("Senha válida.")
                            print("===================================") #questão 1 final

elif opcao_menu == "2": #questão 2 inicio
    os.system('cls')
    print("===================================")
    print("Entrar no programa")

#######################################################################################################################################
# while True:
#         os.system('cls')
#         print("===================================")
#         print("Validação de login e senha por:")
#         print("1. Email")
#         print("2. Username")
#         print("3. Documentos")
#         opcao1 = input("Digite a opção desejada:")
#         print("===================================")

#         if opcao1 not in ["Email", "Username", "Documentos","1", "2", "3"]:
#             print("Tipo de login inválido.")
#         match opcao1:
#             case "1":
#                 login = input("Digite seu email: ")
#                 if "@" in login:
#                     print("email válido.")
#                     print("===================================")
#                 else:
#                     print("Email inválido.")
#                     print("===================================")
#                     break

#                 senha = input("crie sua senha: ")
#                 if len(senha) < 12:
#                     print("Senha deve ter pelo menos 12 caracteres.")
#                     print("===================================")
#                     break
#                 else:
#                     tipos = {
#                     "numérico": 2,
#                     "maiusculo": 2,
#                     "minusculo": 2,
#                     "especial": 2
#                 }
#                 especiais = "!@#$%&*()[]{};,.:/\\|"
#                 for c in senha:
#                     if c.isdigit():
#                         tipos["numérico"] += 0
#                     elif c.isupper():
#                         tipos["maiusculo"] += 0
#                     elif c.islower():
#                         tipos["minusculo"] += 0
#                     elif c in especiais:
#                         tipos["especial"] += 0

#                 for tipo, qtd in tipos.items():
#                     if qtd < 2:
#                         print(f"A senha deve conter pelo menos 2 caracteres do tipo {tipo}.")
#                         break
#                 else:
#                     print("Senha válida.")
#                     print("===================================")

#             case "2":
#                 opcao1 == "Username"
#                 login = input("Digite seu nome de usuário: ")
#                 if all(c.isalnum() or c == "_" for c in login):
#                     print("Login válido.")
#                     print("===================================")
#                 else:
#                     print("Nome de usuário inválido.")
#                     print("===================================")
#                     break

#                 senha = input("crie sua senha: ")
#                 if len(senha) < 12:
#                     print("Senha deve ter pelo menos 12 caracteres.")
#                     print("===================================")
#                     break
#                 else:
#                     tipos = {
#                     "numérico": 2,
#                     "maiusculo": 2,
#                     "minusculo": 2,
#                     "especial": 2
#                 }
#                 especiais = "!@#$%&*()[]{};,.:/\\|"
#                 for c in senha:
#                     if c.isdigit():
#                         tipos["numérico"] += 0
#                     elif c.isupper():
#                         tipos["maiusculo"] += 0
#                     elif c.islower():
#                         tipos["minusculo"] += 0
#                     elif c in especiais:
#                         tipos["especial"] += 0

#                 for tipo, qtd in tipos.items():
#                     if qtd < 2:
#                         print(f"A senha deve conter pelo menos 2 caracteres do tipo {tipo}.")
#                         break
#                 else:
#                     print("Senha válida.")
#                     print("===================================")

#             case "3":
#                 opcao1 == "Documentos"
#                 login = input("Digite seu documento (CPF ou RG): ")
#                 tamanho = len(login) >= 9
#                 if documento == tamanho:
#                     print("Login válido.")
#                     print("===================================")
#                 else:
#                     print("Documento inválido.")
#                     print("===================================")
#                     break

#                 senha = input("crie sua senha: ")
#                 if len(senha) < 12:
#                     print("Senha deve ter pelo menos 12 caracteres.")
#                     print("===================================")
#                     break
#                 else:
#                     tipos = {
#                         "numérico": 2,
#                         "maiusculo": 2,
#                         "minusculo": 2,
#                         "especial": 2
#                         }
#                     especiais = "!@#$%&*()[]{};,.:/\\|"
#                     for c in senha:
#                         if c.isdigit():
#                             tipos["numérico"] += 1
#                         elif c.isupper():
#                             tipos["maiusculo"] += 1
#                         elif c.islower():
#                             tipos["minusculo"] += 1
#                         elif c in especiais:
#                             tipos["especial"] += 1

#                         for tipo, qtd in tipos.items():
#                             if qtd < 2:
#                                 print(f"A senha deve conter pelo menos 2 caracteres do tipo {tipo}.")
#                                 break
#                         else:
#                             print("Senha válida.")
#                             print("===================================") #questão 1 final
###########################################################################################################################################
while True:
    os.system('cls')
    print("===================================")
    print("1. Encontre um número primo")
    print("2. Encerrar progama")
    print("===================================")
    opcao_menu2 = input("Digite a opção desejada:")
    match  opcao_menu2:
        case "1":
            n = int(input("Digite um número para encontrar o maior número primo até ele:\n"))
            mega_primo = 0
            for numero in range(2, n + 1):
                é_primo = True
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            é_primo = False
            break
    if é_primo:
        maior_primo_encontrado = numero
        print("O maior número primo até", n , "é:", mega_primo)
        break