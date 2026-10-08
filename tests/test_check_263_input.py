import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "check_263_input.py"
spec = importlib.util.spec_from_file_location("check_263_input", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class VerifyInputTests(unittest.TestCase):
    def test_missing_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(module.check(Path(tmp)), 2)

    def test_empty_source_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "src/main/java").mkdir(parents=True)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(module.check(Path(tmp)), 3)

    def test_source_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "src/main/java/net/minecraft"
            source.mkdir(parents=True)
            (source / "Example.java").write_text("class Example {}", encoding="utf-8")
            (Path(tmp) / "src/main/resources").mkdir()
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(module.check(Path(tmp)), 0)


if __name__ == "__main__":
    unittest.main()
