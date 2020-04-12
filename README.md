# weatherBodyabottg
 Telegram Bot with OpenWeather API for Yandex.Cloud by Bogdan Pugin
<hr>
Для второго задания отбора в школу будущих CTO выбрал Умный сервис прогноза погоды, уровень со звездочкой, который подразумевает непосредственно рекомендации пользователю как одеться по погоде.

<h3> Язык программирования, технологии, интерфейс и формат ответа пользователю</h3>

Язык программирования - Python.
Использованные технологии - [OpenWeatherMap API](https://openweathermap.org/), [Telegram Bot API](https://core.telegram.org/bots/api).
Интерфейс программы - чат бот в мессенджере Telegram.
Формат ответа пользователю - данные о текущей погоде, полученные от [OpenWeatherMap API](https://openweathermap.org/) подставляются в текстовый шаблон ответа бота:

"⛅️ В городе [Название города на русском/английском в любом регистре] сейчас [облачно/ясно/пасмурно/etc.]

🔥 Температура приблизительно [Округленное значение температуры в градусах цельсия] градусов"

Далее, пользователь получает рекомендации по одежде, которые также основаны на данных от API, Пример:

"Рекомендации по одежде:

🌁 Достаточно тепло - можно идти без куртки

☀️ Дождя нет - зонт не пригодится"
                              
<h3>Видео работы программы</h3> 

Доступ по ссылке: https://youtu.be/oHHJEstbPYQ

После записи видео внес микро измения в шаблон рекомендаций по одежде.

<h3>Поэтапный процесс работы программы</h3>
 Cервис - чат-бот, который по введенному пользователем городу выдает информацию о погоде, а также рекомендации, как одеться, чтобы было комфортно на улице
<ol>
 <li>Получение данных от пользователя с помощью интерфейса мессенджера Telegram</li>
 <li>Формирование запроса к OpenWeatherMap API</li>
 <li>Отправка запроса к OpenWeatherMap API</li>
 <li>Получение ответа от OpenWeatherMap API</li>
 <li>Формирование ответа пользователю с помощью текстового шаблона</li>
 <li>Отправка ответа или сообщение об ошибке пользователю</li>
</ol>

<h3>Как запустить программу</h3>
 <ol>
 <li>Загрузить репозиторий с https://github.com/bodyaswag/weatherBodyabottg/</li>
 <li>Открыть и запустить проект в редакторе кода</li>
 <li>Открыть мессенджер Telegram и найти в поиске @weatherBodyabot</li>
 <li>Взаимодействовать с ботом</li>
 <li>PROFIT</li>
</ol>
