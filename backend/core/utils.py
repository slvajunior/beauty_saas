import re


def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * len(cnpj):
        return False

    def calcula_digito(cnpj, peso):
        soma = sum(int(d) * peso[i] for i, d in enumerate(cnpj))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    primeiro_digito = calcula_digito(cnpj[:12], list(range(5, 1, -1)) + list(range(9, 1, -1)))
    segundo_digito = calcula_digito(cnpj[:13], list(range(6, 1, -1)) + list(range(9, 1, -1)))

    return cnpj[-2:] == primeiro_digito + segundo_digito
