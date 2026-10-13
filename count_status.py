def count_status(results, status="pass"):
    if len(results) == 0:
        return 0
    count = 0
    for result in results:
        if result == status:
            count = count + 1
    return count

data = ["pass", "fail", "pass", "pass", "fail"]
print(count_status(data))           # 3
print(count_status(data, "fail"))   # 2
print(count_status([]))             # 0
print(count_status(data, "skipped"))