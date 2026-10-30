---
type: admin
title: "Hosting, servers & domains"
aliases: [hosting, servers, domains, cloud.growagency.online, Plesk, Fastpath, Cretaforce, Papaki, Enartia]
status: ενεργός
updated: 2026-10-30
---
# Hosting, servers & domains
> Οι servers της GROW (Plesk στη [[fastpath]]) και οι registrars ([[papaki]]/[[enartia]], [[cretaforce]]) όπου η GROW κρατά τα domains των πελατών. Κάθε ανανέωση domain ξανατιμολογείται στον πελάτη.

## Σε μια ματιά
- **Server:** cloud.growagency.online στη [[fastpath]]: Special Managed Services + Plesk License, περίοδος χρέωσης 01–30/09 (💭 πιθανώς μηνιαία) ([[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]]). Σε αυτόν τον server ταιριάζει η προτίμηση του Δήμου για Plesk / File Manager ([[rules]]).
- **Registrars:**
  - [[papaki]] ([[enartia]]): στέλνει e-invoices μέσω Entersoft. Εκεί είναι και domains πελατών, π.χ. baristacademy.gr ([[2026-09-10-enartia-papaki-timologia]], [[2026-08-27-baristacademy-domain-expiration]]).
  - [[cretaforce]]: π.χ. pharmacypan.gr και argyroplastics.gr ([[2026-09-07-cretaforce-pharmacypan-domain-renewal]], [[2026-10-14-cretaforce-domain-argyroplastics]]).
- **Πελάτες με domain/hosting στη GROW** (όσο φαίνεται εδώ):
  - [[pharmacypan]]
  - [[nikas-coffee-expert]] (baristaexpert.gr, baristacademy.gr, barista-academy.gr)
  - [[academicals-foxacademy]] (academicals.gr, email)
  - [[argyroplastics]] (argyroplastics.gr)
  - [[karmiotissa]] (σε μεταφορά προς Cloudflare)
  - [[overoll]] (overoll.us και overoll.shop, τα αγόρασε η GROW)
  - Πηγές: [[2026-09-07-cretaforce-pharmacypan-domain-renewal]], [[2026-09-10-invoice-nikas-barista-domains]], [[2026-09-28-fastpath-ticket-ssh-academicals]], [[2026-10-14-cretaforce-domain-argyroplastics]], [[2026-10-09-karmiotissa-metafora-domain-cloudflare]], [[2026-10-14-overoll-websites-domains]].
- **Ομάδα:**
  - [[vassiliki-giannopoulou]]: τιμολόγια παρόχων.
  - [[marina-papanastasiou]]: τιμολόγηση domains στους πελάτες, θέματα registrar.
  - Ο Δήμος: τεχνικά (tickets, DNS).

## Τρέχουσα κατάσταση
Στις 2026-10-20:
- **Επείγον:** Η [[fastpath]] ειδοποίησε ότι το προτιμολόγιο #58712 (cloud.growagency.online, περίοδος 2026-09-01→30) είναι ανεξόφλητο. Οι υπηρεσίες έχουν προγραμματιστεί για απενεργοποίηση. Μετά την απενεργοποίηση τα δεδομένα κρατούνται 7 ημέρες και μετά διαγράφονται. Ο Δήμος απάντησε «θα ταχτοποιηθεί μέχρι Παρασκευή», δηλαδή έως 2026-10-23 ([[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]]).
- Το ticket 004632 για SSH στα mailboxes του academicals.gr περιμένει ακόμη απάντηση ([[2026-09-28-fastpath-ticket-ssh-academicals]]).

## Ανοιχτά & επόμενα βήματα
- [ ] **Cloudflare Tunnel: αναβάθμιση κάθε cloudflared σε 2026.10.2+** (macOS χωρίς Homebrew 2026.10.3+· Docker image 2026.10.3) λόγω compromised eMudhra certificates — Δήμος — «as soon as possible», ειδοποίηση 2026-10-26· ποιο host τρέχει το tunnel: ασαφές ([[2026-10-26-admin-eidopoiiseis]])
- [ ] **Wordfence 2026-10-27/28: castrum-milos.com «JetEngine» 3.8.4.1 → 3.9.0.1 (Critical 9.8/10)** + Yoast 26.9 → 28.8 + UpdraftPlus· bikos-derma.gr Yoast 20.5 → 28.8· barolobeach.gr Safe SVG 2.4.0 → 2.5.2· foxacademy.gr The Plus Addons 6.4.16 → 6.6.0· logaraslaw.com CookieYes 3.4.2 → 3.5.8· baristacademy.gr WPBakery + Ultimate Addons αποτυγχάνουν στο auto-update (ξανά) — Δήμος/τεχνικός — castrum **άμεσα** ([[2026-10-28-admin-eidopoiiseis]])
- [ ] Wordfence: update «Really Simple Security» στο foxacademy.gr (9.6.0 → 9.8.4, **High 8.8/10**) και στο pagopolis.gr (9.8.3 → 9.8.4)· «Super Forms» στο baristacademy.gr (6.3.322 → 6.3.323) — Δήμος — από 2026-10-27 ([[2026-10-26-admin-eidopoiiseis]])
- [ ] goldenvisagreece.online **έληξε 2026-10-21** (Papaki) — ανανέωση ή όχι; — Δήμος ([[2026-10-24-admin-eidopoiiseis]])
- [ ] lucaffe.gr: προειδοποίηση λήξης (FORTH, 2026-10-25) — [[nikas-coffee-expert]] — ημερομηνία ασαφής ([[2026-10-24-admin-eidopoiiseis]])
- [ ] Ανανέωση machevuoi.gr ή όχι — Δήμος — **έως 2026-11-04** ([[2026-10-20-machevuoi-gr-lixi-domain]])
- [ ] **Εξόφληση Fastpath #58712: 507,78 €**. Αλλιώς διακόπτεται το cloud.growagency.online και ό,τι φιλοξενεί (ποια sites: ασαφές) — Δήμος — **άμεσα**: η Fastpath δεν έδωσε προθεσμία, η διακοπή είναι ήδη προγραμματισμένη· ο Δήμος υποσχέθηκε έως 2026-10-23 ([[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]])
- [ ] Απάντηση της Fastpath στο ticket 004632: το SSH key δεν έχει πρόσβαση στα mailboxes του academicals.gr (χρειάζεται για backup και διαγραφή παλιών email) — Fastpath — ανοιχτό από 2026-09-28 ([[2026-09-28-fastpath-ticket-ssh-academicals]]). Σχετικά: [[academicals-foxacademy]]
- [ ] Εκδόθηκε το τιμολόγιο προς [[pharmacypan]] («Τιμολόγιο Πανόπουλος») για την ανανέωση του pharmacypan.gr; — Μαρίνα/Βασιλική — ασαφές (λήξη domain 2026-09-14) ([[2026-09-07-cretaforce-pharmacypan-domain-renewal]])
- [ ] Τιμολόγιο προς [[nikas-coffee-expert]] για 3 domains (25 € + ΦΠΑ το καθένα) — Μαρίνα — ασαφές αν εκδόθηκε ([[2026-09-10-invoice-nikas-barista-domains]])
- [ ] Επικοινωνία με τον [[giorgos-tzortzopoulos]] για το argyroplastics.gr, όπως ζήτησε η Cretaforce — Δήμος/Μαρίνα — ανοιχτό από 2026-10-14 ([[2026-10-14-cretaforce-domain-argyroplastics]])
- [ ] Η GROW φιλοξενεί τα email της [[karmiotissa]] μέχρι να τα μεταφέρει η admin22 — GROW — έως ~2026-10-31 ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]])

## Αποφάσεις
- 2026-09-01 — Δεν επεκτείνουμε το storage στους servers της GROW για τα email της Academicals (~100 €/μήνα). Προτείνεται Microsoft Exchange Online ή αρχειοθέτηση ([[2026-09-01-academicals-foxacademy-email-storage]]).
- Κάθε ανανέωση domain πελάτη ξανατιμολογείται στον πελάτη (π.χ. «Τιμολόγιο Πανόπουλος», «25 + fpa to kathena») ([[2026-09-07-cretaforce-pharmacypan-domain-renewal]], [[2026-09-10-invoice-nikas-barista-domains]]).

## Χρονολόγιο
- 2026-10-30 — Wordfence: ενεργή εκμετάλλευση RCE στο upgrade-window (λύση: WP 7.1.4). Νέα alerts: logaraslaw, barolobeach, foxacademy, baristacademy, pagopolis, susurrousclothing, montessori-littleland ([[2026-10-30-admin-eidopoiiseis]]).
- 2026-10-28 — WordPress 7.1.4 αυτόματα σε 9 sites (και castrum-milos)· νέα Wordfence alerts σε exodikastikos, baristacademy, foxacademy, barolosantorini, bikos-derma, poullaides, montessori-littleland, tsiklitiria, susurrous (lockout + admin login)· Papaki WHOIS για marketingagencygreece.online ([[2026-10-29-admin-eidopoiiseis]]).
- 2026-10-27/28 — Wordfence: **castrum-milos.com JetEngine Critical 9.8** (+Yoast, UpdraftPlus)· foxacademy.gr The Plus Addons (6.4)· bikos-derma.gr Yoast 20.5 → 28.8· barolobeach.gr Safe SVG· logaraslaw.com CookieYes (medium)· baristacademy.gr επανάληψη Super Forms, αποτυχία auto-update WPBakery/Ultimate Addons και ληγμένη Easy Appointments connection ([[2026-10-28-admin-eidopoiiseis]]).
- 2026-10-26/27 — Cloudflare: [Action Required] αναβάθμιση cloudflared σε 2026.10.2+. Wordfence: foxacademy.gr critical (Really Simple Security, +18 παλιά issues), baristacademy.gr medium (Super Forms, +4), pagopolis.gr medium (Really Simple Security, +7) και lockout 4 ωρών μετά από 20 αποτυχημένα login με username «dimos» από IP στη Βραζιλία (💭 Υπόθεση: brute-force). baristacademy.gr: Easy Appointments connection ληγμένη από 2022-12-31. Enartia: νέο e-invoice μέσω Entersoft ([[2026-10-26-admin-eidopoiiseis]]).
- 2026-10-25 — Papaki: goldenvisagreece.online ληγμένο από 2026-10-21· FORTH: λήξη lucaffe.gr· Wordfence alerts baristacademy.gr (connection expiring, αποτυχία ενημέρωσης plugins, problems found) και susurrousclothing.com (admin login, lockout 24/10) ([[2026-10-24-admin-eidopoiiseis]]).
- 2026-10-20 — Το machevuoi.gr (Papaki, GROW AGENCY EE) λήγει 2026-11-04· FASTPATH «αναμένουμε την εξόφληση» ([[2026-10-20-machevuoi-gr-lixi-domain]], [[2026-10-20-fastpath-apantisi-ticket]]).
- 2026-10-19/20 — Fastpath, ticket 836805: «Διακοπή υπηρεσιών λόγω οφειλών». Ο Δήμος υποσχέθηκε εξόφληση έως 2026-10-23 ([[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]]).
- 2026-10-14 — Cretaforce: τους πήρε τηλέφωνο ο ιδιοκτήτης του argyroplastics.gr. Επειδή το domain το διαχειρίζεται η GROW, ζητούν να επικοινωνήσει ο Δήμος. Προωθήθηκε στη Μαρίνα ([[2026-10-14-cretaforce-domain-argyroplastics]]).
- 2026-10-07 — Δύο e-invoices Enartia/Papaki → Βασιλική ([[2026-10-07-enartia-papaki-timologia]]).
- 2026-10-07 — Τα nameservers του karmiotissa.com άλλαξαν σε Cloudflare. Το domain φεύγει από το Papaki της GROW ([[2026-10-09-karmiotissa-metafora-domain-cloudflare]]).
- 2026-09-28 — Ticket Fastpath 004632 για SSH στα mailboxes του academicals.gr, χαμηλή προτεραιότητα ([[2026-09-28-fastpath-ticket-ssh-academicals]]).
- 2026-09-10 — Τέσσερα e-invoices Enartia/Papaki μέσω Entersoft (PDF + peppol XML) → Βασιλική ([[2026-09-10-enartia-invoice-notification]], [[2026-09-10-enartia-papaki-timologia]]). Ίδια μέρα: σημείωμα τιμολόγησης 3 domains του Nikas ([[2026-09-10-invoice-nikas-barista-domains]]).
- 2026-09-07 — Cretaforce: ανανέωση του pharmacypan.gr για 2 έτη (λήξη 2026-09-14), 16,47 € → Μαρίνα/Βασιλική, «Τιμολόγιο Πανόπουλος» ([[2026-09-07-cretaforce-pharmacypan-domain-renewal]]).
- 2026-08-27 — Ειδοποίηση λήξης του baristacademy.gr (2026-09-11 23:59 UTC). Registrar: Enartia/papaki ([[2026-08-27-baristacademy-domain-expiration]]).

## Οικονομικά
| Στοιχείο | Ποσό | Χρεώνεται σε | Πηγή |
|---|---|---|---|
| Fastpath #58712: Special Managed Services (Σεπτ. 2026) | 387,50 € | GROW | [[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]] |
| Fastpath #58712: Plesk License | 22,00 € | GROW | [[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]] |
| Fastpath #58712: ΦΠΑ 24% | 98,28 € → **σύνολο 507,78 €** | GROW | [[2026-10-20-fastpath-diakopi-ypiresion-ofeiles]] |
| pharmacypan.gr, 2 έτη (Cretaforce) | 13,28 € + ΦΠΑ = 16,47 € | [[pharmacypan]] | [[2026-09-07-cretaforce-pharmacypan-domain-renewal]] |
| 3 domains Nikas | 25 € + ΦΠΑ το καθένα | [[nikas-coffee-expert]] | [[2026-09-10-invoice-nikas-barista-domains]] |
| Enartia/Papaki e-invoices (2026-09-10 ×4, 2026-10-07 ×2) | ποσά μόνο στα PDF | GROW | [[2026-09-10-enartia-papaki-timologia]], [[2026-10-07-enartia-papaki-timologia]] |
| Επέκταση storage email Academicals (απορρίφθηκε) | ~100 €/μήνα | — | [[2026-09-01-academicals-foxacademy-email-storage]] |

## Σημειώσεις
- 💭 Υπόθεση: Η Fastpath χρεώνει μηνιαία (η περίοδος 01–30/09 είναι ένας μήνας), άρα έρχεται νέο προτιμολόγιο κάθε μήνα. Οι πηγές δεν το επιβεβαιώνουν.
- 💭 Υπόθεση: Τα 6 e-invoices της Enartia αφορούν ανανεώσεις domains (π.χ. baristacademy.gr). Οι πηγές δεν λένε ποια domains.
- Τεχνικά ο Δήμος δουλεύει μόνος του τα tickets και τα DNS records. Στα tickets γράφει σύντομα: «Προσπαθώ να συνδεθώ στα email boxes με ssh για να τραβήξω κάποια back up» ([[2026-09-28-fastpath-ticket-ssh-academicals]]).
- Auth codes, κωδικοί, τραπεζικά παρόχων: [στοιχείο παραλείφθηκε].
