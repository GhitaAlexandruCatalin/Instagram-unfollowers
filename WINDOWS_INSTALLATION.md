# Windows Installation Guide

## Prerequisites

1. Python 3
2. instaloader package

---

## Step 1: Install Python

### Check if Python is installed

1. Open Command Prompt (CMD):
   - Press `Win + R`
   - Type `cmd` and hit Enter

2. Run:
   ```cmd
   python --version
   ```

If you see `Python 3.x.x`, you're good to go. If not, follow the steps below.

### Installing Python

1. Go to https://www.python.org/downloads/ and download the latest Python 3 version.
2. Run the installer.
3. **IMPORTANT**: Check the box for **"Add Python to PATH"** before clicking install.
4. Finish the installation.
5. Open a new CMD window and type `python --version` to verify.

---

## Step 2: Install instaloader

In CMD, run:

```cmd
pip install instaloader
```

If that doesn't work, try:

```cmd
python -m pip install instaloader
```

---

## Step 3: Copy the script

Bring the `instagram_followers_checker.py` script to your Windows machine.
You can place it on your Desktop, for example: `C:\Users\YourUsername\Desktop\Instagram\`

---

## Step 4: Run the script

1. Open CMD and navigate to your folder:

   ```cmd
   cd C:\Users\YourUsername\Desktop\Instagram
   ```

2. Run the checker:

   ```cmd
   python instagram_followers_checker.py
   ```

3. Type in your username, password (will be hidden), and 2FA code if prompted.

---

## Results

The script will show who isn't following you back in the terminal and also save a `.txt` results file in the same directory.

---

## Troubleshooting

- **"python is not recognized..."**: You didn't add Python to PATH during installation. Reinstall Python and make sure to check the "Add Python to PATH" box.
- **"pip is not recognized..."**: Use `python -m pip install instaloader` instead.
- **Script hangs at downloading list**: Normal behavior for large accounts due to rate limits. Just wait it out.
