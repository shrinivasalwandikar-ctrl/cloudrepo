# Hi Shrinivas App

Simple Node app that displays a welcome message.

Run locally:

```bash
npm install   # not required for this minimal app
npm start
```

Then open: http://localhost:3000
# CloudAutomation — Express + Bootstrap Starter

This project is a minimal Express.js app serving a Bootstrap 5 landing page.

Quick start

1. Install Node.js (LTS) so `node` and `npm` are available.
   - Windows: download from https://nodejs.org or use `winget`/`choco`.

2. From the project folder install dependencies and run the server.

PowerShell (if you encounter script policy issues):

```powershell
cd C:/Users/DELL/Desktop/cloudAutomation
npm.cmd install
node app.js
```

Or from CMD / Git Bash:

```bash
cd C:/Users/DELL/Desktop/cloudAutomation
npm install
npm start
```

3. Open http://localhost:3000

Files

# Files

- `app.js` — Express server entrypoint
- `index.html` — main page served from project root
- `public/` — static assets (CSS, images)

PowerShell note

If PowerShell blocks `npm` with an error like:

```
File C:\Program Files\nodejs\npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

Either run `node app.js` directly, use `npm.cmd install` / `npm.cmd run start`, or change your execution policy (example below — use with caution):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```

Development

- `npm run dev` — start with `nodemon` (install globally or as devDependency)

This README was updated to include PowerShell workarounds and direct run instructions.
# CloudAutomation — Express + Bootstrap Starter

This folder contains a minimal Express.js app that serves a Bootstrap 5 home page.

Quick start

1. Install dependencies:

```bash
npm install
```

2. Start the server:

```bash
npm start
```

3. Open http://localhost:3000 in your browser.

Notes

- `index.html` is at the project root and uses Bootstrap 5 via CDN.
- To develop with automatic restarts, install `nodemon` and run `npm run dev`.
# cloudrepo
