---
type: playbook
title: "Playbook — demo Booking App για studio"
updated: 2026-11-28
---
# Playbook — demo Booking App για studio
> Πώς στήνεται ένα demo του [[booking-app]] για υποψήφιο studio και πώς τρέχει ο κύκλος call → προσφορά, από την πρώτη περίπτωση: «Pilates by Anastasia» (2026-11-25 → 27). Πηγή: [[log]], [[booking-app]].

## Χρονοδιάγραμμα (πραγματικό)
| Βήμα | Ημ/νία ώρα | Διάρκεια | Πηγή |
|---|---|---|---|
| Call A. Mavrou (AM Pilates) | 2026-11-25 12:00–13:00 | 1 ώρα | [[2026-11-25_2026-12-02]] |
| Demo v1 στο growagency.online/demo (branding, δεδομένα στον browser) | 13:10 | 10′ | [[log]] |
| Μεταφορά σε δικό του Cloudflare worker με βάση (κοινά δεδομένα σε όλες τις συσκευές) | 13:25 | 15′ | [[log]] |
| Live στο workers.dev · υπηρεσίες Pilates + Pilates Cardio (αλλαγή Δήμου) | 13:30–13:45 | 20′ | [[log]] |
| Προσφορά με link demo στην πελάτισσα | 14:23 | ~1,5 ώρα μετά το call | [[2026-11-25-booking-app-am-pilates-prosfora]] |
| Online αγορά πακέτων — Stripe Checkout (test mode) | 2026-11-27 15:15 | | [[log]] |
| Viva Smart Checkout δίπλα στο Stripe, επιλογή ανά studio | 15:55 | 40′ | [[log]] |
| Stripe test + Viva demo συνδεδεμένα live | 16:20 | 25′ | [[log]] |

## Funnel εβδομάδας 23–27/11
- 10 calls με 9 studios → **6 προσφορές** (Breathe, Μαύρου, [[roppas-studio]], Αθανασία, Bosoultherapy, Εμμανουέλα) → **0 απαντήσεις, 0 υπογραφές** έως 27/11 · 1 no-show (Μελικίδης 27/11) · 4 calls χωρίς προσφορά ακόμα (Κουντούρης, Pavlova, Γκότσης, Μίχου) ([[booking-app]], [[2026-11-27-weekly-report-data]]).
- Τιμές καταλόγου: από 49 €/μήνα + ΦΠΑ, setup από 180 € ([[prices]]). myDATA μέσω [[wrapp]] (λογαριασμός ανά studio, 0 € ενεργοποίηση, Lite 109 € / Core 169 €/έτος).

## Τι στράβωσε
1. v1 με δεδομένα στον browser → ξαναφτιάχτηκε server-side 15′ μετά.
2. Demo με όνομα συγκεκριμένου studio στάλθηκε και σε άλλο studio (Ρόππας).
3. Το demo password γράφτηκε στη σελίδα του εγκεφάλου (αφαιρέθηκε 2026-11-28).
4. «CHECK MAIL» → προσφορά στάλθηκε 3′ μετά, πριν τον έλεγχο του Δήμου.
5. Διπλό ραντεβού 30/11 14:00 · call που έχασε η Μαρίνα 20/11.
6. Καμία προσφορά δεν έχει follow-up με ημερομηνία.

## Checklist για την επόμενη φορά
- [ ] Demo server-side από την αρχή (worker + βάση, noindex), με **ουδέτερο** όνομα όταν πάει σε τρίτους.
- [ ] Υπηρεσίες/πακέτα του studio από το call, πριν το demo.
- [ ] Πληρωμή: ρώτα στο call Stripe ή Viva· σχέδιο απόδειξης myDATA (Wrapp) **πριν** ενεργοποιηθούν πληρωμές.
- [ ] Προσφορά ίδια μέρα με το call — με 15′ περιθώριο για έλεγχο Δήμου αν ζητηθεί.
- [ ] Follow-up κάθε προσφοράς σε 3 εργάσιμες, με ημερομηνία στο Asana.
- [ ] Κωδικοί demo/test ποτέ στο repo.
- [ ] Εκκρεμεί: πλήρης δοκιμαστική πληρωμή, απόδειξη myDATA, μεταφορά κώδικα στο Vanessa app.
