"""Fuzz target for the Backend Django URL dispatcher.

Run locally with:
    pip install atheris
    python -m atheris Backend/fuzz_targets/urls_fuzz.py

This is a scaffold target. It exercises the URL resolution path
with random inputs so that any future regressions in the URL
dispatcher (e.g. ReDoS in path-to-regexp, or a routing
table that throws on edge cases) surface as crashes or
harness failures rather than 500s in production.
"""

import atheris
import sys

with atheris.instrument_imports():
    from django.urls import resolve, Resolver404


def TestOneInput(data: bytes) -> None:
    fdp = atheris.FuzzedDataProvider(data)
    raw_path = fdp.ConsumeUnicodeNoSurrogates(255)
    if not raw_path.startswith("/"):
        raw_path = "/" + raw_path
    try:
        resolve(raw_path)
    except Resolver404:
        pass
    except Exception:  # noqa: BLE001
        # Re-raise as atheris crash
        raise


if __name__ == "__main__":
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
