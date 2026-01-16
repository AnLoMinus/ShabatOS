# ✅ מה חסר לפני “הקודקס” — ShabatOS

**SaBaOS (Sabbath + OS)**

**📅 תאריך לועזי:** 16 בינואר 2026
**📅 תאריך עברי:** כ״ז בטבת ה׳תשפ״ו
**⏰ שעה (Asia/Jerusalem):** 15:12

מה שרואים כרגע במאגר: יש לך `README.md`, `guideline.md`, `roadmap.md` ותיקיית `.github/workflows`—אבל עדיין אין את שלד הקבצים/קוד שה־README עצמו מציע (docs/, systemd/, scripts/, shabatos/ וכו’). ([GitHub][1])

---

## 🧱 1) שלד מאגר חובה להטמעה (Repo Skeleton)

אלה קבצים שחסרים כדי שהמאגר “יעמוד על רגליים”:

* 📜 `LICENSE` (רישוי ברור)
* 🛡️ `SECURITY.md` (דיווח חולשות + מדיניות)
* 🤝 `CONTRIBUTING.md` (איך תורמים נכון)
* 🧑‍⚖️ `CODE_OF_CONDUCT.md` (התנהלות קהילה)
* 🧾 `CHANGELOG.md` (היסטוריית גרסאות)
* 🗺️ `docs/`:

  * 📄 `vision.md`
  * 📄 `halachic-principles.md`
  * 📄 `threat-model.md`
  * 📄 `architecture.md` (החלטות מערכת + גבולות)
  * 📄 `faq.md` (מה מותר/אסור, חירום, וכו’)

> למה זה קריטי? כי כרגע ה־README מתאר מבנה מלא—אבל המאגר בפועל עוד לא מכיל אותו. ([GitHub][1])

---

## ⚙️ 2) קוד מינימלי (MVP) שצריך להיות בפנים

כדי שהקודקס “יתפוס” על משהו אמיתי, תטמיע מינימום:

### 🧩 Core

* 📁 `shabatos/config/shabatos.yaml` (קונפיג יחיד, נקי, מתועד)
* 📁 `shabatos/daemon/shabatosd.py` (תזמון + טריגרים)
* 📁 `shabatos/daemon/lockdown.py` (יישום נעילות)
* 📁 `shabatos/cli/shabatosctl.py` (פקודות: status/enable/disable/test)

### 🕰️ systemd

* 📁 `systemd/shabatosd.service`
* 📁 `systemd/shabatosd.timer`

### 🧰 scripts

* 📁 `scripts/install.sh` (העתקה, הרשאות, enable)
* 📁 `scripts/enable-lockdown.sh`
* 📁 `scripts/disable-lockdown.sh`

---

## 🛡️ 3) “נעילה אמיתית” — מה חסר בהקשחה

כאן שווה להשלים לפני הקודקס כדי שלא תבנה על בסיס חלש:

* 🌐 **Network Kill Switch כפול**: גם `nmcli off` וגם חומת־אש (nftables/ufw) כ־fallback
* ⏱️ **מניעת עקיפה דרך שינוי שעה**: בדיקות sanity (סטיות זמן קיצוניות → alert/log)
* 🔒 **Allowlist קשיח**: אם אפליקציה לא ברשימה → נחסמת (לא “רק להזהיר”)
* 📣 **לוגים לא־רגישים**: רק מה שצריך, בלי מידע אישי

---

## 🧪 4) בדיקות + CI לפני “ריצה על אמת”

בתוך `.github/workflows` כבר יש לך תיקייה, אבל כדי שהקודקס יעבוד נקי, כדאי לוודא שיש:

* ✅ בדיקות יחידה (pytest) לרכיבי scheduler/lockdown
* ✅ “Dry Run Mode” שמדמה שבת בלי לנתק באמת (לבדיקות)
* ✅ CI שמריץ lint + tests על כל push/pr
* ✅ “Safety Gate”: אם בדיקות נכשלות → אין merge

---

## 📦 5) גרסאות, תיוגים והפצה

לפני שאתה מפעיל קודקס שמייצר מהלכים אוטומטיים:

* 🏷️ גרסה קבועה: `VERSION` אחת (למשל `0.1.0`)
* 🧾 `CHANGELOG.md` עם תבנית
* 📌 GitHub Releases (גם אם ריק בהתחלה)
* 📄 `INSTALL.md` (התקנה מהירה + הסרה)

---

## 🚑 6) מדיניות חירום (Pikuach-Nefesh) כתובה וקודית

זה חייב להיות “חוק ברזל”:

* 🔑 PIN hash בלבד (בלי טקסט גלוי)
* ⏲️ פתיחה לזמן מוגבל בלבד
* 🧾 רישום שימוש (timestamp + משך + מצב)
* 🔁 חזרה אוטומטית לנעילה

---

## 🧰 “רשימת זהב” קצרה לפני קודקס ✅

אם אתה רוצה בדיקה מהירה—אלה 12 הסעיפים שהייתי משלים קודם:

1. LICENSE
2. SECURITY.md
3. CONTRIBUTING.md
4. CODE_OF_CONDUCT.md
5. docs/* (חזון/הלכה/Threat Model/ארכיטקטורה)
6. shabatos.yaml
7. shabatosd.py
8. lockdown.py
9. shabatosctl.py
10. systemd service+timer
11. install/enable/disable scripts
12. CI: lint+tests+dry-run

---

## 🎤 פזמון ראפ (4 שורות) 🕯️🔥

שבת נכנסת—המערכת סוגרת שערים 🚪
בלי רעש, בלי רשת, רק אור בנשמה ✨
קודקס ירד—רק אם הבסיס עומד חזק 🧱
ShabatOS עולה—שקט נהיה חוק קבוע 🛡️

---

## 🧾 קרדיטים 🔗

* 📌 מאגר הפרויקט ShabatOS (AnLoMinus) ([GitHub][1])

---

## ✨ משפט קודש לסיום

**“וְשָׁמְרוּ בְּנֵי יִשְׂרָאֵל אֶת־הַשַּׁבָּת… בְּרִית עוֹלָם”** (שמות ל״א)

**🔢 מספר המידות:** 12

[1]: https://github.com/AnLoMinus/ShabatOS/ "GitHub - AnLoMinus/ShabatOS: ️ ShabatOS — מערכת הפעלה לשבת"
