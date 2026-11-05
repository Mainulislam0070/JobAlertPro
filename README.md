# JobAlert Pro  (v1.1.0)

A modern Windows desktop app that watches remote job sources, alerts you the moment a matching
**photo editing, retouching, or AI image generation** job is posted, and helps you apply with
AI-written emails that carry your CV and portfolio.

**Developed by Mainul Islam**

## Features
- Dark, modern UI (CustomTkinter) with job cards, *Open job*, *Copy link* and *Draft application*
- Watches: Reddit (r/forhire hiring posts, r/HireaDesigner, r/DesignJobs), RemoteOK, Remotive,
  Jobicy, We Work Remotely
- Your own keyword list, Windows notifications, optional Telegram alerts, system-tray mode
- **Profile**: your name, email, portfolio link, CV file, skills and rates - saved once
- **AI applications**: Gemini or Claude writes a short, tailored email per job and scores the match
- **Approve first (default)**: review/edit the draft, then press Send
- **Auto (guarded, optional)**: sends by itself only if ALL of these pass:
  - the post contains exactly one email address,
  - the AI says the job fits and the score is at least your minimum,
  - the daily limit is not reached,
  - you have not emailed that address before,
  - the draft contains no link other than your portfolio.
  Anything else stays a draft for you to review.
- Applications tab with drafts and a sent log (never emails the same client twice by accident)
- **Reset** button clears jobs, log, history, applications, profile, keys and settings

## Run from source
```bash
pip install -r requirements.txt
python app.py
```

## First-time setup
1. **Profile tab**: name, email, portfolio, CV, and a clear description of your skills. The AI may
   only use facts written here.
2. **Auto Apply tab**:
   - Choose Gemini or Claude, paste an API key (Gemini has a free tier; model names are editable).
   - Email account (Gmail): host `smtp.gmail.com`, port `465`, and a Google **App password**
     (Google Account -> Security -> 2-Step Verification -> App passwords).
   - Press **Test AI** and **Send test email to myself**.
3. Start monitoring. New jobs that contain an email address get a draft automatically; use
   **Draft application** on any other job card.

## Telegram alerts (optional)
1. In Telegram, message **@BotFather** -> `/newbot` -> copy the bot token.
2. Send any message to your bot, open `https://api.telegram.org/bot<TOKEN>/getUpdates`, copy `chat` -> `id`.
3. Paste both into *Settings*, then **Send Test Notification**.

## Build the EXE locally
```bash
pip install pyinstaller
pyinstaller JobAlertPro.spec --clean --noconfirm
# Output: dist/JobAlertPro.exe
```

## Release the EXE on GitHub
1. Create a GitHub repository and push all files in this folder.
2. Tag and push:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```
3. GitHub Actions (`.github/workflows/build-release.yml`) builds `JobAlertPro.exe` on Windows and
   attaches it to a new Release. You can also run it from the **Actions** tab.

## Safety notes
- Applying by bot is not allowed on Upwork, Fiverr or LinkedIn - use those sites manually.
  This app only emails addresses that clients published in their own posts.
- Keep the daily limit low (3-5). Many identical cold emails can get your address marked as spam.
- Always read the first few AI drafts before trusting Auto mode.
- Job post text is treated as untrusted data; the AI cannot change the recipient, and Auto mode
  blocks drafts that contain unexpected links.
- API key, email app password and Telegram token are stored in the Windows Credential Manager
  (via `keyring`). If that is unavailable they fall back to `%APPDATA%\JobAlertPro\config.json`.
- Settings: `%APPDATA%\JobAlertPro\config.json`, applications: `%APPDATA%\JobAlertPro\applications.json`.
- Source feeds can change or rate-limit; failures appear in the *Log* tab.

## License
MIT - (c) Mainul Islam
