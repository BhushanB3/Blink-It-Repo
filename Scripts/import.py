import pandas as pd

df = pd.read_csv("C:/2nd Milestone/Power BI Project/Blinkit/Raw Data/Category_Icons.csv")
print(df.head())
table_name = "Category_Icons"

with open(f"{table_name}.sql", "w", encoding="utf-8") as f:
    f.write(f"CREATE TABLE {table_name} (\n")
    for col in df.columns:
        f.write(f"  `{col}` TEXT,\n")
    f.seek(f.tell() - 2)  # remove last comma
    f.write("\n);\n")

    for _, row in df.iterrows():
        values = "', '".join(str(x).replace("'", "''") for x in row)
        f.write(f"INSERT INTO {table_name} VALUES ('{values}');\n")
