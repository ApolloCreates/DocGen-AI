from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def create_documentation_zip(
    output_dir: Path,
) -> Path:

    zip_path = output_dir.parent / f"{output_dir.name}-docs.zip"

    with ZipFile(
        zip_path,
        "w",
        compression=ZIP_DEFLATED,
    ) as archive:

        for file in output_dir.iterdir():

            if file.is_file():

                archive.write(
                    file,
                    arcname=file.name,
                )

    return zip_path