---
type: project
title: "Tagora (Google CSS)"
aliases: [Tagora, tagora.online, hello@tagora.online]
status: ενεργός
updated: 2026-11-27
---
# Tagora
> Ελληνική υπηρεσία σύγκρισης τιμών της GROW (tagora.online) που μπαίνει στο πρόγραμμα CSS της Google, ώστε οι Shopping καμπάνιες των πελατών να τρέχουν με έως 20% φθηνότερα κλικ.

## Σε μια ματιά
- **Τι είναι:** Comparison Shopping Service της GROW· τα καταστήματα συνδέονται με XML feed ή plugin, auto-update κάθε 6 ώρες ([[2026-11-03-tagora-launch]]).
- **Όροι για πελάτες:** δωρεάν για συνεργάτες της GROW ([[2026-11-03-tagora-launch]]).
- **Domain/email:** tagora.online (GoDaddy + Cloudflare, 2026-11-03)· hello@tagora.online → dimos@ μέσω Cloudflare Email Routing ([[2026-11-03-admin-eidopoiiseis]], [[2026-11-03-tagora-launch]]).
- **Κώδικας:** repo dimosbc89/pazari, branch claude/tagora-rebrand (WooCommerce plugin) ([[2026-11-03-tagora-launch]]).
- Σχετικό: [[pricespot]] (💭 Υπόθεση: η ίδια ιδέα).

## Τρέχουσα κατάσταση (στις 2026-11-19)
- 2026-11-19 20:50: ξανά «2 καταστήματα δεν συγχρονίζονται» — **Danaos Stores και LeatherBrands** (τα προϊόντα μένουν online, τα καταστήματα ενημερώθηκαν). Η Danaos αποτυγχάνει από 2026-11-04 (**16 ημέρες**), ενώ τρέχει το Pre Black Friday της από 2026-11-19 ([[2026-11-19-tagora-danaos-leatherbrands-sync]]).
- Καταστήματα στις πηγές: [[danaos]] (feed 6.280 προϊόντα), LeatherBrands, [[nomud]] και [[tandem-concept]] (plugin, 0 προϊόντα) ([[2026-11-03-tagora-launch-update-2026-11-06]], [[2026-11-03-tagora-launch]]).
- Η έγκριση ως CSS από τη Google θέλει καταστήματα με πραγματικά προϊόντα· ανοιχτά Merchant Center store ratings και Shopping API (project tagora-css-2026) ([[2026-11-03-tagora-launch]], [[2026-11-10-admin-omada-mikra]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Sync αποτυγχάνει και για LeatherBrands (νέο, 2026-11-16· ξανά 2026-11-19) — Δήμος ([[2026-11-16-danaos-pre-black-friday]], [[2026-11-19-tagora-danaos-leatherbrands-sync]])
- [ ] Διόρθωση sync Danaos + plugin (NOMUD/Tandem 0 προϊόντα) — Δήμος ([[2026-11-03-tagora-launch-update-2026-11-06]])
- [ ] Tandem: η αίτηση μέσω plugin βρήκε 0 προϊόντα — Δήμος ([[2026-11-03-tagora-launch]])
- [ ] CI «WooCommerce plugin» απέτυχε (pazari, claude/tagora-rebrand) — Δήμος ([[2026-11-03-tagora-launch]])
- [x] ✓ Εγγραφή/feed από Danaos — Φιόλα Σκράκι — μπήκε 2026-11-04 με skroutz.xml (6.280 προϊόντα) ([[2026-11-03-tagora-launch]], [[2026-11-03-tagora-launch-update-2026-11-06]])

## Αποφάσεις
- —

## Χρονολόγιο
- **2026-11-26 21:40** — Ξανά αποτυχία sync Danaos Stores & LeatherBrands ([[2026-11-26-admin-eidopoiiseis]]).
- **2026-11-24 21:30** — Sync Danaos/LeatherBrands απέτυχε ξανά ([[2026-11-24-tagora-danaos-sync-apotyxia]]).
- **2026-11-23 21:20** — Αποτυχία sync για Danaos Stores & LeatherBrands ([[2026-11-23-tagora-danaos-sync-apotyxia]]).
- 2026-11-19 — Sync απέτυχε ξανά: Danaos Stores + LeatherBrands ([[2026-11-19-tagora-danaos-leatherbrands-sync]]).
- 2026-11-16 — Sync απέτυχε: Danaos Stores + LeatherBrands ([[2026-11-16-danaos-pre-black-friday]]).
- 2026-11-14/15 — Sync Danaos Stores απέτυχε ξανά και τις δύο μέρες ([[2026-11-14-tagora-danaos-sync-apetyxe]]).
- 2026-11-10 — Sync Danaos Stores απέτυχε ξανά (5η μέρα) ([[2026-11-10-asana-omada-mikra]]).
- 2026-11-09 — Ο sync Danaos Stores απέτυχε 4η μέρα · Shopping API support: να γραφτεί το project tagora-css-2026 με το parent CSS group account ID ([[2026-11-10-admin-omada-mikra]]).
- 2026-11-06/07/08 — Ο συγχρονισμός Danaos Stores απέτυχε ξανά και τις 3 μέρες ([[2026-11-09-admin-eidopoiiseis]]).
- 2026-11-04/05 — Αιτήσεις Danaos (6.280, skroutz.xml) και NOMUD (0, plugin)· 2 αποτυχημένα sync Danaos· το Merchant Center ζητά store ratings ([[2026-11-03-tagora-launch-update-2026-11-06]]).
- 2026-11-04 — Η Google χρειάζεται καταστήματα με πραγματικά προϊόντα για έγκριση CSS → ο Δήμος μαζεύει πελάτες GROW· pitch προς Danaos· αίτηση Tandem (0 προϊόντα)· CI fail ([[2026-11-03-tagora-launch]]).
- 2026-11-03 — Αγορά tagora.online, Cloudflare, δοκιμή email routing ([[2026-11-03-admin-eidopoiiseis]], [[2026-11-03-tagora-launch]]).

## Οικονομικά
- Δωρεάν για πελάτες GROW. Μοντέλο εσόδων: ασαφές.

## Σημειώσεις
- LeatherBrands: κατάστημα στο Tagora — αν είναι πελάτης GROW ή ποιος είναι: ασαφές (καμία σελίδα στο repo) ([[2026-11-16-danaos-pre-black-friday]]).
- Η ειδοποίηση αποτυχίας sync στέλνεται το πολύ μία φορά τη μέρα και τα καταστήματα παίρνουν email αυτόματα — άρα η Danaos βλέπει την αποτυχία κάθε μέρα από 2026-11-04 ([[2026-11-19-tagora-danaos-leatherbrands-sync]]).
