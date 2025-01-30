import re

def validar_bandeira(numero_cartao):
    bandeiras = {
        'Visa': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
        'MasterCard': re.compile(r'^5[1-5][0-9]{14}$'),
        'American Express': re.compile(r'^3[47][0-9]{13}$'),
        'Diners Club': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
        'Discover': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
        'JCB': re.compile(r'^(?:2131|1800|35\d{3})\d{11}$'),
        'Hipercard': re.compile(r'^(606282|3841)[0-9]{10,13}$'),
        'Aura': re.compile(r'^50[0-9]{14}$'),
        'Voyager': re.compile(r'^8699[0-9]{11}$'),
        'EnRoute': re.compile(r'^(2014|2149)[0-9]{11}$')
    }

    for bandeira, padrao in bandeiras.items():
        if padrao.match(numero_cartao):
            return bandeira
    return 'Bandeira desconhecida'


def validar_numero_cartao(numero_cartao):
    bandeira = validar_bandeira(numero_cartao)
    if bandeira == 'Bandeira desconhecida':
        raise ValueError('Número de cartão inválido')
    return numero_cartao

# Exemplo de uso
try:
    numero_cartao = '6062825624254001'  # Exemplo de Hipercard
    numero_valido = validar_numero_cartao(numero_cartao)
    print(f'O número do cartão é válido: {numero_valido}')
except ValueError as error:
    print(error)
