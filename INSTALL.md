# התקנה מהירה (Draft)

> מסמך זה הוא טיוטה ראשונית, לשיפור בהמשך.

## דרישות

- Linux עם systemd
- Python 3.10+
- הרשאות sudo

## התקנה

```bash
./scripts/install.sh
```

## הסרה

```bash
sudo systemctl disable --now shabatosd.timer
sudo rm -rf /opt/shabatos
```

## מצב בדיקה (Dry Run)

מצב בדיקה יאפשר סימולציה בלי חסימת רשת בפועל. יתווסף בגרסה עתידית.
