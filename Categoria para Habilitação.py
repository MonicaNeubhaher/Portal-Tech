# Programa  : Categoria para CNH
# Autor     : Monica Rodrigues Lopes Neubhaher
# Turma     : 03
# Professor : Ravi Antunes


Qtde:int
QtdePessoas:int
PesoBruto:float

QtdeRodas = 0
QtdePessoas = 0
PesoBruto = 0

QtdeRodas = int(input("Informe a quantidade de rodas do veículo: "))

if QtdeRodas != 0:

    if QtdeRodas < 4:
    
       print("Categoria A")

    else:
        
        QtdePessoas = int(input("Informe a quantidade de pessoas no veículo ou 0 (zero) se não souber: "))
        PesoBruto = float(input("Informe o peso do veículo em Kg ou 0 (zero) se não souber: "))

        if QtdePessoas > 8:
           
          if PesoBruto > 6000:    

              print("Categoria E")
            
          elif (PesoBruto > 3500 and PesoBruto <= 6000):
             
              print("Categoria C")

          else:
               
              print("Categoria D")

        else:     

          if (PesoBruto > 3500 and PesoBruto <= 6000):
             
              print("Categoria C")
            
          elif PesoBruto > 6000:    

              print("Categoria E")
              
          else:
               
              print("Categoria B")

else:    

    print("Quantidade de rodas do veículo não é valida. Tente novamente!")
