
# "Высшая проба" (НИУ ВШЭ), командное программирование, квалификация 2023 

## Команда: ___IGOR VOYTENKO ENJOYERS___

## Состав команды: 
1) Войцехович Александр
2) Сиваков Ярослав
3) Донкеев Григорий

## Формат: ___3 таска, 2/3 правильных для клалификации___

### Задача А:
#### ___Форматирование файла___
>Петя - начинающий программист. Сегодня он написал код из n строк.
>
>К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные места пробелы. А точнее, для i-й строки ему нужно добавить ровно ai пробелов.
>
>Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace. При нажатии на Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела. При нажатии на Backspace в строке удаляется один пробел.
>
>Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое количество пробелов в каждую строку. Помогите ему!

#### Ввод:
>Первая строка входных данных содержит одно целое положительное число n(1≤n≤105) – количество строк в файле.
>Каждая из следующих n строк содержит одно целое неотрицательное число a(0≤a≤109) – количество пробелов, которые нужно добавить в i-ю строку файла.

#### Вывод:
>Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов.

## Полное решение:
(Python 3.11 / C++20)

*Файл: 1_task.py / task_1.cpp*

Python:
```task_1.py
def remainder_counter(remainder):
    count = 0
    if remainder == 1:
        count += 1
    elif remainder == 3 or 2:
        count += 2
    else:
        pass
    return count


counter = 0

spaces_amount = (int(input()) for _ in range(int(input())))
for space in spaces_amount:
    if space % 4 == 0:
        counter += space // 4
    else:
        counter += space // 4
        counter += remainder_counter(space % 4)

print(counter)

```

Объяснение: общее кол-во пробелов *n* можно представить как `n // 4` табов и `n % 4` оставшихся пробелов, причем кол-во оставшихся никогда не равно 0 и не равно 4. Значит, кол-во пробелов находится в диапозоне `[1 - 3]`. Всего кол-во нажатий клавиш может быть *либо 1, либо 2*. То есть, при остатке от деления `n % 4 = 1`. Вынесем вычесление в случае `n % 4 != 0` в отдельную функцию для лучшей производительности. *(0.01s vs ~0.03s)*

C++:

```task_1.cpp
#include <iostream>

using namespace std;

int main() {
    int arr_size;
    cin >> arr_size;
    int* arr = new int[arr_size];

    for (int i = 0; i < arr_size; i++) {
        cin >> arr[i];
    }
    
    long int counter = 0;

    for (int i = 0; i < arr_size; i++) {
        int number = arr[i];
        if (number % 4 == 0) {
            counter += number / 4;
        } else {
            counter += number / 4;
            if (number % 4 == 2 || number % 4 == 3) {
                counter += 2;
            } else {
                counter += 1;
            }
        }
    }
    
    cout << counter;

}

```

Используется тот же самый алгоритм, но код исполняется эффективнее и занимает меньшее количество ОЗУ.


### Задача В:
### ___Плейлисты___
>Костя успешно прошел собеседование и попал на стажировку в отдел разработки сервиса «Музыка».
>Конкретно ему поручили такое задание — научиться подбирать плейлист для группы друзей, родственников или коллег. При этом нужно подобрать такой плейлист, в который входят исключительно нравящиеся всем членам группы песни.
>Костя очень хотел выполнить это задание быстро и качественно, но у него не получается. Помогите ему написать программу, которая составляет плейлист для группы людей.

##### Ввод:
>В первой строке расположено одно натуральное число n(1≤n≤2⋅10^5), где n – количество человек в группе.
>В следующих 2⋅n строках идет описание любимых плейлистов членов группы. По 2 строки на каждого участника.
>В первой из этих 2-х строк расположено число k — количество любимых треков i-го члена группы. В следующей строке расположено k строк через пробел — названия любимых треков i-го участника группы.
>Каждый трек в плейлисте задан в виде строки, все строки уникальны, сумма длин строк не превосходит 2⋅10^6. Строки содержат большие и маленькие латинские буквы и цифры.

#### Вывод:
>Выведите количество, а затем сам список песен через пробел — список треков, которые нравятся каждому участнику группы. Ответ необходимо отсортировать в лексикографическом порядке!

## Полное решение:
(Python 3.11)

```task_2.py
n = int(input()) - 1
input()
playlist = set(input().split())
for i in range(n):
    input()
    playlist = playlist & set(input().split())


playlist = tuple(playlist)
print(len(playlist))
print(*sorted(playlist))

```

*Примечание: Несмотря на более миниатюрное и, казалось бы, элегантное решение, на деле задача оказалась сложнее в эфеективном в плане затраченного ОЗУ и потраченного на выполнение прогаммы времени.*
Если нам нужны песни, содержащиеся во всех выборка, они 100% есть и в первом плейлисте. Поэтому, будем использовать его как основной и имено его будем изменять. Стараемся использовать менее "толстые" для оперативной памяти типы данных (в данном случае - set), так как в решении через списки при числах ~ 2⋅10^6 время на исполнение и затраченное ОЗУ будут колоссальными. 
В переменную n записываем кол-во плейлистов в семье, за исключением первого (но вычитаем 1, так как один плейлист мы получим вне цикла, где данная переменная используется). далее получаем set из песен первого плейлиста, его и возьмем за эдакий "эталон". Далее, в цикле поулчаем новый плейлист (типа данных - также set) и заменяем "эталонный плейлист" на пересечение значений из двух плейлистов => именно те песни, которые есть во всех плейлистах:
`playlist = playlist & set(input().split())`
Стоит заметить, что в строках 2 и 5 стоят 2 метода `input()`, которые никуда не записываются. Это используется, так как по формату ввода нам также даются нигде не используемые данные - количество песен в данном плейлисте. Не записывая эти данные, мы ничего не теряем: они просто уйдут "в никуда", не затрачивая оперативной памяти.
Для сортировки полученой выборки, превратим set (в нем элементы не поддаются сортировке) в tuple (не в список, так как tuple более эффективен) и отсортируем его встроенной функцией.