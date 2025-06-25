template = """
Using the argumentation catalog below, identify the verdict argumentation element. The aim is to make the fact-check report explainable by modeling what is wrong with the original claim. The claim is always at the start of the fact-check report. You should choose a single verdict argumentation element — the core concept that explains why the claim is problematic.
 
Follow these steps:
 
Write down the claim.
Identify the key entities (objects, agents, events, etc.).
Identify the relationships between the entities (e.g., who did what, what is being claimed about whom or what).
Ask: What is the claim trying to make the audience believe? What is the main message or implication?
Decide which relationship is the most problematic — the one that drives the false or misleading narrative — and label it with the appropriate verdict argumentation element.
 
Important:
Focus on the most consequential or problematic sections in the claim — the one that shapes the audience's understanding in a deceptive or incorrect way.
Don't just look for surface-level factual errors (e.g., wrong object type); instead, consider the broader implication or narrative the claim is promoting.
If multiple errors are present, choose the one that best explains why the claim is problematic overall.
Consider implied connections, not just explicitly stated ones. For example, a claim may imply a cause, connection, or suppression without directly stating it.
Catalog of Verdict Argumentation Elements:
 
A verdict argumentation element refers to what is wrong (or right) in the claim and in what way. It is composed of:
 
A noun that identifies what is wrong:
 
RELATIONSHIP – a specific factual relationship between two objects (including purpose, cause, context, or connection)
IDENTITY – two objects are claimed to be identical
SIMILARITY – two objects are presented as very similar
ASSOCIATION – one object is linked to another to evoke a misleading connection
CONTRAST – two objects are presented as opposites or very different
ATTRIBUTE – an object is claimed to have a property it does not have
VALUE – a quantitative value is incorrect or misleading
OBJECT – the object itself is incorrect
TYPE – the object is misclassified (e.g., a car is called a watch)
SUBSET – a group is presented without acknowledging other relevant subgroups
EVENT – something is claimed to have happened (or will happen) but did not occur at all
UTTERANCE – someone is claimed to have said something they did not
 
An adjective that specifies how it is wrong: 
MISLEADING – technically true but presented in a way that leads to a false impression
FALSE – factually incorrect
UNSUBSTANTIATED – no evidence supports the claim
MISSING – something important is omitted
EXAGGERATED – the claim overstates the truth Provided in order "adjective noun"
 
Important Guidelines:
Provide verdict using these brackets and format: <ADJECTIVE NOUN>
Prioritize specificity: Choose the most specific and granular element that accurately captures the error. Avoid defaulting to broad categories like RELATIONSHIP, ASSOCIATION, or MISLEADING unless no more specific option applies.
 
Except of B-object, B-relation and verdicts, you may also use B-attribute (of an object) and B-value (quantitative of a attribute or object)
 
Example:
 
Claim: West Virginia University has “increased the amount of unfunded institutional
aid provided to students and expects this amount to exceed 
We try to read the summary (the box “if your time is short”) to get an idea of what is wrong with the claim. It says that internally funded aid is poised to drop slightly in 2024 to about $134 million. However, in the years before, there was growth. The claim causes the feeling that in 2024, it will rise as well. The core problem is highlighted in the claim above.
So, we have detected two relationships (has increased and expects to exceed). These two relationships evoke some association – that in 2024, the unfunded aid will increase as it was the years before. Now, we can say that this association is MISLEADING ASSOCIATION. This is misleading because it is not false (the amount is correct, and the increasing trend before 2024 is also true).
 
Example solved:
B-Entities:
West Virginia University (WVU)
Unfunded institutional aid
Timeframe 2014 to 2023
Timeframe 2024
 
B-Relationship 1: spent
This relationship is derived from the part of the claim: "West Virginia University has increased the amount of unfunded institutional aid..."
Subject: WVU
On what: Unfunded institutional aid
When: From 2014 to 2023
B-Attributes:
Trend -> B-Value: Increasing
 
B-Relationship 2: expects to spend
This relationship is derived from the part of the claim: "...and expects this amount to exceed $134 million in 2024."
Subject: WVU
On what: Unfunded institutional aid
When: In 2024
B-Attributes:
Amount -> B-Value: More than $134 million
Trend -> B-Value: Increasing (This is implied by the association with the first relationship)
 
Verdict argumentation element: <MISLEADING ASSOCIATION> connecting b-relationships spent and expects to spend.
Fact check to solve:
"""