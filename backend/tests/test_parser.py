from app.parser.service import ParserService


def test_python_parser(tmp_path):

    source = """
class User:
    pass


def hello():
    return "hello"
"""

    test_file = tmp_path / "test.py"

    test_file.write_text(
        source,
        encoding="utf-8",
    )

    service = ParserService()

    result = service.analyze(
        test_file
    )

    assert result is not None

    assert result.language == "python"

    assert len(result.classes) == 1
    assert result.classes[0].name == "User"

    assert len(result.functions) == 1
    assert result.functions[0].name == "hello"