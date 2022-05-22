print("\n --- Parte 1: Receptor - Criação das chaves --- \n")

# Preparando a criação das chaves:
#
p = 29
q = 31
n = p * q
phi_n = (p - 1) * (q - 1)

print("Valores primos utilizados:\np =", p, "\nq =", q)

# Achando o valor de e:
e = 0

invalid_list = []
valid_list = []

for i in range(2, phi_n - 1):
    if phi_n % i == 0:
        invalid_list.append(i)
    else:
        for j in invalid_list:
            if i % j == 0:
                invalid_list.append(i)
                break
    if i not in invalid_list:
        valid_list.append(i)

print("\nValores possíveis de e:", valid_list, sep="\n\n")

inp_e = int(input("\nEscolha um valor da lista para e: "))

if inp_e in valid_list:
    e = inp_e
else:
    print("Valor inválido.")

# Achando o valor de d:
d = 0

for x in range(1, phi_n):
    if (e * x) % phi_n == 1:
        d = x

print("d =", d)
print('{:-^40}'.format("-"))
print("Chave pública (encriptar): {e =", e, ", n =", n, "}")
print("Chave privada (decriptar): {d =", d, ", n =", n, "}")
print('{:-^40}'.format("-"))

print("\n --- Parte 2: Emissor - Criptografar a mensagem com a chave pública --- \n")

# Receber a mensagem e as chaves
m = input("Escreva a mensagem a ser criptografada: ")
e = int(input("Digite o valor númerico de e da chave para criptografar: "))
n = int(input("Digite o valor númerico de n da chave para criptografar: "))

# Transformar a mensagem clara em texto cifrado
mb = []

for i in range(0, len(m)):
    mb.append(ord(m[i]))

# Criptografar a mensagem
c = []

print("\nMensagem criptografada: ", end="")

for i in range(0, len(mb)):
    num = mb[i]
    c.append(chr(num**e % n))
    print(c[i], end="")

print("\n\n --- Parte 3: Receptor - Decriptação da mensagem --- \n")

# Decriptografar a mensagem
md = []

d = int(input("Digite o valor númerico de d da chave para decriptografar: "))
n = int(input("Digite o valor númerico de n da chave para decriptografar: "))

print("\nMensagem decriptografada: ", end="")
for i in range(0, len(mb)):
    num = c[i]
    md += (chr(ord(num)**d % n))
    print(md[i], end="")
