'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

phrase = input("Введите фразу из трех слов: ")

words = phrase.split()
result_words = []

for word in words:
    new_word = ""
    for pos, letter in enumerate(word, start=1):  # взял букву и её позицию (начиная с 1)
        new_word += letter * pos # Дублирую букву pos раз и добавляем к новому слову
    result_words.append(new_word)

final_phrase = " ".join(result_words)
print(final_phrase)