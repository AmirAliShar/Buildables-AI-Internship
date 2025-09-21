## Observations
Part 1: Summarization Task (Gemma Model)

Original Article Word Count: 130

| Temperature | Summary Word Count | Score (1–10) | Observations                                                                     |
| ----------- | ------------------ | ------------ | -------------------------------------------------------------------------------- |

| 0.1         | 52                 | 9            | Very concise and accurate. Captures the main points but leaves out some context. |

| 0.7         | 65                 | 8            | Balanced summary with good details. Slightly verbose but still relevant.         |

| 1.0         | 60                 | 8            | Covers most points and flows naturally. A bit less structured than 0.1.          |



## Conclusion:
Gemma produces accurate and concise summaries across temperatures. Lower temperature (0.1) is the most precise, while higher temperatures (0.7–1.0) add slight creativity and variation.

##Part 2: Question Answering Task (OpenAI Model)

| Temperature | Question Asked                            | Model Response                                           | Score (1–10) | Observations                                                                   |
| ----------- | ----------------------------------------- | -------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------ |

| 0.1         | *Is YouTube expanding monetization?*      | Yes.                                                     | 10           | Perfectly accurate and directly answers the question.                          |

| 0.7         | *How can creators earn money by YouTube?* | Detailed list of monetization methods.                   | 9            | Very comprehensive, though it adds extra methods not mentioned in the article. |

| 1.0         | *Can YouTube give proactive suggestions?* | Yes, with detailed explanation of recommendation system. | 9            | Correct and insightful, but goes beyond article scope.                         |

## Conclusion:
OpenAI is highly reliable for Q&A tasks. Lower temperatures provide concise, factual answers, while higher temperatures generate more detailed, creative, and sometimes extra-contextual responses.

## Final Scoring Comparison

| Model                     | Average Score | Strength                                                     |
| ------------------------- | ------------- | ------------------------------------------------------------ |

| **Gemma (Summarization)** | 8.3 / 10      | Concise and accurate summarization, best at low temperature. |

| **OpenAI (Q\&A)**         | 9.3 / 10      | Excellent factual answers, detailed at higher temperatures.  |

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

Gemma (open-source) is more cost-effective and can be run locally or on cheaper infrastructure, though inference speed may depend on hardware.

OpenAI is faster and more reliable out of the box, but comes with higher usage costs and strict token limits depending on the subscription tier.

In summary: Gemma is cheaper for bulk summarization, while OpenAI is better for production-ready Q&A where speed and accuracy matter.
