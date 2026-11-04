---
type: email-thread
thread_id: 1a1a10a40750de2d
gmail: https://mail.google.com/mail/?authuser=dimos@growagency.online#all/thread-f:1880834091064024621
date_first: 2026-11-03
date_last: 2026-11-03
subject: "New Server"
org: "HotelBrain"
participants: ["Dimitris Giannis <dgiannis@hotelbrain.com>", "Δήμος", "cc: ndaleziou@hotelbrain.com, theodleo@upatras.gr"]
---
Ώρες Αθήνας (UTC+2).

## Μηνύματα
- 2026-11-03 12:52 — ο Dimitris Giannis (Engineering & Hotel ICT Manager) ζητά πλήρη εικόνα ασφάλειας του νέου server: τύπος, datacenter/πιστοποιήσεις, firewall/WAF/DDoS, malware/monitoring, backups, disaster recovery, ευθύνη updates.
- 2026-11-03 14:11 — **ο Δήμος απαντά σημείο προς σημείο**: (1) managed Cloud VM/VPS της [[fastpath]], 8 cores / 16 GB RAM, κοινό περιβάλλον με άλλα sites (όχι dedicated)· (2) TI Sparkle MET-2, Μεταμόρφωση — ISO 27001, PCI-DSS, Tier III· (3) Fail2Ban, ModSecurity (Comodo rules), Plesk Firewall, «Under Attack Mode» κατόπιν συμβάντος· (4) ImunifyAV+ ημερήσια σάρωση 03:00, monitoring Plesk/Grafana· (5) incremental backup καθημερινά 04:00, full εβδομαδιαίο, retention 2 full, offsite κάθε 7 ημέρες· (6) DR 0–24 ώρες· (7) updates από τη GROW, κρίσιμα άμεσα.

## Εκκρεμότητες
- Αντίδραση Dimitris Giannis.
