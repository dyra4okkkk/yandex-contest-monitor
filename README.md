
# Yandex Contest Monitor 🚀

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Requests](https://img.shields.io/badge/library-requests-brightgreen)
![Concurrency](https://img.shields.io/badge/architecture-multithreading-orange)

*(🇷🇺 Русская версия находится ниже / Russian version is below)*

**Yandex Contest Monitor** is a highly concurrent OSINT and data scraping tool designed to monitor and discover hidden or upcoming programming contests and exams on the Yandex Contest platform. 

Initially developed to automate the discovery of academic assignments, the tool utilizes robust multithreading and TCP connection pooling to efficiently scan thousands of endpoints in seconds.

## ⚙️ Features
* **High-Speed Network I/O:** Uses `concurrent.futures.ThreadPoolExecutor` and `requests.Session()` to maximize throughput while minimizing resource footprint.
* **Smart Filtering:** Bypasses generic registration walls and strictly matches HTML payloads against configurable search patterns.
* **Environment Configuration:** Secure handling of authorization cookies via `.env` files (Zero hardcode).
* **Fault-Tolerant:** Gracefully handles network timeouts and HTTP errors without crashing the main thread pool.

## 🛠️ Stack & Architecture
* **Language:** Python
* **Core Libraries:** `requests`, `python-dotenv`, `concurrent.futures`

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/dyra4okkkk/yandex-contest-monitor.git](https://github.com/dyra4okkkk/yandex-contest-monitor.git)
   cd yandex-contest-monitor

```

2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Configure the environment:**
Copy the example config and add your authorization cookie.
```bash
cp .env.example .env

```


*Edit `.env` and paste your Yandex `raw_cookie` along with target ID ranges.*
4. **Customize Search Patterns:**
By default, the script looks for specific keywords. Open `src/config.py` and modify the `SEARCH_PATTERNS` list to include the exact words or phrases you are looking for in the contest HTML:
```python
# Example: Change this to your target keywords
SEARCH_PATTERNS = ["Data Structures", "2026"]
#in scraper.py change this
if "Зарегистрироваться" in html: #"Register" if english
```


5. **Run the monitor:**
```bash
python src/main.py

```



---

# Yandex Contest Monitor 🚀 (🇷🇺 Русский)

**Yandex Contest Monitor** — это высокопроизводительный OSINT-инструмент и парсер данных, предназначенный для поиска скрытых или предстоящих соревнований и экзаменов по программированию на платформе Яндекс Контест.

Инструмент был разработан для автоматизации поиска академических заданий. Он использует многопоточность и переиспользование TCP-соединений (Connection Pooling) для эффективного сканирования тысяч эндпоинтов за секунды.

## ⚙️ Особенности

* **Высокая скорость сетевого I/O:** Использование `concurrent.futures.ThreadPoolExecutor` и `requests.Session()` для максимизации пропускной способности.
* **Умная фильтрация:** Инструмент обходит стандартные страницы регистрации и ищет точные совпадения по заданным паттернам в HTML.
* **Безопасная конфигурация:** Работа с авторизационными куки через файлы `.env` (никакого хардкода).
* **Отказоустойчивость:** Корректная обработка сетевых таймаутов и HTTP-ошибок без падения основного пула потоков.

## 🛠️ Стек и Архитектура

* **Язык:** Python
* **Библиотеки:** `requests`, `python-dotenv`, `concurrent.futures`

## 🚀 Установка и Запуск

1. **Клонируйте репозиторий:**
```bash
git clone [https://github.com/dyra4okkkk/yandex-contest-monitor.git](https://github.com/dyra4okkkk/yandex-contest-monitor.git)
cd yandex-contest-monitor

```


2. **Установите зависимости:**
```bash
pip install -r requirements.txt

```


3. **Настройте окружение:**
Скопируйте шаблон конфигурации и добавьте ваши данные.
```bash
cp .env.example .env

```


*Отредактируйте файл `.env`, вставив ваш `raw_cookie` от Яндекса и нужные диапазоны ID.*
4. **Настройте паттерны поиска:**
По умолчанию скрипт ищет определенные ключевые слова. Откройте файл `src/config.py` и измените список `SEARCH_PATTERNS`, чтобы он содержал те слова или фразы, которые нужны именно вам:
```python
# Пример: Измените эти значения на нужные вам ключевые слова
SEARCH_PATTERNS = ["АиСД", "2026"]

```


5. **Запустите мониторинг:**
```bash
python src/main.py

```


