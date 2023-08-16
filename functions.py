
def input_choice():
    print('0. Exit')
    print('1. Write sentence to file')
    print('2. Read sentence from the file')

    return input('Choose a choice: ')

def write_to_file(sentence):
    with open('file.txt', 'w') as file:
        file.writelines([sent + '\n' for sent in sentence])

def read_from_file():
    with open('file.txt', 'r') as file:
        sentenceFromFile = file.readlines()
        sentence = [sent.rstrip('\n') for sent in sentenceFromFile]
        if len(sentenceFromFile) == 0:
            print('Файл пуст')
            return
    return print(' '.join(sentence))

