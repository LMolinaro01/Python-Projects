class Guitarra:

    def __init__(self, tamanhoCorda, formato, afinacao, captadores):
        self.tamanhoCorda = tamanhoCorda
        self.formato = formato
        self.afinacao = afinacao
        self.captadores = captadores
    
    def tocar(self, nome, notasPminuto):
        print(f"\n*Solando com a {nome}* São tocadas {notasPminuto} notas por minuto!")

    def afinar(self, padraoAfinacao):
        print(f"\nAfinando a guitarrra na afinação: {padraoAfinacao}")


#Criando objetos da classe guitarra (Criando guitarras, eu já descrevi o que uma guitarra fazia)

user = input("\nSaudações! Primeiramente, qual seria seu nome?: ")

print(f"\nOlá {user}! ", end = "")

guitarraUserFormato = input("Qual o modelo/formato da sua Guitarra? (Ex: Les Paul, Strato): ")
guitarraUserAfinacao = input("\nQual a afinação da Guitarra?: ")
guitarraUserTamanhoCorda = input("\nQual o Tamanho da corda de sua guitarra?: ")
guitarraUserCaptador = input("\nQuais são dos Captadores?: ")

guitarraUser = Guitarra(guitarraUserTamanhoCorda, guitarraUserFormato, guitarraUserAfinacao, guitarraUserCaptador)

print(f"\nInformações da {guitarraUser.formato} de {user}: \n\n  -Expressura da Corda: {guitarraUser.tamanhoCorda} \n\n  -Formato da Guitarra: {guitarraUser.formato} \n\n  -Afinação: {guitarraUser.afinacao} \n\n  -Captadores: {guitarraUser.captadores}")

GibsonLP = Guitarra("0.9", "Les Paul", "Padrão", "Humbuckers") #Cada espaço entre a virgula me refiro a uma característica da classe
FenderStrato = Guitarra("0.10", "Stratocaster", "1/2 Tom abaixo", "Padrão Fender Strato")

print(f"\nInformações da {GibsonLP.formato}: \n\n  -Expressura da Corda: {GibsonLP.tamanhoCorda} \n\n  -Formato da Guitarra: {GibsonLP.formato} \n\n  -Afinação: {GibsonLP.afinacao} \n\n  -Captadores: {GibsonLP.captadores}") 
#Printei cada característica do objeto, me referenciando a classe

print(f"\nInformações da Fender Stratocaster: \n\n  -Expressura da Corda: {FenderStrato.tamanhoCorda} \n\n  -Formato da Guitarra: {FenderStrato.formato} \n\n  -Afinação: {FenderStrato.afinacao} \n\n  -Captadores: {FenderStrato.captadores}")
    
GibsonLP.tocar("Les Paul", "129") #Chamei a função tocar, e atribuí ela a Les paul
GibsonLP.afinar(GibsonLP.afinacao)

GibsonLP.tocar("Fender Stratocaster", "169")
GibsonLP.afinar(FenderStrato.afinacao)
