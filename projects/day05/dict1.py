student={
    "name": "Ivan",
    "age": 20,
    "grades":[5,5,4]}
print(round(sum(student.get("grades"))/len(student.get("grades")), 2))
def get_value_safe(dict, key):
    if key in dict:
        return dict[key]
    else:
        return None
prises={
    "хлеб": 60,
    "молоко": 90,
    "яйца": 120}
for key in prises:
    if prises[key]>70:
        print(key,prises[key])
def merge_dicts(d1,d2):
    for k1 in d1:
        for k2 in d2:
            if k1==k2:
                d3=d2[k2]+d1[k1]
            elif k1!=k2:
                d3=d3+d1[k1]+d2[k2]
