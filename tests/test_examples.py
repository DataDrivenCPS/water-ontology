def test_examples_validate(example_file, example_validation_result):
    assert not example_validation_result["has_example_warnings_or_violations"], (
        f"{example_file} produced a SHACL warning or violation:\n"
        f"{example_validation_result['report_string']}"
    )
