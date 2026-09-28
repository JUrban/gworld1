# Source archive

The publisher is https://shpilrain.ccny.cuny.edu/gworld/problems/. Retrieval date: 28 September 2026. `manifest.json` contains URLs, UTC retrieval times, HTTP results, content types, last-modified headers where supplied, byte lengths, SHA-256 hashes and discovered links.

`raw/` contains the original bytes of the main index, all 16 linked category pages, the Hall of Fame, `Back.html`, `Back2.html`, and `Aut_F3.pdf`: 21 successful downloads. A 22nd URL, the publisher's erroneous `Back.htm`, returned 404. The adjacent correct link and full background page are available. No category or numbered problem was lost to that broken link.

`scripts/snapshot_sources.py` traverses document/resource links within the supplied `/gworld/problems/` directory, strips fragments for downloading, and ignores HTML comments. References to papers or sites outside this directory are indexed in the manifest but are **not** recursively downloaded. The old external visitor-counter image is not part of the mathematical corpus. The additional Gardam bibliographic check is recorded separately in `status-evidence.json`.

HTML declares ISO-8859-1. `raw/` preserves those bytes unchanged. The search index decodes that encoding, and the convenience wrappers use UTF-8. Original markup and literal TeX-like notation can be malformed; derived text and the convenience wrappers are not certified transcriptions. Compare original source and rendering before making a mathematical claim.

`problems/ID/source-fragment.html` is a verbatim byte slice, whose offsets and hash are recorded in `data/problems.json`. `statement.html` adds an offline wrapper and a local base URL so background links remain usable. Markdown/plain text is only a finding aid. Rebuild derived indexes during preparation with `python3 scripts/build_catalog.py`; the source downloader refuses to overwrite an existing snapshot.

The source collection and linked documents retain their original authorship. Archiving them here does not assign a new license to third-party material.
