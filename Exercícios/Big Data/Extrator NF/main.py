import re

#(?=Valor Total:\s*R\$\s*([\d,]*))
#Não pega 200.000,00

#(?<=Valor Total:\sR\$)\s+([\d]{1,3}(?:[.\d]{3})*(?:,\d{2})?)
#Pega 200.000,00

