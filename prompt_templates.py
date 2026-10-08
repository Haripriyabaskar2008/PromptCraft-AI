def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer the following task directly and accurately.

Task:
{task}
""".strip()

    if technique == "One-shot":
        return f"""
Use the example below to understand the expected style.

Example:
Task: Explain Python.
Answer: Python is a high-level programming language used to
build applications, automate tasks, and analyze data.

Now answer this task:
{task}
""".strip()

    if technique == "Few-shot":
        return f"""
Study the examples and follow their style.

Example 1:
Task: What is AI?
Answer: AI is technology that enables computers to perform
tasks that normally require human intelligence.

Example 2:
Task: What is ML?
Answer: Machine learning is a part of AI where systems learn
patterns from data to make predictions or decisions.

Example 3:
Task: What is NLP?
Answer: NLP enables computers to process and understand
human language.

Now answer:
{task}
""".strip()

    if technique == "CoT":
        return f"""
Solve the following task carefully.

First identify the important information, then work through
the solution logically, and finally provide a concise final
answer.

Do not reveal private or internal chain-of-thought.
Provide only a short explanation of the key steps.

Task:
{task}
""".strip()

    if technique == "Manual CoT":
        return f"""
Use the following explicit reasoning structure.

Step 1 - Understand the task:
Identify what is being asked.

Step 2 - Identify information:
List the important facts, inputs, or constraints.

Step 3 - Apply the method:
Describe the main calculation, rule, or approach.

Step 4 - Verify:
Check whether the result is reasonable.

Step 5 - Final answer:
Give the final answer clearly.

Task:
{task}
""".strip()

    if technique == "ToT":
        return f"""
Solve the task by exploring multiple possible approaches.

Approach A:
Suggest one possible solution and briefly evaluate it.

Approach B:
Suggest a second possible solution and briefly evaluate it.

Approach C:
Suggest a third possible solution when useful.

Selection:
Compare the approaches and select the most suitable one.

Final answer:
Provide the selected answer with a concise explanation.

Do not reveal private or internal chain-of-thought.

Task:
{task}
""".strip()

    raise ValueError("Unknown prompting technique")