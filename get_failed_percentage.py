def get_failed_percentage(results):
    count = {}

    for items in results:
        if items in count:
            count[items]= count[items]+1
        else:
            count[items]= 1

    if "fail" in count:
        percentage = (count["fail"] / len(results)) * 100
    else:
        percentage = 0

    return percentage

print (get_failed_percentage(["pass", "fail", "pass", "pass"]))