const CACHE_NAME = 'racing-game-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/manifest.json'
];

// Установка service worker
self.addEventListener('install', (event) => {
  console.log('Service Worker: установка...');
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('Service Worker: кэширование файлов');
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// Активация service worker
self.addEventListener('activate', (event) => {
  console.log('Service Worker: активация...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Service Worker: удаление старого кэша', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Перехват запросов
self.addEventListener('fetch', (event) => {
  // Только GET запросы
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((response) => {
      // Если в кэше, вернуть оттуда
      if (response) {
        return response;
      }

      // Иначе, загрузить из сети
      return fetch(event.request).then((response) => {
        // Если сеть недоступна, вернуть кэшированный файл
        if (!response || response.status !== 200 || response.type === 'error') {
          return response;
        }

        // Кэшировать новые ответы
        const responseToCache = response.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });

        return response;
      }).catch(() => {
        // Если сеть не работает, вернуть кэш
        return caches.match(event.request);
      });
    })
  );
});
