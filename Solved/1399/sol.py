class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dict = {}
        vals = [str(i) for i in range(1,n+1)]
        sums = [sum(int(digit) for digit in numb) for numb in vals]

        for number,sum_number in zip(vals,sums):
            current = sum_dict.get(sum_number)
            if current:
                current.append(number)
            else:
                current = [number]
            sum_dict[sum_number]= current

        
        max_size = max(len(group) for group in sum_dict.values())
        return sum(1 for group in sum_dict.values() if len(group)==max_size)
            



def main():
    s =Solution()
    print(s.countLargestGroup(13))

if __name__ == "__main__":
    main()