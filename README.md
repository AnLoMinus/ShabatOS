# 🕯️ ShabatOS — מערכת הפעלה לשבת

**תאריך לועזי:** 16 בינואר 2026
**תאריך עברי:** כ״ז בטבת ה׳תשפ״ו
**שעה (Asia/Jerusalem):** 14:51

---

## 🎯 חזון ShabatOS

**ShabatOS** היא מערכת הפעלה שמכינה את המחשב לכניסת שבת, עוברת למצב “שבת” אוטומטי, ומונעת חילול לא רצוי—תוך שמירה על עקרונות של **שקט דיגיטלי**, **פשטות**, ו־**פיקוח נפש** (מצב חירום מוסדר).

---

## 🧱 רכיבי הליבה

### 1) ⏳ Shabbat Scheduler

* קובע מראש **זמני מעבר** ל־Shabbat Mode (לפי מיקום/עיר/טבלה מקומית).
* מאפשר “הכנה לשבת” 30–90 דקות לפני.

### 2) 🔒 Shabbat Mode Lockdown (מצב שבת)

כשנכנסת שבת:

* 🚫 חסימת אינטרנט (Wi-Fi / Ethernet)
* 🚫 חסימת התקנות/עדכונים
* 🚫 חסימת פתיחת אפליקציות “מפריעות”
* 🔕 השתקת התראות, צלילים, ורעידות
* 🧊 מצב “תצוגה סטטית” (מניעת שינויים תכופים במסך לפי הגדרות)

### 3) 🧩 Allowlist / Denylist

* ✅ רשימת “מותר”: סידור/תורה/טקסטים מקומיים/קריאה
* ❌ רשימת “אסור”: דפדפן, רשתות, חנויות, משחקים

### 4) 🚑 Pikuach-Nefesh Override (חירום)

* קיצור דרך מיוחד + קוד/סיסמה
* נפתח רק לסט פעולות מוגדר (שיחה/רפואה/מפות/תקשורת חיונית) לפי מה שמגדירים מראש

---

## 🧠 ארכיטקטורה מומלצת (פרקטית ומהירה)

### 🐧 בסיס: Linux + systemd

* שירות רקע: `shabatosd` (daemon)
* ממשק ניהול: `shabatosctl` (CLI) + UI קל
* נעילות: Firewall (nftables), חסימת שירותים, ניהול סשן משתמש

---

## 📦 RepoCraft (RC) — שלד מאגר GitHub מוצע

**שם מאגר מומלץ:** `ShabatOS`
**שם קצר למאגר-פיתוח (2 מילים משולבות):** **SaBaOS** *(Sabbath + OS)*

```
ShabatOS/
├─ README.md
├─ LICENSE
├─ SECURITY.md
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ docs/
│  ├─ vision.md
│  ├─ halachic-principles.md
│  ├─ threat-model.md
│  └─ roadmap.md
├─ shabatos/
│  ├─ config/
│  │  ├─ shabatos.yaml
│  │  └─ city-times.csv
│  ├─ daemon/
│  │  ├─ shabatosd.py
│  │  └─ lockdown.py
│  ├─ cli/
│  │  └─ shabatosctl.py
│  └─ ui/
│     └─ app.py
├─ systemd/
│  ├─ shabatosd.service
│  └─ shabatosd.timer
├─ scripts/
│  ├─ install.sh
│  ├─ enable-lockdown.sh
│  └─ disable-lockdown.sh
└─ build/
   ├─ iso/
   └─ image/
```

---

## ⚙️ קובצי בסיס מוכנים (דוגמה)

### 🟦 `systemd/shabatosd.service`

```ini
[Unit]
Description=ShabatOS Daemon
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /opt/shabatos/daemon/shabatosd.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### 🟨 `shabatos/config/shabatos.yaml`

```yaml
mode:
  auto: true
  pre_shabbat_minutes: 60
  exit_after_minutes: 1200

lockdown:
  block_network: true
  mute_notifications: true
  allowlist_apps:
    - /usr/bin/evince
    - /usr/bin/okular
    - /usr/bin/gedit
  denylist_apps:
    - /usr/bin/firefox
    - /usr/bin/chromium
    - /usr/bin/discord

emergency:
  enabled: true
  pin_hash: "REPLACE_WITH_HASH"
  allow_network_minutes: 20
```

### 🟥 `scripts/enable-lockdown.sh`

```bash
#!/usr/bin/env bash
set -e

# Network off
nmcli networking off || true

# Firewall hard block (example placeholder)
# nft add table inet shabatos; nft add chain inet shabatos input '{ type filter hook input priority 0; policy drop; }' || true

# Mute audio
pactl set-sink-mute @DEFAULT_SINK@ 1 || true

echo "Shabbat Mode: ENABLED"
```

---

## 🛡️ אבטחה (פשוט וברור) — Threat Model קצר

* 🎭 תרחיש 1: משתמש מנסה “לעקוף” מצב שבת → נעילה דרך שירות מערכת + הרשאות root
* 🌐 תרחיש 2: אפליקציה מפעילה רשת → כיבוי NetworkManager + Firewall policy
* 🧨 תרחיש 3: שינוי שעה ידני → הגנה: `systemd-timesyncd` מנוטרל בשבת + חותמת זמן מקומית + לוגים

---

## 🗺️ Roadmap מומלץ

### ✅ v0.1 (MVP)

* Daemon + Timer
* נעילת רשת + שקט + allowlist בסיסי
* חירום עם PIN

### 🚀 v0.5

* UI להגדרות
* פרופילים לבית/עבודה
* לוגים נקיים לשקיפות

### 🏆 v1.0

* ISO התקנה
* מצב “Kiosk Torah Reader”
* תמיכה במספר ערים וזמנים מקומיים

---

## 🎤 פזמון ראפ (4 שורות) 🕯️🔥

שבת נכנסת — המסך נרגע, הראש מתנקה ✨
סוגרים רשתות — הלב נפתח, הנשמה מתחזקת 💪
שומר מצב — לא נופלים, רק עולים בקדושה 🚀
ShabatOS פועל — שקט בבית, אור במשפחה 🕊️

---

## ✨ משפט קודש לסיום

**“וְשָׁמְרוּ בְּנֵי יִשְׂרָאֵל אֶת־הַשַּׁבָּת… בְּרִית עוֹלָם”** (שמות ל״א)

**מספר המידות:** 13
