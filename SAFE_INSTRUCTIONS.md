# Instagram Followers Checker - Data Export Method (Safe)

## Why use this method?

- **No login needed**: You don't have to enter your password anywhere.
- **No API usage**: Zero automated API requests.
- **No ban risk**: You only rely on data officially provided by Instagram.

---

## How to export your data

1. Open Instagram on your phone or browser.
2. Go to **Settings**.
3. Look for **Accounts Centre -> Your information and permissions** (or **Privacy and Security -> Data Download**).
4. Select **Download your information**.
5. Choose **Some of your information** and pick:
   - **Followers and following**
   - **Connections** (if available)
6. Make sure the format is set to **JSON** (very important) and the data range to **All time**.
7. Submit the request. Instagram will email you a link. This usually takes between 15 minutes and an hour.
8. Download the ZIP file from the email and extract it.

---

## Running the script

### Automatic path detection

```bash
cd /Users/alexg/Documents/Instagram
python3 instagram_safe_checker.py
```

If you extracted your Instagram ZIP in the same folder, you can just press Enter when prompted.

### Specific path

Otherwise, run the script and provide the full path to your extracted folder when prompted. For example:

```
/Users/alexg/Downloads/instagram-alexg-2026-01-26
```

---

## Folder structure

After extracting the ZIP, you should see something like this:

```
instagram-username-2026-01-26/
├── connections/
│   └── followers_and_following/
│       ├── followers.json
│       └── following.json
└── ...
```

Or depending on the export version:

```
instagram-username-2026-01-26/
├── followers_1.json
├── following.json
└── ...
```

The script will automatically search for the needed JSON files in the regular locations.

---

## What does the script do?

1. Reads the JSON files locally on your machine.
2. Extracts the followers/following data.
3. Compares the lists.
4. Outputs the accounts that don't follow you back.
5. Saves everything to a local text file.

No internet connection is required to run the comparison.

---

## Troubleshooting

- **Missing JSON files**: Make sure you actually extracted the ZIP and that you requested JSON format instead of HTML.
- **Didn't get the email**: Check your spam folder. Sometimes it can take longer, up to 48 hours.

---

## Comparison: Safe vs API Method

| Feature            | Safe Method (Data Export)     | API Method                            |
| ------------------ | ----------------------------- | ------------------------------------- |
| **Ban Risk**       | None                          | Low (but possible)                    |
| **Login Required** | No                            | Yes (plus 2FA if enabled)             |
| **Setup Time**     | Includes wait time for export | < 1 minute                            |
| **Frequency**      | Can use anytime               | Best used sparingly (1-2 times/month) |
| **Data Update**    | Manual (re-export needed)     | Real-time                             |

Choose the safe method if you don't mind waiting for the export. Use the API script if you need instant results and accept the login requirements.
