from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        same_count =0
        i =0
        while(i<len(chars)):
            if i+1 == len(chars):
                if same_count>0:
                    same_count_str = str(same_count+1)
                    extra_space = len(same_count_str)
                    for _ in range(same_count-extra_space):
                        chars.pop(i-same_count)

                    for j in range(extra_space):
                        replace_index = i+1-same_count+j
                        chars[replace_index]=same_count_str[j]
                break
            if chars[i]==chars[i+1]:
                same_count +=1
            elif same_count >0:
                same_count_str = str(same_count+1)
                extra_space = len(same_count_str)
                for _ in range(same_count-extra_space):
                        chars.pop(i-same_count)
                for j in range(extra_space):
                    replace_index = i+1-same_count+j
                    chars[replace_index]=same_count_str[j]
                same_count =0
            i +=1
        return len(chars)
    
    
    
def main():
    s = Solution()
    s.compress(["a","a","a","b","b","a","a"])
    
if __name__ =="__main__":
    main()
                