from main import load_works, done_count, done_total, longest_done_time

def test_load_works_normal_csv():
    works, has_error, errors = load_works("sample/works.csv")

    assert has_error == False
    assert done_count(works) == 3
    assert done_total(works) == 135

    longest, longest_name = longest_done_time(works)

    assert longest == 60
    assert longest_name == "Python Learning"

def test_load_works_invalid_csv():
    works, has_error, errors = load_works("sample/works_invalid.csv")

    assert has_error == True
    assert len(errors) == 2

    assert errors[0]["gyo"] == 2
    assert errors[1]["gyo"] == 3

    assert errors[0]["row"] == ["Image Creation", "abc", "done"]
    assert errors[1]["row"] == ["Document Review", "30"]

def test_load_works_file_not_found():
    works, has_error, errors = load_works("sample/not_found.csv")

    assert works == []
    assert has_error == True
    assert errors == []

def test_load_works_empty_csv():
    works, has_error, errors = load_works("sample/works_empty.csv")

    assert works == []
    assert has_error == False
    assert errors == []

    assert done_count(works) == 0
    assert done_total(works) == 0

    longest, longest_name = longest_done_time(works)

    assert longest == 0
    assert longest_name == None

def test_no_done_works():
    works, has_error, errors = load_works("sample/works_no_done.csv")

    assert has_error == False
    assert done_count(works) == 0
    assert done_total(works) == 0

    longest, longest_name = longest_done_time(works)

    assert longest == 0
    assert longest_name == None