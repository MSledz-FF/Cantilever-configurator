# Composite Cantilever Designer

A self-contained 2D geometry editor for exploring pull and push composite OLE cantilever arrangements.

## Features

- Side-by-side Pull and Push configurations
- Draggable tube joints and slider connections
- Live tube-length and joint-angle tables
- Individual padlocks for tube lengths, joint angles and reference inputs
- Numeric constraint solver for locked values
- Independent system height, walkout, registration arm, drop bracket and mast bracket separation inputs
- Level top tube and live registration-tube angle
- UK standard-gauge rails, track centreline and ±230 mm stagger references
- Non-rotating registration assembly that slides along the registration tube

## Run locally

Open `index.html` directly in a modern browser, or run:

```bash
python run_local.py
```

The Python launcher starts a local server and opens the designer automatically.

## Publish with GitHub Pages

1. Open **Settings → Pages** in the repository.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Select the `main` branch and `/(root)` folder.
4. Click **Save**.

The site is static and has no package or build dependencies.

## Engineering note

The built-in solver maintains only the values locked in the interface. It does not verify compliance with Network Rail standards, EN 50119, electrical clearances, structural loading or product acceptance requirements.
