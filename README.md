# First lab

### Що таке лінійні трансформації?
**_Лінійна трансформація_** — це функція, яка відображає вектор з одного векторного простору на інший вектор в іншому векторному просторі. Щоб функція вважалася лінійною, вона повинна відповідати двом основним умовам:

1. **Збереження суми**: якщо ми беремо два вектори u і v у вихідному векторному просторі, лінійне перетворення має зберегти суму цих векторів. Іншими словами, якщо ми застосовуємо перетворення до суми u і v, результат повинен дорівнювати сумі окремих перетворень u і v. Математично це виражається як T(u + v) = T(u) + T(v).

2. **Збереження множення на скаляр**: якщо ми візьмемо вектор u у вихідному векторному просторі та помножимо цей вектор на скаляр c, лінійне перетворення має зберегти це множення. Іншими словами, якщо ми застосовуємо перетворення до вектора, помноженого на c, результат повинен дорівнювати множенню перетворення вектора на c. Математично це виражається як T(cu) = cT(u).

### Як і в яких галузях застосовуються лінійні трансформації? 
1. _Електроніка_: для аналізу та проектування електричних кіл, для моделювання та прогнозування поведінки електричного кола. Це дозволяє інженерам проектувати більш ефективні та оптимізовані схеми.
2. _Сфера телекомунікацій_: для кодування та декодування аудіо- та відеосигналів, що дозволяє ефективно передавати інформацію по каналах зв’язку. При стисненні даних лінійні перетворення дозволяють зменшити розміри файлів без втрати якості інформації.
3. _Інформатика_: для виконання таких операцій, як обертання, масштабування та фільтрація зображень при обробці.
4. _Криптографія_: для безпечного шифрування та дешифрування даних.
5. _Комп'ютерна графіка_: для трансформації геометричних об'єктів, для зміни розміру, повороту, або зміщення об'єктів.
6. _Фізика_: для опису таких явищ, як обертання та відображення об’єктів у тривимірному просторі та розуміння, як змінюються координати об'єкта після застосування перетворення.
7. _Інженерія та архітектура_: у процесі проектування будівель, механізмів, транспортних засобів.

### Що таке матриця лінійної трансформації та як її можна інтерпретувати? 
**_Матриця лінійної трансформації (відображення)_** - це матриця, за допомогою якої можна подати будь-яке лінійне відображення.
Таке представлення є зручним, бо дозволяє обчислювати композицію лінійних відображень через звичайний добуток матриць.
Така матриця лінійного відображення визначена не однозначно, а залежить від вибору базисів у просторах.

Матрицю лінійної трансформації можна інтерпретувати як правило, яке описує, як кожна точка у вихідному просторі буде перетворюватися під впливом певної трансформації. Кожен стовпець матриці описує напрямок, у який вектори вхідного простору будуть переходити після застосування трансформації.

### Які особливості та властивості має матриця обертання?
1. Матриця обертання завжди є квадратною.
2. Оскільки поворот — це перетворення координат, при якому зберігаються довжини векторів, то матриця повороту є ортогональною матрицею:
обернена матриця дорівнює транспонованій матриці
3. Визначник завжди = 1.
4. Добутком матриць повороту є матриця повороту.
5. Матриця обертання зберігає відстані між точками у просторі (відстані між точками перед та після обертання залишаються незмінними).

### Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2. 
Так, фінальний результат лінійних трансформацій може змінюватися в залежності від порядку, в якому вони застосовуються.
Наприклад, якщо спочатку виконати обертання, а потім масштабування, результат буде інший, ніж якщо спочатку масштабувати, а потім обертати.
Це відбувається через те, що лінійні трансформації не комутативні, тобто порядок їх застосування впливає на кінцевий результат.
Тому важливо враховувати порядок трансформацій при їх застосуванні, особливо якщо потрібно досягти конкретного кінцевого результату.

### Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію? 
Щоб знайти матрицю лінійної трансформації, яка поверне все до початкового вигляду, потрібно знайти обернену матрицю цієї трансформації. Обернена матриця діє як зворотне перетворення, яке скасовує ефект трансформації. Її можна знайти через алгебраїчні доповнення або методом Гаусса-Жордана 
Якщо визначний матриці рівний 0, то оберненої матриці не існує і ми її не зможемо знайти.
Обернену трансформацію не завжди можна здійснити. При проектуванні векторів на координатні осі або при тривіальному нульовому перетворенні визначник матриці прямого оператора дорівнює нулю і оберненої матриціне існує.

### Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)? А якщо більше 1? Дорівнює 1? Дорівнює 0?
* Якщо модуль визначника **менше** **1**, то трансформація стискає або зменшує розмір об'єктів у просторі.
* Якщо модуль визначника **більше** **1**, то трансформація розтягує або збільшує розмір об'єктів у просторі.
* Якщо модуль визначника **дорівнює 1**, то розмір об'єктів у просторі залишається незмінним.
* Якщо модуль визначника матриці трансформації **дорівнює нулю**, то не існує оберненої матриці (до цієї).
