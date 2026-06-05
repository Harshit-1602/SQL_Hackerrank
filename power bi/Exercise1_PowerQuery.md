# Pillar 1: Power Query Exercise (Movies Data)

In this exercise, we will clean and prepare `movies.csv` for analysis. Movie datasets are excellent for learning because they require diverse transformations.

## Step 1: Get Data
1. Open **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV**.
3. Select: `C:\Users\harsh\OneDrive\Desktop\backup_CD\movies.csv`
4. Click **Transform Data**.

## Step 2: Transformation Challenges
Once in the **Power Query Editor**, try to perform these specific tasks:

1.  **Extract Year:** If there is a `Release Date` column, select it, go to the **Add Column** ribbon -> **Date** -> **Year** -> **Year**. This creates a clean "Year" column without changing the original date.
2.  **Clean Genre Strings:** If genres are listed like "Action|Adventure|Sci-Fi", try right-clicking the column -> **Split Column** -> **By Delimiter** -> Use the `|` character.
3.  **Handle Missing Ratings:** If some movies have no rating (null), use **Replace Values** to change `null` to `0` or "Unrated".
4.  **Currency Conversion:** If Budget/Revenue are in a text format (e.g., "$10M"), you can use **Replace Values** to remove the "$" and then change the Data Type to **Fixed Decimal Number**.

## Step 3: The "Applied Steps" Power
Check the **Applied Steps** pane on the right. 
- You've just built a **data pipeline**. 
- If you update the `movies.csv` file later with new movies, you just click "Refresh" in Power BI, and all these cleaning steps will run automatically on the new data!

## Goal
Clean the data until it looks like a perfect table, then click **Close & Apply**.
