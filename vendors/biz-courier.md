---
type: vendor
title: "BIZ Courier & Logistics"
aliases: [BIZ Courier, Biz, ebiz, BIZ Courier & Logistics S.A., bizcourier.eu, BIZ LiNK]
status: ενεργός
updated: 2026-10-20
---
# BIZ Courier & Logistics
> Courier και 3PL (αποθήκη/WMS) που έχει επιλέξει η [[tandem-concept]]. Η GROW συνδέει το WooCommerce e-shop της Tandem με τη BIZ μέσω API / BIZ LiNK και ετοιμάζει το BOX NOW.

## Σε μια ματιά
- **Ρόλος:** αποθήκη και αποστολές του e-shop tandemconcept.gr. Το e-shop εξυπηρετείται από την αποθήκη Biz Courier ([[2026-09-24-tandem-eshop-quantities]])· warehouse «BIZ GR Koropi» (προς επιβεβαίωση) ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]]).
- **Τεχνικά:** API / Web Service (SOAP neworder), plugin BIZ LiNK για WooCommerce (σήμερα 1.1.28· αναβάθμιση σε 1.3.2+ και BIZ LiNK FF 1.3.0+ για BOX NOW), BIZ LiNK Onboarding Questionnaire ([[2026-09-14-tandem-bizcourier-it-coordination]], [[2026-10-12-bizcourier-bizlink-fix-boxnow]], [[2026-10-12-bizcourier-woocommerce-admin-boxnow]]).
- **Επαφές:** [[aliki-theochari]] (Director of Customer Success· κύρια επαφή για integration και BOX NOW)· [[jose-fernando-trujillo-heron]] (Business Development and Marketing Specialist· εμπορικά, τιμοκατάλογος Box Now)· itsupport@ (τεχνική ομάδα)· customersupport@, georgia@, i.gorobets@ ([[2026-09-14-tandem-bizcourier-it-coordination]], [[2026-10-12-bizcourier-bizlink-fix-boxnow]], [[2026-08-26-online-appointment-bizcourier-tandem]]).
- **Ομάδα GROW:** ο Δήμος.

## Τρέχουσα κατάσταση (στις 2026-10-20)
- Στις 2026-10-12 η GROW έφτιαξε compatibility layer για το Add Supply (κενά bookings χωρίς προϊόντα) και έστειλε 6 τεχνικές ερωτήσεις πριν την αναβάθμιση για BOX NOW. Η Aliki έβαλε στο thread την τεχνική ομάδα· απάντηση δεν φαίνεται ([[2026-10-12-bizcourier-bizlink-fix-boxnow]]).
- Ο Δήμος ζήτησε ενεργοποίηση του BOX NOW και τα αρχεία, αφού πήρε τον οδηγό Scribe (2026-10-12) ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Απαντήσεις στις 6 ερωτήσεις: θα υπάρχει η διόρθωση στη νέα έκδοση; neworder; απενεργοποίηση του layer; αλλαγές σε payload/SOAP; διατήρηση ρυθμίσεων/mapping; θέλουν patch; — BIZ itsupport@ — από 2026-10-12 ([[2026-10-12-bizcourier-bizlink-fix-boxnow]])
- [ ] Ενεργοποίηση «Biz FF Last Mile Locker (BOX NOW) GR», Service Code, plugins BIZ LiNK 1.3.2+ / FF 1.3.0+, επιβεβαίωση warehouse, συμβατότητα WooCommerce & PHP 8.3 — BIZ — από 2026-10-12 ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]])
- [ ] Ρύθμιση BOX NOW — Δήμος — μετά τις οδηγίες της BIZ ([[2026-10-12-bizcourier-bizlink-fix-boxnow]])
- [ ] Αν υπογράφηκε ο τιμοκατάλογος Box Now — ασαφές ([[2026-09-07-biz-courier-boxnow-codes]])
- [ ] Αλλαγή του admin κωδικού που στάλθηκε με απλό email στις 2026-09-18 — GROW — χωρίς ημερομηνία ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]])
- [x] Onboarding Questionnaire — Δήμος — 2026-09-14 ([[2026-09-14-tandem-bizcourier-it-coordination]])
- [x] Admin λογαριασμός WooCommerce για τη BIZ — Δήμος — 2026-09-18 ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]])

## Αποφάσεις
- [[2026-10-12-bizlink-compatibility-layer]]: compatibility layer της GROW χωρίς αλλαγή στον κώδικα του BIZ LiNK· κανένα BOX NOW πριν τις οδηγίες· κανένα credential ή δεδομένο πελάτη με email.
- Η διασύνδεση γίνεται μέσω API / BIZ LiNK για WooCommerce ([[2026-09-14-tandem-bizcourier-it-coordination]]).
- Το Box Now μπαίνει στα sender profiles του WooCommerce μόνο αφού ολοκληρωθεί το integration (θέση BIZ, 2026-09-07) ([[2026-09-07-biz-courier-boxnow-codes]]).
- Τα χαμένα δέματα αποζημιώνονται με βάση το τιμολόγιο αγοράς του προϊόντος (θέση BIZ) ([[2026-08-26-online-appointment-bizcourier-tandem]]).

## Χρονολόγιο
- 2026-10-12 — Fix στο Add Supply και ερωτήσεις για BOX NOW ([[2026-10-12-bizcourier-bizlink-fix-boxnow]])· οδηγός Scribe για BOX NOW Locker Delivery ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]]).
- 2026-09-18 — Η BIZ ζητά admin στο WordPress/WooCommerce· η πρόσκληση δεν δουλεύει και ο Δήμος στέλνει password reset και στοιχεία σύνδεσης [διαπιστευτήρια παραλείφθηκαν] ([[2026-10-12-bizcourier-woocommerce-admin-boxnow]]).
- 2026-09-14 — Το store είναι έτοιμο· το questionnaire έγραφε Shopify, ο Δήμος πήρε το σωστό link για WooCommerce και απάντησε «Finished» ([[2026-09-14-tandem-bizcourier-it-coordination]]).
- 2026-09-08 — Call Δήμου–Aliki 14:00 («Αλίκη biz courier call») ([[2026-09-07-biz-courier-boxnow-codes]], [[2026-07-20_2026-11-03]]).
- 2026-09-07 — Ο Δήμος: «Now is everything ready can we have the codes from box now» ([[2026-09-07-biz-courier-boxnow-codes]]).
- 2026-09-01 — Ο Δήμος λέει στην Tandem ότι το 3PL Bridge είναι έτοιμο και θα πάρει διευκρινίσεις από την Aliki ([[2026-09-01-tandem-epsilon-eshop-bridge]]).
- 2026-08-28 — Online meeting με Tandem και λογιστή: πωλήσεις εκτός ΕΕ, χαμένα δέματα, αποστολές & επιστροφές ([[2026-08-26-online-appointment-bizcourier-tandem]], [[2026-07-20_2026-11-03]]).
- 2026-06-04 — Ο George ζητά κωδικούς Box Now και διαδικασία επίσπευσης για προϊόντα από το φυσικό κατάστημα ([[2026-09-07-biz-courier-boxnow-codes]]).
- 2026-05-22 → 2026-05-29 — Account, Client Activation Letter, Web Service Integration Guide. Ο Δήμος είχε ζητήσει docs, credentials (sandbox → production), λίστα services, rate limits και technical contact ([[2026-09-14-tandem-bizcourier-it-coordination]]).
- 2026-04-27 — Ο George συστήνει τον Δήμο στη BIZ ([[2026-09-14-tandem-bizcourier-it-coordination]]).

## Οικονομικά
- Τιμοκατάλογος Box Now: αναφέρεται, ποσά δεν φαίνονται ([[2026-09-07-biz-courier-boxnow-codes]]).
- Τη σύμβαση με τη BIZ την έχει η Tandem, όχι η GROW ([[2026-09-14-tandem-bizcourier-it-coordination]]).

## Σημειώσεις
- Τα τεχνικά emails του Δήμου προς τη BIZ είναι τυπικά και πλήρως δομημένα, με επικεφαλίδες και λίστες ([[2026-10-12-bizcourier-bizlink-fix-boxnow]]).
- Η BIZ αργεί: οι κωδικοί Box Now εκκρεμούν από τον Ιούνιο ([[2026-09-07-biz-courier-boxnow-codes]]).
- Από παλαιότερες συνομιλίες: emails για BIZ Courier WMS/API ([[2026-10-20-prohgoumenes-synomilies-claude]]).
