---
type: decision
title: "Hotel sites HotelBrain: read-only API sync από WebHotelier αντί για scraping"
aliases: [webhotelier sync, multi-property api]
status: ενεργός
updated: 2026-10-20
---
# Hotel sites HotelBrain: read-only API sync από WebHotelier
> Αποφασίστηκε ότι τα static data των ξενοδοχείων θα συγχρονίζονται από το API της [[webhotelier]] στα WordPress sites της GROW και όχι με scraping. Αφορά 4 sites και 90 καταλύματα.

## Σε μια ματιά
- **Sites:** [[mr-mrs-white]] (23), [[anayia]] (24), September City Living (2), GHH (41) ([[2026-09-14-hotelbrain-webhotelier-api]]).
- **Ποιος:** ο Δήμος (αρχιτεκτονική), η [[niki-daleziou]] (σύσταση στη WebHotelier), η WebHotelier (Άγγελος Λώλης) ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Τρέχουσα κατάσταση (στις 2026-10-20)
- Η WebHotelier περιμένει από 2026-09-14 τη λίστα codes του GHH και επιβεβαίωση για ένα Multi-Property API account ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Mapping (property name, WordPress record, booking-engine URL, property code) — Δήμος (υπόσχεση 2026-09-11) ([[2026-09-14-hotelbrain-webhotelier-api]])
- [ ] Λίστα codes GHH και επιβεβαίωση account — GROW — από 2026-09-14 ([[2026-09-14-hotelbrain-webhotelier-api]])

## Αποφάσεις
- **Τι αποφασίστηκε** ([[2026-09-14-hotelbrain-webhotelier-api]]):
  - read-only sync μία φορά την ημέρα, με cache στη βάση του WordPress
  - mapping με property, room και rate codes
  - endpoints: Property Search, Room Listing, Rate Listing, και infourl για Property Info
  - το marketing και SEO περιεχόμενο μένει στο WordPress
  - οι κρατήσεις γίνονται στο booking engine (WebHotelier Site Integration)
- **Εναλλακτική:** data scraping. Ο Δήμος το απέρριψε: «δεν είναι σωστή μεθοδολογία» ([[2026-09-14-hotelbrain-webhotelier-api]]).
- **Γιατί:** η HotelBrain ήθελε τα sites να τραβάνε δεδομένα αυτόματα, όπως το hotelbrain.com ([[2026-09-02-hotelbrain-webhotelier-data-sync]]). Το «from price» μέσω των Availability APIs είχε απορριφθεί από τη WebHotelier τον Μάρτιο 2026 ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Χρονολόγιο
- 2026-09-14 — Η WebHotelier προτείνει Multi-Property API account ([[2026-09-14-hotelbrain-webhotelier-api]]).
- 2026-09-02 — Αίτημα της HotelBrain για αυτόματο sync ([[2026-09-02-hotelbrain-webhotelier-data-sync]]).
- 2026-03 — Απόρριψη του BAR / Availability APIs ([[2026-09-14-hotelbrain-webhotelier-api]]).

## Οικονομικά
- Ασαφές.
- **Τεχνικά όρια:** rate limit 50 req/s ([[2026-09-14-hotelbrain-webhotelier-api]]).
