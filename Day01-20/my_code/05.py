
height = float(input("请输入身高（m）："))
weight = float(input("请输入体重（kg）："))

BMI = weight / (height ** 2)
print(f"体质指数：{BMI = :.2f}")
if BMI < 18.5:
    print("偏瘦")
elif BMI > 24:
    print("偏胖")
else:
    print("正常")