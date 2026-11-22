"""Validate generated local pages/assets/anchors using the actual MkDocs configuration."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from mkdocs.config import load_config


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.references = []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])


def main():
    root = Path(__file__).resolve().parents[1]
    config = load_config(config_file=str(root / "mkdocs.yml"))
    site = Path(config["site_dir"]).resolve()
    base = config["site_url"].rstrip("/") + "/"
    origin = urlsplit(base)
    prefix = unquote(origin.path)
    pages = {path: Page(path.read_text(encoding="utf-8")) for path in site.rglob("*.html")}
    if not pages:
        raise ValueError("No built HTML pages found")
    failures = []
    checked = 0
    for path, page in pages.items():
        relative = path.relative_to(site).as_posix()
        for reference in page.references:
            target = urlsplit(urljoin(urljoin(base, relative), reference))
            if target.scheme not in ("http", "https") or target.netloc != origin.netloc:
                continue
            target_path = unquote(target.path)
            if not target_path.startswith(prefix):
                continue
            destination = (site / target_path[len(prefix):]).resolve()
            if not destination.is_relative_to(site):
                failures.append(f"{relative}: target leaves site: {reference}")
                continue
            if destination.is_dir():
                destination /= "index.html"
            if not destination.is_file():
                failures.append(f"{relative}: missing file: {reference}")
                continue
            checked += 1
            if target.fragment and destination.suffix == ".html":
                if destination not in pages or unquote(target.fragment) not in pages[destination].ids:
                    failures.append(f"{relative}: missing fragment: {reference}")
    if failures:
        raise ValueError("Invalid site references:\n" + "\n".join(sorted(set(failures))))
    print(f"Verified {checked} local links/assets across {len(pages)} HTML pages.")


if __name__ == "__main__":
    main()
