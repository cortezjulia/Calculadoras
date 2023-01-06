#menu
print('****Seja bem-vindo ao guia de calculadoras!****')
print('Escolha agora qual função você quer usar,\
digitando o número correspondente: ')


print('------------------------------------------------------')
print('Porcentagem(%)--> 1            Tempo(s/min/horas)--> 2')
print('------------------------------------------------------')
print('Expressão numérica(+-/*)--> 3      Raiz quadrada --> 4')
print('------------------------------------------------------')
print('Potenciação --> 5       Índice de Massa Corporal --> 6')

flag_opcao=0
opcao=int(input('Insira o número: '))

if opcao==1:
    flag_opcao=1
elif opcao==2:
     flag_opcao=2
elif opcao==3:
     flag_opcao=3
elif opcao==4:
     flag_opcao=4
elif opcao==5:
     flag_opcao=5
elif opcao==6:
     flag_opcao=6

if flag_opcao==1:
    print('Insira dois valores para calcular o parâmetro faltante:')
    print('------------------------------------------------------')
    print('Quantia total[1] --- Porcentagem[2] --- quantia correspondente a porcentagem[3]')

    opcao_porcento1=input('Digite a primeira opção: ')
    valor_porcento1=float(input('Digite o valor para essa opção: '))

    opcao_porcento2=input('Digite a segunda opção: ')
    valor_porcento2=float(input('Digite o valor para essa opção: '))
    
    if (opcao_porcento1 or opcao_porcento2== '1') and (opcao_porcento1 or opcao_porcento2=='2'):
        valor_porcentagem=(valor_porcento1*valor_porcento2)/100
        
        
    if (opcao_porcento1 or opcao_porcento2== '1') and (opcao_porcento1 or opcao_porcento2== '3'):
        if opcao_porcento1==1:
            porcentagem=(100*valor_porcento2)/valor_porcento1
        else:
            porcentagem=(100*valor_porcento1)/valor_porcento2
    
    if (opcao_porcento1 or opcao_porcento2== '2') and (opcao_porcento1 or opcao_porcento2== '3'):
       if opcao_porcento1==2:
            porcentagem=(100*valor_porcento2)/valor_porcento1
            print(f'Para o valor de {valor_porcento2}, igual a {valor_porcento1}, o TOTAL é de {valor_porcentagem}')
       else:
            porcentagem=(100*valor_porcento1)/valor_porcento2
            print(f'Para o valor de {valor_porcento1}, igual a {valor_porcento2}, o TOTAL é de {valor_porcentagem}')
       
    
    
if flag_opcao==2:
    print('temp')

if flag_opcao==3:
    
     print('Utilize apenas números e as seguintes operações:+-/*')
     expressao=input('Insira a expressão a ser calculada: ')
     valor_expressao=eval(expressao)
     print(f'O valor obtido dessa operação é: {valor_expressao}')
if flag_opcao==4:
    print("Vamos fazer a raiz quadrada de um número!")
    recebe_raiz=float(input('Digite um número: '))
    calcula_raiz=recebe_raiz**0.5
    print(f"A raiz quadrada do número {recebe_raiz} é {calcula_raiz:.4f}")

if flag_opcao==5:
    print("Vamos fazer a potenciação de um número!")
    recebe_base=float(input('Digite um número para a base: '))
    recebe_expoente=float(input('Digite um número para o expoente: '))
    flag_pot=1

    calcula_pot=recebe_base
    while flag_pot<recebe_expoente:
        flag_pot=flag_pot+1
        calcula_pot=calcula_pot*recebe_base
        
    print(f'O valor de {recebe_base} elevado a {recebe_expoente} é igual a {calcula_pot:.2f}')


    


   


    
