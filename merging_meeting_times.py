"""Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

   >>> merge_ranges(  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
   [(0, 1), (3, 8), (9, 12)]

"""


def merge_ranges(times):
    sorted_times = sorted(times)
    results = [sorted_times[0]]
    for time in sorted_times:
        time_not_exist_in_results = True
        # look thru results if time is connected to any of res, merge or skip
        for i, result in enumerate(results):
            if result[0] <= time[0] <= result[1] or result[0] <= time[1] <= result[1]:
                time_not_exist_in_results = False
                start_time, end_time = result[0], result[1]
                if time[1] > result[1]:
                    end_time = time[1]
                if time[0] < result[0]:
                    start_time = time[0]
                results[i] = (start_time, end_time)
        # else append time in times
        if time_not_exist_in_results:
            results.append(time)
    return(results)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. GREAT JOB!\n")
