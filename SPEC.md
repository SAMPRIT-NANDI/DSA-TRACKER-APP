# DSA 50-Day TCS Preparation Tracker - Specification

## Project Overview
- **Project Name**: DSA 50-Day TCS Tracker
- **Type**: Web Application (Streamlit + React + JavaScript)
- **Core Functionality**: A comprehensive 50-day DSA tracking system with progress monitoring, achievements, and performance analytics for TCS placement preparation
- **Target Users**: Students/Job seekers preparing for TCS interviews

## Technology Stack
- **Backend**: Python (Streamlit)
- **Frontend**: React.js + JavaScript
- **Styling**: Custom CSS + Beautiful UI components
- **Data Storage**: Local JSON file for progress persistence

## Problem Categories (Organized by Approach)
Based on the provided links, problems are grouped by similar approach:

### 1. Number System (Day 1-8)
- Basic Operations: Fibonacci, Sum of array, Armstrong, Palindrome
- Divisibility: Large number divisible by 9, Leap year
- Math Operations: Even/Oodd, Circle intersection, Perfect number
- Advanced: Max product of three, Power of two, Climbing stairs, Factors, Hex conversion, Happy number

### 2. Array and String (Day 9-28)
- Basic Array: Sum, Remove duplicates, Subarray sum, Paths
- Finding Elements: Second largest, Majority element
- Sorting: Sort 0s 1s 2s, Good pairs
- Transformation: Rotate array, Single number
- Sliding Window: Max subarray, Sliding window maximum
- Searching: Mean/Median, Next greater element, Union of arrays
- 2D Arrays: Pascal triangle, Set matrix zeros, Rotate image, Spiral matrix
- String: Stock buy/sell, Two sum, String operations, Common characters
- Advanced String: Reverse, Palindrome, Anagram, Roman to integer, etc.

### 3. Sorting (Day 29-35)
- Selection Sort, Bubble Sort, Insertion Sort, Merge Sort, Quick Sort

### 4. Searching (Day 36-45)
- Linear Search, Binary Search
- Advanced: Floor, Ceil, Insert position, Koko eating bananas
- Rotated Array: Search in rotated, Find min in rotated, Peak element

### 5. Revision & Mock Tests (Day 46-50)
- Full revision and practice tests

## UI/UX Specification

### Color Palette
- Primary: #0D47A1 (Deep Blue)
- Secondary: #1565C0 (Blue)
- Accent: #00E676 (Green - for success/achievements)
- Warning: #FF9800 (Orange)
- Background: #0A0E17 (Dark Navy)
- Card Background: #1A1F2E (Dark Slate)
- Text Primary: #FFFFFF
- Text Secondary: #B0BEC5

### Typography
- Headings: Poppins Bold
- Body: Inter Regular
- Code/Problems: Fira Code

### Layout Structure
1. **Sidebar Navigation**
   - Home/Dashboard
   - Daily Plan
   - Progress Tracker
   - Achievements
   - Performance Analytics

2. **Main Content Area**
   - Day-wise content cards
   - Problem links with checkboxes
   - Progress indicators
   - Achievement badges

3. **Dashboard**
   - Overall progress percentage
   - Problems completed count
   - Current streak
   - Achievement gallery
   - Performance charts

### Components
- Day Card: Shows day number, topics, problem links
- Problem Item: Checkbox, title, difficulty tag, link
- Progress Bar: Animated, shows completion %
- Achievement Badge: Icon, name, unlock date
- Stats Card: Icon, value, label

## Functionality Specification

### Core Features
1. **50-Day Study Plan**
   - Daily breakdown of topics
   - Curated problem links
   - Topic-wise grouping

2. **Progress Tracking**
   - Mark problems as completed
   - Track completion percentage
   - Save progress locally

3. **Achievement System**
   - "First Blood" - Complete first problem
   - "On Fire" - 7-day streak
   - "Dedicated" - 30-day streak
   - "Perfectionist" - Complete all problems
   - Topic-specific achievements
   - Milestone badges

4. **Performance Dashboard**
   - Total problems completed
   - Category-wise progress
   - Daily/weekly progress chart
   - Streak counter
   - Time spent tracking

5. **Consecutive Achievement**
   - Daily login/study tracking
   - Streak counter with rewards
   - Calendar view of activity

### User Interactions
- Click problem link to open in new tab
- Checkbox to mark complete
- Filter by category
- Search problems
- View achievement details
- Export progress report

## Acceptance Criteria
1. ✅ All 50 days displayed with correct topic distribution
2. ✅ All problem links from GeeksforGeeks and LeetCode included
3. ✅ Problems grouped by similar approach
4. ✅ Progress persists between sessions
5. ✅ Achievements unlock correctly
6. ✅ Dashboard shows accurate statistics
7. ✅ Beautiful dark theme UI
8. ✅ Responsive design
9. ✅ All external links work correctly
10. ✅ Streak tracking functions properly

