from typing import List

dict_digits = {
    "0": ["._.", "|.|", "|_|"],
    "1": ["...", "..|", "..|"],
    "2": ["._.", "._|", "|_."],
    "3": ["._.", "._|", "._|"],
    "4": ["...", "|_|", "..|"],
    "5": ["._.", "|_.", "._|"],
    "6": ["._.", "|_.", "|_|"],
    "7": ["._.", "..|", "..|"],
    "8": ["._.", "|_|", "|_|"],
    "9": ["._.", "|_|", "..|"],
}


class LCD:
    def __init__(self, input_digits: int, spacing: int = None):
        self._input_digits = str(input_digits)
        self._spacing = self._gen_str_spacing(spacing)

    @staticmethod
    def _gen_str_spacing(spacing) -> str:
        if spacing:
            return "".join(" " for _ in range(spacing))
        return ""

    def _get_input_digits_to_list(self) -> List[str]:
        assert len(self._input_digits) > 0
        return [digit for digit in self._input_digits]

    @staticmethod
    def get_single_digit_row(digit: int, row) -> str:
        return f"{dict_digits[str(digit)][row]}"

    def get_digits_in_str_format(self) -> str:
        my_list_digits = ["\n"]
        for row in range(3):
            for digit in self._get_input_digits_to_list():
                my_list_digits.append(self.get_single_digit_row(digit=digit, row=row))
                my_list_digits.append(self._spacing)
            my_list_digits.append("\n")

        return "".join(my_list_digits)


if __name__ == '__main__':
    lcd = LCD(123456789, spacing=2)
    lcd_digit = lcd.get_digits_in_str_format()
    print(lcd_digit)
