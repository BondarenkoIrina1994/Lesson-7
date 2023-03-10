# Задание №1.
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке.
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод:
# Парам пам-пам

def number_syllables(fraza): 
    vowels=['А','Е','Ё','И','О','У','Ы','Э','Ю','Я']
    return (sum((1 for j in fraza if j in vowels)))

def check_fraza(element):
    if len(set(element))==1:
        print('Парам пам-пам')
    else:
        print('Пам парам')

fraza_vinni_pukha=list(input('Введите стихотворение Винни-Пуха:').upper().split(" "))
check_fraza(map(number_syllables,fraza_vinni_pukha))