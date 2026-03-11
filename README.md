# DSA 50-Day TCS Preparation Tracker

A comprehensive tracking system to help you prepare for TCS interviews with 50 days of curated DSA problems from GeeksforGeeks and LeetCode.

## 🚀 Features

- **📅 50-Day Study Plan**: Organized by topics (Number System, Array & String, Sorting, Searching)
- **✅ Progress Tracking**: Mark problems as completed with local storage persistence
- **🔥 Streak System**: Track your consecutive study days
- **🏆 Achievements**: Unlock badges for completing milestones
- **📊 Dashboard**: Visual progress charts and statistics
- **🎨 Beautiful UI**: Modern dark theme with gradient accents

## 🛠️ Tech Stack

- **Backend**: Python (Streamlit)
- **Frontend**: React.js (via CDN)
- **Styling**: Custom CSS with Beautiful UI
- **Data Storage**: Local JSON/LocalStorage

## 📋 Problem Categories (Organized by Approach)

### 1. Number System (Days 1-8)
- Fibonacci, Armstrong Numbers, Palindrome, Divisibility, Math Operations

### 2. Array and String (Days 9-28)
- Basic Array Operations, Finding Elements, Sorting, Transformation, Sliding Window, 2D Arrays, String Operations

### 3. Sorting (Days 29-35)
- Selection Sort, Bubble Sort, Insertion Sort, Merge Sort, Quick Sort

### 4. Searching (Days 36-45)
- Linear Search, Binary Search, Advanced Binary Search, Rotated Array

### 5. Revision & Mock Tests (Days 46-50)
- Full Revision and Practice Tests

## 🚦 How to Run

### Option 1: Streamlit Cloud (Recommended - No Setup!)
Deploy to Streamlit Cloud with one click:
1. Go to https://share.streamlit.io
2. Connect your GitHub account
3. Select repository: `SAMPRIT-NANDI/DSA-TRACKER-APP`
4. Main file: `app.py`
5. Click **Deploy!**

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/SAMPRIT-NANDI/DSA-TRACKER-APP.git
cd DSA-TRACKER-APP

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Option 3: React/HTML Version
Open `index.html` in your browser.

## 📱 Features Overview

### Dashboard
- Overall progress percentage
- Problems completed count
- Current streak
- Category-wise progress
- Achievement gallery

### Daily Plan
- Day selector slider
- Problems for each day
- Topic tags
- Click to mark complete
- Direct links to problems

### Progress
- Visual progress bar
- 50-day calendar view
- List of completed problems

### Achievements
- 🎯 First Blood - Complete first problem
- 🔥 On Fire - 7-day streak
- 💪 Dedicated - 30-day streak
- 🏆 Perfectionist - Complete all 50 days
- 🔢 Number Master - All Number System problems
- ⚔️ Array Warrior - All Array problems
- 📊 Sorting Expert - All Sorting problems
- 🔍 Search Master - All Searching problems
- 🌅 Early Bird - 5 problems before day 10
- 📈 Consistent - 14 consecutive days

## 💡 TCS Preparation Tips

1. **Focus on Number System & Array** - Frequently asked in TCS
2. **Practice Sorting & Searching** - Binary search and sorting algorithms are important
3. **String handling** - TCS often asks string manipulation questions
4. **Time Complexity** - Be prepared for time/space complexity questions
5. **Daily Practice** - Maintain your streak for better retention

## 📝 Data Storage

- **React Version**: Uses browser LocalStorage
- **Streamlit Version**: Uses local `dsa_tracker_data.json` file

Your progress is automatically saved!

## 🎨 Design

- Dark theme with gradient accents
- Responsive design
- Smooth animations
- Custom scrollbar
- Achievement badges with animations

---

Good luck with your TCS preparation! 🎯

