print('welcome to encode and decode')
direction = str(input('please input encode or decode: ')).lower()
text = str(input('please enter your massage here:  ')).lower()
shift = int(input('please enter your number of shifts:  '))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', '.', ',']



def encode(text=text, shift=shift):
    encode_text = ''
    for letter in text:
        letter_position = alphabet.index(letter)
        letter_position += shift
        letter_position %= len(alphabet)
        encode_text += alphabet[letter_position]
    print(f'the encode text is: \n{encode_text}')

def decode(text=text, shift=shift):
    decode_text = ''
    for letter in text:
        letter_position = alphabet.index(letter)
        letter_position -= shift
        letter_position %= len(alphabet)
        decode_text += alphabet[letter_position]
    print(f'the encode text is: \n{decode_text}')


if direction == 'encode':
    encode()
elif direction == 'decode':
    decode()