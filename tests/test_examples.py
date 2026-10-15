def test_examples_validate(example_file, example_validation_result):
    # Warnings and info results are allowed: they flag modeling advice from S223
    # (for example, a property no sensor observes), not an invalid model.
    assert not example_validation_result["has_example_violations"], (
        f"{example_file} produced a SHACL violation:\n"
        f"{example_validation_result['report_string']}"
    )
