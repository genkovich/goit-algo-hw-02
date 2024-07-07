from collections import deque


def is_palindrome(s):
    s = s.lower().replace(' ', '')
    s = ''.join([c for c in s if c.isalpha()])

    deq = deque(s)
    if len(deq) == 0:
        return False

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False

    return True


def main():
    s = 'taco cat'
    print(is_palindrome(s))

    s = 'hello'
    print(is_palindrome(s))

    s = "Eva, can I see bees in a cave?"
    print(is_palindrome(s))


if __name__ == '__main__':
    main()
