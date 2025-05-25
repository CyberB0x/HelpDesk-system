# HelpDesk System

Простая система поддержки пользователей (HelpDesk) на Django. Поддерживает создание заявок, переписку по заявкам, роли пользователей и авторизацию.

## 📦 Возможности

- Регистрация и авторизация пользователей
- Создание заявок (tickets)
- Просмотр всех заявок и детализация
- Переписка внутри заявки
- Админка для управления
- Email-уведомления (можно подключить)
- Поддержка ролей (администратор, сотрудник, пользователь)

---

## 🛠️ Установка

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/your-username/helpdesk-system.git
   cd helpdesk-system
```

## Установите зависимости:
```commandline
   pip install -r requirements.txt

```

## Настройте базу данных в settings.py (MySQL):
```commandline
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'helpdesk_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
## 💽 Структура проекта

```commandline
   helpdesk/
│
├── tickets/                # Приложение с заявками
│   ├── models.py           # Модели Ticket, Message
│   ├── views.py            # Представления
│   ├── forms.py            # Формы
│   ├── templates/tickets/  # Шаблоны
│   └── urls.py             # URL-ы
│
├── templates/              # Базовые HTML-шаблоны
├── static/                 # CSS/JS (если есть)
├── helpdesk/               # Настройки Django
│
├── manage.py
└── requirements.txt

```
## 📬 Контакты
* Автор: Arslon
* Проект для портфолио
* Email-уведомления можно добавить через EmailMessage и send_mail.