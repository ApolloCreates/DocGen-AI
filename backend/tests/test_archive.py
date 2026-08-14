from pathlib import Path

from app.services.archive import create_documentation_zip


def test_create_documentation_zip(tmp_path):

    output_dir = tmp_path / "TestRepo"

    output_dir.mkdir()

    (output_dir / "README.md").write_text(
        "# Test Repository",
        encoding="utf-8",
    )

    (output_dir / "SUMMARY.md").write_text(
        "# Summary",
        encoding="utf-8",
    )

    zip_path = create_documentation_zip(
        output_dir
    )

    assert zip_path.exists()

    assert zip_path.name == "TestRepo-docs.zip"

    assert zip_path.stat().st_size > 0