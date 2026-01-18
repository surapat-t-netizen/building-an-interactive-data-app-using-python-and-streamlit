import pandas as pd


# สร้างข้อมูลขึ้นมาใช้งานในรูปแบบ DataFrame
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df.head())

print(df["calories"])
print(df["duration"])

# AVG
print(df["calories"].mean())

df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")
print(df.head(10))