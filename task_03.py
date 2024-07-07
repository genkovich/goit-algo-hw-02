def check_open_close_brackets(s):
    stack = []

    brackets_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        try:
            closing_bracket = brackets_dict[char]
            if stack[-1] == closing_bracket:
                stack.pop()
            else:
                return False
        except KeyError:
            if char in brackets_dict.values():
                stack.append(char)

        except IndexError:
            return False

    return len(stack) == 0


def main():
    s = '( ){[ 1 ]( 1 + 3 )( ){ }}'
    print(check_open_close_brackets(s))

    s = '( 23 ( 2 - 3);'
    print(check_open_close_brackets(s))

    s = '( 11 }'
    print(check_open_close_brackets(s))


if __name__ == '__main__':
    main()
