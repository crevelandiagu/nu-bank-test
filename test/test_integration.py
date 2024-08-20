import sys
import main
from .examples import TEST_EXAMPLES


def test_app_main_user_case_base(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_BASE"), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_base_one(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_BASE_ONE"), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 10000.0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_base_two(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_BASE"), TEST_EXAMPLES.get("EXAMPLE_BASE_ONE"), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}]\n[{"tax": 0}, {"tax": 10000.0}]\n'

    assert captured.out == expected_output

def test_app_main_user_case_exm_one(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_1"), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_two(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_2").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 10000.0}, {"tax": 0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_three(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_3").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 1000.0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_four(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_4").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_five(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_5").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 10000.0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_six(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_6").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 3000.0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_seven(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_7").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 3000.0}, {"tax": 0}, {"tax": 0}, {"tax": 3700.0}, {"tax": 0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_eight(monkeypatch, capsys):
    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_8").replace('\n', ''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 80000.0}, {"tax": 0}, {"tax": 60000.0}]\n'
    assert captured.out == expected_output

def test_app_main_user_case_exm_nine(monkeypatch, capsys):

    # Mock stdin input
    monkeypatch.setattr(sys, 'stdin', [TEST_EXAMPLES.get("EXAMPLE_9").replace('\n',''), 'exit'])

    main.app_main()

    captured = capsys.readouterr()
    expected_output = '[{"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 0}, {"tax": 1000.0}, {"tax": 2400.0}]\n'
    assert captured.out == expected_output