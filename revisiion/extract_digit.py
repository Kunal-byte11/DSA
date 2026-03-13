def extract_digit(num : int) -> None:
    n = num
    while num >0:
        last_digit = num % 10
        print(last_digit , end="")
        num = num // 10
(extract_digit(56789))
