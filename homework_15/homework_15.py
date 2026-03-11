""""
Одно слово
Напишите программу, которая обрабатывает список из строки удаляет все строки, содержащие более одного слова, 
а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
new_list = []

for word in text_list:
    if len(word.split()) == 1:
        new_list.append(word.lower())

print(f"Обработанный список: {new_list}")

"""
Обновление цен товаров

Дан список товаров с ценами. Программа должна применить скидку к каждому товару и
добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.

Данные:

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

Пример вывода:

Введите скидку (в процентах): 17

Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse               25.00$        20.75$
Keyboard            75.00$        62.25$
Monitor            200.00$       166.00$
"""""

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

discount_input = input("Введите скидку (в процентах): ")
discount = float(discount_input)

header_product, header_old_price, header_new_price = "Товар", "Старая цена", "Новая цена"
print(f"{header_product:<20} {header_old_price:>10} {header_new_price:>14}")

for item in products:
    product_name = item[0]
    old_price = item[1]
    new_price = old_price * (1 - discount / 100)
    print(f"{product_name:<20} {old_price:>10.2f}$ {new_price:>13.2f}$")
