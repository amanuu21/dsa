1from typing import List
2
3class Solution:
4    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
5        result = []
6        i = 0
7        
8        while i < len(words):
9            # Step 1: Greedily pack as many words as possible into the current line
10            line_words = []
11            line_length = 0
12            
13            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
14                line_words.append(words[i])
15                line_length += len(words[i])
16                i += 1
17            
18            # Step 2: Build the line
19            if i == len(words):
20                # Last line: left-justified
21                line = ' '.join(line_words)
22                line += ' ' * (maxWidth - len(line))
23                result.append(line)
24            else:
25                # Regular line: fully justified
26                total_spaces = maxWidth - line_length
27                num_gaps = len(line_words) - 1
28                
29                if num_gaps == 0:
30                    # Only one word in the line
31                    line = line_words[0] + ' ' * total_spaces
32                else:
33                    # Distribute spaces as evenly as possible
34                    spaces_per_gap = total_spaces // num_gaps
35                    extra_spaces = total_spaces % num_gaps
36                    
37                    line = []
38                    for j in range(num_gaps):
39                        line.append(line_words[j])
40                        spaces = spaces_per_gap + (1 if j < extra_spaces else 0)
41                        line.append(' ' * spaces)
42                    line.append(line_words[-1])
43                    line = ''.join(line)
44                
45                result.append(line)
46        
47        return result