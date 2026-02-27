# Mac & Linux Installation Guide

## Getting Started

To run these tools on macOS or Linux, you'll need **Python 3**. Most macOS and Linux systems already have it installed.

### Step 1: Verify Python 3

Open your **Terminal** and type:

```bash
python3 --version
```

If it shows `Python 3.x.x`, you are good to proceed. If not:

- **Mac:** Install it via [Homebrew](https://brew.sh/): `brew install python` or download it from [python.org](https://www.python.org/downloads/).
- **Ubuntu/Debian:** run `sudo apt update && sudo apt install python3 python3-pip`

---

## Step 2: Install Required Packages

If you plan to use the **API method** (`instagram_followers_checker.py`), you need to install the `instaloader` package.

Run this command in your terminal:

```bash
pip3 install instaloader
```

_(If you get a permissions error, try `python3 -m pip install instaloader`)_

---

## Step 3: Run the Scripts

First, navigate to the folder where you placed the scripts using the `cd` command. For example:

```bash
cd ~/Documents/Instagram
```

### Option A: Safe Method (Recommended)

This method requires you to download your data from Instagram first. Read the `SAFE_INSTRUCTIONS.md` for details.

To run it:

```bash
python3 instagram_safe_checker.py
```

_(Or simply double click / run `sh run_safe.sh`)_

### Option B: API Method

This method requires you to log in with your username and password.

To run it:

```bash
python3 instagram_followers_checker.py
```

_(Or simply double click / run `sh run.sh`)_

---

## Troubleshooting

- **"Command not found: pip3"**: You need to install pip. On Mac run `python3 -m ensurepip`. On Linux run `sudo apt install python3-pip`.
- **"ModuleNotFoundError: No module named 'instaloader'"**: Re-run the installation command (`pip3 install instaloader`). Make sure you use `pip3` and not just `pip`.
