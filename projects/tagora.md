---
type: project
title: "Tagora (Google CSS)"
aliases: [Tagora, tagora.online, hello@tagora.online]
status: ενεργός
updated: 2026-11-17
---
# Tagora
> Ελληνική υπηρεσία σύγκρισης τιμών της GROW (tagora.online) που μπαίνει στο πρόγραμμα CSS της Google, ώστε οι Shopping καμπάνιες των πελατών να τρέχουν με έως 20% φθηνότερα κλικ.

## Σε μια ματιά
- **Τι είναι:** Comparison Shopping Service της GROW· τα καταστήματα συνδέονται με XML feed ή plugin, auto-update κάθε 6 ώρες ([[2026-11-03-tagora-launch]]).
- **Όροι για πελάτες:** δωρεάν για συνεργάτες της GROW ([[2026-11-03-tagora-launch]]).
- **Domain/email:** tagora.online (GoDaddy + Cloudflare, 2026-11-03)· hello@tagora.online → dimos@ μέσω Cloudflare Email Routing ([[2026-11-03-admin-eidopoiiseis]], [[2026-11-03-tagora-launch]]).
- **Κώδικας:** repo dimosbc89/pazari, branch claude/tagora-rebrand (WooCommerce plugin) ([[2026-11-03-tagora-launch]]).
- Σχετικό: [[pricespot]] (💭 Υπόθεση: η ίδια ιδέα).

## Τρέχουσα κατάσταση (στις 2026-11-17)
- 2026-11-16 20:20: νέα ειδοποίηση «2 καταστήματα δεν συγχρονίζονται» — **Danaos Stores και LeatherBrands**· τα υπάρχοντα προϊόντα μένουν online, τα καταστήματα ενημερώθηκαν ([[2026-11-16-danaos-pre-black-friday]]).
- Danaos Stores μέσα με feed (6.280 προϊόντα) αλλά **sync απέτυχε 4/11 και 5/11**· νέα αίτηση [[nomud]] με **0 προϊόντα** (plugin)· Merchant Center ζητά store ratings ([[2026-11-03-tagora-launch-update-2026-11-06]]).

*Από 2026-11-04:*
- Η Google χρειάζεται καταστήματα με πραγματικά προϊόντα για να εγκρίνει το Tagora ως CSS — ο Δήμος μαζεύει πελάτες GROW. Πρώτο pitch στη [[danaos]]· πρώτη αίτηση από [[tandem-concept]] (0 προϊόντα) ([[2026-11-03-tagora-launch]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Sync αποτυγχάνει και για LeatherBrands (νέο, 2026-11-16) — Δήμος ([[2026-11-16-danaos-pre-black-friday]])
- [ ] Διόρθωση sync Danaos + plugin (NOMUD/Tandem 0 προϊόντα) — Δήμος ([[2026-11-03-tagora-launch-update-2026-11-06]])
- [ ] Tandem: η αίτηση μέσω plugin βρήκε 0 προϊόντα — Δήμος ([[2026-11-03-tagora-launch]])
- [ ] CI «WooCommerce plugin» απέτυχε (pazari, claude/tagora-rebrand) — Δήμος ([[2026-11-03-tagora-launch]])
- [ ] Εγγραφή/feed από Danaos — Φιόλα Σκράκι ([[2026-11-03-tagora-launch]])

## Αποφάσεις
- —

## Χρονολόγιο
- 2026-11-16 — Sync απέτυχε: Danaos Stores + LeatherBrands ([[2026-11-16-danaos-pre-black-friday]]).
- 2026-11-14/15 — Sync Danaos Stores απέτυχε ξανά και τις δύο μέρες ([[2026-11-14-tagora-danaos-sync-apetyxe]]).
- 2026-11-10 — Sync Danaos Stores απέτυχε ξανά (5η μέρα) ([[2026-11-10-asana-omada-mikra]]).
- 2026-11-09 — Ο sync Danaos Stores απέτυχε 4η μέρα · Shopping API support: να γραφτεί το project tagora-css-2026 με το parent CSS group account ID ([[2026-11-10-admin-omada-mikra]]).
- 2026-11-06/07/08 — Ο συγχρονισμός Danaos Stores απέτυχε ξανά και τις 3 μέρες ([[2026-11-09-admin-eidopoiiseis]]).
- 2026-11-04/05 — Αιτήσεις Danaos (6.280) και NOMUD (0)· 2 αποτυχημένα sync Danaos ([[2026-11-03-tagora-launch-update-2026-11-06]]).
- 2026-11-04 — Pitch προς Danaos· αίτηση Tandem (0 προϊόντα)· CI fail ([[2026-11-03-tagora-launch]]).
- 2026-11-03 — Αγορά tagora.online, Cloudflare, δοκιμή email routing ([[2026-11-03-admin-eidopoiiseis]], [[2026-11-03-tagora-launch]]).

## Οικονομικά
- Δωρεάν για πελάτες GROW. Μοντέλο εσόδων: ασαφές.

## Σημειώσεις
- —
