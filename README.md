Курсовая работа по Джанго

Заполните ".env.sample" своими данными и переименуйте его в ".env"

Для создания суперпользователя: python manage.py create_admin

Для запуска сайта: python manage.py runserver


DevBlog

v.2.1
1. Модель Blog
2. CRUD для Blog
3. Главная страница выводит статистику, и популярные блоги

v.2
1. Настройка периодических задач
2. Скрипт отправки рассылок

v.1.4.1
1. На главной отображаются только кнопки к контроллерам которых у пользователя есть доступ
2. При создании пользователя ему назначается группа
3. Стандартизированные карточки, и прочий визуал 

v.1.4
1. На все контроллеры работы с рассылками добавлен PermissionRequiredMixin
2. Добавлены группы manager, user, admin
3. Пользователь может видеть/изменять/удалять только свои объекты
4. Модератор может видеть все рассылки, а изменять только статус, бан пользователей реализован через is_active
5. Админ может почти всё

v.1.3
1. Регистрация пользователя, верификация почты
2. Логин, выход
3. Редактирование профиля
4. Ограничения доступа для не авторизованных пользователей

v.1.2
1. Исправлена логика связей моделей между собой
2. CRUD для Client
3. CRUD для Mailing
4. Read контроллеры для MailingTry

v1.1
1. Базовые html страница, навигация, вывод главной
2. CRUD для Message

v.1
1. Приложение mailings
2. Модели Message, Client, Mailing, MailingTry
3. Приложение main

v.0
1. Установлены базовые библиотеки для работы сайта
2. Все чувствительные данные засекречены
3. Добавлена модель User