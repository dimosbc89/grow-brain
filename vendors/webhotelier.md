---
type: vendor
title: "WebHotelier"
aliases: [webhotelier, webhotelier.net, primalres, WebHotelier API]
status: ενεργός
updated: 2026-10-20
---
# WebHotelier
> Booking engine και πηγή δεδομένων για τα ξενοδοχεία της [[hotelbrain]]. Η GROW χρειάζεται το API της για να συγχρονίζει τα στατικά δεδομένα στα hotel websites που φτιάχνει.

## Σε μια ματιά
- **Ρόλος:** booking engine (WebHotelier Site Integration) και API για ([[2026-09-14-hotelbrain-webhotelier-api]]):
  - static data: περιγραφές, room types, facilities, policies, φωτογραφίες, booking URLs
  - availability
- **Επαφή:** Άγγελος Λώλης (dev@webhotelier.net), Application Support Engineer, webhotelier | primalres ([[2026-09-14-hotelbrain-webhotelier-api]]).
- **Πελάτες GROW που αφορά:**
  - [[mr-mrs-white]] (23 καταλύματα)
  - [[anayia]] (24)
  - September City Living (2)
  - GHH / ghh.gr (41)

  Σύνολο 90 καταλύματα ([[2026-09-14-hotelbrain-webhotelier-api]]).
- **Ομάδα GROW:** ο Δήμος. Από την πλευρά της HotelBrain: [[niki-daleziou]], [[panos-paleologos]].

## Τρέχουσα κατάσταση (στις 2026-10-20)
- Στις 2026-09-14 η WebHotelier είπε ότι μπορεί να εκδώσει Multi-Property API account. Πρώτα χρειάζεται τη λίστα με τα property codes του GHH, για να φτιάξει συγκεντρωτικό source για τα 41 καταλύματα, και επιβεβαίωση. Η GROW δεν έχει απαντήσει ακόμα στο thread ([[2026-09-14-hotelbrain-webhotelier-api]]).
- Τα Availability APIs (BAR, για «from price») απορρίφθηκαν τον Μάρτιο 2026. Από τις 16/3 δεν υπάρχουν νέα ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Λίστα property codes GHH και επιβεβαίωση ενός Multi-Property API account για και τα 90 καταλύματα — GROW (Δήμος) — ζητήθηκε 2026-09-14 ([[2026-09-14-hotelbrain-webhotelier-api]])
- [ ] Αναλυτικό mapping (property name, WordPress record, booking-engine URL, property code) — Δήμος (υπόσχεση 2026-09-11) ([[2026-09-14-hotelbrain-webhotelier-api]])
- [ ] Έκδοση credentials — WebHotelier — μετά την επιβεβαίωση ([[2026-09-14-hotelbrain-webhotelier-api]])
- [ ] Πρόσβαση στα Availability APIs (BAR) — WebHotelier — εκκρεμεί εσωτερικά από 2026-03 ([[2026-09-14-hotelbrain-webhotelier-api]])

## Αποφάσεις
- Read-only sync μία φορά την ημέρα. Βλ. [[2026-09-14-hotelbrain-webhotelier-api-sync]] ([[2026-09-14-hotelbrain-webhotelier-api]]).
- **Endpoints:** Property Search, Room Listing, Rate Listing, και infourl για Property Info ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Χρονολόγιο
- 2026-09-14 — Απάντηση για το Multi-Property API account, με αίτημα για τη λίστα codes του GHH ([[2026-09-14-hotelbrain-webhotelier-api]]).
- 2026-09 — Ο Δήμος ξαναθέτει το θέμα μέσω της HotelBrain: «Ναι κάνε μας την σύσταση και αναλαμβάνουμε εμείς.» ([[2026-09-14-hotelbrain-webhotelier-api]]).
- 2026-09-02 — Η HotelBrain ρωτά αν τα sites μπορούν να τραβάνε δεδομένα αυτόματα. Ο Δήμος: η WebHotelier δεν έδινε πρόσβαση API ([[2026-09-02-hotelbrain-webhotelier-data-sync]]).
- 2026-03-16 — Τελευταία νέα για το αίτημα BAR ([[2026-09-14-hotelbrain-webhotelier-api]]).
- 2026-03-02 — Ο Δήμος ζητά πρόσβαση στο endpoint BAR για το mrandmrswhitehotels.com ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Οικονομικά
- Κόστος για το API: ασαφές.
- **Τεχνικά όρια:** rate limit 50 requests/δευτερόλεπτο για τα static data· IP allowlisting προαιρετικό ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Σημειώσεις
- Τα API credentials, όταν εκδοθούν, δεν γράφονται εδώ: [στοιχείο παραλείφθηκε].
