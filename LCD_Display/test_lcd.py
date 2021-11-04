import pytest
from lcd import LCD, dict_digits


@pytest.mark.parametrize("int_digit, row, str_digit", [
    (0, 0, "._."),
    (1, 0, "..."),
    (2, 0, "._."),
])
def test_lcd_print_only_one_row_for_a_digit(int_digit, row, str_digit):
    lcd = LCD(int_digit)
    lcd_digit = lcd.get_single_digit_row(digit=int_digit, row=row)
    assert lcd_digit == str_digit


@pytest.mark.parametrize("int_digit, str_digit", [
    (0, "\n._.\n"
        "|.|\n"
        "|_|\n"),
    (1, "\n...\n"
        "..|\n"
        "..|\n"),
    (2, "\n._.\n"
        "._|\n"
        "|_.\n"),
])
def test_lcd_print_only_one_digit(int_digit, str_digit):
    lcd = LCD(int_digit)
    lcd_digit = lcd.get_digits_in_str_format()
    assert lcd_digit == str_digit


@pytest.mark.parametrize("int_digit, str_digit", [
    (12, "\n...._.\n"
         "..|._|\n"
         "..||_.\n"),
    (34, "\n._....\n"
         "._||_|\n"
         "._|..|\n"),
])
def test_lcd_print_several_digits(int_digit, str_digit):
    lcd = LCD(int_digit)
    lcd_digit = lcd.get_digits_in_str_format()
    assert lcd_digit == str_digit


@pytest.mark.parametrize("int_digit, spacing, str_digit", [
    (12, 2, "\n...  ._.\n"
            "..|  ._|\n"
            "..|  |_.\n"),
])
def test_lcd_print_several_digits_with_space_in_between(int_digit, spacing, str_digit):
    lcd = LCD(int_digit, spacing)
    lcd_digit = lcd.get_digits_in_str_format()
    print(f"Generated: {lcd_digit}")
    print(f"Expected:  {str_digit}")
    assert lcd_digit == str_digit
