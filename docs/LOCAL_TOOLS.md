# Local statement rendering

Chromium's additional shared libraries were extracted during preparation
under ignored `scratch/browser-libs/root`. When they are present, invoke
the existing renderer from the repository root as follows:

```sh
LD_LIBRARY_PATH="$PWD/scratch/browser-libs/root/usr/lib/x86_64-linux-gnu" .venv/bin/python scripts/render_statement.py PROBLEM_ID
```

On 29 September 2026 an invocation without that path failed to find
libatk. The libraries were already present; supplying the path restored
rendering, with no installation or package refresh. O6 and MA7 captures
were successfully generated and actually viewed afterward. The earlier
failed attempts remain documented.

This directory is local infrastructure, not a tracked dependency bundle.
A new machine must supply its own compatible browser libraries and
Playwright browser. The renderer refuses to overwrite an existing capture;
its generated metadata initially says visual inspection is pending until
the image has actually been inspected.
