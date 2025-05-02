
height = float(input("请输入身高（cm）："))
weight = float(input("请输入体重（kg）："))

BMI = weight / (height / 100) ** 2
print(f"体质指数：{BMI = :.2f}")
if BMI < 18.5:
    print("偏瘦")
elif BMI < 24:
    print("身材很棒")
elif BMI < 27:
    print("体重过重")
elif BMI < 30:
    print("轻度肥胖")
elif BMI < 35:
    print("中度肥胖")
else:
    print("重度肥胖")
