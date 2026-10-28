import re

CAPACITY = 10
INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


def read_integer(prompt: str) -> int | None:
    raw = input(prompt).strip()
    if not re.fullmatch(r"[+-]?\d+", raw):
        raise ValueError

    value = int(raw)
    if not INT_MIN <= value <= INT_MAX:
        raise ValueError
    return value


def display_stacks(values: list[int], left_top: int, right_top: int) -> None:
    stack_1 = values[: left_top + 1]
    stack_2 = values[right_top:][::-1]

    print("Stack 1 (left to right):", *stack_1 if stack_1 else ["empty"])
    print("Stack 2 (right to left):", *stack_2 if stack_2 else ["empty"])


def main() -> None:
    values = [0] * CAPACITY
    left_top = -1
    right_top = CAPACITY

    while True:
        print("\nDouble-Ended Stack (two stacks in one array)")
        print("1. Push onto Stack 1")
        print("2. Pop from Stack 1")
        print("3. Push onto Stack 2")
        print("4. Pop from Stack 2")
        print("5. Display both stacks")
        print("6. Exit")

        try:
            choice = read_integer("Enter your choice: ")
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue
        except EOFError:
            print("\nInput ended. Exiting.")
            break

        if choice is None:
            print("\nInput ended. Exiting.")
            break

        if choice in (1, 3):
            if left_top + 1 == right_top:
                print("Stack overflow: the array is full.")
                continue

            try:
                value = read_integer("Enter the value to push: ")
            except ValueError:
                print("Invalid value. Enter a whole number.")
                continue
            except EOFError:
                print("\nInput ended. Exiting.")
                break

            if value is None:
                print("\nInput ended. Exiting.")
                break

            if choice == 1:
                left_top += 1
                values[left_top] = value
                print(f"{value} pushed onto Stack 1.")
            else:
                right_top -= 1
                values[right_top] = value
                print(f"{value} pushed onto Stack 2.")
        elif choice == 2:
            if left_top == -1:
                print("Stack 1 underflow: the stack is empty.")
            else:
                print(f"{values[left_top]} popped from Stack 1.")
                left_top -= 1
        elif choice == 4:
            if right_top == CAPACITY:
                print("Stack 2 underflow: the stack is empty.")
            else:
                print(f"{values[right_top]} popped from Stack 2.")
                right_top += 1
        elif choice == 5:
            display_stacks(values, left_top, right_top)
        elif choice == 6:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Select a number from 1 to 6.")


if __name__ == "__main__":
    main()
