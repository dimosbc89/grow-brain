---
type: email-thread
thread_id: 19caeff7d55732c8
gmail: https://mail.google.com/mail/?authuser=dimos@growagency.online#all/thread-f:1858561643958973128
date_first: 2026-03-02
date_last: 2026-09-14
subject: "RE: ΑPI HOTELS HOTELBRAIN"
org: "HotelBrain (Mr & Mrs White Hotels, ANAYIA, September City Living, GHH) × WebHotelier"
participants: ["Άγγελος Λώλης <dev@webhotelier.net> — Application Support Engineer, webhotelier | primalres", "Niki Daleziou <ndaleziou@hotelbrain.com> — Digital Marketing Manager, HOTELBRAIN S.A.", "<panos@hotelbrain.com> — HotelBrain (ρόλος ασαφής)", "Dimosthenis Chrisanthopoulos <dimos@growagency.online> — Founder, GROW Agency (κατασκευή & τεχνική υποστήριξη websites)"]
---
## Τι συμβαίνει
Τον Μάρτιο ο Δήμος ζήτησε από τη WebHotelier API πρόσβαση (endpoint BAR) για να δείχνει "from price" στα δωμάτια του mrandmrswhitehotels.com (B2C)· η WebHotelier αρνήθηκε πρόσβαση σε Availability APIs και το έθεσε εσωτερικά, χωρίς νεότερα μετά τις 16/3. Τον Σεπτέμβριο ο Δήμος επανέφερε το θέμα μέσω HotelBrain (Niki), ζητώντας read-only συγχρονισμό static data (περιγραφές, room types, facilities, policies, φωτογραφίες, booking URLs) για 4 sites: mrandmrswhitehotels.com (23), anayiaresorts.com (24), septembercityliving.com (2), ghh.gr (41)· booking μέσω WebHotelier Site Integration. Η WebHotelier (14/9) μπορεί να εκδώσει Multi-Property API account, αλλά για τα 41 του GHH χρειάζεται λίστα property codes για να φτιάξει συγκεντρωτικό source.
## Αποφάσεις
- Αρχιτεκτονική: read-only API sync 1 φορά/ημέρα με cache στη βάση WordPress, mapping με property/room/rate codes· marketing/SEO περιεχόμενο μένει στο WordPress· κρατήσεις στο booking engine.
- Endpoints: Property Search, Room Listing, Rate Listing (+ infourl για Property Info).
## Δεσμεύσεις του Δήμου
- Να στείλει αναλυτικό mapping (property name, WordPress record, booking-engine URL, property code) για επιβεβαίωση scope (υπόσχεση 11/9).
## Εκκρεμότητες
- GROW → WebHotelier: λίστα property codes GHH και επιβεβαίωση αν θέλουν ένα Multi-Property API account για όλα τα 90 καταλύματα (ζητήθηκε 14/9).
- WebHotelier: έκδοση credentials μετά την επιβεβαίωση.
## Ποσά & προθεσμίες
- Rate limit static data: 50 requests/δευτερόλεπτο· IP allowlisting προαιρετικό.
- 90 καταλύματα συνολικά (23 + 24 + 2 + 41).
## Ύφος του Δήμου
- "θα μπορούσα να κάνω data scrapping αλλα δεν είναι σωστή μεθοδολογία"
- "Ναι κάνε μας την σύσταση και αναλαμβάνουμε εμείς."
