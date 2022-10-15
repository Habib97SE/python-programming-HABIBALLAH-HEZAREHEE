def count_money(amount: int) -> dict:
    """
        Write down how many we have. 
        Params: 
            amount - int: the amount of money which we need to calculate
        Returns: 
            dict : The result in dictionary with the standard amount as key and how much we have as value
    """
    final_result = {}
    for standard in [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]:
        if amount == 0:
            break
        remained = amount % standard
        final_result[f"{standard}kr"] = amount - remained
        amount = remained
    return final_result


def main():
    print(count_money(1000))
    print(count_money(999))
    print(count_money(23))


if __name__ == "__main__":
    main()
