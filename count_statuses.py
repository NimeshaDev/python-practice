def count_statuses(status):
    count= {}

    for items in status:
        if items in count:
        
            count[items]= count[items]+1
        else:
            count[items]=1

    return count

print (count_statuses(["pass", "fail", "pass", "pass", "fail"]))