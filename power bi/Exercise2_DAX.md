# Pillar 2: DAX & Modeling (Movies Data)

Now that your data is clean, it's time to add "Intelligence" to your report using **DAX (Data Analysis Expressions)**.

## What is DAX?
DAX is the formula language of Power BI (similar to Excel formulas, but more powerful). We use it to create **Measures**.

## Exercise: Creating Your First Measures

### 1. Total Number of Movies
We want a count of how many movies are in our list.
1. In the **Data** pane (on the far right), right-click your `movies` table.
2. Select **New measure**.
3. In the formula bar at the top, type exactly this:
   `Total Movies = COUNT(movies[title])` 
   *(Note: replace [title] with whatever your movie title column is named)*
4. Press Enter.

### 2. Average Rating
If your data has a rating/score column:
1. Right-click the table again -> **New measure**.
2. Type:
   `Average Rating = AVERAGE(movies[vote_average])`
   *(Note: replace [vote_average] with your rating column name)*
3. Press Enter.

### 3. Total Profit (The Power of "Calculated Measures")
If you have Budget and Revenue columns:
1. Create a measure for **Total Revenue**:
   `Total Revenue = SUM(movies[revenue])`
2. Create a measure for **Total Budget**:
   `Total Budget = SUM(movies[budget])`
3. Now, create a measure for **Profit** using the first two:
   `Total Profit = [Total Revenue] - [Total Budget]`

## Why Measures?
Unlike a normal column, a **Measure** calculates "on the fly" based on the filters you select in your report. If you filter for the year "2020", your `Average Rating` measure will automatically update to show the average only for 2020!

## Next Step
Once you have created at least two measures, look at the **Report View** (the blank canvas icon on the left). Drag a **Card** visual onto the canvas and drag your `Total Movies` measure into it!
