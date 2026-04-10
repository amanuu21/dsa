1from collections import Counter
2
3class Solution:
4    def findSubstring(self, s: str, words: List[str]) -> List[int]:
5        if not s or not words:
6            return []
7
8        word_len = len(words[0])
9        word_count = len(words)
10        total_len = word_len * word_count
11        word_map = Counter(words)
12        result = []
13
14        for i in range(word_len):
15            left = i
16            current_map = {}
17            count = 0
18
19            for right in range(i, len(s) - word_len + 1, word_len):
20                word = s[right:right + word_len]
21
22                if word in word_map:
23                    current_map[word] = current_map.get(word, 0) + 1
24                    count += 1
25
26                    while current_map[word] > word_map[word]:
27                        left_word = s[left:left + word_len]
28                        current_map[left_word] -= 1
29                        left += word_len
30                        count -= 1
31
32                    if count == word_count:
33                        result.append(left)
34
35                        left_word = s[left:left + word_len]
36                        current_map[left_word] -= 1
37                        left += word_len
38                        count -= 1
39                else:
40                    current_map.clear()
41                    count = 0
42                    left = right + word_len
43
44        return result