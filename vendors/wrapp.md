---
type: vendor
title: "Wrapp"
aliases: [wrapp.ai, Wrapp myDATA]
status: prospect
updated: 2026-11-25
---
# Wrapp
> Πάροχος έκδοσης παραστατικών myDATA με API· υποψήφιος για τις αποδείξεις των studios στο [[booking-app]].

## Σε μια ματιά
- **Επαφή:** Κωνσταντίνος Σκαναβής (constantinos@wrapp.ai).
- **Για τη GROW:** integration myDATA στο [[booking-app]] — κάθε studio με δικό του λογαριασμό Wrapp.

## Τρέχουσα κατάσταση
Στις 2026-11-25: απάντησε 2026-11-24 στις ερωτήσεις του Δήμου (Partners Onboarding API, Invoice API, Stripe flow, staging) και προτείνει call 25/11 15:30, 26/11 12:00 ή 27/11 15:30 ([[2026-11-24-wrapp-mydata-partners-api-studios]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Επιλογή slot για call — Δήμος ([[2026-11-24-wrapp-mydata-partners-api-studios]])
- [ ] Staging λογαριασμός + Partner API key για δοκιμές — Δήμος (💭)

## Αποφάσεις
- —

## Χρονολόγιο
- **2026-11-24** — Αναλυτική απάντηση για το μοντέλο λογαριασμού ανά studio, τιμές, Stripe + πρόταση call ([[2026-11-24-wrapp-mydata-partners-api-studios]]).

## Οικονομικά
- Ανά studio/έτος (+ΦΠΑ): Lite 109 € (6.000 παραστατικά) · Core 169 € (18.000· απαιτείται για POS) · Plus 239 € (200.000) · Max 549 € (750.000) · Ultra 1.999 € (4M). Όλα με API. Χωρίς κόστος ενεργοποίησης· πληρωμή απευθείας από το studio με κάρτα· **καμία προμήθεια για τη GROW** ([[2026-11-24-wrapp-mydata-partners-api-studios]]).

## Σημειώσεις
- Stripe: στο success webhook POST /invoices με payment_method_type 3 και external_id = Stripe id (προστασία από διπλά — 422).
