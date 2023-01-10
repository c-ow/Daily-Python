import string

def list_solution():
    mc = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    alphabet = list(string.ascii_lowercase)
    translated = []

    translate = input('Input to translate:\n')
    if translate[0] == '.' or translate[0] == '-':
        strings = translate.split('/')
        for i in strings:
            if i in mc:
                mc_index = mc.index(i)
                translated.append(alphabet[mc_index])
            elif i == '':
                translated.append(' ')
    else:
        for i in translate:
            if i in alphabet:
                alphabet_index = alphabet.index(i)
                translated.append(mc[alphabet_index])
                translated.append(mc[-1])
            elif i == ' ':
                translated.append(mc[-1])
    translated = "".join(str(i)for i in translated)
    return 'Translation:\n' + translated

def dict_solution():
    alphabet_mc = {
        '.-':'a', 
        '-...':'b', 
        '-.-.':'c', 
        '-..':'d', 
        '.':'e', 
        '..-.':'f', 
        '--.':'g', 
        '....':'h',
        '..':'i',
        '.---':'j',
        '-.-':'k',
        '.-..':'l',
        '--':'m',
        '-.':'n',
        '---':'o',
        '.--.':'p',
        '--.-':'q',
        '.-.':'r',
        '...':'s',
        '-':'t',
        '..-':'u',
        '...-':'v',
        '.--':'w',
        '-..-':'x',
        '-.--':'y',
        '--..':'z',
        '':' '
    }
    translate = input("Input to translate: \n")
    if translate[0] == '.' or translate[0] == '-':
        strings = translate.split('/')
        translated = [alphabet_mc.get(i) for i in strings if i in alphabet_mc.keys()]
    else:
        translated = [key + '/' for i in translate for key, value in alphabet_mc.items() if value == i]
    translated = "".join(str(x)for x in translated)
    return 'Translation:\n' + translated

print(list_solution())