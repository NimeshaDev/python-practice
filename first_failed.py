def first_failed(tests):
    for name, status in tests:
        if status == "fail":
            return name
    return None

tests = [("login", "pass"), ("search", "fail"), ("logout", "fail")]
print(first_failed(tests))                 # search
print(first_failed([("login", "pass")]))   # None