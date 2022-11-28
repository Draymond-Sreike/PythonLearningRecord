staff = \
    {
        "王力鸿":
            {
                "部门": "科技部",
                "工资": 3000,
                "级别": 1
            },
        "周杰轮":
            {
                "部门": "市场部",
                "工资": 5000,
                "级别": 2
            },
        "林俊节":
            {
                "部门": "市场部",
                "工资": 7000,
                "级别": 3
            },
        "张学油":
            {
                "部门": "科技部",
                "工资": 4000,
                "级别": 1
            },
        "刘德滑":
            {
                "部门": "市场部",
                "工资": 6000,
                "级别": 2
            }
    }

for individual in staff:
    print(f"修改前{individual}:{staff[individual]}")

for individual in staff:
    if staff[individual]["级别"] == 1:
        staff[individual]["级别"] += 1
        staff[individual]["工资"] += 1000

for individual in staff:
    print(f"修改后{individual}:{staff[individual]}")