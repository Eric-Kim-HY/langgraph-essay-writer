PLAN_PROMPT = """As an expert essay planner, create a comprehensive outline for a 5-paragraph essay on the given topic. Include:
1. A clear thesis statement
2. Main points for each paragraph
3. Potential supporting details or examples
4. Any specific instructions or notes for each section"""

WRITER_PROMPT = """As a skilled essay writer, craft an exceptional 5-paragraph essay based on the provided outline and topic. Your essay should:
1. Have a strong introduction with a clear thesis
2. Develop each main point thoroughly
3. Use relevant evidence and examples
4. Conclude effectively, reinforcing the main argument

If critique is provided, revise your essay accordingly, focusing on the areas of improvement mentioned.

Utilize the following information as needed:

------

{content}"""

REFLECTION_PROMPT = """As an experienced essay evaluator, provide a thorough critique of the submitted essay. Your feedback should include:
1. Overall assessment of the essay's strengths and weaknesses
2. Specific recommendations for improvement in:
   - Content depth and relevance
   - Structure and organization
   - Writing style and clarity
   - Use of evidence and examples
3. Suggestions for enhancing the essay's impact and effectiveness"""

RESEARCH_PLAN_PROMPT = """As a diligent researcher, generate 3 focused search queries to gather relevant information for the following essay topic. Ensure your queries are:
1. Specific to the main aspects of the topic
2. Likely to yield credible and diverse sources
3. Formulated to uncover both factual information and analytical perspectives"""

RESEARCH_CRITIQUE_PROMPT = """Based on the provided revision requests, formulate 3 targeted search queries to gather additional information. Your queries should:
1. Address specific areas mentioned in the critique
2. Aim to fill any identified knowledge gaps
3. Seek out authoritative sources to strengthen the essay's arguments"""