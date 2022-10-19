# https://leetcode.com/problems/expressive-words/


def run(s, words):
    query_count = _get_count(s)
    words_count = [_get_count(count_occ) for count_occ in words]

    final_matches = 0
    for word in words_count:
        if len(word) != len(query_count):
            continue

        all_match = []
        for item in zip(word, query_count):
            if item[0][0] != item[1][0]:
                all_match = [False]
                break
            else:
                if item[1][1] >= 3 and item[1][1] >= item[0][1]:
                    all_match.append(True)
                elif item[1][1] == item[0][1]:
                    all_match.append(True)
                else:
                    all_match.append(False)
                    break
        if all(all_match):
            final_matches += 1
    return final_matches


def _get_count(s):
    rp = 1
    lp = 0

    count_occ = []
    count = 1
    while rp < len(s):
        if s[lp] == s[rp]:
            count += 1
            rp += 1
        else:
            count_occ.append((s[lp], count))
            lp = rp
            rp = lp + 1
            count = 1
    count_occ.append((s[lp], count))
    return count_occ


if __name__ == '__main__':
    s = "heeeeellooo"
    words = ["hello", "hi", "helo"]
    print(run(s, words))

    s = "zzzzzyyyyy"
    words = ["zzyy", "zy", "zyy"]
    print(run(s, words))
