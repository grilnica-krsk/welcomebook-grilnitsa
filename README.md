# Welcome Book — Грильница

> Защищённая интерактивная книга для быстрого введения новых сотрудников в компанию "Грильница"

## 🔐 Информация о безопасности

**Обфусцированный путь:** `wb-4c2e0a519df3`

**⚠️ ВАЖНО:** Сразу после публикации на GitHub Pages:

1. **Сгенерируйте хеш пароля** (откройте консоль браузера F12):
   ```javascript
   async function sha256(message) {
     const msgBuffer = new TextEncoder().encode(message);
     const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
     const hashArray = Array.from(new Uint8Array(hashBuffer));
     return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
   }
   
   // Замените "ВАШ_ПАРОЛЬ" на реальный пароль
   await sha256("ВАШ_ПАРОЛЬ");
   ```

2. **Замените хеш в файле** `wb-4c2e0a519df3/index.html`:
   - Найдите строку: `const VALID_HASH = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855';`
   - Замените на ваш сгенерированный хеш

3. **Обновите URL для QR-кода** в том же файле:
   - Найдите строку: `const bookURL = 'https://YOUR_USERNAME.github.io/welcomebook-grilnitsa/wb-4c2e0a519df3/';`
   - Замените `YOUR_USERNAME` на ваш GitHub username

4. **Закоммитьте изменения**:
   ```bash
   git add wb-4c2e0a519df3/index.html
   git commit -m "feat: обновлен пароль и URL для QR-кода"
   git push
   ```

## 📋 Структура проекта

```
welcomebook-grilnitsa/
├── .nojekyll                    # Отключает Jekyll
├── robots.txt                   # Блокирует индексацию
├── 404.html                     # Кастомная страница ошибки
├── index.html                   # Корневая заглушка
└── wb-4c2e0a519df3/            # Обфусцированная директория
    └── index.html               # Защищённый Welcome Book
```

## 🚀 Публикация на GitHub Pages

### Шаг 1: Создание репозитория

1. Перейдите на https://github.com/new
2. **Repository name:** `welcomebook-grilnitsa`
3. **Description:** `Welcome Book для новых сотрудников`
4. **Visibility:** Public (для бесплатного GitHub Pages)
5. Не добавляйте README, .gitignore, license
6. Нажмите **Create repository**

### Шаг 2: Подключение и публикация

```bash
# Подключите remote (замените YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/welcomebook-grilnitsa.git

# Отправьте код
git branch -M main
git push -u origin main
```

### Шаг 3: Настройка GitHub Pages

1. Перейдите в **Settings** → **Pages**
2. **Source:** Deploy from a branch
3. **Branch:** main / (root)
4. Нажмите **Save**

Через 1-2 минуты сайт будет доступен по адресу:
```
https://YOUR_USERNAME.github.io/welcomebook-grilnitsa/
```

### Шаг 4: Финальный URL для сотрудников

```
https://YOUR_USERNAME.github.io/welcomebook-grilnitsa/wb-4c2e0a519df3/
```

**Этот URL нужно:**
- Распространять только новым сотрудникам
- Преобразовать в QR-код (см. ниже)
- Не публиковать в открытых источниках

## 📱 Генерация QR-кода

### Вариант 1: Онлайн (рекомендуется)

1. Откройте https://www.qr-code-generator.com/
2. Вставьте финальный URL
3. Скачайте в высоком разрешении (PNG/SVG)

### Вариант 2: Python

```python
import qrcode

url = "https://YOUR_USERNAME.github.io/welcomebook-grilnitsa/wb-4c2e0a519df3/"

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("welcomebook_qr.png")
```

## 🔑 Управление паролем

### Смена пароля

1. Сгенерируйте новый SHA-256 хеш (см. раздел "Информация о безопасности")
2. Обновите `VALID_HASH` в файле `wb-4c2e0a519df3/index.html`
3. Закоммитьте и запушьте изменения
4. GitHub Pages обновится через 1-2 минуты

### Рекомендации

- Используйте сложный пароль (минимум 12 символов)
- Сообщайте пароль отдельно от ссылки
- Меняйте пароль раз в квартал
- Не используйте очевидные пароли

## 📷 Добавление фотографий команды

После публикации останется добавить фотографии в два раздела:

### PAGE 4: КОМАНДА (управляющие)

**Где:** секция `.team-placeholder`  
**Что добавить:**
- Фото управляющих и топ-менеджмента
- ФИО и должности
- QR-код на видео-визитку (опционально)

### PAGE 5: СТАРОЖИЛЫ (ветераны)

**Где:** секция `.veteran-placeholder` (3 блока)  
**Что добавить:**
- Фото сотрудника
- Имя и ресторан
- Стаж в компании
- Карьерный рост
- Цитата «Почему мне нравится здесь работать»

## ✅ Чек-лист после публикации

- [ ] Сгенерирован и установлен SHA-256 хеш пароля
- [ ] Обновлён URL для QR-кода в JavaScript
- [ ] Изменения закоммичены и запушены
- [ ] GitHub Pages настроен (main branch, root)
- [ ] Welcome Book открывается по финальному URL
- [ ] Password Gate работает корректно
- [ ] Сгенерирован QR-код с финальным URL
- [ ] Протестирован доступ через QR-код
- [ ] Пароль передан HR отдельно от ссылки

## 🛡️ Уровни защиты

1. **Обфусцированный URL** — случайная директория `wb-4c2e0a519df3`
2. **Password Gate** — SHA-256 хеш пароля на клиентской стороне
3. **Robots.txt** — блокировка всех поисковых роботов
4. **Meta noindex** — дополнительная защита от индексации
5. **Отсутствие навигации** — нет ссылок с главной страницы

## 📞 Контакты

**Отдел персонала "Грильница"**  
Телефон: +7 995 524-29-97  
Telegram: https://t.me/+DSZkMa4Hx6AxNTAy

---

**Создано с помощью Claude Code**  
Версия: 1.0.0  
Дата: 2026-06-12
