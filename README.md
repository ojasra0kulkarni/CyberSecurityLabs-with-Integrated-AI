# Cyber Security Lab — Red Team vs Blue Team Dashboard

An educational cybersecurity lab: a Flask dashboard that logs and visualizes simulated Red Team (attack) and Blue Team (defense) events, paired with setup instructions for a real 3-VM practice range.

## VM lab setup

The lab (see `templates/vm_setup.html` / the in-app "VM Setup" page) walks through building a local, isolated practice range:

- 🟥 **Red Team** — Kali Linux
- 🟦 **Blue Team** — Ubuntu
- 🪓 **Victim** — Metasploitable2
- 📡 Networked together in an isolated VM network for hands-on offense/defense practice

## Dashboard

- `/` — entry page
- `/vm-setup` — VM lab setup instructions
- `/dashboard` — Red vs Blue event log
- `POST /attack`, `POST /defend` — log a simulated attack/defense event (in-memory, resets on restart)

`tools/redblue.py` currently returns simulated/placeholder events — it's a scaffold for logging real exercise activity, not an attack tool itself.

## Running locally

```bash
pip install flask
python app.py
```

## Stack

Flask · Jinja2 templates · vanilla CSS/JS

## Intended use

For personal learning, CTF practice, and authorized lab environments only — run attacks and exploits solely against machines you own or are explicitly authorized to test (e.g. the bundled Metasploitable2 victim VM).
