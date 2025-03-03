from abc import ABC
import time


class Reverse(ABC):
    def reverse_string(self, string: str) -> str:
        """Reverse String"""

    def get_time(
        self,
    ) -> float:
        return time.process_time()


class BruteForce(Reverse):
    def reverse_string(self, string):
        reverse_string = ""
        for s in range(len(string) - 1, -1, -1):
            reverse_string += string[s]
        return reverse_string


class TwoPoint(Reverse):
    def reverse_string(self, string):
        begin_pointer = 0
        end_pointer = len(string) - 1
        l_string = list(string)

        while begin_pointer <= end_pointer:
            l_string = self.swap(begin_pointer, end_pointer, l_string)
            begin_pointer += 1
            end_pointer -= 1
        return string

    def swap(self, begin_pointer: int, end_pointer: int, string: list) -> str:
        string[begin_pointer] = string[end_pointer]
        string[end_pointer] = string[begin_pointer]
        return string


def main():
    initial_string = "Hello"
    print(f"Initial String is: {initial_string}")
    brut_force = BruteForce()
    init_time = brut_force.get_time()
    reversed_string = brut_force.reverse_string(initial_string)
    print(f"Reversed string is: {reversed_string}")
    print(
        f"Reversing with {brut_force.__class__.__name__} took: {brut_force.get_time() - init_time} "
    )

    two_point = TwoPoint()
    init_time = two_point.get_time()
    reversed_string = two_point.reverse_string(initial_string)
    print(f"Reversed string is: {reversed_string}")
    print(
        f"Reversing with {two_point.__class__.__name__} took: {two_point.get_time() - init_time} "
    )


if __name__ == "__main__":
    main()
