peso= float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

IMC= peso/(alt**2)
if IMC <= 18.5:
    print ("Você está abaixo do peso ideal")
else:
    if IMC > 18.5 and IMC <= 24.9:
        print("Parabéns — você está em seu peso normal!")
    else:
        if IMC >= 25.0 and IMC <= 29.9:
            print("Você está acima de seu peso (sobrepeso)")
        else:
            if IMC >= 30.0 and IMC <= 34.9:
                print("Obesidade grau I")
            else:
                if IMC >= 35.0 and IMC <= 39.9:
                    print("Obesidade grau II")
                else:
                    IMC >= 40.0
                    print("Obesidade grau III")
print("Seu IMC é de",IMC)