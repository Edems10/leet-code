import random
from timeit import timeit
from typing import List

import numpy as np

from quick_sort import QuickSort


def generate_random_array(size: int) -> List[int]:
    return [random.randint(0, 100) for _ in range(size)]


def generate_random_nparray(size: int) -> np.ndarray:
    return np.random.randint(0, 101, size)


def wrapperNumpyQuickSort(qs: QuickSort) -> List[int]:
    """Function to wrap the quicksort call for timeit."""
    qs.numpyQuickSort()


def wrapperMyQuickSort(qs: QuickSort) -> List[int]:
    """Function to wrap the quicksort call for timeit."""
    qs.myQuickSortImplementation(qs.array)


def default_sorting_algorithm(array: List[int]) -> List[int]:
    return array.sort()


def narray_numpy_sorting(array: np.ndarray, kind="quicksort") -> List[int]:
    np.sort(array, kind="quicksort")


def main():

    ARRAY_SIZE = 50000
    NUMBER_OF_TESTS = 10
    numbers_array = generate_random_array(ARRAY_SIZE)
    np_numbers_array = generate_random_nparray(ARRAY_SIZE)
    qs = QuickSort(array_to_sort=numbers_array)

    # Collect execution times for different sorting methods
    execution_times = []

    # NumPy sorting algorithms
    numpy_sorts = ["quicksort", "mergesort", "heapsort", "stable"]
    for sort_kind in numpy_sorts:
        exec_time = timeit(
            lambda: narray_numpy_sorting(np_numbers_array, kind=sort_kind),
            number=NUMBER_OF_TESTS,
        )
        execution_times.append((f"numpy {sort_kind}", exec_time))

    # Existing sorting functions
    execution_times.append(
        (
            "wrapperNumpyQuickSort",
            timeit(lambda: wrapperNumpyQuickSort(qs), number=NUMBER_OF_TESTS),
        )
    )
    execution_times.append(
        (
            "wrapperMyQuickSort",
            timeit(lambda: wrapperMyQuickSort(qs), number=NUMBER_OF_TESTS),
        )
    )
    execution_times.append(
        (
            "default_sorting_algorithm",
            timeit(
                lambda: default_sorting_algorithm(numbers_array), number=NUMBER_OF_TESTS
            ),
        )
    )

    # Sort by execution time (fastest first)
    execution_times.sort(key=lambda x: x[1])

    # Get the slowest time for comparison
    slowest_time = execution_times[-1][1]

    # Print out results
    print(f"{'Algorithm':<30}{'Time (s)':<15}{'Relative Speed'}")
    for name, exec_time in execution_times:
        relative_speed = slowest_time / exec_time
        print(
            f"{name:<30}{exec_time:.6f}{' ' * 5}{relative_speed:.2f}x faster than slowest"
        )


if __name__ == "__main__":
    main()
