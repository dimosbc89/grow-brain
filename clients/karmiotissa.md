---
type: client
title: "Καρμιώτισσα (Karmiotissa, Κύπρος)"
aliases: [Karmiotissa, Καρμιώτισσα, karmiotissa.com]
status: κλειστός
updated: 2026-10-21
---
# Καρμιώτισσα (Karmiotissa)
> Κυπριακός πελάτης που ήρθε μέσω [[marketing-coach-cy]]. Η GROW είχε το domain karmiotissa.com στο [[papaki]], τα email και τα DNS. Από 2026-10 φεύγει προς Co-Win και admin22 και η GROW κρατά τα email μόνο προσωρινά.

## Σε μια ματιά
- **Υπηρεσίες GROW:** domain (Papaki), DNS, φιλοξενία email ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- **Επαφές:**
  - [[petros-goulas]] ([[marketing-coach-cy]]), ο μεσάζων ([[2026-09-16-karmiotissa-pegasus-domain-transfer]])
  - [[panayiotis-aresti]]: Marketing Manager της Co-Win, ανέλαβε το νέο site ([[2026-09-16-karmiotissa-pegasus-domain-transfer]])
  - [[andreas-nikolaou]]: Information Security Officer της admin22, που είναι το IT της Καρμιώτισσας ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
  - στην admin22, σε cc: Fedros Avraam, Thanasis Pampakas, Stefanos Panagiotou ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
  - ΠΗΓΑΣΟΣ ΠΛΗΡΟΦΟΡΙΚΗ (ticketing «ARENA GAMES»): Σίμος Χατζηκώστας (Διευθυντής) και Manolis Georgiou ([[2026-07-25-karmiotissa-tickets-a-record]])
- **Ομάδα GROW:** ο Δήμος.

## Τρέχουσα κατάσταση (στις 2026-10-20)
- **Domain:** οι nameservers άλλαξαν σε Cloudflare στις 2026-10-07 και δόθηκε auth code. Η admin22 κάνει μεταφορά registrar στο Cloudflare. Δεν είναι σαφές αν ολοκληρώθηκε η έγκριση ή η απελευθέρωση από το Papaki ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- **Email:** στις 2026-10-09 όλα λειτουργούσαν εκτός από το director@karmiotissa.com. Τα email μένουν στη φιλοξενία της GROW μέχρι να τα μεταφέρει η admin22 στους servers της, έως το τέλος Οκτωβρίου 2026 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).

## Ανοιχτά & επόμενα βήματα
- [ ] Στοιχεία πρόσβασης executivesecretary@ στον Andreas με ασφαλή τρόπο (όχι email) — Δήμος — από 2026-10-20 ([[2026-10-20-karmiotissa-aitima-kodikou-email]])
- [ ] Πρόβλημα στο director@karmiotissa.com: ο Δήμος πρότεινε reset κωδικού — admin22 να απαντήσει — από 2026-10-09 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
- [ ] Έγκριση και απελευθέρωση του transfer από το Papaki — GROW — ζητήθηκε 2026-10-07, ολοκλήρωση ασαφής ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
- [ ] Μεταφορά των email στους servers της admin22 και μετά τερματισμός της φιλοξενίας στη GROW — admin22 — έως 2026-10-31 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
- [ ] Πρόσβαση στο Pegasus για σύνδεση του ticketing με το νέο site — GROW — ζητήθηκε 2026-07-27, ασαφές αν δόθηκε ([[2026-09-16-karmiotissa-pegasus-domain-transfer]])
- [ ] Το «Email» του θέματος «ARENA GAMES - Subdomain & Email» δεν συζητήθηκε. Ασαφές αν εκκρεμεί ([[2026-07-25-karmiotissa-tickets-a-record]])
- [x] Auth code (EPP) για το domain — Δήμος — 2026-10-07. Το ζητούσε η Co-Win από 2026-07-27 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]], [[2026-09-16-karmiotissa-pegasus-domain-transfer]])
- [x] Export όλων των mailboxes (EML και MBOX ανά λογαριασμό) και των 27 DNS records — Δήμος — 2026-10-02 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
- [x] A records για το νέο site και CNAME _acme-challenge για SSL — Δήμος — 2026-09-29 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])
- [x] A record «tickets» για το tickets.karmiotissa.com — Δήμος — 2026-07-25 ([[2026-07-25-karmiotissa-tickets-a-record]])

## Αποφάσεις
- Η Καρμιώτισσα μεταφέρει site, domain και email σε άλλον πάροχο, την Co-Win/admin22 ([[2026-09-16-karmiotissa-pegasus-domain-transfer]]).
- 2026-10-07: το domain πάει στο Cloudflare, όχι σε άλλο λογαριασμό Papaki. Τα email μένουν προσωρινά στη GROW. Βλ. [[2026-10-07-karmiotissa-domain-cloudflare]] ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).

## Χρονολόγιο
- 2026-10-20 — Ο [[andreas-nikolaou]] (admin22) ζητά τον κωδικό του executivesecretary@karmiotissa.com για τη μεταφορά των emails, μέσω ασφαλούς τρόπου ([[2026-10-20-karmiotissa-aitima-kodikou-email]]).
- 2026-10-09 — Όλα τα email λειτουργούν εκτός από το director@. Ο Δήμος προτείνει reset κωδικού ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- 2026-10-07 — Ο Δήμος δίνει auth code και αλλάζει nameservers σε Cloudflare: «οκ δεν είχα ενημερωθεί για αυτό. αλλαξαν οι nameservers.» ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- 2026-10-02 — Export των mailboxes και των 27 DNS records ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- 2026-09-29 — A records για το νέο site και CNAME για SSL: «δεν έχει εφαρμοστεί το κάνουμε τωρα.» ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- 2026-09-28 — Η admin22 στέλνει «URGENT-CRITICAL»: ζητά μεταφορά της διαχείρισης του karmiotissa.com ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- 2026-09-16 — Η Co-Win ρωτά «Any update?». Από τη GROW δεν φαίνεται απάντηση ([[2026-09-16-karmiotissa-pegasus-domain-transfer]]).
- 2026-07-27 — Ο Panayiotis διευκρινίζει τι χρειάζεται: EPP/Auth Code, backup και στοιχεία μεταφοράς των email, πρόσβαση Pegasus ([[2026-09-16-karmiotissa-pegasus-domain-transfer]]).
- 2026-07-24 — Ο Petros προωθεί το αίτημα της Co-Win. Ο Δήμος: «Καλημέρα τι χρειάζεστε ακριβώς ;» ([[2026-09-16-karmiotissa-pegasus-domain-transfer]]).
- 2026-07-25 — Ο Δήμος: «Έχει περάσει το record.», για το tickets.karmiotissa.com ([[2026-07-25-karmiotissa-tickets-a-record]]).
- 2026-07-22 — Η ΠΗΓΑΣΟΣ ζητά A record για το tickets.karmiotissa.com ([[2026-07-25-karmiotissa-tickets-a-record]]).

## Οικονομικά
- Ασαφές: δεν υπάρχουν στις πηγές.
- 💭 Υπόθεση: μετά την αποχώρηση πρέπει να σταματήσουν οι χρεώσεις για domain και email και να ελεγχθεί αν υπάρχει υπόλοιπο.

## Σημειώσεις
- Το αίτημα της Co-Win (2026-07-27) έμεινε αναπάντητο περίπου 2 μήνες, ώσπου ήρθε το «URGENT-CRITICAL» της admin22 στις 2026-09-28 ([[2026-09-16-karmiotissa-pegasus-domain-transfer]], [[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- Ο [[panayiotis-aresti]] εμφανίζεται με email @co-win.io τον Ιούλιο–Σεπτέμβριο και @admin22.com τον Οκτώβριο ([[2026-09-16-karmiotissa-pegasus-domain-transfer]], [[2026-10-09-karmiotissa-metafora-domain-cloudflare]]). Η σχέση Co-Win και admin22 είναι ασαφής.
- Τα στοιχεία του auth code και του λογαριασμού Papaki δεν καταγράφονται εδώ: [στοιχείο παραλείφθηκε].
