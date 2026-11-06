# JobAlert Pro  (v1.3.0)

A modern Windows desktop app that watches remote job sources, alerts you the moment a matching
**photo editing, retouching, or AI image generation** job is posted, and helps you apply with
AI-written emails that carry your CV and portfolio.

**Developed by Mainul Islam**

## Features
- Dark, modern UI (CustomTkinter) with job cards, *Open job*, *Copy link* and *Draft application*
- Watches: Reddit (r/forhire hiring posts, r/HireaDesigner, r/DesignJobs), RemoteOK, Remotive,
  Jobicy, We Work Remotely, Working Nomads
- Your own keyword list, Windows notifications, optional Telegram alerts, system-tray mode
- **Profile**: your name, email, portfolio link, CV file, **portfolio PDF**, skills and rates - saved once
- **AI applications**: Gemini or Claude writes a short, tailored email per job and scores the match
- **Approve first (default)**: the app writes the email, attaches your CV and portfolio PDF automatically,
  and shows everything in a review window (recipient, subject, text, attached files). You can type the
  client's name and press **Apply name** to personalise the greeting. You only review it and press **Send**.
- **Auto (guarded, optional)**: sends by itself only if ALL of these pass:
  - the post contains exactly one email address,
  - the AI says the job fits and the score is at least your minimum,
  - the daily limit is not reached,
  - you have not emailed that address before,
  - the draft contains no link other than your portfolio.
  Anything else stays a draft for you to review.
- Applications tab with drafts and a sent log (never emails the same client twice by accident)
- **Instagram tab (manual sending):** jobs that mention an Instagram handle are added to a client list
  automatically (or add clients by hand). Click **Copy & Open DM**: the AI writes a short personal message
  (if none exists yet), it is copied to your clipboard and the client's Instagram chat opens. You paste it and
  press Send yourself, then click **Mark sent**. A follow-up reminder appears after 3 days, and **Write
  follow-up (AI)** drafts a polite nudge. Nothing is ever sent automatically.
- **Outreach tab (new):** paste a list of studio / photographer / creative-director websites (or load a .txt /
  .csv file; Instagram profile links work too). **Find contacts** reads each site's own public pages (home +
  contact-like pages, one site at a time, respecting robots.txt) and collects the email address, Instagram
  handle and WhatsApp number it finds. Each lead gets three buttons:
  - **Email**: the AI writes a personal intro using what the site says about them, your CV and portfolio PDF are
    attached, you review it in the normal review window and press Send. An opt-out line (and your optional
    address) is added automatically.
  - **Instagram**: Copy & Open DM, same manual flow as the Instagram tab.
  - **WhatsApp**: opens a wa.me chat with the message pre-filled; you press Send in WhatsApp.
  Leads have statuses (New, Contacted, Follow-up due after 3 days, Replied, Done) and **Do not contact**:
  a DNC lead is never emailed again. The daily email limit asks for confirmation before you go over it.
- **Job Boards tab:** one-click searches for Twine, FreeUp, Indeed, Glassdoor, FlexJobs, SimplyHired, Remote.co,
  Behance, Dribbble, The Dots, Creativepool, Guru, PeoplePerHour, Workana, Contra, Working Nomads, Remotive,
  Wellfound, Jobspresso, The Creative Loft, OpenTrain AI and Virtual Vocations. Each button opens a Google search
  limited to that site and to the last 24 hours / week / month. Nothing is scraped.
- **Reset** button clears jobs, log, history, applications, Instagram clients, profile, keys and settings

## Run from source
```bash
pip install -r requirements.txt
python app.py
```

## First-time setup
1. **Profile tab**: name, email, portfolio link, CV, portfolio PDF (keep both under about 20 MB), and a clear description of your skills. The AI may
   only use facts written here.
2. **Auto Apply tab**:
   - Choose Gemini or Claude, paste an API key (Gemini has a free tier; model names are editable).
   - Email account (Gmail): host `smtp.gmail.com`, port `465`, and a Google **App password**
     (Google Account -> Security -> 2-Step Verification -> App passwords).
   - Press **Test AI** and **Send test email to myself**.
3. Start monitoring. New jobs that contain an email address get a draft automatically; use
   **Draft application** on any other job card.

## Instagram tips
- Instagram's rules do not allow bots to message people, so this app only prepares the message.
- Instagram DMs cannot carry PDF files, so the Instagram message links your portfolio instead (upload the PDF to Google Drive and paste the share link in the Profile tab). Use email when you want the PDF attached.
- If the chat link does not open a conversation, use **Open profile** in the client window.
- Send roughly 10-15 new DMs per day at most, and personalise each one. Many identical DMs get flagged as spam.

## Cold outreach: be careful
- Nothing is sent automatically for leads. You review every email, and Instagram / WhatsApp messages are sent by you.
- Anti-spam laws differ (US CAN-SPAM, EU/UK GDPR and PECR, Canada CASL). Contact businesses with a relevant offer,
  be honest, and mark anyone who says "no thanks" as Do not contact.
- WhatsApp and Instagram can block accounts that send many unsolicited messages. Keep it to a few per day and
  personalise each one.
- Many studios publish no email, only a contact form; those leads show no email and you can use Instagram or the
  website form yourself.

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
   git tag v1.3.0
   git push origin v1.3.0
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
- Settings: `%APPDATA%\JobAlertPro\config.json`, applications: `%APPDATA%\JobAlertPro\applications.json`, Instagram clients: `%APPDATA%\JobAlertPro\clients.json`, outreach leads: `%APPDATA%\JobAlertPro\leads.json`.
- Source feeds can change or rate-limit; failures appear in the *Log* tab.

## License
MIT - (c) Mainul Islam
