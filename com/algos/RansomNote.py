# Check if ransome_note is constructable from magazine
import _collections


class Solution:
    def is_constructable(self, ransom_note, magazine):
        mag_dict = _collections.defaultdict(int)
        for char in magazine:
            mag_dict[char] = mag_dict[char] + 1
        for char in ransom_note:
            mag_dict[char] = mag_dict[char] - 1
            if mag_dict[char] < 0:
                return False
        return True


print(Solution().is_constructable("addab", "aabcdde"))
