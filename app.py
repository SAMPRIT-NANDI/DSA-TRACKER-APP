"""
DSA 50-Day TCS Preparation Tracker
A comprehensive tracking system with Streamlit, React components, and beautiful CSS
"""

import streamlit as st
import json
import os
from datetime import datetime, timedelta
import base64

# Page Configuration
st.set_page_config(
    page_title="DSA 50-Day TCS Tracker",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Beautiful UI
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500&display=swap');
    
    /* Main Theme */
    :root {
        --primary: #0D47A1;
        --secondary: #1565C0;
        --accent: #00E676;
        --warning: #FF9800;
        --bg-dark: #0A0E17;
        --card-bg: #1A1F2E;
        --text-primary: #FFFFFF;
        --text-secondary: #B0BEC5;
    }
    
    /* Global Styles */
    .stApp {
        background: var(--bg-dark);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #0D47A1 0%, #1A1F2E 100%);
    }
    
    /* Headings */
    h1, h2, h3, h4 {
        font-family: 'Poppins', sans-serif !important;
        color: var(--text-primary) !important;
    }
    
    h1 {
        background: linear-gradient(90deg, #00E676, #00B0FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700 !important;
    }
    
    /* Cards */
    .day-card {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(0, 230, 118, 0.1);
        transition: all 0.3s ease;
    }
    
    .day-card:hover {
        border-color: rgba(0, 230, 118, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 230, 118, 0.1);
    }
    
    /* Problem Links */
    .problem-link {
        display: flex;
        align-items: center;
        padding: 12px 16px;
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        margin: 8px 0;
        text-decoration: none;
        color: var(--text-secondary);
        transition: all 0.3s ease;
        font-family: 'Fira Code', monospace;
        font-size: 14px;
    }
    
    .problem-link:hover {
        background: rgba(0, 230, 118, 0.1);
        color: var(--accent);
        padding-left: 20px;
    }
    
    .problem-link.completed {
        background: rgba(0, 230, 118, 0.15);
        color: var(--accent);
        border-left: 3px solid var(--accent);
    }
    
    /* Progress Bar */
    .progress-container {
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        height: 30px;
        overflow: hidden;
        position: relative;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #00E676, #00B0FF);
        height: 100%;
        border-radius: 20px;
        transition: width 0.5s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        color: #000;
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #1A1F2E 0%, #2D3548 100%);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .stat-value {
        font-size: 36px;
        font-weight: 700;
        color: var(--accent);
        font-family: 'Poppins', sans-serif;
    }
    
    .stat-label {
        font-size: 14px;
        color: var(--text-secondary);
        margin-top: 5px;
    }
    
    /* Achievements */
    .achievement-badge {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        color: #000;
        font-weight: 600;
    }
    
    .achievement-badge.locked {
        background: #2D3548;
        color: #666;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.05);
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
        color: var(--text-secondary);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #00E676, #00B0FF);
        color: #000 !important;
        font-weight: 600;
    }
    
    /* Checkbox */
    .stCheckbox > label > div:first-child {
        border-color: var(--accent) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #00E676, #00B0FF);
        border: none;
        border-radius: 10px;
        color: #000;
        font-weight: 600;
        padding: 10px 24px;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(0, 230, 118, 0.3);
    }
    
    /* Sidebar Navigation */
    .nav-item {
        padding: 12px 16px;
        border-radius: 10px;
        margin: 5px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        color: var(--text-secondary);
    }
    
    .nav-item:hover, .nav-item.active {
        background: rgba(0, 230, 118, 0.1);
        color: var(--accent);
    }
    
    /* Category Headers */
    .category-header {
        background: linear-gradient(90deg, #0D47A1, #1565C0);
        padding: 15px 20px;
        border-radius: 12px;
        margin: 20px 0 10px 0;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Day Badge */
    .day-badge {
        background: linear-gradient(135deg, #00E676, #00B0FF);
        color: #000;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 12px;
    }
    
    /* Topic Tag */
    .topic-tag {
        background: rgba(255, 152, 0, 0.2);
        color: #FF9800;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 12px;
    }
    
    /* Calendar */
    .calendar-day {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        margin: 2px;
    }
    
    .calendar-day.completed {
        background: var(--accent);
        color: #000;
    }
    
    .calendar-day.missed {
        background: #FF5252;
        color: #fff;
    }
    
    .calendar-day.today {
        border: 2px solid var(--accent);
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1A1F2E;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00E676, #00B0FF);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Data Storage File
DATA_FILE = "dsa_tracker_data.json"

# Initialize Data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "completed_problems": [],
        "streak": 0,
        "last_active": None,
        "achievements": [],
        "total_time_spent": 0,
        "daily_completion": {}
    }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# DSA Problems Database - Organized by Approach
DSA_PROBLEMS = {
    "Number System": {
        "days": [1, 2, 3, 4, 5, 6, 7, 8],
        "topics": ["Fibonacci", "Sum", "Armstrong", "Palindrome", "Divisibility", "Leap Year", "Math Operations", "Advanced Math"],
        "problems": [
            {"day": 1, "title": "Sum of Fibonacci Numbers", "link": "https://www.geeksforgeeks.org/sum-fibonacci-numbers/", "topic": "Fibonacci"},
            {"day": 1, "title": "Sum of Array Elements", "link": "https://www.geeksforgeeks.org/program-find-sum-elements-given-array/", "topic": "Sum"},
            {"day": 2, "title": "Armstrong Numbers", "link": "https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1", "topic": "Armstrong"},
            {"day": 2, "title": "Palindrome Number", "link": "https://www.geeksforgeeks.org/problems/palindrome0746/1", "topic": "Palindrome"},
            {"day": 3, "title": "Check Large Number Divisible by 9", "link": "https://www.geeksforgeeks.org/check-large-number-divisible-9-not/", "topic": "Divisibility"},
            {"day": 3, "title": "Leap Year", "link": "https://www.geeksforgeeks.org/problems/leap-year0943/1", "topic": "Leap Year"},
            {"day": 4, "title": "Floating Point - Even or Odd", "link": "https://www.geeksforgeeks.org/problems/floating-point-number-even-or-odd0146/1", "topic": "Math Operations"},
            {"day": 4, "title": "Area of Intersection of Two Circles", "link": "https://www.geeksforgeeks.org/problems/area-of-intersection-of-two-circles0653/1", "topic": "Math Operations"},
            {"day": 5, "title": "Odd or Even", "link": "https://www.geeksforgeeks.org/problems/odd-or-even3618/1", "topic": "Math Operations"},
            {"day": 5, "title": "Perfect Number", "link": "https://www.geeksforgeeks.org/perfect-number/", "topic": "Math Operations"},
            {"day": 6, "title": "Maximum Product of Three Numbers", "link": "https://leetcode.com/problems/maximum-product-of-three-numbers/description/", "topic": "Advanced Math"},
            {"day": 6, "title": "Power of Two", "link": "https://leetcode.com/problems/power-of-two/description/", "topic": "Advanced Math"},
            {"day": 7, "title": "Pow(x, n)", "link": "https://leetcode.com/problems/powx-n/description/", "topic": "Advanced Math"},
            {"day": 7, "title": "Swap Two Numbers", "link": "https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1", "topic": "Basic Operations"},
            {"day": 8, "title": "Climbing Stairs", "link": "https://leetcode.com/problems/climbing-stairs/description/", "topic": "Dynamic Programming"},
            {"day": 8, "title": "Find All Factors of a Number", "link": "https://www.geeksforgeeks.org/find-all-factors-of-a-natural-number-in-sorted-order/", "topic": "Advanced Math"},
            {"day": 8, "title": "Convert Number to Hexadecimal", "link": "https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/", "topic": "Advanced Math"},
            {"day": 8, "title": "Happy Number", "link": "https://leetcode.com/problems/happy-number/description/", "topic": "Advanced Math"},
        ]
    },
    "Array and String": {
        "days": list(range(9, 29)),
        "topics": ["Basic Array", "Finding Elements", "Sorting", "Transformation", "Sliding Window", "2D Arrays", "String Operations"],
        "problems": [
            {"day": 9, "title": "Sum of Array Elements", "link": "https://www.geeksforgeeks.org/program-find-sum-elements-given-array/", "topic": "Basic Array"},
            {"day": 9, "title": "Remove Duplicates from Sorted Array", "link": "https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/", "topic": "Basic Array"},
            {"day": 10, "title": "Subarray Sum Equals K", "link": "https://leetcode.com/problems/subarray-sum-equals-k/description/", "topic": "Sliding Window"},
            {"day": 10, "title": "Count All Paths - Top Left to Bottom Right", "link": "https://www.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right3011/1", "topic": "Basic Array"},
            {"day": 11, "title": "Find Second Largest Element", "link": "https://www.geeksforgeeks.org/find-second-largest-element-array/", "topic": "Finding Elements"},
            {"day": 11, "title": "Majority Element", "link": "https://www.geeksforgeeks.org/problems/majority-element-1587115620/1", "topic": "Finding Elements"},
            {"day": 12, "title": "Sort an Array of 0s, 1s and 2s", "link": "https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1", "topic": "Sorting"},
            {"day": 12, "title": "Number of Good Pairs", "link": "https://leetcode.com/problems/number-of-good-pairs/description/", "topic": "Sorting"},
            {"day": 13, "title": "Rotate Array", "link": "https://leetcode.com/problems/rotate-array/description/", "topic": "Transformation"},
            {"day": 13, "title": "Single Number", "link": "https://leetcode.com/problems/single-number/description/", "topic": "Transformation"},
            {"day": 14, "title": "Sliding Window Maximum", "link": "https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/", "topic": "Sliding Window"},
            {"day": 14, "title": "Sliding Window Maximum (LeetCode)", "link": "https://leetcode.com/problems/sliding-window-maximum/description/", "topic": "Sliding Window"},
            {"day": 15, "title": "Mean and Median of Array", "link": "https://www.geeksforgeeks.org/program-for-mean-and-median-of-an-unsorted-array/", "topic": "Finding Elements"},
            {"day": 15, "title": "Next Greater Element I", "link": "https://leetcode.com/problems/next-greater-element-i/description/", "topic": "Finding Elements"},
            {"day": 16, "title": "Union of Two Sorted Arrays", "link": "https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1", "topic": "Finding Elements"},
            {"day": 16, "title": "Pascal's Triangle", "link": "https://leetcode.com/problems/pascals-triangle/description/", "topic": "2D Arrays"},
            {"day": 17, "title": "Set Matrix Zeroes", "link": "https://leetcode.com/problems/set-matrix-zeroes/description/", "topic": "2D Arrays"},
            {"day": 17, "title": "Rotate Image", "link": "https://leetcode.com/problems/rotate-image/description/", "topic": "2D Arrays"},
            {"day": 18, "title": "Spiral Matrix", "link": "https://leetcode.com/problems/spiral-matrix/description/", "topic": "2D Arrays"},
            {"day": 18, "title": "Best Time to Buy and Sell Stock", "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/", "topic": "Array"},
            {"day": 19, "title": "Two Sum", "link": "https://leetcode.com/problems/two-sum/description/", "topic": "Finding Elements"},
            {"day": 19, "title": "Find and Replace in String", "link": "https://www.geeksforgeeks.org/problems/find-an-replace-in-string/1", "topic": "String Operations"},
            {"day": 20, "title": "Remove Characters from First String", "link": "https://www.geeksforgeeks.org/remove-characters-from-the-first-string-which-are-present-in-the-second-string/", "topic": "String Operations"},
            {"day": 20, "title": "Find Common Characters", "link": "https://leetcode.com/problems/find-common-characters/description/", "topic": "String Operations"},
            {"day": 21, "title": "Reverse a String", "link": "https://www.geeksforgeeks.org/reverse-a-string-in-java/", "topic": "String Operations"},
            {"day": 21, "title": "Reverse Words in a String", "link": "https://leetcode.com/problems/reverse-words-in-a-string/", "topic": "String Operations"},
            {"day": 22, "title": "Print Characters in Order of Occurrence", "link": "https://www.geeksforgeeks.org/print-characters-frequencies-order-occurrence/", "topic": "String Operations"},
            {"day": 22, "title": "Largest Odd Number in String", "link": "https://leetcode.com/problems/largest-odd-number-in-string/", "topic": "String Operations"},
            {"day": 23, "title": "Longest Common Prefix", "link": "https://leetcode.com/problems/longest-common-prefix/", "topic": "String Operations"},
            {"day": 23, "title": "Count Binary Substrings", "link": "https://leetcode.com/problems/count-binary-substrings/description/", "topic": "String Operations"},
            {"day": 24, "title": "Rotate String", "link": "https://leetcode.com/problems/rotate-string/description/", "topic": "String Operations"},
            {"day": 24, "title": "Valid Anagram", "link": "https://leetcode.com/problems/valid-anagram/description/", "topic": "String Operations"},
            {"day": 25, "title": "Excel Sheet Column Number", "link": "https://leetcode.com/problems/excel-sheet-column-number/description/", "topic": "String Operations"},
            {"day": 25, "title": "Count Unique Characters of All Substrings", "link": "https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/", "topic": "String Operations"},
            {"day": 26, "title": "Check Palindrome String", "link": "https://www.geeksforgeeks.org/c-program-check-given-string-palindrome/", "topic": "String Operations"},
            {"day": 26, "title": "Implement strStr()", "link": "https://www.geeksforgeeks.org/problems/implement-strstr/1", "topic": "String Operations"},
            {"day": 27, "title": "Sort Characters By Frequency", "link": "https://leetcode.com/problems/sort-characters-by-frequency/description/", "topic": "String Operations"},
            {"day": 27, "title": "Roman to Integer", "link": "https://leetcode.com/problems/roman-to-integer/description/", "topic": "String Operations"},
            {"day": 28, "title": "Count Number of Substrings", "link": "https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1", "topic": "String Operations"},
        ]
    },
    "Sorting": {
        "days": list(range(29, 36)),
        "topics": ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"],
        "problems": [
            {"day": 29, "title": "Selection Sort", "link": "https://www.geeksforgeeks.org/problems/selection-sort/1", "topic": "Selection Sort"},
            {"day": 30, "title": "Bubble Sort", "link": "https://www.geeksforgeeks.org/problems/bubble-sort/1", "topic": "Bubble Sort"},
            {"day": 31, "title": "Insertion Sort", "link": "https://www.geeksforgeeks.org/problems/insertion-sort/1", "topic": "Insertion Sort"},
            {"day": 32, "title": "Merge Sort", "link": "https://www.geeksforgeeks.org/problems/merge-sort/1", "topic": "Merge Sort"},
            {"day": 33, "title": "Quick Sort", "link": "https://www.geeksforgeeks.org/problems/quick-sort/1", "topic": "Quick Sort"},
        ]
    },
    "Searching": {
        "days": list(range(36, 46)),
        "topics": ["Linear Search", "Binary Search", "Advanced Binary Search", "Rotated Array"],
        "problems": [
            {"day": 36, "title": "Linear Search", "link": "https://www.geeksforgeeks.org/linear-search/", "topic": "Linear Search"},
            {"day": 36, "title": "Binary Search", "link": "https://leetcode.com/problems/binary-search/description/", "topic": "Binary Search"},
            {"day": 37, "title": "Floor in a Sorted Array", "link": "https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1", "topic": "Binary Search"},
            {"day": 37, "title": "Ceil the Floor", "link": "https://www.geeksforgeeks.org/problems/ceil-the-floor2802/0", "topic": "Binary Search"},
            {"day": 38, "title": "Search Insert Position", "link": "https://leetcode.com/problems/search-insert-position/description/", "topic": "Binary Search"},
            {"day": 38, "title": "Koko Eating Bananas", "link": "https://leetcode.com/problems/koko-eating-bananas/description/", "topic": "Advanced Binary Search"},
            {"day": 39, "title": "Search in Rotated Sorted Array", "link": "https://leetcode.com/problems/search-in-rotated-sorted-array/description/", "topic": "Rotated Array"},
            {"day": 39, "title": "Search in Rotated Sorted Array II", "link": "https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/", "topic": "Rotated Array"},
            {"day": 40, "title": "Find Minimum in Rotated Sorted Array", "link": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/", "topic": "Rotated Array"},
            {"day": 40, "title": "Find Peak Element", "link": "https://leetcode.com/problems/find-peak-element/description/", "topic": "Advanced Binary Search"},
        ]
    },
    "Revision & Mock Tests": {
        "days": list(range(46, 51)),
        "topics": ["Full Revision", "Practice Tests", "Mock Interviews"],
        "problems": [
            {"day": 46, "title": "Full Revision - Number System", "link": "#", "topic": "Full Revision"},
            {"day": 47, "title": "Full Revision - Array & String", "link": "#", "topic": "Full Revision"},
            {"day": 48, "title": "Full Revision - Sorting & Searching", "link": "#", "topic": "Full Revision"},
            {"day": 49, "title": "Mock Test 1", "link": "#", "topic": "Practice Tests"},
            {"day": 50, "title": "Mock Test 2", "link": "#", "topic": "Practice Tests"},
        ]
    }
}

# Achievements Database
ACHIEVEMENTS = {
    "first_blood": {
        "name": "🎯 First Blood",
        "description": "Complete your first problem",
        "icon": "🎯",
        "condition": lambda data: len(data.get("completed_problems", [])) >= 1
    },
    "on_fire": {
        "name": "🔥 On Fire",
        "description": "7-day streak",
        "icon": "🔥",
        "condition": lambda data: data.get("streak", 0) >= 7
    },
    "dedicated": {
        "name": "💪 Dedicated",
        "description": "30-day streak",
        "icon": "💪",
        "condition": lambda data: data.get("streak", 0) >= 30
    },
    "perfectionist": {
        "name": "🏆 Perfectionist",
        "description": "Complete all 50 days",
        "icon": "🏆",
        "condition": lambda data: len(data.get("completed_problems", [])) >= 50
    },
    "number_master": {
        "name": "🔢 Number Master",
        "description": "Complete all Number System problems",
        "icon": "🔢",
        "condition": lambda data: len([p for p in data.get("completed_problems", []) if "Number System" in p]) >= 18
    },
    "array_warrior": {
        "name": "⚔️ Array Warrior",
        "description": "Complete all Array problems",
        "icon": "⚔️",
        "condition": lambda data: len([p for p in data.get("completed_problems", []) if "Array" in p]) >= 30
    },
    "sorting_expert": {
        "name": "📊 Sorting Expert",
        "description": "Complete all Sorting problems",
        "icon": "📊",
        "condition": lambda data: len([p for p in data.get("completed_problems", []) if "Sorting" in p]) >= 5
    },
    "search_master": {
        "name": "🔍 Search Master",
        "description": "Complete all Searching problems",
        "icon": "🔍",
        "condition": lambda data: len([p for p in data.get("completed_problems", []) if "Searching" in p]) >= 10
    },
    "early_bird": {
        "name": "🌅 Early Bird",
        "description": "Complete 5 problems before day 10",
        "icon": "🌅",
        "condition": lambda data: len([p for p in data.get("completed_problems", []) if p.startswith("Day 0") or p.startswith("Day 1") or p.startswith("Day 2") or p.startswith("Day 3") or p.startswith("Day 4") or p.startswith("Day 5") or p.startswith("Day 6") or p.startswith("Day 7") or p.startswith("Day 8") or p.startswith("Day 9")]) >= 5
    },
    "consistent": {
        "name": "📈 Consistent",
        "description": "Study for 14 consecutive days",
        "icon": "📈",
        "condition": lambda data: data.get("streak", 0) >= 14
    }
}

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = load_data()

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard"

# Update streak function
def update_streak():
    data = st.session_state.data
    today = datetime.now().date()
    
    if data["last_active"]:
        last_active = datetime.strptime(data["last_active"], "%Y-%m-%d").date()
        if last_active == today:
            return  # Already active today
        elif last_active == today - timedelta(days=1):
            data["streak"] += 1
        else:
            data["streak"] = 1
    else:
        data["streak"] = 1
    
    data["last_active"] = today.strftime("%Y-%m-%d")
    save_data(data)

# Check achievements
def check_achievements():
    data = st.session_state.data
    new_achievements = []
    
    for key, achievement in ACHIEVEMENTS.items():
        if key not in data["achievements"] and achievement["condition"](data):
            data["achievements"].append(key)
            new_achievements.append(achievement)
    
    if new_achievements:
        save_data(data)
    
    return new_achievements

# Calculate progress
def get_progress():
    data = st.session_state.data
    total_problems = sum(len(cat["problems"]) for cat in DSA_PROBLEMS.values())
    completed = len(data["completed_problems"])
    return (completed / total_problems * 100) if total_problems > 0 else 0

# Sidebar Navigation
def create_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h2 style="background: linear-gradient(90deg, #00E676, #00B0FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;">
                🎯 DSA TRACKER
            </h2>
            <p style="color: #B0BEC5; margin-top: 5px;">50 Days TCS Prep</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Streak Display
        data = st.session_state.data
        st.markdown(f"""
        <div class="stat-card" style="margin: 20px 0;">
            <div class="stat-value" style="font-size: 28px;">🔥 {data.get('streak', 0)}</div>
            <div class="stat-label">Day Streak</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Navigation")
        
        pages = [
            ("Dashboard", "📊"),
            ("Daily Plan", "📅"),
            ("Progress", "📈"),
            ("Achievements", "🏆"),
            ("Analytics", "📉")
        ]
        
        for page, icon in pages:
            if st.session_state.current_page == page:
                st.markdown(f"""
                <div class="nav-item active">
                    {icon} {page}
                </div>
                """, unsafe_allow_html=True)
            else:
                if st.button(f"{icon} {page}", key=f"nav_{page}"):
                    st.session_state.current_page = page
                    st.rerun()
        
        st.markdown("---")
        
        # Quick Stats in Sidebar
        progress = get_progress()
        st.markdown(f"""
        <div style="padding: 15px; background: rgba(255,255,255,0.05); border-radius: 10px;">
            <p style="margin: 0; color: #B0BEC5; font-size: 12px;">Overall Progress</p>
            <div style="font-size: 24px; font-weight: 700; color: #00E676;">{progress:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

# Dashboard Page
def show_dashboard():
    data = st.session_state.data
    progress = get_progress()
    
    # Header
    st.markdown("""
    <div style="text-align: center; padding: 30px 0;">
        <h1>🚀 Welcome to Your 50-Day DSA Journey!</h1>
        <p style="color: #B0BEC5; font-size: 18px;">Track your progress to ace TCS interviews</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_problems = sum(len(cat["problems"]) for cat in DSA_PROBLEMS.values())
        completed = len(data["completed_problems"])
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{completed}/{total_problems}</div>
            <div class="stat-label">Problems Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        days_completed = len(set([p.get("day", 0) for p in get_completed_problems_details()]))
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{days_completed}/50</div>
            <div class="stat-label">Days Completed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">🔥 {data.get('streak', 0)}</div>
            <div class="stat-label">Current Streak</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        achievements_count = len(data.get("achievements", []))
        total_achievements = len(ACHIEVEMENTS)
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{achievements_count}/{total_achievements}</div>
            <div class="stat-label">Achievements</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Progress Bar
    st.markdown(f"""
    <div style="margin: 30px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span style="color: #B0BEC5;">Overall Progress</span>
            <span style="color: #00E676; font-weight: 600;">{progress:.1f}%</span>
        </div>
        <div class="progress-container">
            <div class="progress-bar" style="width: {progress}%;">{progress:.1f}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Category Progress
    st.markdown("### 📚 Category Progress")
    
    for category, cat_data in DSA_PROBLEMS.items():
        cat_problems = cat_data["problems"]
        cat_completed = len([p for p in cat_problems if f"{category}::{p['title']}" in data["completed_problems"]])
        cat_total = len(cat_problems)
        cat_progress = (cat_completed / cat_total * 100) if cat_total > 0 else 0
        
        with st.expander(f"📖 {category} ({cat_completed}/{cat_total} completed)"):
            st.progress(cat_progress / 100)
            st.write(f"**Topics:** {', '.join(cat_data['topics'][:3])}...")
    
    # Recent Achievements
    st.markdown("### 🏆 Recent Achievements")
    
    achievement_cols = st.columns(4)
    for i, (key, achievement) in enumerate(ACHIEVEMENTS.items()):
        with achievement_cols[i % 4]:
            if key in data.get("achievements", []):
                st.markdown(f"""
                <div class="achievement-badge">
                    <div style="font-size: 30px;">{achievement['icon']}</div>
                    <div style="font-size: 12px; margin-top: 5px;">{achievement['name']}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="achievement-badge locked">
                    <div style="font-size: 30px;">🔒</div>
                    <div style="font-size: 12px; margin-top: 5px;">Locked</div>
                </div>
                """, unsafe_allow_html=True)

# Helper function to get completed problems details
def get_completed_problems_details():
    data = st.session_state.data
    completed = []
    for category, cat_data in DSA_PROBLEMS.items():
        for problem in cat_data["problems"]:
            if f"{category}::{problem['title']}" in data["completed_problems"]:
                completed.append({**problem, "category": category})
    return completed

# Daily Plan Page
def show_daily_plan():
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1>📅 Daily Study Plan</h1>
        <p style="color: #B0BEC5;">Follow this plan to complete DSA in 50 days</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Day selector
    selected_day = st.slider("Select Day", 1, 50, 1)
    
    # Find which category this day belongs to
    for category, cat_data in DSA_PROBLEMS.items():
        if selected_day in cat_data["days"]:
            st.markdown(f"""
            <div class="category-header">
                📚 {category} - Day {selected_day}
            </div>
            """, unsafe_allow_html=True)
            
            # Get problems for this day
            day_problems = [p for p in cat_data["problems"] if p["day"] == selected_day]
            
            for problem in day_problems:
                problem_key = f"{category}::{problem['title']}"
                is_completed = problem_key in st.session_state.data["completed_problems"]
                
                col1, col2 = st.columns([1, 5])
                
                with col1:
                    new_state = st.checkbox(
                        "✅",
                        value=is_completed,
                        key=f"checkbox_{problem_key}",
                        help="Mark as completed"
                    )
                    if new_state != is_completed:
                        if new_state:
                            st.session_state.data["completed_problems"].append(problem_key)
                            update_streak()
                            new_achievements = check_achievements()
                            if new_achievements:
                                st.success(f"🎉 Unlocked: {new_achievements[0]['name']}!")
                        else:
                            st.session_state.data["completed_problems"].remove(problem_key)
                        save_data(st.session_state.data)
                
                with col2:
                    topic_tag = f"""
                    <span class="topic-tag">{problem['topic']}</span>
                    """
                    st.markdown(topic_tag, unsafe_allow_html=True)
                    
                    link_text = f"✅ {problem['title']}" if is_completed else problem['title']
                    st.markdown(f"""
                    <a href="{problem['link']}" target="_blank" class="problem-link {'completed' if is_completed else ''}">
                        🔗 {link_text}
                    </a>
                    """, unsafe_allow_html=True)
            
            break

# Progress Page
def show_progress():
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1>📈 Your Progress</h1>
        <p style="color: #B0BEC5;">Track your journey day by day</p>
    </div>
    """, unsafe_allow_html=True)
    
    data = st.session_state.data
    progress = get_progress()
    
    # Overall Progress
    st.markdown(f"""
    <div style="margin: 30px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <span style="color: #B0BEC5;">Overall Completion</span>
            <span style="color: #00E676; font-weight: 600;">{progress:.1f}%</span>
        </div>
        <div class="progress-container">
            <div class="progress-bar" style="width: {progress}%;">{progress:.1f}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Calendar View
    st.markdown("### 📅 Activity Calendar")
    
    # Create calendar grid
    calendar_html = '<div style="display: flex; flex-wrap: wrap; gap: 5px; margin: 20px 0;">'
    for day in range(1, 51):
        if day in data.get("daily_completion", {}):
            calendar_html += f'<div class="calendar-day completed" title="Day {day}">{day}</div>'
        else:
            calendar_html += f'<div class="calendar-day" title="Day {day}">{day}</div>'
    calendar_html += '</div>'
    st.markdown(calendar_html, unsafe_allow_html=True)
    
    # Completed Problems List
    st.markdown("### ✅ Completed Problems")
    
    completed = get_completed_problems_details()
    if completed:
        for item in completed:
            st.markdown(f"""
            <div class="problem-link completed">
                ✅ Day {item['day']} - {item['title']} ({item['category']})
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No problems completed yet. Start solving!")

# Achievements Page
def show_achievements():
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1>🏆 Achievements</h1>
        <p style="color: #B0BEC5;">Unlock badges by completing challenges</p>
    </div>
    """, unsafe_allow_html=True)
    
    data = st.session_state.data
    
    # Achievement Grid
    cols = st.columns(3)
    for i, (key, achievement) in enumerate(ACHIEVEMENTS.items()):
        with cols[i % 3]:
            if key in data.get("achievements", []):
                st.markdown(f"""
                <div class="achievement-badge" style="margin: 10px 0;">
                    <div style="font-size: 40px;">{achievement['icon']}</div>
                    <div style="font-size: 16px; margin-top: 10px; font-weight: 700;">{achievement['name']}</div>
                    <div style="font-size: 12px; margin-top: 5px; opacity: 0.8;">{achievement['description']}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="achievement-badge locked" style="margin: 10px 0;">
                    <div style="font-size: 40px;">🔒</div>
                    <div style="font-size: 16px; margin-top: 10px; font-weight: 700;">{achievement['name']}</div>
                    <div style="font-size: 12px; margin-top: 5px; opacity: 0.6;">{achievement['description']}</div>
                </div>
                """, unsafe_allow_html=True)

# Analytics Page
def show_analytics():
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1>📉 Performance Analytics</h1>
        <p style="color: #B0BEC5;">Analyze your DSA preparation progress</p>
    </div>
    """, unsafe_allow_html=True)
    
    data = st.session_state.data
    
    # Stats Summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_problems = sum(len(cat["problems"]) for cat in DSA_PROBLEMS.values())
        completed = len(data["completed_problems"])
        st.metric("Total Problems", f"{completed}/{total_problems}")
    
    with col2:
        st.metric("Current Streak", f"{data.get('streak', 0)} days")
    
    with col3:
        achievements = len(data.get("achievements", []))
        st.metric("Achievements Unlocked", f"{achievements}/{len(ACHIEVEMENTS)}")
    
    # Category Breakdown
    st.markdown("### 📊 Category Breakdown")
    
    category_data = []
    for category, cat_data in DSA_PROBLEMS.items():
        cat_problems = cat_data["problems"]
        cat_completed = len([p for p in cat_problems if f"{category}::{p['title']}" in data["completed_problems"]])
        cat_total = len(cat_problems)
        category_data.append({
            "category": category,
            "completed": cat_completed,
            "total": cat_total,
            "percentage": (cat_completed / cat_total * 100) if cat_total > 0 else 0
        })
    
    # Display category bars
    for cat in category_data:
        st.markdown(f"""
        <div style="margin: 15px 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                <span style="color: #B0BEC5;">{cat['category']}</span>
                <span style="color: #00E676;">{cat['completed']}/{cat['total']} ({cat['percentage']:.1f}%)</span>
            </div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {cat['percentage']}%;">{cat['percentage']:.1f}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tips Section
    st.markdown("### 💡 Tips for TCS Preparation")
    st.info("""
    1. **Focus on Number System & Array** - These are frequently asked in TCS
    2. **Practice Sorting & Searching** - Binary search and sorting algorithms are important
    3. **String handling** - TCS often asks string manipulation questions
    4. **Time Complexity** - Be prepared for time/space complexity questions
    5. **Daily Practice** - Maintain your streak for better retention
    """)

# Main App
def main():
    create_sidebar()
    
    if st.session_state.current_page == "Dashboard":
        show_dashboard()
    elif st.session_state.current_page == "Daily Plan":
        show_daily_plan()
    elif st.session_state.current_page == "Progress":
        show_progress()
    elif st.session_state.current_page == "Achievements":
        show_achievements()
    elif st.session_state.current_page == "Analytics":
        show_analytics()

if __name__ == "__main__":
    main()

