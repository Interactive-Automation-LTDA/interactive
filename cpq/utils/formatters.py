def phone_number(number):
    if len(number) == 8:
        return f'{number[:4]}-{number[4:]}'
    elif len(number) == 9:
        return f'{number[:5]}-{number[5:]}'
    else:
        return number


def full_phone_number(number, cod_country=None, ddd=None):
    resultado = ''

    if cod_country:
        resultado += f'+{cod_country} '
    if ddd:
        resultado += f'({ddd}) '
    if len(number) == 8:
        resultado += f'{number[:4]}-{number[4:]}'
    elif len(number) == 9:
        resultado += f'{number[:5]}-{number[5:]}'
    else:
        resultado += number
    return resultado


def cep(cep):
    return f'{cep[:5]}-{cep[5:]}'


def cpf_cnpj(cpf_cnpj):
    if len(cpf_cnpj) == 11:
        return f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}'
    if len(cpf_cnpj) == 14:
        return f'{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:]}'