import re

INVALID_CPF_KNOW = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999',
]


class Validator:
    def _first_valid_cpf_digit(self, cpf_no_mask):
        result = 0
        numbers = list(range(2, 11))
        first_digit = cpf_no_mask[:9]
        
        for index in cpf_no_mask[:9]:
            result += int(index) * numbers[-1]
            numbers.pop()
        
        rest = (result * 10) % 11
        if rest == 10:
            rest = 0
        
        return str(rest) == first_digit
    

    def _second_valid_cpf_digit(self, cpf_no_mask):
        result = 0
        numbers = list(range(2, 12))
        second_digit = cpf_no_mask[-1]
        
        for index in cpf_no_mask[:10]:
            result += int(index) * numbers[-1]
            numbers.pop()
        
        rest = (result * 10) % 11
        if rest == 10:
            rest = 0
        
        return str(rest) == second_digit
    

    def _first_digit_cnpj_valid(self, cnpj_no_mask):
        result = 0
        first_sequence = list(range(2, 6))
        second_sequence = list(range(2, 10))
        first_digit = cnpj_no_mask[-2]

        for index in cnpj_no_mask[:12]:
            if first_sequence:
                result += int(index) * first_sequence[-1]
                first_sequence.pop()
            else:
                result += int(index) * second_sequence[-1]
                second_sequence.pop()
        
        rest = result % 11
        if rest < 2:
            rest = 0
        else:
            rest = 11 - rest
        
        return str(rest) == first_digit
    

    def _second_digit_cnpj_valid(self, cnpj_no_mask):
        result = 0
        first_sequence = list(range(2, 7))
        second_sequence = list(range(2, 10))
        second_digit = cnpj_no_mask[-1]

        for index in cnpj_no_mask[:13]:
            if first_sequence:
                result += int(index) * first_sequence[-1]
                first_sequence.pop()
            else:
                result += int(index) * second_sequence[-1]
                second_sequence.pop()
        
        rest = result % 11
        if rest < 2:
            rest = 0
        else:
            rest = 11 - rest
        
        return str(rest) == second_digit
    
    def mask_number_removal(self, number):
        return re.sub('[^0-9]', '', number)
    
    def valid_cpf(self, cpf_no_mask):
        if cpf_no_mask in INVALID_CPF_KNOW:
            return False
        if not self._first_valid_cpf_digit(cpf_no_mask):
            return False
        if not self._second_valid_cpf_digit(cpf_no_mask):
            return False
        
        return True
    
    def valid_cnpj(self, cnpj_no_mask):
        if not self._first_digit_cnpj_valid(cnpj_no_mask):
            return False
        if not self._second_digit_cnpj_valid(cnpj_no_mask):
            return False
        
        return True
    
    def cpf_cnpj_validator(self, cpf_cnpj):
        cpf_cnpj_tmp = self.mask_number_removal(cpf_cnpj)

        if len(cpf_cnpj_tmp) == 11:
            return self.valid_cpf(cpf_cnpj_tmp)
        elif len(cpf_cnpj_tmp) == 14:
            return self.valid_cnpj(cpf_cnpj_tmp)
        else:
            return False
        
    
    def api_cpf_cnpj_validation(self, cpf_cnpj):
        if not self.cpf_cnpj_validator(cpf_cnpj):
            raise {"cpf_cnpj invalido": cpf_cnpj}