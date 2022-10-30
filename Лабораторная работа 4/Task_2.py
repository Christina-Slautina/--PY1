def get_count_char(str_):
    letter_dict = {}
    str_new = str_.lower()
    for letter in str_new:
        if letter.isalpha():
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict

# так как в задании написано, что нужно создать вторую функцию, исходя из первой, а именно использовать первый словарь,
# то процентное соотношение посчитано, не включая символов, так как они и не включались в первый словарь.


def percent_of_letters(new_dict):
    percent_dict = {}
    total = sum(new_dict.values())
    for letter in new_dict:
        percent_dict[letter] = round(100 * new_dict[letter] / total, 1)
    return percent_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_1 = get_count_char(main_str)
print(dict_1)

dict_2 = percent_of_letters(dict_1)
print(dict_2)

# Проверка
total_total = sum(dict_2.values())
print(round(total_total, 1))
