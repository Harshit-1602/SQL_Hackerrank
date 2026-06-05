# Pillar 1 Deep Dive: The Power Query Masterclass

Power Query is where **80% of the work** happens. If your data isn't clean here, your charts will be wrong later.

## 1. How to get back into Power Query
Since you already loaded the data:
1. Look at the top ribbon in Power BI.
2. Click the **Transform Data** button (it has a small table and pencil icon).
3. This opens a **new window** called the Power Query Editor.

## 2. The "Power Moves" to Practice

### Move A: Fix Data Types (The #1 Error)
Look at the top left of every column header.
- `ABC` = Text
- `123` = Whole Number
- `1.2` = Decimal Number
- `📅` = Date
**Task:** Ensure your `Budget` and `Revenue` are **Decimal Numbers** and your `Release Date` is a **Date**. If they show `ABC`, click the icon and change them.

### Move B: Remove Unnecessary Columns
You don't need every column for a good dashboard.
- Select a column you don't need (e.g., `homepage` or `tagline`).
- Right-click -> **Remove**. 
- *Why?* This makes your Power BI file smaller and faster.

### Move C: Filter Out Garbage
- Click the drop-down arrow on the `title` column.
- Uncheck `(null)` or `(blank)` if they exist.
- This ensures your "Total Movies" count doesn't include empty rows.

### Move D: The "Add Column from Examples" (Magic)
This is the fastest way to transform data without formulas.
1. Go to the **Add Column** ribbon at the top.
2. Click **Column from Examples** -> **From Selection**.
3. If you have a date like `2015-12-18`, just type `December` in the new column.
4. Power Query will "guess" you want the Month Name and fill the rest for you!

## 3. The "Safety Net": Applied Steps
On the right, you see **Applied Steps**.
- Every move you just made is a step.
- **Do not be afraid to experiment.** If you mess up, just click the `X` next to the step to delete it.

## Your Goal
Perform at least 3 transformations (Rename a column, Change a data type, and Remove a column). Then click **Close & Apply** in the top left.
