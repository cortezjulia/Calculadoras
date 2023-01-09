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
    #conferir erro
    print('Insira dois valores para calcular o parâmetro faltante:')
    print('------------------------------------------------------')
    print('Quantia total[1] --- Porcentagem[2] --- quantia correspondente a porcentagem[3]')

    opcao_porcento1=input('Digite a primeira opção: ')
    valor_porcento1=float(input('Digite o valor para essa opção: '))

    opcao_porcento2=input('Digite a segunda opção: ')
    valor_porcento2=float(input('Digite o valor para essa opção: '))
    
    if (opcao_porcento1 or opcao_porcento2== '1') and (opcao_porcento1 or opcao_porcento2=='2'):
        valor_porcentagem=(valor_porcento1*valor_porcento2)/100
        if opcao_porcento1=='1':
            print(f'Para o valor de {valor_porcentagem}, igual a {valor_porcento2}, o TOTAL é de {valor_porcento1}')
        elif opcao_porcento1=='2':
            print(f'Para o valor de {valor_porcentagem}, igual a {valor_porcento1}, o TOTAL é de {valor_porcento2}')
    
  
    elif (opcao_porcento1 or opcao_porcento2== '1') and (opcao_porcento1 or opcao_porcento2=='3'):
        if opcao_porcento1=='1':
            calcula_porcentagem=(100*valor_porcento2)/(valor_porcento1)
            print(f'Para o valor de {valor_porcento2}, igual a {calcula_porcentagem}, o TOTAL é de {valor_porcento1}')
        
        elif opcao_porcento1=='3':
            calcula_porcentagem=(100*valor_porcento1)/(valor_porcento2)
            print(f'Para o valor de {valor_porcento1}, igual a {calcula_porcentagem}, o TOTAL é de {valor_porcento2}')

    elif (opcao_porcento1 or opcao_porcento2== '2') and (opcao_porcento1 or opcao_porcento2=='3'):
        if opcao_porcento1=='2':
            total=(100*valor_porcento2)/(valor_porcento1)
            print(f'Para o valor de {valor_porcento2}, igual a {valor_porcento1}, o TOTAL é de {total}')
        
        elif opcao_porcento1=='3':
            total=(100*valor_porcento1)/(valor_porcento2)
            print(f'Para o valor de {valor_porcento1}, igual a {valor_porcento2}, o TOTAL é de {total}')

if flag_opcao==2:
    #falta corrigir problema: quando o numero estiver no formato "0numero"
    flag_possui_zero=0
    print('Você deseja somar ou subtrair hrs/min/secs?')
    opcao_tempo=input('Entre com [1] para Soma e [2] para Subtrair: ')

    tempo_hora_1=float(input('Entre com a hora iniciais: '))
    tempo_min_1=float(input('Entre com os minutos iniciais: '))
    tempo_sec_1=float(input('Entre com os segundos iniciais: '))
    
    tempo_hora_2=float(input('Entre com a hora finais: '))
    tempo_min_2=float(input('Entre com os minutos finais: '))
    tempo_sec_2=float(input('Entre com os segundos finais: '))

   

    if opcao_tempo =='1':
        calcula_hora=(tempo_hora_1+tempo_hora_2)
        calcula_min=(tempo_min_1+tempo_min_2)
        calcula_sec=(tempo_sec_1+tempo_sec_2)
        
        print(f'O somatório desses intervalos é {calcula_hora}:{calcula_min}:{calcula_sec}')
        
         
    
    elif opcao_tempo=='2':
        if tempo_hora_1>=tempo_hora_2: 
            calcula_hora=(tempo_hora_1-tempo_hora_2)
            calcula_min=(tempo_min_1-tempo_min_2)
            calcula_sec=(tempo_sec_1-tempo_sec_2)
            print(f'A diferença entre esses intervalos é {calcula_hora}:{calcula_min}:{calcula_sec}')
        else:
            calcula_hora=(tempo_hora_2-tempo_hora_1)
            calcula_min=(tempo_min_2-tempo_min_1)
            calcula_sec=(tempo_sec_2-tempo_sec_1)
            
            print(f'O somatório desses intervalos é {calcula_hora}:{calcula_min}:{calcula_sec}')
        


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

if flag_opcao==6:
    print('Vamos calcular o seu IMC!')
    nome_imc=(input('Insira seu nome: '))
    altura_imc=float(input('Insira a sua altura em metros: '))
    peso_imc=float(input('Insira o seu peso: '))
    imc=(peso_imc)/(altura_imc*altura_imc)
    print(f'Sr(a) {nome_imc}, seu peso é {peso_imc}, sua altura {altura_imc}, dessa forma o IMC é de {imc}')

    


   


    
