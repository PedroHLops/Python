import os

lista = []
lista2 = []
cadastro = {}
y = m =  c =  0

while True:
    os.system('clear')
    x = 0
    print('[1] Cadastrar um novo colaborador')
    print('[2] Mostrar colaboradores')
    print('[3] Remover colaorador')
    print('[4] Fechar programa')
    x = str(input(''))
    
    if x == '1':
       os.system('clear')
       while True:
           cadastro['nome'] = str(input('Nome:'))
           while True:
                a = str(input('Idade:'))
                cadastro['idade'] = a
                a.isnumeric()
                if a.isnumeric() == True:
                    break
           cadastro['sexo'] = str(input('Sexo:'))   
           cadastro['area'] = str(input('Area:'))
           while True:
                    a = str(input('CTPS: '))
                    cadastro['CTPS'] = a
                    a.isnumeric()
                    if a.isnumeric() == True:
                        break
           lista.append(cadastro.copy())
           break           
           
                    
    elif x == '2':
        os.system('clear')
        while True:
             if len(lista) == 0:
                 print('Não existe nenhum colaborador cadastrado')
                 str(input('Pressione ENTER para continuar'))
                 break
             y = 0
             for e in lista:
                 print(lista[y])
                 y += 1
             print('[1] Filtrar colaboradores')
             print('[2] Voltar')             
             
             x = str(input(''))
             
               
             if x == '1':
                 filtro = str(input('Filtro: '))
                 vf = str(input('Valor do filtro: '))
                 y = 0
                 if filtro == 'idade':
                     print('escolha mais um paranmetro')
                     print(f'[1] Maior ou igual a {vf}')
                     print(f'[2] Menor ou igual a {vf}')
                     print(f'[3] igual a {vf}')
                     x = str(input(''))
                 
                     if x == '1':
                         for e in lista: 
                             if lista[y][filtro] >= vf:
                                 lista2.append(lista[y])
                                 y += 1
                         print(lista2)
                         lista2.clear()
                         break
                     elif x == '2':
                         for e in lista: 
                             if lista[y][filtro] <= vf:
                                 lista2.append(lista[y])
                                 y += 1
                         print(lista2)
                         lista2.clear()
                         break
                     elif x == '3':
                          for e in lista: 
                              if lista[y][filtro] <= vf:
                                  lista2.append(lista[y])
                                  y += 1
                          print(lista2)
                          lista2.clear()
                          break
                     
                     for e in lista: 
                         if lista[y][filtro] == vf:
                             lista2.append(lista[y])
                             y += 1
                         print(lista2)
                         lista2.clear()
                         break
             elif x == '2':
                 break    
             else:
                 print('valor nao cadastrado')
                 str(input('Pressione ENTER para continuar'))
                 break               
              

                 
    elif x == '3':
        os.system('clear')
        while True:
            if len(lista) == 0:
                 print('Não existe nenhum colaborador cadastrado')
                 str(input('Pressione ENTER para continuar'))
                 break
            x = str(input('Digite o CTPS do colaborador: '))
            j = 0
            y = 0
            for e in lista:
                if x == lista[y]['CTPS']:
                    print(lista[y])
                    del(lista[y])
                    j += 1
                y +=1
                if j == 0:
                    print('Não foi encontrado nenhum colaborador com esse numero de CTPS')
            break

    elif x == '4':
        exit()
        
    else:
        print('Valor não cadastrado')
        str(input('Pressione ENTER para continuar'))