📑 Prompting Strategies Evaluation Report
1. Zero-Shot Prompts & Outputs
Benchmark Questions

Prompt: Translate "Good morning, how are you?" into French
Output: Bonjour, comment allez-vous ?

Prompt: Summarize: "The stock market rose today due to gains in the technology sector."
Output: The stock market rose today because of technology sector gains.

Prompt: Classify the sentiment: "I am extremely happy with the service."
Output: Positive

Logic Puzzles

Prompt: Alice is older than Bob. Bob is older than Charlie. Who is the youngest?
Answer: Charlie

Prompt: There are three boxes mislabeled. One has apples, one has oranges, one mixed. You may take one fruit. How to relabel correctly?
Answer: Take from "mixed" box and relabel based on result.

Math Problem

Prompt: A train travels 60 km in 1 hour. How far in 4 hours?
Answer: 240 km

Reasoning Task

Prompt: Farmer has 5 cows, each produces 8 liters/day. How much total milk?
Answer: 40 liters

2. Few-Shot Prompts & Outputs
Benchmark Questions

Prompt: Translate "Good morning, how are you?" into French
Output: Bonjour, comment allez-vous ?

Prompt: Summarize stock market text
Output: The stock market went up today.

Prompt: Classify sentiment of "I am extremely happy with the service."
Output: Positive

Logic Puzzles

Prompt: Alice, Bob, Charlie puzzle
Answer: Charlie

Prompt: Box labeling puzzle
Answer: Detailed step-by-step elimination process ending with correct labels.

Math Problem

Prompt: Train problem
Answer: Step-by-step → 240 km

Reasoning Task

Prompt: Farmer milk problem
Answer: Step-by-step → 40 liters

3. Chain-of-Thought (CoT) Prompts & Outputs
Benchmark Questions

Prompt: Translate "Good morning, how are you?"
Output: Detailed breakdown of "bonjour" + formal/informal → Final: Bonjour, comment allez-vous ?

Prompt: Summarize stock market sentence
Output: Full step-by-step analysis → Final: The stock market increased today due to technology sector.

Prompt: Classify sentiment of "I am extremely happy..."
Output: Step-by-step keyword analysis → Final: Positive

Logic Puzzles

Prompt: Alice, Bob, Charlie
Output: Step-by-step reasoning → Charlie

Prompt: Box labeling puzzle
Output: Detailed logical deduction → Correct relabeling of all boxes

Math Problem

Prompt: Train problem
Output: Step-by-step speed × time → 240 km

Reasoning Task

Prompt: Farmer milk problem
Output: Step-by-step multiplication → 40 liters

4. Rubric-Based Evaluation
Task	Method	Correctness	Reasoning Clarity	Completeness	Conciseness	Score/12
| Task          | Method    | Correctness | Reasoning Clarity | Completeness | Conciseness | Score/12 |
| ------------- | --------- | ----------- | ----------------- | ------------ | ----------- | -------- |
| Translation   | Zero-Shot | 3           | 0                 | 3            | 3           | **9**    |
| Translation   | Few-Shot  | 3           | 2                 | 3            | 3           | **11**   |
| Translation   | CoT       | 3           | 3                 | 3            | 2           | **11**   |
| Summarization | Zero-Shot | 3           | 0                 | 2            | 3           | **8**    |
| Summarization | Few-Shot  | 2           | 2                 | 2            | 3           | **9**    |
| Summarization | CoT       | 3           | 3                 | 3            | 2           | **11**   |
| Sentiment     | Zero-Shot | 3           | 0                 | 3            | 3           | **9**    |
| Sentiment     | Few-Shot  | 3           | 2                 | 3            | 3           | **11**   |
| Sentiment     | CoT       | 3           | 3                 | 3            | 2           | **11**   |
| Puzzle 1      | Zero-Shot | 3           | 0                 | 3            | 3           | **9**    |
| Puzzle 1      | Few-Shot  | 3           | 2                 | 3            | 3           | **11**   |
| Puzzle 1      | CoT       | 3           | 3                 | 3            | 2           | **11**   |
| Puzzle 2      | Zero-Shot | 2           | 1                 | 2            | 2           | **7**    |
| Puzzle 2      | Few-Shot  | 3           | 3                 | 3            | 2           | **11**   |
| Puzzle 2      | CoT       | 3           | 3                 | 3            | 2           | **11**   |
| Math          | Zero-Shot | 3           | 0                 | 3            | 3           | **9**    |
| Math          | Few-Shot  | 3           | 2                 | 3            | 3           | **11**   |
| Math          | CoT       | 3           | 3                 | 3            | 2           | **11**   |
| Reasoning     | Zero-Shot | 3           | 0                 | 2            | 3           | **8**    |
| Reasoning     | Few-Shot  | 3           | 2                 | 3            | 3           | **11**   |
| Reasoning     | CoT       | 3           | 3                 | 3            | 2           | **11**   |


6. Observations & Insights

Zero-Shot: Best for quick, simple tasks (translation, classification). Weak in reasoning-heavy puzzles.

Few-Shot: Improved consistency and step-by-step answers in math and reasoning tasks.

CoT: Gave the best reasoning clarity (especially for puzzles & summarization). Sometimes verbose but most logical.

6. Reflection Questions

Q1. Which method gave the most accurate results?  
➡ Few-Shot and CoT both outperformed Zero-Shot. CoT was best for reasoning-heavy tasks, Few-Shot for structured answers.

Q2. Did the CoT prompts improve reasoning quality?  
➡ Yes ✅ CoT significantly improved reasoning by forcing the model to explain step-by-step, especially in logic puzzles and math.


Q3. How much do examples influence the model’s responses?  
➡ Examples had a big influence: Few-Shot made the model more consistent and avoided shortcuts. It helped in tasks like summarization where Zero-Shot was too brief.
