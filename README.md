# LookingForVacationSpot - Study Project

* [Демо-версия сайта](https://www.pythonanywhere.com/user/AlmazNuriakhmetov)
* [Панель администратора](https://www.pythonanywhere.com/user/AlmazNuriakhmetov/admin)
* [Проект на GitHub](https://github.com/Almaznur1/LookingForVacationSpot)

 # Куда пойти — Москва глазами Артёма

Сайт о самых интересных местах в Москве. Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)


## Как добавить новую локацию

* Откройте [панель администратора](https://www.pythonanywhere.com/user/AlmazNuriakhmetov/admin)
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
python manage.py migrate
```

* Запустите сервер при помощи `manage.py`


```
python .\manage.py runserver
```

* Откройте в браузере страницу с данными посетителей хранилища по следующему адресу:

`127.0.0.1:8000`

## Тестовые данные

Тестовые данные можно получить на странице [GitHub](https://github.com/devmanorg/where-to-go-places).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
