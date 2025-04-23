import pandas as pd

# Excel file path
excel_file = "C:/2nd Milestone/Power BI Project/Blinkit/Raw Data/Rating_Icon.xlsx"
sheet_name = "Sheet1"  # change if needed
table_name = "Rating_Icon"

# Read Excel file
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Create SQL dump
with open(f"{table_name}.sql", "w", encoding="utf-8") as f:
    # CREATE TABLE
    f.write(f"CREATE TABLE `{table_name}` (\n")
    for col in df.columns:
        f.write(f"  `{col}` TEXT,\n")
    f.seek(f.tell() - 2)  # remove last comma
    f.write("\n);\n\n")

    # INSERT INTO
    for _, row in df.iterrows():
        values = "', '".join(str(x).replace("'", "''") for x in row)
        f.write(f"INSERT INTO `{table_name}` VALUES ('{values}');\n")

print(f"Dump created: {table_name}.sql ✅")
