tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
ids, nomes  = zip(*tupla_iteravel)

ids = list(ids)
nomes = list(nomes)

print("IDs = ", ids)
print("Nomes = ", nomes)