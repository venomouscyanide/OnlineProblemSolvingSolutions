def _edge_case(s, lp, rp):
    condition = False
    if rp < len(s):
        condition = (s[lp] == "I" and s[rp] in ["V", "X"]) or \
                    (s[lp] == "X" and s[rp] in ["L", "C"]) or (
                            s[lp] == "C" and s[rp] in ["D", "M"])
    return condition


class Solution:
    def romanToInt(self, s: str) -> int:
        number_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        lp, rp = 0, 1
        total_value = 0
        while lp < len(s):
            if _edge_case(s, lp, rp):
                value = number_map[s[rp]] - number_map[s[lp]]
                lp = rp + 1
                rp = lp + 1
            else:
                value = number_map[s[lp]]
                lp += 1
                rp += 1
            total_value += value

        return total_value


if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))
