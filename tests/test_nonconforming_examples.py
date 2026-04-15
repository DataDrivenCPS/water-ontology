def test_nonconforming_examples_fail_validation(
    nonconforming_example_file,
    nonconforming_example_validation_result,
):
    assert nonconforming_example_validation_result["has_example_violations"], (
        f"{nonconforming_example_file} unexpectedly passed SHACL validation:\n"
        f"{nonconforming_example_validation_result['report_string']}"
    )
