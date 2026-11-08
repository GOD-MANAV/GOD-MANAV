"""Generates the animated SVG artwork used by the profile README.

Run:  python scripts/build_assets.py
Every file lands in assets/. Edit the data below and re-run to change copy or colours.

All artwork draws on its own dark panel, so it reads well in GitHub's light and dark themes.
Static attributes carry the look; <style> and SMIL only add motion, so nothing breaks
where animation is stripped.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'Cascadia Code', Consolas, 'SF Mono', Menlo, monospace"


def write(name, svg):
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", name)


def text_w(s, size, k=0.56):
    """Rough text width for layout; good enough for pills and chips."""
    return len(s) * size * k


# ---------------------------------------------------------------- hero
def hero():
    pills = [
        ("Chrome Extensions", "#A78BFA"),
        ("AI Apps", "#22D3EE"),
        ("Automation", "#F472B6"),
        ("Game Dev", "#FBBF24"),
        ("Hardware", "#34D399"),
    ]
    x, chips = 64, []
    for i, (label, c) in enumerate(pills):
        w = text_w(label, 15, 0.55) + 30
        chips.append(
            f'<g class="pill" style="animation-delay:{0.9 + i * 0.12:.2f}s">'
            f'<rect x="{x:.0f}" y="246" width="{w:.0f}" height="34" rx="17" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-opacity="0.55"/>'
            f'<text x="{x + w / 2:.0f}" y="268" text-anchor="middle" font-family="{SANS}" font-size="15" font-weight="600" fill="{c}">{escape(label)}</text></g>'
        )
        x += w + 10

    stars = [(120, 40, 1.2, 3), (310, 300, 1, 4), (480, 36, 1.4, 5), (650, 310, 1, 3.5),
             (700, 60, 1.6, 4.5), (980, 40, 1.2, 6), (940, 320, 1.3, 3.2), (40, 300, 1, 5.5),
             (560, 120, 0.9, 4.2), (250, 120, 0.8, 6.3)]
    star_svg = "".join(
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" opacity="0.6">'
        f'<animate attributeName="opacity" values="0.15;0.9;0.15" dur="{d}s" repeatCount="indefinite"/></circle>'
        for cx, cy, r, d in stars
    )

    write("hero.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="340" viewBox="0 0 1000 340" role="img" aria-label="Manav Yadav. I build tools that turn hours of busywork into one click.">
<style>
  .fade {{ animation: rise .9s cubic-bezier(.2,.8,.2,1) both; }}
  .d1 {{ animation-delay: .1s }} .d2 {{ animation-delay: .3s }} .d3 {{ animation-delay: .55s }}
  .pill {{ animation: rise .7s cubic-bezier(.2,.8,.2,1) both; }}
  @keyframes rise {{ from {{ opacity: 0; transform: translateY(14px) }} to {{ opacity: 1; transform: none }} }}
</style>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#070B1A"/><stop offset="1" stop-color="#160B33"/>
  </linearGradient>
  <linearGradient id="name" x1="0" y1="0" x2="1" y2="0" spreadMethod="reflect">
    <stop offset="0" stop-color="#C4B5FD"/><stop offset="0.5" stop-color="#22D3EE"/><stop offset="1" stop-color="#F472B6"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0;0 0" dur="8s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#A78BFA"/><stop offset="0.5" stop-color="#22D3EE" stop-opacity="0.2"/><stop offset="1" stop-color="#F472B6"/>
  </linearGradient>
  <radialGradient id="core" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#22D3EE" stop-opacity="0.45"/><stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>
  </radialGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="45"/></filter>
  <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#ffffff" stroke-opacity="0.05"/></pattern>
  <clipPath id="clip"><rect width="1000" height="340" rx="26"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="1000" height="340" fill="url(#bg)"/>
  <g filter="url(#blur)" opacity="0.6">
    <ellipse cx="780" cy="70" rx="210" ry="120" fill="#7C3AED"><animate attributeName="cx" values="780;640;780" dur="14s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="930" cy="280" rx="190" ry="110" fill="#0891B2"><animate attributeName="cy" values="280;200;280" dur="11s" repeatCount="indefinite"/></ellipse>
    <ellipse cx="520" cy="330" rx="170" ry="80" fill="#DB2777"><animate attributeName="cx" values="520;660;520" dur="16s" repeatCount="indefinite"/></ellipse>
  </g>
  <rect width="1000" height="340" fill="url(#grid)"/>
  {star_svg}

  <g class="fade d1"><text x="64" y="96" font-family="{MONO}" font-size="15" letter-spacing="4" fill="#94A3B8">HELLO, WORLD. I'M</text></g>
  <g class="fade d2"><text x="60" y="172" font-family="{SANS}" font-size="78" font-weight="800" letter-spacing="-1.5" fill="url(#name)">Manav Yadav</text></g>
  <g class="fade d3"><text x="64" y="216" font-family="{SANS}" font-size="21" fill="#E2E8F0">I build tools that turn hours of busywork into one click.</text></g>
  {''.join(chips)}

  <g transform="translate(860 170)">
    <circle r="120" fill="url(#core)"/>
    <circle r="62" fill="none" stroke="#A78BFA" stroke-opacity="0.35" stroke-dasharray="4 7"/>
    <circle r="92" fill="none" stroke="#22D3EE" stroke-opacity="0.25"/>
    <circle r="122" fill="none" stroke="#F472B6" stroke-opacity="0.2" stroke-dasharray="2 10"/>
    <g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite"/>
      <circle cx="62" cy="0" r="7" fill="#A78BFA"/></g>
    <g><animateTransform attributeName="transform" type="rotate" from="120" to="-240" dur="15s" repeatCount="indefinite"/>
      <circle cx="92" cy="0" r="6" fill="#22D3EE"/><circle cx="-92" cy="0" r="4" fill="#FBBF24"/></g>
    <g><animateTransform attributeName="transform" type="rotate" from="200" to="560" dur="24s" repeatCount="indefinite"/>
      <circle cx="122" cy="0" r="5" fill="#F472B6"/><circle cx="0" cy="122" r="3.5" fill="#34D399"/></g>
    <rect x="-38" y="-38" width="76" height="76" rx="20" fill="#0F172A" stroke="url(#edge)" stroke-width="2"/>
    <text x="0" y="10" text-anchor="middle" font-family="{MONO}" font-size="28" font-weight="700" fill="#E2E8F0">&lt;/&gt;</text>
  </g>
</g>
<rect x="1" y="1" width="998" height="338" rx="25" fill="none" stroke="url(#edge)" stroke-opacity="0.6" stroke-width="2"/>
</svg>""")


# ---------------------------------------------------------------- section headers
SECTIONS = [
    ("about", "01", "About me", "who I am and what I'm working on", "#A78BFA", "#6366F1"),
    ("stack", "02", "Tech stack", "the tools I reach for", "#22D3EE", "#3B82F6"),
    ("projects", "03", "Featured projects", "things I've shipped", "#F472B6", "#F97316"),
    ("stats", "04", "GitHub stats", "updated automatically", "#FBBF24", "#EF4444"),
    ("snake", "05", "Contribution snake", "it eats my commits every day", "#34D399", "#14B8A6"),
]


def headers():
    for key, num, title, sub, c1, c2 in SECTIONS:
        tw = text_w(title, 28, 0.56)
        write(f"header-{key}.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="84" viewBox="0 0 1000 84" role="img" aria-label="{escape(title)}">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0" spreadMethod="reflect">
    <stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0;0 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{c1}" stop-opacity="0.18"/><stop offset="1" stop-color="{c1}" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="1000" height="84" rx="20" fill="#0B1020"/>
<rect width="1000" height="84" rx="20" fill="url(#fade)"/>
<rect x="24" y="20" width="44" height="44" rx="13" fill="url(#g)"/>
<text x="46" y="49" text-anchor="middle" font-family="{MONO}" font-size="17" font-weight="700" fill="#0B1020">{num}</text>
<text x="88" y="51" font-family="{SANS}" font-size="28" font-weight="700" fill="#F8FAFC">{escape(title)}</text>
<text x="{88 + tw + 18:.0f}" y="50" font-family="{MONO}" font-size="14" fill="#94A3B8">// {escape(sub)}</text>
<rect x="88" y="62" width="{tw:.0f}" height="3" rx="1.5" fill="url(#g)">
  <animate attributeName="width" values="0;{tw:.0f}" dur="1.2s" fill="freeze"/>
</rect>
<g fill="{c1}">
  <circle cx="940" cy="42" r="4"><animate attributeName="opacity" values="1;.2;1" dur="1.8s" repeatCount="indefinite"/></circle>
  <circle cx="956" cy="42" r="4" opacity=".6"><animate attributeName="opacity" values=".2;1;.2" dur="1.8s" repeatCount="indefinite"/></circle>
  <circle cx="972" cy="42" r="4" opacity=".3"><animate attributeName="opacity" values="1;.2;1" dur="1.8s" begin=".6s" repeatCount="indefinite"/></circle>
</g>
</svg>""")


# ---------------------------------------------------------------- about terminal
def about():
    P = "#34D399"   # prompt green
    lines = [
        ("cmd", "whoami"),
        ("out", "Manav Yadav. A builder who automates the boring stuff."),
        ("cmd", "cat now.txt"),
        ("out", "Building SaveSutra, an AI second brain for everything you save."),
        ("cmd", "ls interests/"),
        ("ls", ["ai-agents/", "browser-extensions/", "game-design/", "hardware/"]),
        ("cmd", "echo $MOTTO"),
        ("motto", "\"Ship it first. Then make it beautiful.\""),
    ]
    colors = ["#22D3EE", "#F472B6", "#FBBF24", "#A78BFA"]
    y, rows = 108, []
    for i, (kind, val) in enumerate(lines):
        d = 0.35 + i * 0.45
        if kind == "cmd":
            body = (f'<text x="40" y="{y}" font-family="{MONO}" font-size="17">'
                    f'<tspan fill="{P}">manav@github</tspan><tspan fill="#64748B">:</tspan>'
                    f'<tspan fill="#60A5FA">~</tspan><tspan fill="#64748B">$ </tspan>'
                    f'<tspan fill="#F8FAFC">{escape(val)}</tspan></text>')
        elif kind == "ls":
            x, parts = 40, []
            for j, item in enumerate(val):
                parts.append(f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="17" fill="{colors[j % 4]}">{escape(item)}</text>')
                x += text_w(item, 17, 0.6) + 26
            body = "".join(parts)
        elif kind == "motto":
            body = f'<text x="40" y="{y}" font-family="{MONO}" font-size="17" font-style="italic" fill="#FBBF24">{escape(val)}</text>'
        else:
            body = f'<text x="40" y="{y}" font-family="{MONO}" font-size="17" fill="#CBD5E1">{escape(val)}</text>'
        rows.append(f'<g class="ln" style="animation-delay:{d:.2f}s">{body}</g>')
        y += 34 if kind != "cmd" else 30
        if kind != "cmd":
            y += 6
    cursor_y = y - 14
    height = y + 30

    write("about.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-label="About Manav: a builder who automates the boring stuff, currently building SaveSutra.">
<style>
  .ln {{ animation: type .5s steps(12, end) both; }}
  @keyframes type {{ from {{ opacity: 0; clip-path: inset(0 100% 0 0) }} to {{ opacity: 1; clip-path: inset(0 0 0 0) }} }}
</style>
<defs>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#34D399" stop-opacity="0.7"/><stop offset="1" stop-color="#22D3EE" stop-opacity="0.15"/>
  </linearGradient>
  <radialGradient id="glow" cx="1" cy="0" r="0.9">
    <stop offset="0" stop-color="#34D399" stop-opacity="0.16"/><stop offset="1" stop-color="#34D399" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="1000" height="{height}" rx="22" fill="#0A0F1C"/>
<rect width="1000" height="{height}" rx="22" fill="url(#glow)"/>
<path d="M0 22 a22 22 0 0 1 22 -22 h956 a22 22 0 0 1 22 22 v28 h-1000 z" fill="#111827"/>
<circle cx="32" cy="25" r="7" fill="#FF5F57"/><circle cx="56" cy="25" r="7" fill="#FEBC2E"/><circle cx="80" cy="25" r="7" fill="#28C840"/>
<text x="500" y="31" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#64748B">manav@github: ~ (zsh)</text>
{''.join(rows)}
<rect x="40" y="{cursor_y}" width="11" height="20" fill="{P}">
  <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
</rect>
<rect x="1" y="1" width="998" height="{height - 2}" rx="21" fill="none" stroke="url(#edge)" stroke-width="2"/>
</svg>""")


# ---------------------------------------------------------------- project cards
PROJECTS = [
    ("savesutra", "SaveSutra", "AI second brain for links",
     ["Share any reel, video or link and get a summary,", "category, places and products found inside it."],
     ["TypeScript", "AI", "WhatsApp bot"], "#F59E0B", "#EF4444", "brain"),
    ("mailmerge", "Mail Merge Pro", "Free bulk email for Sheets + Gmail",
     ["Personalised mail merge with templates, scheduling", "and attachments. No API keys, no fees."],
     ["Apps Script", "HTML", "Gmail"], "#3B82F6", "#06B6D4", "mail"),
    ("phishing", "Phishing Serious Game", "Learn to spot phishing by playing",
     ["A Unity game that trains players to catch", "phishing attacks before they click."],
     ["Unity", "C#", "Security"], "#EC4899", "#8B5CF6", "shield"),
    ("pico", "Pico HID Tool", "Raspberry Pi Pico keystroke injector",
     ["A rubber-ducky style HID device for security", "research and learning, built on a Pico."],
     ["Python", "Raspberry Pi", "Hardware"], "#10B981", "#84CC16", "chip"),
    ("snakeqr", "Snake in a QR Code", "A whole game in one QR code",
     ["A complete, playable Snake game squeezed into", "a single scannable QR code."],
     ["Batch", "Size hacking", "Games"], "#14B8A6", "#A3E635", "qr"),
]

ICONS = {  # 24x24 stroke icons, drawn at 2x
    "brain": '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-1z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "chip": '<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>',
    "qr": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3M21 14v7h-4M14 21v-3"/>',
}


def cards():
    for key, name, tag, desc, chips, c1, c2, icon in PROJECTS:
        cx, chip_svg = 32, []
        for chip in chips:
            w = text_w(chip, 13, 0.6) + 22
            chip_svg.append(
                f'<rect x="{cx:.0f}" y="196" width="{w:.0f}" height="26" rx="13" fill="{c1}" fill-opacity="0.12" stroke="{c1}" stroke-opacity="0.4"/>'
                f'<text x="{cx + w / 2:.0f}" y="213" text-anchor="middle" font-family="{SANS}" font-size="13" font-weight="600" fill="{c1}">{escape(chip)}</text>'
            )
            cx += w + 8
        write(f"card-{key}.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="480" height="250" viewBox="0 0 480 250" role="img" aria-label="{escape(name)}: {escape(tag)}">
<defs>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1" spreadMethod="reflect">
    <stop offset="0" stop-color="{c1}"/><stop offset="0.5" stop-color="{c2}" stop-opacity="0.15"/><stop offset="1" stop-color="{c2}"/>
    <animateTransform attributeName="gradientTransform" type="rotate" values="0 .5 .5;360 .5 .5" dur="10s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="tile" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
  <radialGradient id="glow" cx="1" cy="0" r="1">
    <stop offset="0" stop-color="{c1}" stop-opacity="0.28"/><stop offset="0.6" stop-color="{c2}" stop-opacity="0.05"/><stop offset="1" stop-color="{c2}" stop-opacity="0"/>
  </radialGradient>
  <clipPath id="clip"><rect width="480" height="250" rx="20"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="480" height="250" fill="#0B1020"/>
  <rect width="480" height="250" fill="url(#glow)">
    <animate attributeName="opacity" values="0.7;1;0.7" dur="5s" repeatCount="indefinite"/>
  </rect>
  <circle cx="430" cy="40" r="90" fill="none" stroke="{c1}" stroke-opacity="0.12"/>
  <circle cx="430" cy="40" r="130" fill="none" stroke="{c2}" stroke-opacity="0.08"/>
</g>
<rect x="32" y="30" width="56" height="56" rx="16" fill="url(#tile)"/>
<g transform="translate(44 42) scale(1.333)" fill="none" stroke="#0B1020" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
<text x="104" y="56" font-family="{SANS}" font-size="23" font-weight="700" fill="#F8FAFC">{escape(name)}</text>
<text x="104" y="80" font-family="{SANS}" font-size="14" font-weight="600" fill="{c1}">{escape(tag)}</text>
<text x="32" y="130" font-family="{SANS}" font-size="15" fill="#CBD5E1">{escape(desc[0])}</text>
<text x="32" y="154" font-family="{SANS}" font-size="15" fill="#CBD5E1">{escape(desc[1])}</text>
{''.join(chip_svg)}
<g transform="translate(436 209)" fill="none" stroke="{c1}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M-8 8 8 -8M-2 -8h10v10"/>
</g>
<rect x="1" y="1" width="478" height="248" rx="19" fill="none" stroke="url(#edge)" stroke-width="2"/>
</svg>""")


# ---------------------------------------------------------------- footer
def footer():
    def wave(amp, period, base, width=2000):
        d = f"M0 {base} Q{period / 4} {base - amp} {period / 2} {base}"
        x = period / 2
        while x < width:
            x += period / 2
            d += f" T{x:.0f} {base}"
        return d + f" L{width} 150 L0 150 Z"

    write("footer.svg", f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="150" viewBox="0 0 1000 150" role="img" aria-label="Thanks for stopping by. Keep building.">
<defs>
  <linearGradient id="w1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7C3AED"/><stop offset=".5" stop-color="#0891B2"/><stop offset="1" stop-color="#DB2777"/></linearGradient>
  <linearGradient id="w2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22D3EE"/><stop offset="1" stop-color="#A78BFA"/></linearGradient>
  <clipPath id="clip"><rect width="1000" height="150" rx="24"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="1000" height="150" fill="#070B1A"/>
  <path d="{wave(14, 250, 96)}" fill="url(#w1)" opacity="0.35">
    <animateTransform attributeName="transform" type="translate" values="0 0;-500 0" dur="9s" repeatCount="indefinite"/>
  </path>
  <path d="{wave(10, 200, 112)}" fill="url(#w2)" opacity="0.3">
    <animateTransform attributeName="transform" type="translate" values="-400 0;0 0" dur="7s" repeatCount="indefinite"/>
  </path>
  <text x="500" y="58" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="700" fill="#F8FAFC">Thanks for stopping by</text>
  <text x="500" y="84" text-anchor="middle" font-family="{MONO}" font-size="14" fill="#94A3B8">keep building, keep shipping</text>
</g>
</svg>""")


if __name__ == "__main__":
    hero()
    headers()
    about()
    cards()
    footer()
