user_input = input("Enter sentence:\n")

translation = user_input[:]  # Make a copy of the string

# Spanish to English, all numbers 1 to 100
translation = translation.replace('cero', 'zero')
translation = translation.replace('uno', 'one')
translation = translation.replace('dos', 'two')
translation = translation.replace('tres', 'three')
translation = translation.replace('quatro', 'four')
translation = translation.replace('cinco', 'five')
translation = translation.replace('diez y seis', 'sixteen')
translation = translation.replace('diez y siete', 'seventeen')
translation = translation.replace('diez y ocho', 'eighteen')
translation = translation.replace('diez y nueve', 'nineteen')
translation = translation.replace('seis', 'six')
translation = translation.replace('siete', 'seven')
translation = translation.replace('ocho', 'eight')
translation = translation.replace('nueve', 'nine')
translation = translation.replace('diez', 'ten')
translation = translation.replace('once', 'eleven')
translation = translation.replace('doce', 'twelve')
translation = translation.replace('trece', 'thirteen')
translation = translation.replace('catorce', 'fourteen')
translation = translation.replace('quince', 'fifteen')
translation = translation.replace('veinte', 'twenty')
translation = translation.replace('veinte y ', 'twenty-')
translation = translation.replace('treinta', 'thirty')
translation = translation.replace('treinta y ', 'thirty-')
translation = translation.replace('cuarenta', 'forty')
translation = translation.replace('cuarenta y ', 'forty-')
translation = translation.replace('cincuenta', 'fifty')
translation = translation.replace('cincuenta y ', 'fifty-')
translation = translation.replace('sesenta', 'sixty')
translation = translation.replace('sesenta y ', 'sixty-')
translation = translation.replace('setenta', 'seventy')
translation = translation.replace('setenta y ', 'seventy-')
translation = translation.replace('ochenta', 'eighty')
translation = translation.replace('ochenta y ', 'eighty')
translation = translation.replace('noventa', 'ninety-')
translation = translation.replace('noventa y ', 'ninety-')
translation = translation.replace('cien', 'one-hundred')

print('Translation:', translation)