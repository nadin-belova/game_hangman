import random

word_list = ['функция','производная','дискриминант','аксиома','интеграл','гипербола','вектор','константа','лемма','парабола','факториал','абсцисса','аппликата','катет','гипотенуза','площадь','угол','тангенс','косинус','синус']

# функция получения случайного слова из списка в верхнем регистре
def get_word():
    return random.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: полностью сделанная виселица
                ''' 
                   --------
                   |      |
                   |      💀
                   |     /|\\
                   |      |
                   |     / \ 
                   |     
                   |     ___
                   |     | |
                -------
                ''',
                # виселица без веревки 😭
                '''
                   --------
                   |
                   |      
                   |      😭
                   |     /|\\
                   |      |
                   |     / \ 
                   |     ___
                   |     | |
                -------
                ''',
                # виселица без перекладины и веревки 😨
                '''
                   
                   |
                   |      
                   |      😨
                   |     /|\\
                   |      |
                   |     / \ 
                   |     ___
                   |     | |
                -------
                ''',
                # половина веселицы 😖
                '''
                         
                      
                          😖
                         /|\\
                   |      |
                   |     / \ 
                   |     ___
                   |     | |
                -------
                ''',
                # основание виселицы 😩
                '''
                   
                          😩
                         /|\\
                          |
                         / \ 
                         ___
                         | |
                -------
                ''',
                # нет виселицы🥺
                '''
                
                          🥺
                         /|\\
                          |
                         / \ 
                         ___
                         | |
                
                   
                ''',
                # нет виселицы и человека,один стул
                '''
                   
                         
                         
                       
                         
                         ___
                         | |
                
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Давайте играть в угадайку слов!')
    print(f'Виселица: {display_hangman(tries)}')
    print(f'Загаданное слово: {word_completion}')

    while tries >= 0:
        if tries == 0:
            print('Увы, попытки закончились, Вы не угадали слово')
            print(f'Загаданное слово: {word}')
            print(f'Виселица: {display_hangman(tries)}')
            break
        word_input = input('Введите букву или слово: ').upper()
        if 'А' <= word_input <= 'Я' or word_input.isalpha():

            if word_input in guessed_letters or word_input in guessed_words:
                print('Вы это уже вводили')
                continue
            elif len(word_input) == 1 and word_input in word:
                for i in range(len(word)):
                    if word[i] == word_input:
                        word_completion = word_completion[:i] + word_input + word_completion[i+1:]
                    elif word_completion == word:
                       print('Поздравляю, Вы угадали слово! Вы победили!')
                       print(f'Загаданное слово: {word}')
                       break
                guessed_letters.append(word_input)
                    
                print(f'Вы угадали букву\n{word_completion}')
            elif len(word_input) == 1 and word_input not in word:
                tries -= 1
                guessed_letters.append(word_input)
                print(f'ВЫ не угадали букву, осталось попыток {tries}')
                print(word_completion)
                print(f'Виселица: {display_hangman(tries)}')
            
            elif len(word_input) > 1:
                if word_input == word:
                    print('Поздравляю, Вы угадали слово! Вы победили!')
                    print(f'Загаданное слово: {word}')
                    break
                else:
                    tries -= 1
                    guessed_words.append(word_input)
                    print(f'Вы не угадали слово, осталось попыток {tries}')
                    print(word_completion)
                    print(f'Виселица: {display_hangman(tries)}')
           

        else:
            print('Вы ввели не букву и не слово, попробуйте еще раз')

while True:
    word = get_word()
    play(word)
    repeat = input('Хотите сыграть еще раз?(да/нет) ').lower()
    if repeat == 'да':
        print('\n')
    elif repeat == 'нет':
        print('Возвращайтесь снова, до свидания!')
        break
    else:
        break