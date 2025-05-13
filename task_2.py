from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:

        if not isinstance(strings, list) or any(
            not isinstance(s, str) for s in strings
        ):
            raise TypeError("Input must be a list of strings.")

        if not strings:
            return ""

        for i, string in enumerate(strings):
            trie.put(string, i)

        current = self.root
        common_prefix = []

        while True:
            children_keys = list(current.children.keys())

            if len(children_keys) != 1:
                break

            char = children_keys[0]
            current = current.children[char]

            if current.value is None and len(strings) != self.size:
                break

            common_prefix.append(char)

        return "".join(common_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    # print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    # print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    # print(trie.find_longest_common_word(strings))
    assert trie.find_longest_common_word(strings) == ""
