"""Lightweight project health checks for interview/demo readiness."""

import importlib
import pathlib
import sys

MODULES = [
    "app",
    "audio.recorder",
    "config.settings",
    "export.email_sender",
    "export.pdf_export",
    "pipeline.meeting_pipeline",
    "stt.stt_manager",
    "stt.whisper_stt",
]


def compile_check(root: pathlib.Path) -> list[str]:
    failures: list[str] = []
    for py_file in sorted(root.rglob("*.py")):
        if "__pycache__" in py_file.parts:
            continue
        try:
            source = py_file.read_text(encoding="utf-8")
            compile(source, str(py_file), "exec")
        except Exception as exc:  # pragma: no cover - script only
            failures.append(f"compile failed: {py_file} -> {exc}")
    return failures


def import_check() -> list[str]:
    failures: list[str] = []
    for module in MODULES:
        try:
            importlib.import_module(module)
        except Exception as exc:  # pragma: no cover - script only
            failures.append(f"import failed: {module} -> {exc}")
    return failures


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    compile_failures = compile_check(root)
    import_failures = import_check()

    print("Compile check:", "PASS" if not compile_failures else "FAIL")
    print("Import check:", "PASS" if not import_failures else "FAIL")

    for err in compile_failures + import_failures:
        print(" -", err)

    ok = not compile_failures and not import_failures
    print("Overall:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
