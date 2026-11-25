> 🌍 Read this in: **English** | [Česky](01-setup.cs.md)

# 01 · Setup

## What you need

- The **Claude desktop app** (macOS or Windows), signed in with your Quanti account (Team or
  Enterprise). Cowork and chat are one app since September 2026: a conversation that works with
  files on your computer is a Cowork session.
- Cowork and Skills enabled for the organisation (the admin does this; see [prep](prep.md)).
- This repository downloaded: **Code → Download ZIP** on GitHub, unzip to `~/Documents/qti-cowork-sales`.
  No git needed.

## 1. Install the plugin

If the admin set `quanti-sales` to *Installed by default* or *Required*, it is already there;
skip to step 2.

Otherwise: **Customize → Plugins → Upload** and pick `dist/quanti-sales.zip` from the repository.

Check: in **Customize → Plugins** the plugin `quanti-sales` lists four skills: `quanti-brand`,
`quanti-offer`, `deck-review`, `tender-check`.

## 2. Open the working folder

Start a new conversation and give Claude access to the folder
`~/Documents/qti-cowork-sales/sample-data`. Everything Claude writes lands there, next to the
inputs, so you can open the files in PowerPoint, Word or Excel straight away.

> Work on copies. Claude can overwrite files in the folder you give it; for real client work,
> give it a project folder, not your whole Documents.

## 3. Smoke test

```
Jaké barvy a písmo používá Quanti a kam patří logo?
```

The answer must name `#DF2686`, `#4D1254`, Montserrat (Arial as the system font) and "logo
always in the bottom-right corner". If Claude answers in general terms, the plugin is not
active: check step 1.

## How it works

When you send a message, Claude sees the **descriptions** of all installed skills. The
`quanti-brand` description says "use whenever you create anything a client will see", so it is
loaded for decks and offers even if you never name it. You can also call a skill directly with
`/quanti-brand` or by naming it in the prompt; that is more reliable during the workshop.
