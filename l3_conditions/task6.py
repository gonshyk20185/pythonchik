# Write the body of the function to make the script work without errors
def largest_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)


if __name__ == "__main__":
    # Do not change the below asserts
    assert largest_of_three(1, 2, 3) == 3
    assert largest_of_three(10, 5, 7) == 10
    assert largest_of_three(-1, -2, -3) == -1
