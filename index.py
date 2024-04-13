#nome do trabalhador
name=[]
lista=name
while 1:
    name+=[input('digite seu nome')]
    print(lista)
#ver se possui certificado váido
    certificado=int(input('você possui o certificado em dia? digite "1" para SIM e "0" para NÃO'))
#senão...
    if certificado!=1:
        print('Procuramos profissionais com o certificado em dia')
        name-=name
        break
#verificando a altura do trabalhador
    altura=float(input('qual a sua altura em metros?'))
    if altura<1.70:
        print('você é muito baixo para o trabalho')
        break
#ver se tem mais trabalhadores para informar
    informar_trabalhadores=int(input('voce tem mais algum trabalhador para informar? digite "1" para SIM e "0" para NÃO'))
    if informar_trabalhadores==0:
        print(lista)
        break
    