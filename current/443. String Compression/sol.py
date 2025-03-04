from typing import List


class Solution:
    
    def handle_end(self,same_count,i,chars):
        if same_count>0:
            same_count_str = str(same_count+1)
            extra_space = len(same_count_str)
            for _ in range(same_count-extra_space):
                chars.pop(i-same_count)

            for j in range(extra_space):
                replace_index = i+1-same_count+j
                chars[replace_index]=same_count_str[j]
        return chars
    
    def handle_same_count(self,same_count,i,chars)->tuple[List[str],int]:
        same_count_str = str(same_count+1)
        extra_space = len(same_count_str)
        for _ in range(same_count-extra_space):
                chars.pop(i-same_count)
        for j in range(extra_space):
            replace_index = i+1-same_count+j
            chars[replace_index]=same_count_str[j]
        return chars,i-same_count-1+extra_space
    
    def compress(self, chars: List[str]) -> int:
        same_count =0
        i =0
        while(i<len(chars)):
            if i+1 == len(chars):
                chars = self.handle_end(same_count,i,chars)
                break
            if chars[i]==chars[i+1]:
                same_count +=1
            elif same_count >0:
                chars,i =self.handle_same_count(same_count,i,chars)
                same_count = 0
            i +=1
        return len(chars)
    
    
    
def main():
    s = Solution()
    s.compress(["b","l","l","l","l","l","l","4","4","W","W","&","d","d","d","@","D","D",".",".",".","8","8","8","U","V",">","J","J","k","H","H","=","l","[","[","[","[","[","[","[","a","a","'","<","[","[","y","V","l","l","'","$","E","`","v","k","E","E","t","t","t","t","t","=","=","0","C","a","l","l","l","r","R","M","M","c","c","c","A","A","S","9","9","9","9",")",")","\\","s","\\","\\","y","W","W","W","J","J","J","J","6","6","<","<","E","u","e","e","e","e","e","e","e","e","e","9","9","9","9","R","8","?","F","3","&","&","&","&","f","%","%","2","2","2",")",")",")","J","p","|","D","D","D","s","t","V","V","?","^","^","S","3","3","3","3","h","*","|","|","b","b","a","a","a","r","r","r","r","J",".","^","^","~","g",":",":",":","(","4","4","4","4","w","w","w","w","w","w","w","C","?","=","d","L",":","0","0","c","w","w","w","w","w","w","{","{","t","k","k","k","&","&","&","h","j","j","j","0","3","l",";",";",";",";",";",".",".",".","%","1","1","1","l","9","?","?","?","t",">","E","N","N","@",">",".",".","I","a","a","a","a","B","7","7","{","o","o","-","+","+","+","+","o","o","}","B","B","r","r","r","q","4","4","4","9","W","W","W","W","W","'","'","'","g","J","(","(","(","(","t","t","?",";","g","g","g","0","]","]","]"])
    
if __name__ =="__main__":
    main()
                