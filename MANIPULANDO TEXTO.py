#fateamento 
"""
ANÁLISE:

len(frase) 
21 caracteres
(curso em video python)
^^^^^ mostra quantas caracteres tem 

frase.count("o")
^^^^ conta quantas vezes aparece a letra O minuscula

frase.find("deo") 
^^^^ encontra o deo na frase, se n existir deo na string, ele dara -1 indicando que é inexistente 

"curso" in frase
^^^^ dira se existe a palavra "curso" entre (in) a frase (string), se sim dira true e se n dira false

TRANSFORMAÇÂO:

frase.replace("python", "android")
^^^^ na string onde estiver escrito python ele irar substituir por android

frase.upper()
^^^^^ o que já é maiusculo ele mantem, o que n for ele troca e deixa maiusculo

frase.lower()
^^^^ mesmo do upper só que o contrario, deixa minusculo

frase.capitalize()
^^^^ deixa a primeira letra da string em maiuscula

frase.title()
^^^^ deixa toda frase dps do espaço com a letra maiuscula EX: curso em video python (Curso Em Video Python)

frase.strip()
^^^^ remove espaços vacuos no inicio e no final de uma string EX: XXXXAprendendo pythonXXX

frase.split()
^^^^ divide uma string transformando em uma lista com cada palavra contando do 01
Ex: curso em video
    01234 01 01234

" ".join(frase)
^^^^ redefine o split

 ** Todo metodo termina com () ex: .upper( )

"""