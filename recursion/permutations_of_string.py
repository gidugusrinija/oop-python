def get_permutations(s):
    chars = list(s)
    result = []

    def backtrack(start_index):
        if start_index == len(chars):
            result.append("".join(chars))
            return

        used_chars = set()

        for i in range(start_index, len(chars)):
            if chars[i] in used_chars:
                continue
            used_chars.add(chars[i])

            chars[start_index], chars[i] = chars[i], chars[start_index]
            backtrack(start_index + 1)
            chars[start_index], chars[i] = chars[i], chars[start_index]

    backtrack(0)
    return result


stri = "ab"

print(get_permutations(stri))
