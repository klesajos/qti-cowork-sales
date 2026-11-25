> 🌍 Read this in: [English](01-setup.md) | **Česky**

# 01 · Nastavení

## Co potřebujete

- **Desktopovou aplikaci Claude** (macOS nebo Windows), přihlášenou účtem Quanti (Team nebo
  Enterprise). Cowork a chat jsou od září 2026 jedna aplikace: konverzace, která pracuje se
  soubory na vašem počítači, je Cowork.
- Cowork a Skills zapnuté pro organizaci (zařídí admin; viz [přípravu](prep.cs.md)).
- Stažený tento repozitář: na GitHubu **Code → Download ZIP**, rozbalit do
  `~/Documents/qti-cowork-sales`. Git není potřeba.

## 1. Instalace pluginu

Pokud admin nastavil `quanti-sales` jako *Installed by default* nebo *Required*, už ho máte;
pokračujte krokem 2.

Jinak: **Customize → Plugins → Upload** a vyberte `dist/quanti-sales.zip` z repozitáře.

Kontrola: v **Customize → Plugins** má plugin `quanti-sales` čtyři skilly: `quanti-brand`,
`quanti-offer`, `deck-review`, `tender-check`.

## 2. Pracovní složka

Založte novou konverzaci a dejte Claude přístup ke složce
`~/Documents/qti-cowork-sales/sample-data`. Všechno, co Claude vytvoří, se uloží tam, vedle
podkladů, takže soubory hned otevřete v PowerPointu, Wordu nebo Excelu.

> Pracujte na kopiích. Claude může soubory ve složce přepsat; pro skutečnou práci s klienty mu
> dejte složku projektu, ne celé Dokumenty.

## 3. Rychlý test

```
Jaké barvy a písmo používá Quanti a kam patří logo?
```

Odpověď musí obsahovat `#DF2686`, `#4D1254`, Montserrat (Arial jako systémové písmo) a „logo
vždy v pravém dolním rohu“. Pokud Claude odpoví obecně, plugin není aktivní: zkontrolujte krok 1.

## Jak to funguje

Když pošlete zprávu, Claude vidí **popisy** všech nainstalovaných skillů. Popis `quanti-brand`
říká „použij vždy, když vytváříš něco, co uvidí klient“, takže se načte u prezentací i nabídek,
i když ho nejmenujete. Skill můžete zavolat i přímo, `/quanti-brand` nebo jménem v promptu;
na workshopu je to spolehlivější.
