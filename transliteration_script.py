def english_to_bulgarian_phonetic(text):
    # Mapping for common multi-character phonetic patterns
    special_map = {
        'are': 'ар',
        'amazing': 'амейзинг',
        'revolut': 'револют',
        'people': 'пийпъл',
        'europe': 'юръп',
        'louise': 'луис',
        'great': 'грейт',
        'savings': 'сейвингс',
        'knight': 'найт',
        'island': 'айланд',
        'debt': 'дет',
        'wrist': 'рист',
        'through': 'тру',
        'aesthetic': 'естетик',
        'phoenix': 'феникс',
        'tion': 'шън',
        'sion': 'жън',
        'ch': 'ч',
        'sh': 'ш',
        'th': 'т',
        'ph': 'ф',
        'qu': 'кв',
        'ck': 'к',
        'ing': 'инг',
        'igh': 'ай',
        'ea': 'ий',
        'ee': 'и',
        'oo': 'у',
        'ou': 'ау',
        'oi': 'ой',
        'oy': 'ой',
        'aw': 'о',
        'ai': 'ей',
        'ay': 'ей',
        'au': 'о',
        'ei': 'ей',
        'eu': 'ю',
        'ue': 'ю',
        'oa': 'о',
        'ed': 'д',
        'able': 'ъбъл',
        'ous': 'ъс'
    }

    # Mapping for individual character sounds
    phonetic_map = {
        'a': 'а', 'b': 'б', 'c': 'к', 'd': 'д', 'e': 'е', 'f': 'ф',
        'g': 'г', 'h': 'х', 'i': 'и', 'j': 'дж', 'k': 'к', 'l': 'л',
        'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'к', 'r': 'р',
        's': 'с', 't': 'т', 'u': 'у', 'v': 'в', 'w': 'у', 'x': 'кс',
        'y': 'ай', 'z': 'з'
    }

    # Rules for silent letters
    silent_letters = {'k', 'w', 'b', 'h'}  # Silent letters in specific contexts

    # Contextual rules for specific letters
    def get_phonetic_for_c(prev_char, next_char):
        if next_char in ('e', 'i', 'y'):
            return 'с'
        else:
            return 'к'

    def get_phonetic_for_g(next_char):
        if next_char in ('e', 'i', 'y'):
            return 'дж'
        else:
            return 'г'

    def get_phonetic_for_u(prev_char):
        if prev_char in ('r', 'l'):
            return 'ю'
        return 'у'

    def get_phonetic_for_y(prev_char, next_char):
        if next_char == 'e':
            return 'ай'
        elif prev_char in ('a', 'e', 'o'):
            return 'й'
        return 'ай'

    # Apply special transliteration rules for known patterns
    lower_text = text.lower()
    for key, value in special_map.items():
        if key in lower_text:
            lower_text = lower_text.replace(key, value)

    transliterated = []
    text_length = len(lower_text)

    i = 0
    while i < text_length:
        char = lower_text[i]
        prev_char = lower_text[i - 1] if i > 0 else ''
        next_char = lower_text[i + 1] if i < text_length - 1 else ''

        # Handle multi-character special cases first
        if i < text_length - 1 and lower_text[i:i + 2] in special_map:
            transliterated.append(special_map[lower_text[i:i + 2]])
            i += 2
        elif i < text_length - 2 and lower_text[i:i + 3] in special_map:
            transliterated.append(special_map[lower_text[i:i + 3]])
            i += 3
        elif i < text_length - 3 and lower_text[i:i + 4] in special_map:
            transliterated.append(special_map[lower_text[i:i + 4]])
            i += 4
        # Handle silent letters
        elif char in silent_letters and next_char not in ('a', 'e', 'i', 'o', 'u'):
            i += 1
        # Handle individual characters with context rules
        elif char == 'c':
            transliterated.append(get_phonetic_for_c(prev_char, next_char))
            i += 1
        elif char == 'g':
            transliterated.append(get_phonetic_for_g(next_char))
            i += 1
        elif char == 'u':
            transliterated.append(get_phonetic_for_u(prev_char))
            i += 1
        elif char == 'y':
            transliterated.append(get_phonetic_for_y(prev_char, next_char))
            i += 1
        elif char in phonetic_map:
            transliterated.append(phonetic_map[char])
            i += 1
        else:
            transliterated.append(char)
            i += 1

    return ''.join(transliterated)


text = "Revolut, Europe, LOUISE, great savings, knight, island, and people are amazing."
transliterated_text = english_to_bulgarian_phonetic(text)

print(transliterated_text)
