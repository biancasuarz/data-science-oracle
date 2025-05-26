notas = [9.0,9.7,9.8,10.0]

def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"
    
    return(media, situacao)

print(boletim(notas))