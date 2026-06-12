# 📱 Запуск игры как мобильного приложения (Capacitor)

## Что мы сделали?
✅ PWA (Progressive Web App) версия игры готова  
✅ Offline режим (service worker)  
✅ Manifest для установки  

Теперь упакуем в реальное iOS/Android приложение через **Capacitor**.

---

## 🚀 Установка (5 минут)

### Требования:
- Node.js 14+ ([скачать](https://nodejs.org))
- Для iOS: Mac + Xcode
- Для Android: Android Studio

### Шаг 1: Инициализация проекта

```bash
# Перейди в папку игры
cd /Users/Admin/Desktop/игра

# Инициализируй новый Capacitor проект
npm init -y
npm install @capacitor/core @capacitor/cli

# Инициализируй Capacitor
npx cap init
```

Ответь на вопросы:
```
App name: Гоночная Игра
App Package ID: com.racingame.app
```

### Шаг 2: Добавь платформы

```bash
# Для iOS (только на Mac)
npx cap add ios

# Для Android (всем)
npx cap add android
```

### Шаг 3: Синхронизируй файлы

```bash
npx cap sync
```

---

## 🍎 Запуск на iOS (Mac)

```bash
# Открой проект в Xcode
npx cap open ios
```

В Xcode:
1. Выбери симулятор iPhone (вверху слева)
2. Нажми Play (▶️)
3. Готово! Игра откроется в симуляторе

**Или на реальном iPhone:**
1. Подключи iPhone к Mac
2. В Xcode: Signing & Capabilities → выбери свой аккаунт Apple
3. Build (⌘B)

---

## 🤖 Запуск на Android

```bash
# Открой проект в Android Studio
npx cap open android
```

В Android Studio:
1. Выбери виртуальный девайс (AVD Manager)
2. Нажми Run (▶️)
3. Готово!

**Или на реальном Android:**
1. Включи Developer Mode на телефоне
2. Подключи через USB
3. Run (▶️)

---

## 📦 Публикация в App Store

### iOS:
1. Созданий App ID в Apple Developer
2. В Xcode: Product → Archive
3. Upload в App Store Connect
4. Ожидай одобрения (1-3 дня)

### Android:
1. Созданий Google Play Developer аккаунт ($25)
2. В Android Studio: Build → Generate Signed Bundle
3. Upload в Google Play Console
4. Готово к публикации (несколько часов)

---

## 🔧 Обновление игры

Если изменил index.html, синхронизируй:

```bash
npx cap sync
```

Потом перезагрузи приложение в симуляторе/телефоне.

---

## ✨ Особенности PWA

- ✅ **Offline режим** — играть можно без интернета
- ✅ **Автообновление** — service worker кэширует новые версии
- ✅ **Быстрая загрузка** — благодаря кэшированию
- ✅ **Сохранение монет** — localStorage работает везде

---

## 🆘 Проблемы?

**Service Worker не работает:**
```bash
# Очистить кэш браузера
npx cap sync --fresh
```

**iOS не обновляется:**
```bash
# Полная пересборка
rm -rf ios/
npx cap add ios
npx cap open ios
```

**Android не видит изменения:**
```bash
# Полная пересборка
rm -rf android/
npx cap add android
npx cap open android
```

---

## 📊 Размеры файлов

- **PWA (веб):** ~50KB
- **iOS приложение:** ~25MB
- **Android приложение:** ~30MB

---

## 🎯 Следующие шаги

1. Установи Node.js и Capacitor
2. Запусти `npx cap init`
3. Добавь iOS/Android
4. Открой в Xcode/Android Studio
5. Запусти на симуляторе
6. Готово к публикации!

**Вопросы?** Спроси помощь по конкретному шагу 🚀
