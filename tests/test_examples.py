def test_examples_validate(example_file, example_validation_result):
    assert not example_validation_result["has_example_violations"], (
        f"{example_file} failed SHACL validation:\n"
        f"{example_validation_result['report_string']}"
    )
