dicionario = "qwertyuiopasdfghjklzxcvbnm"
alfabeto = "abcdefghijklmnopqrstuvwxyz"

senha = "luiz"
senha_criptografada = ""

for letra in alfabeto:
    posicao = ord(letra) - ord("a")
    senha_criptografada += dicionario[posicao]
    print(senha_criptografada)

print(senha_criptografada)
