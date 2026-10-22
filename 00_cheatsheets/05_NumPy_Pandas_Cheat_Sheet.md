# Module 6 Cheat Sheet: NumPy and Pandas

A quick reference for beginner NumPy and Pandas concepts, especially useful for Data Engineering.

## 1. NumPy Basics

| Method / Concept | Description | Code Example |
|---|---|---|
| `import numpy` | Imports NumPy using its common alias. | `import numpy as np` |
| `np.array()` | Creates a NumPy array. | `np.array([10, 20, 30])` |
| `ndim` | Returns the number of dimensions. | `arr.ndim` |
| `shape` | Returns the dimensions of an array. | `arr.shape` |
| `size` | Returns the number of elements. | `arr.size` |
| `dtype` | Returns the array element data type. | `arr.dtype` |
| `np.zeros()` | Creates an array of zeros. | `np.zeros(3)` |
| `np.ones()` | Creates an array of ones. | `np.ones(3)` |
| `np.arange()` | Creates an array of values within a range. | `np.arange(1, 6)` |
| `np.linspace()` | Creates evenly spaced numbers. | `np.linspace(0, 10, 5)` |

## 2. NumPy Indexing and Operations

| Method / Concept | Description | Code Example |
|---|---|---|
| Indexing | Accesses an array element. | `arr[0]` |
| Negative Indexing | Accesses elements from the end. | `arr[-1]` |
| Slicing | Selects multiple elements. | `arr[1:4]` |
| 2D Indexing | Accesses a value by row and column. | `arr[0, 1]` |
| Column Selection | Selects an entire column. | `arr[:, 0]` |
| Boolean Indexing | Selects matching values. | `arr[arr > 20]` |
| Addition | Adds values element by element. | `arr + 10` |
| Multiplication | Multiplies values element by element. | `arr * 2` |
| Broadcasting | Performs operations across compatible shapes. | `arr + np.array([1, 2, 3])` |
| `copy()` | Creates an independent array copy. | `arr.copy()` |

## 3. Important NumPy Functions

| Method | Description | Code Example |
|---|---|---|
| `np.sum()` | Calculates the total. | `np.sum(arr)` |
| `np.mean()` | Calculates the average. | `np.mean(arr)` |
| `np.min()` | Returns the minimum value. | `np.min(arr)` |
| `np.max()` | Returns the maximum value. | `np.max(arr)` |
| `np.median()` | Returns the median. | `np.median(arr)` |
| `np.std()` | Calculates standard deviation. | `np.std(arr)` |
| `reshape()` | Changes array dimensions. | `arr.reshape(2, 3)` |
| `flatten()` | Converts an array to one dimension. | `arr.flatten()` |
| `np.unique()` | Returns sorted unique values for common numeric arrays. | `np.unique(arr)` |
| `np.concatenate()` | Combines arrays. | `np.concatenate((a, b))` |
| `np.where()` | Selects values based on conditions. | `np.where(arr > 10, "High", "Low")` |
| `np.isnan()` | Identifies NaN values. | `np.isnan(arr)` |
| `np.nanmean()` | Calculates the mean while ignoring NaN. | `np.nanmean(arr)` |
| `axis=0` | Aggregates down rows, producing column results. | `np.sum(matrix, axis=0)` |
| `axis=1` | Aggregates across columns, producing row results. | `np.sum(matrix, axis=1)` |

## 4. Pandas Basics

| Method / Concept | Description | Code Example |
|---|---|---|
| `import pandas` | Imports Pandas using its common alias. | `import pandas as pd` |
| `pd.Series()` | Creates one-dimensional labeled data. | `pd.Series([10, 20, 30])` |
| `pd.DataFrame()` | Creates tabular data. | `pd.DataFrame({"Name": ["Ali", "Sara"]})` |
| `shape` | Returns the number of rows and columns. | `df.shape` |
| `columns` | Returns column names. | `df.columns` |
| `dtypes` | Returns column data types. | `df.dtypes` |
| `head()` | Displays the first rows. | `df.head(5)` |
| `tail()` | Displays the last rows. | `df.tail(5)` |
| `info()` | Displays DataFrame information. | `df.info()` |
| `describe()` | Displays descriptive statistics. | `df.describe()` |

## 5. Reading and Writing Files

| Method | Description | Code Example |
|---|---|---|
| `pd.read_csv()` | Reads a CSV file. | `pd.read_csv("data.csv")` |
| `pd.read_json()` | Reads JSON data. | `pd.read_json("data.json")` |
| `pd.read_excel()` | Reads an Excel file. | `pd.read_excel("data.xlsx")` |
| `to_csv()` | Saves a DataFrame to CSV. | `df.to_csv("output.csv", index=False)` |
| `to_json()` | Saves a DataFrame to JSON. | `df.to_json("output.json", orient="records")` |
| `to_excel()` | Saves a DataFrame to Excel. | `df.to_excel("output.xlsx", index=False)` |

## 6. Selecting and Filtering Data

| Method / Concept | Description | Code Example |
|---|---|---|
| Column Selection | Selects one column as a Series. | `df["Name"]` |
| Multiple Columns | Selects columns as a DataFrame. | `df[["Name", "Age"]]` |
| `loc[]` | Selects using row and column labels. | `df.loc[0, "Name"]` |
| `iloc[]` | Selects using integer positions. | `df.iloc[0, 1]` |
| Boolean Filtering | Selects rows matching a condition. | `df[df["Age"] > 25]` |
| AND Filtering | Requires both conditions. | `df[(df["Age"] > 25) & (df["Salary"] > 50000)]` |
| OR Filtering | Requires at least one condition. | `df[(df["Age"] > 25) \| (df["Salary"] > 50000)]` |
| `isin()` | Checks membership in specified values. | `df[df["City"].isin(["Paris", "Berlin"])]` |
| `between()` | Filters values within an inclusive range. | `df[df["Age"].between(20, 30)]` |
| `str.contains()` | Matches text patterns. | `df[df["Name"].str.contains("a", na=False)]` |

## 7. Data Cleaning

| Method | Description | Code Example |
|---|---|---|
| `isna()` | Identifies missing values. | `df.isna()` |
| `isna().sum()` | Counts missing values by column. | `df.isna().sum()` |
| `dropna()` | Removes rows with missing values by default. | `df.dropna()` |
| `fillna()` | Replaces missing values. | `df.fillna(0)` |
| `duplicated()` | Identifies duplicate rows. | `df.duplicated()` |
| `drop_duplicates()` | Removes duplicate rows. | `df.drop_duplicates()` |
| `astype()` | Converts data types. | `df["Age"].astype(int)` |
| `pd.to_datetime()` | Converts data to datetime values. | `pd.to_datetime(df["Date"])` |
| `str.strip()` | Removes leading and trailing spaces. | `df["Name"].str.strip()` |
| `str.lower()` | Converts text to lowercase. | `df["City"].str.lower()` |
| `replace()` | Replaces matching values. | `df["City"].replace("NY", "New York")` |
| `rename()` | Renames columns. | `df.rename(columns={"Name": "Employee"})` |
| `reset_index()` | Resets the index. | `df.reset_index(drop=True)` |

## 8. GroupBy and Aggregation

| Method | Description | Code Example |
|---|---|---|
| `groupby()` | Groups rows based on column values. | `df.groupby("Department")` |
| `sum()` | Calculates totals per group. | `df.groupby("Department")["Salary"].sum()` |
| `mean()` | Calculates averages per group. | `df.groupby("Department")["Salary"].mean()` |
| `count()` | Counts non-missing values. | `df.groupby("Department")["Salary"].count()` |
| `size()` | Counts all rows in each group. | `df.groupby("Department").size()` |
| `min()` | Finds the minimum per group. | `df.groupby("Department")["Salary"].min()` |
| `max()` | Finds the maximum per group. | `df.groupby("Department")["Salary"].max()` |
| `agg()` | Performs multiple aggregations. | `df.groupby("Department")["Salary"].agg(["sum", "mean"])` |
| `sort_values()` | Sorts values or aggregated results. | `df.sort_values("Salary", ascending=False)` |

## 9. Merging and Joining

| Method / Concept | Description | Code Example |
|---|---|---|
| `pd.merge()` | Combines DataFrames using matching keys. | `pd.merge(df1, df2, on="ID")` |
| Inner Join | Keeps matching keys from both sides. | `pd.merge(df1, df2, on="ID", how="inner")` |
| Left Join | Keeps all rows from the left side. | `pd.merge(df1, df2, on="ID", how="left")` |
| Right Join | Keeps all rows from the right side. | `pd.merge(df1, df2, on="ID", how="right")` |
| Outer Join | Keeps all keys from both sides. | `pd.merge(df1, df2, on="ID", how="outer")` |
| `concat(axis=0)` | Stacks DataFrames vertically. | `pd.concat([df1, df2], axis=0)` |
| `concat(axis=1)` | Combines DataFrames horizontally by index. | `pd.concat([df1, df2], axis=1)` |
| `suffixes` | Renames overlapping non-key columns during a merge. | `pd.merge(df1, df2, on="ID", suffixes=("_left", "_right"))` |

## NumPy and Pandas Glossary

| Term | Definition |
|---|---|
| NumPy | Python library for numerical computing and multidimensional arrays. |
| ndarray | NumPy's multidimensional array object. |
| Dimension | An axis of an array, such as rows or columns. |
| Shape | The size of each array dimension. |
| Broadcasting | Applying operations to arrays with compatible shapes. |
| Vectorization | Performing array operations without writing explicit Python loops. |
| Pandas | Python library for tabular data manipulation and analysis. |
| Series | One-dimensional labeled data structure. |
| DataFrame | Two-dimensional labeled table containing rows and columns. |
| Index | Labels used to identify rows. |
| Filtering | Selecting rows that satisfy conditions. |
| Missing Value | A value absent from a dataset. |
| NaN | A special floating-point value representing Not a Number, commonly used for missing numeric data. |
| Aggregation | Summarizing data using totals, averages, counts, or other calculations. |
| GroupBy | Dividing data into groups to perform calculations. |
| Merge | Combining related DataFrames using matching keys. |
| Join | Combining data from related tables based on keys or indexes. |
| Concatenation | Combining objects by stacking rows or columns. |