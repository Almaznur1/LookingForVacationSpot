# LookingForVacationSpot - Study Project

* [Демо-версия сайта](http://77.223.99.110:8000)
* [Панель администратора](http://77.223.99.110:8000/admin/)
* [Проект на GitHub](https://github.com/Almaznur1/LookingForVacationSpot)

 # Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](./site.png)


## Как добавить новую локацию

* Откройте [панель администратора](https://almaznuriakhmetov.pythonanywhere.com/admin)
* В левой колонке выберите `Места`
* Вы можете добавить новую локацию и отредактировать имеющиеся

## Как запустить

Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

* Скачайте код с [GitHub](https://github.com/Almaznur1/LookingForVacationSpot)

Перед запуском необходимо настроить переменные окружения. В репозитории имеется файл `.env.example` со следующим содержанием:

```
SECRET_KEY=<put here your secret key>
ALLOWED_HOSTS=localhost,127.0.0.1,<add here your website address>
DEBUG=<set False for development and True for production>
```

* Переименуйте его в `.env` и занесите в него настройки вашего сайта

```
* SECRET_KEY=<секретный ключ, с помощью которого шифруются пароли пользователей вашего сайта>

* ALLOWED_HOSTS=<[Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django.]>

* DEBUG=<Выставьте True, чтобы видеть отладочную информацию при разработке сайта. Значение False стоит по умолчанию>
```

* Сделайте миграцию БД

```
python manage.py makemigrations places
python manage.py migrate
```

* Запустите сервер при помощи `manage.py`


```
python .\manage.py runserver
```

* Откройте в браузере страницу с данными посетителей хранилища по следующему адресу:

`127.0.0.1:8000`

## Тестовые данные

Загрузите [тестовые данные](https://github.com/devmanorg/where-to-go-places), чтобы увидеть как это работает:

Для этого запустите команду:

```
python manage.py load_place http://адрес/файла.json
```

Json файл должен быть следующего формата:
```
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
