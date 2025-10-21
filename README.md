# QA Analyst Technical Assessment

**Candidate:** Shane O'Neill  
**Language Used:** Python  
**Completion Date:** 10/21/2025

### Structure
qa-analyst-assessment/

├── README.md                     
├── requirements.txt            
├── part1-functional/
│   └── solution.py             
├── part2-api-testing/
│   └── test_api.py             

## Part 1: Functional Programming
- **Time Spent:** ~30 minutes  
- **Approach:** Wrote a function that removes repeated numbers from a list while keeping the original order. The original list stays unchanged.

## Part 2: API Testing
- **Time Spent:** ~30 minutes  
- **Approach:** Wrote 3 tests:
  - One to check if user info comes back correctly
  - One to check if adding a new post works
  - One to check what happens when a user doesn't exist

## How to Run

### Part 1
```bash
python part1-functional/solution.py
```

### Part 2
```bash
pip install -r requirements.txt
pytest part2-api-testing/test_api.py
```


