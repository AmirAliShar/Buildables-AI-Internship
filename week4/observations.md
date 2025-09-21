## Observations

Original Article Word Count: 130
| Task Type         | Model           | Temperature | Output Quality                    | Word Count | Score (/5)       | Notes                                     |
| ----------------- | --------------- | ----------- | --------------------------------- | ---------- | ---------------- | ----------------------------------------- |
| Summarization     | Gemma           | 0.1         | Concise, very factual             | 52         | 5                | Captured main points without extra info   |
| Summarization     | Gemma           | 0.7         | Balanced, clear, slight expansion | 65         | 4                | Added some context, still accurate        |
| Summarization     | Gemma           | 1.0         | Detailed, a bit verbose           | 60         | 4                | Still faithful, but more creative wording |
| Q\&A              | OpenAI          | 0.1         | Direct yes/no                     | –          | 5                | Accurate, very short answer               |
| Q\&A              | OpenAI          | 0.7         | Comprehensive, detailed           | –          | 4                | Added extra info beyond given article     |
| Q\&A              | OpenAI          | 1.0         | Proactive, contextual             | –          | 4                | Correct but leaned on external knowledge  |
| **Average Score** | **Gemma = 4.3** |             |                                   |            | **OpenAI = 4.3** | Both performed equally well overall       |



## Conclusion:
Gemma produces accurate and concise summaries across temperatures. Lower temperature (0.1) is the most precise, while higher temperatures (0.7–1.0) add slight creativity and variation.

OpenAI is highly reliable for Q&A tasks. Lower temperatures provide concise, factual answers, while higher temperatures generate more detailed, creative, and sometimes extra-contextual responses.


## 💡 Discussion Points

# Which model was better overall for summarization? Why?

Gemma was better for summarization because it consistently produced concise, accurate summaries that stayed close to the original text. At lower temperatures (0.1), it avoided unnecessary elaboration and stuck to the core points.

# Which model provided more accurate answers in the Q&A task?

OpenAI performed better in Q&A. Its answers were direct, factual, and well-structured. At higher temperatures, it provided richer context, though sometimes it introduced extra details not explicitly in the article.

# Did one model seem more “creative” or more “factual”? How might this affect which one you’d choose for a specific application?

Gemma leaned more factual and structured, which is ideal for summarization tasks where precision matters.

OpenAI leaned more creative, especially at higher temperatures, making it useful when broader context or human-like explanations are needed.

# For real applications:

Use Gemma for tasks requiring accurate condensation of text (summarization, note-taking).

Use OpenAI for interactive Q&A, tutoring, or tasks where richer explanations are valuable.

# What differences did you notice in cost, speed, or token limits between the models?

# 💸 Cost, Speed, and Token Limits

**Gemma (via Groq):**

Cost: Free to use on Groq.

Speed: Inference is reasonably fast, though can vary slightly depending on Groq’s server load.

Token Limits: No strict published limits, but larger inputs may slow down processing. Works well for summarization tasks.

**OpenAI OSS (via Groq):**

Cost: Free to use on Groq as well.

Speed: Often faster and more optimized on Groq’s hardware, making it better for real-time Q&A.

Token Limits: Similar practical constraints as Gemma, though Groq manages token efficiency well. Handles structured outputs reliably.

# Summary: Both models are free when accessed via Groq.

Gemma is better suited for bulk summarization where cost efficiency and decent performance matter.

OpenAI OSS performs better for interactive Q&A tasks where speed and accuracy are more important.
