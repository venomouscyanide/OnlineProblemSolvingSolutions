# https://leetcode.com/problems/validate-ip-address/
import string


def _check_v4(queryIP):
    for number in queryIP:
        try:
            int_number = int(number)
            if number.startswith("0") and len(number) > 1:
                return False

            if 0 <= int_number <= 255:
                continue

            return False
        except:
            return False

    return True


def _check_v6(queryIP):
    valid_chars = set("ABCDEF").union(set("abcdef").union(set(string.digits)))

    for number in queryIP:
        try:
            len_n = len(number)
            if not number:
                return False
            if len_n > 4:
                return False
            for char in number:
                if char not in valid_chars:
                    return False
        except:
            return False

    return True


def run(queryIP):
    split_v4 = queryIP.split(".")
    split_v6 = queryIP.split(":")
    check = "Neither"

    if len(split_v4) != 4 and len(split_v6) != 8:
        return check

    check_v4 = check_v6 = False
    if len(split_v4) == 4:
        check_v4 = _check_v4(split_v4)
    else:
        check_v6 = _check_v6(split_v6)

    if check_v4:
        check = "IPv4"
    if check_v6:
        check = "IPv6"

    return check


if __name__ == '__main__':
    queryIP = "172.16.254.123"
    print(run(queryIP))

    queryIP = "2001:0dp8:85a3:00:0:8A2E:0370:7334"
    print(run(queryIP))

    queryIP = "256.256.256.256"
    print(run(queryIP))
