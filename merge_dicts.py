def merge_dicts(first, second):

    results={}

    for items in first:
        results[items]=first[items]

    for items in second:
        results[items]= second[items]


    return results

print(merge_dicts({"Ann": 111, "Bob": 222}, {"Bob": 999, "Cara": 333}))