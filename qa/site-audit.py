from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
VIEWPORTS = [
    ("desktop", 1440, 900),
    ("laptop", 1280, 800),
    ("tablet", 768, 1024),
    ("mobile", 390, 844),
    ("narrow", 320, 800),
]
DOCS = {
    "resume.html": 2200,
    "cover-letter.html": 1400,
    "interview-brief.html": 1300,
    "entry-plan.html": 1200,
    "field-build-brief.html": 1400,
}


def inline_html(name: str) -> str:
    html = (ROOT / name).read_text()
    css = (ROOT / "brand-tokens.css").read_text() + "\n" + (ROOT / "styles.css").read_text().replace("@import url('brand-tokens.css');", "")
    extra = ROOT / "documents.css"
    if extra.exists():
        css += "\n" + extra.read_text().replace("@import url('brand-tokens.css');", "")
    html = html.replace('<link rel="stylesheet" href="styles.css">', f"<style>{css}</style>")
    html = html.replace('<link rel="stylesheet" href="documents.css">', "")
    if (ROOT / "app.js").exists():
        html = html.replace('<script src="app.js"></script>', f"<script>{(ROOT / 'app.js').read_text()}</script>")
    return html


def overlap(a, b):
    return min(a["right"], b["right"]) - max(a["x"], b["x"]) > 0 and min(a["bottom"], b["bottom"]) - max(a["y"], b["y"]) > 0


def main() -> None:
    failures = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox"])
        for label, width, height in VIEWPORTS:
            page = browser.new_page(viewport={"width": width, "height": height})
            page.set_content(inline_html("index.html"), wait_until="load")
            page.wait_for_timeout(250)
            data = page.evaluate(
                """() => {
                    const rect = el => { const r = el.getBoundingClientRect(); return {x:r.x,y:r.y,right:r.right,bottom:r.bottom,width:r.width,height:r.height}; };
                    const h1 = document.querySelector('.hero h1');
                    const chip = document.querySelector('.return-chip');
                    return {
                        bodyOverflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                        headlineOverflow: h1.scrollWidth - h1.clientWidth,
                        chip: chip ? rect(chip) : null,
                        layers: [...document.querySelectorAll('.layer')].map(rect),
                        heroHasBuildline: !!document.querySelector('.hero .buildline'),
                        modelExists: !!document.querySelector('#model .buildline'),
                        documentCards: document.querySelectorAll('#documents .document-card').length,
                        documentsBeforeFooter: (() => { const d=document.querySelector('#documents'), f=document.querySelector('footer'); return !!d && !!f && d.compareDocumentPosition(f) & Node.DOCUMENT_POSITION_FOLLOWING; })(),
                    };
                }"""
            )
            if data["bodyOverflow"] > 1:
                failures.append(f"{label}: horizontal overflow {data['bodyOverflow']}px")
            if data["headlineOverflow"] > 1:
                failures.append(f"{label}: headline text exceeds its box by {data['headlineOverflow']}px")
            if data["heroHasBuildline"]:
                failures.append(f"{label}: full Buildline interaction remains inside the hero")
            if not data["modelExists"]:
                failures.append(f"{label}: dedicated Buildline section is missing")
            if data["documentCards"] != 5:
                failures.append(f"{label}: expected 5 application-kit cards, found {data['documentCards']}")
            if not data["documentsBeforeFooter"]:
                failures.append(f"{label}: application kit is not a discoverable pre-footer section")
            if data["chip"]:
                for index, layer in enumerate(data["layers"]):
                    if overlap(data["chip"], layer):
                        failures.append(f"{label}: return output overlaps layer {index + 1}")
            page.close()

        for route, minimum_text in DOCS.items():
            page = browser.new_page(viewport={"width": 1280, "height": 800})
            page.set_content(inline_html(route), wait_until="load")
            data = page.evaluate(
                """() => ({
                    iframeCount: document.querySelectorAll('iframe').length,
                    onlineDocument: !!document.querySelector('.online-document'),
                    mainText: document.querySelector('main')?.innerText.trim().length || 0,
                    download: !!document.querySelector('a[download][href$=".pdf"]'),
                })"""
            )
            if data["iframeCount"]:
                failures.append(f"{route}: embeds a PDF iframe")
            if not data["onlineDocument"]:
                failures.append(f"{route}: missing native online document")
            if data["mainText"] < minimum_text:
                failures.append(f"{route}: native text is too sparse ({data['mainText']} < {minimum_text})")
            if not data["download"]:
                failures.append(f"{route}: missing native PDF download")
            page.close()
        browser.close()

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print("PASS")


if __name__ == "__main__":
    main()
