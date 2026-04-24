const CACHE_NAME = 'get-fit-v1';

// We don't necessarily need to cache everything for a simple showcase,
// but an active fetch listener is REQUIRED by browsers to trigger the PWA install prompt.
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(clients.claim());
});
