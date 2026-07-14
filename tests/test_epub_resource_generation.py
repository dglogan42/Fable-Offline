import tempfile
import unittest
import zipfile
from pathlib import Path

import red_rising_companion_guide as generator


class EpubResourceGenerationTests(unittest.TestCase):
    def test_build_epub_from_python_and_epub_resources(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)

            py_resource = tmp_path / "notes.py"
            py_resource.write_text(
                '"""Module docstring for the resource."""\n'
                '# A helpful comment\n'
                'def describe():\n'
                '    """Function docstring for chapter content."""\n'
                '    return "python source"\n',
                encoding="utf-8",
            )

            existing_epub = tmp_path / "source.epub"
            with zipfile.ZipFile(existing_epub, "w", zipfile.ZIP_DEFLATED) as archive:
                archive.writestr(
                    "mimetype",
                    "application/epub+zip",
                    compress_type=zipfile.ZIP_STORED,
                )
                archive.writestr(
                    "META-INF/container.xml",
                    """<?xml version=\"1.0\"?>
<container version=\"1.0\" xmlns=\"urn:oasis:names:tc:opendocument:xmlns:container\">
  <rootfiles><rootfile full-path=\"OEBPS/content.opf\" media-type=\"application/oebps-package+xml\"/></rootfiles>
</container>""",
                )
                archive.writestr(
                    "OEBPS/chapter.xhtml",
                    """<?xml version=\"1.0\"?>
<!DOCTYPE html>
<html xmlns=\"http://www.w3.org/1999/xhtml\">
<head><title>Existing chapter</title></head>
<body><h1>Existing chapter</h1><p>From an existing EPUB.</p></body>
</html>""",
                )
                archive.writestr(
                    "OEBPS/content.opf",
                    """<?xml version=\"1.0\"?>
<package xmlns=\"http://www.idpf.org/2007/opf\" version=\"3.0\">
  <metadata xmlns:dc=\"http://purl.org/dc/elements/1.1/\"><dc:title>Seed</dc:title></metadata>
  <manifest></manifest><spine></spine>
</package>""",
                )

            output_path = tmp_path / "combined.epub"
            result = generator.create_epub(
                resource_paths=[str(py_resource), str(existing_epub)],
                output_path=str(output_path),
                title="Combined Resource Guide",
                creator="Fable",
            )

            self.assertEqual(str(output_path), result)
            self.assertTrue(output_path.exists())

            with zipfile.ZipFile(output_path) as archive:
                names = archive.namelist()
                self.assertIn("OEBPS/content.opf", names)
                self.assertIn("OEBPS/chapter_00_notes.xhtml", names)
                self.assertIn("OEBPS/chapter_01_source.xhtml", names)

                py_content = archive.read("OEBPS/chapter_00_notes.xhtml").decode("utf-8")
                self.assertIn("Module docstring for the resource.", py_content)
                self.assertIn("Function docstring for chapter content.", py_content)

                epub_content = archive.read("OEBPS/chapter_01_source.xhtml").decode("utf-8")
                self.assertIn("Existing chapter", epub_content)
                self.assertIn("From an existing EPUB.", epub_content)


if __name__ == "__main__":
    unittest.main()
