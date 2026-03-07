"""
combine_datasets.py
Fixed version - text variation added to prevent overfitting
"""

import pandas as pd
import numpy as np
import json
import os
import warnings
warnings.filterwarnings('ignore')

os.makedirs("model_artifacts", exist_ok=True)

TARGET_CAREERS = {
    "Software":             "Software Engineer",
    "Web Devel":            "Software Engineer",
    "Data Scien":           "Data Scientist",
    "Machine Learning":     "AI/ML Engineer",
    "Computer Research":    "AI/ML Engineer",
    "UX":                   "UX Designer",
    "User Experience":      "UX Designer",
    "Graphic Des":          "Graphic Designer",
    "Information Systems":  "Product Manager",
    "Cybersec":             "Cybersecurity Analyst",
    "Information Security": "Cybersecurity Analyst",
    "Marketing Man":        "Marketing Manager",
    "Financial Anal":       "Financial Analyst",
    "Physician":            "Doctor",
    "Surgeon":              "Doctor",
    "Psycholog":            "Psychologist",
    "Lawyer":               "Lawyer",
    "Postsecondary Teacher":"Educator",
    "Architect":            "Architect",
    "Mechanical Eng":       "Mechanical Engineer",
    "Civil Eng":            "Civil Engineer",
    "Research Scien":       "Research Scientist",
    "Human Resources Man":  "HR Manager",
    "Writers":              "Content Creator",
    "Biochem":              "Biotechnologist",
    "Environmental Scien":  "Environmental Scientist",
    "Operations Man":       "Entrepreneur",
    "Management Anal":      "Business Consultant",
    "Logistician":          "Supply Chain Manager",
}

RIASEC_COLS = ['Realistic','Investigative','Artistic','Social','Enterprising','Conventional']

# ─────────────────────────────────────────
# TEXT PROFILES — 5 VARIATIONS PER CAREER
# ─────────────────────────────────────────
TEXT_PROFILES = {
    "Software Engineer": {
        "problems": [
            "I love debugging complex systems and finding elegant solutions to logic problems",
            "I enjoy building scalable backend systems that handle millions of users",
            "I get excited solving algorithmic challenges and optimizing code performance",
            "I love automating repetitive tasks and making entire systems more efficient",
            "I enjoy designing clean APIs and writing maintainable readable code",
        ],
        "dreams": [
            "I would build open source tools that millions of developers use every day",
            "I would create software products that solve real problems for real people",
            "I would develop the infrastructure that powers the next generation internet",
            "I would build developer tools that make programming ten times faster",
            "I would contribute to AI systems that genuinely help people in daily life",
        ],
        "skills": [
            "People say I explain technical concepts in a very clear and simple way",
            "Friends say I write the cleanest most readable code they have ever seen",
            "Colleagues say I debug problems faster than anyone else on the team",
            "People always ask me to review their code and system architecture designs",
            "My peers say I can pick up any new technology extremely quickly",
        ]
    },
    "Data Scientist": {
        "problems": [
            "I love finding hidden patterns in large datasets that others completely miss",
            "I enjoy using statistical methods to answer questions with no obvious answer",
            "I get excited when data tells a story that changes how people make decisions",
            "I love building predictive models that learn from historical data to forecast future",
            "I enjoy cleaning messy data and turning chaos into structured meaningful insights",
        ],
        "dreams": [
            "I would analyze global health data to predict and prevent disease outbreaks",
            "I would use machine learning to solve climate change and environmental problems",
            "I would build recommendation systems that truly understand what people need",
            "I would run my own data consultancy helping companies make smarter decisions",
            "I would create data pipelines that power real time decision making at scale",
        ],
        "skills": [
            "People say I have an exceptional ability to find meaning in numbers and data",
            "My professors always praised my statistical thinking and analytical approach",
            "Friends say I can turn complicated data into clear and compelling visualizations",
            "I am known for my patience in cleaning and structuring messy datasets",
            "People say I can explain complex analysis results to non technical audiences",
        ]
    },
    "AI/ML Engineer": {
        "problems": [
            "I love building systems that learn and improve from experience over time",
            "I enjoy training neural networks and pushing boundaries of what models can do",
            "I get excited by the challenge of deploying ML models into real production systems",
            "I love reading research papers and implementing state of the art algorithms",
            "I enjoy optimizing model performance and reducing inference latency at scale",
        ],
        "dreams": [
            "I would build AI systems that accelerate scientific discovery across every field",
            "I would create AI tools that make education personalized for every student",
            "I would develop responsible AI frameworks that benefit all of humanity equally",
            "I would build the next generation of AI assistants that truly understand humans",
            "I would run an AI research lab working on problems that matter most to society",
        ],
        "skills": [
            "People say I have an exceptional ability to combine math and engineering thinking",
            "My colleagues say I can implement complex research papers faster than anyone",
            "I am known for my ability to debug models and identify subtle training issues",
            "Friends say I can explain neural networks in a way that actually makes sense",
            "People say I have remarkable intuition for which ML approach will work best",
        ]
    },
    "UX Designer": {
        "problems": [
            "I love observing how people interact with products and finding friction points",
            "I get passionate when I can redesign an experience to make it truly intuitive",
            "I enjoy conducting user research and translating insights into better designs",
            "I love the process of wireframing prototyping and testing with real users",
            "I enjoy finding the gap between what users say they want and what they need",
        ],
        "dreams": [
            "I would design accessibility tools that make technology usable for everyone",
            "I would create digital experiences so intuitive they feel completely invisible",
            "I would run a design studio focused on human centered product design globally",
            "I would design the next generation of healthcare interfaces that save lives",
            "I would build design systems that make great UX the default not the exception",
        ],
        "skills": [
            "People say I have an exceptional ability to understand what others truly need",
            "My colleagues say I can spot a bad user experience from a mile away instantly",
            "Friends always ask me to review apps and websites before they launch them",
            "I am known for my empathy and ability to think from the user perspective",
            "People say I can facilitate user research sessions that reveal deep insights",
        ]
    },
    "Graphic Designer": {
        "problems": [
            "I love solving visual communication problems through design and typography",
            "I get excited when I transform a vague brief into a compelling visual story",
            "I enjoy the challenge of making complex information beautiful and digestible",
            "I love finding the perfect color palette and layout that makes a brand memorable",
            "I enjoy creating visual systems that remain consistent across all touchpoints",
        ],
        "dreams": [
            "I would run my own creative studio designing brand identities for startups",
            "I would design book covers and album art for my favorite artists and authors",
            "I would create visual campaigns for social causes I deeply believe in",
            "I would build a design school that teaches visual thinking to young people",
            "I would design the visual identity for a brand that becomes globally iconic",
        ],
        "skills": [
            "People say I have an extraordinary eye for color harmony and visual balance",
            "Friends always ask me to design invitations logos and social media content",
            "I am known for my ability to communicate emotions through visual elements",
            "My peers say my design work is always instantly recognizable and distinctive",
            "People say I can produce beautiful work extremely quickly under tight deadlines",
        ]
    },
    "Product Manager": {
        "problems": [
            "I love sitting at the intersection of business technology and user needs",
            "I get excited by defining what to build and why it will create real user value",
            "I enjoy prioritizing competing demands and deciding with limited information",
            "I love the process of taking a product from zero to one and then scaling it",
            "I enjoy aligning engineering design and business teams toward one clear goal",
        ],
        "dreams": [
            "I would build a product that solves a massive problem for billions of people",
            "I would lead product at a company whose mission I believe in completely",
            "I would start my own startup and take a product from idea to market leader",
            "I would reshape an entire industry through a product nobody imagined before",
            "I would build a product culture where every team member thinks like an owner",
        ],
        "skills": [
            "People say I have an exceptional ability to align teams around a shared vision",
            "Colleagues say I can translate technical complexity into clear business value",
            "I am known for my strategic thinking and ability to see the big picture clearly",
            "Friends say I naturally take charge in group projects and keep everyone on track",
            "People say I can say no to good ideas to protect focus on the most important",
        ]
    },
    "Cybersecurity Analyst": {
        "problems": [
            "I love thinking like an attacker to find vulnerabilities before hackers do",
            "I get excited by the challenge of protecting systems from increasingly clever threats",
            "I enjoy reverse engineering malware and understanding how attacks work internally",
            "I love the cat and mouse game of security where the threats never stop evolving",
            "I enjoy building detection systems that catch anomalies before damage is done",
        ],
        "dreams": [
            "I would build security systems that protect critical national infrastructure",
            "I would run a cybersecurity firm that defends companies from nation state attacks",
            "I would develop open source security tools used by defenders worldwide",
            "I would train the next generation of ethical hackers and security researchers",
            "I would create security awareness programs that protect millions of everyday users",
        ],
        "skills": [
            "People say I have an extraordinary ability to think several steps ahead defensively",
            "Friends say I am obsessively detail oriented and never miss anything suspicious",
            "I am known for staying calm and methodical when systems are under active attack",
            "Colleagues say I can find the one vulnerability in a system everyone else missed",
            "People say I have an exceptional ability to communicate risk to non technical teams",
        ]
    },
    "Marketing Manager": {
        "problems": [
            "I love figuring out what makes people buy and how to influence their decisions",
            "I get excited by the challenge of making a brand stand out in a crowded market",
            "I enjoy combining creativity and data to build campaigns that actually convert",
            "I love the puzzle of understanding an audience and speaking directly to their needs",
            "I enjoy finding the one insight about customers that changes everything about strategy",
        ],
        "dreams": [
            "I would build a global brand that becomes a cultural icon and movement",
            "I would run marketing for products I genuinely believe change peoples lives",
            "I would start a creative agency that tells powerful brand stories worldwide",
            "I would use marketing to promote social causes and drive real lasting change",
            "I would build a community around a brand so strong it markets itself organically",
        ],
        "skills": [
            "People say I have a natural talent for storytelling and persuasive communication",
            "Friends say I always know exactly what to say to get people excited about ideas",
            "I am known for my creativity and ability to spot emerging trends before anyone else",
            "My colleagues say I can build genuine connections with almost anyone I meet",
            "People say I can write copy that makes people feel understood and compelled to act",
        ]
    },
    "Financial Analyst": {
        "problems": [
            "I love analyzing financial statements and finding opportunities others overlook",
            "I get excited by building financial models that predict business performance",
            "I enjoy assessing risk and making data driven investment decisions confidently",
            "I love studying market trends and understanding the forces that drive economies",
            "I enjoy finding the financial story hidden inside a complex set of numbers",
        ],
        "dreams": [
            "I would manage an investment fund that generates returns for thousands of people",
            "I would advise startups on financial strategy and help them scale successfully",
            "I would build financial literacy programs for people who never had access to them",
            "I would analyze global markets and write research that shapes investment decisions",
            "I would create financial models that help governments allocate resources better",
        ],
        "skills": [
            "People say I have an exceptional ability to work with numbers and spreadsheets",
            "My professors praised my precision and attention to detail in financial modeling",
            "Friends say I can explain complex financial concepts in a simple and clear way",
            "I am known for my disciplined and methodical approach to every problem I face",
            "People say I can build a financial model from scratch faster than anyone they know",
        ]
    },
    "Doctor": {
        "problems": [
            "I love solving complex diagnostic puzzles where every symptom is a clue to solve",
            "I feel most fulfilled when I can relieve someone pain or cure their illness",
            "I enjoy studying the human body and understanding how all systems interact",
            "I get satisfaction from making critical decisions that directly save human lives",
            "I love the challenge of staying current with rapidly evolving medical research",
        ],
        "dreams": [
            "I would run a free clinic in underserved communities providing quality healthcare",
            "I would research rare diseases and develop treatments that do not yet exist today",
            "I would combine technology and medicine to revolutionize patient care completely",
            "I would train the next generation of doctors in developing countries worldwide",
            "I would build healthcare systems that make quality medicine accessible to everyone",
        ],
        "skills": [
            "People say I remain calm and composed in high pressure emergency situations",
            "Friends always come to me when they need careful and thoughtful medical advice",
            "I am known for my attention to detail and thoroughness in everything I do daily",
            "People say I have a natural ability to make others feel safe and well cared for",
            "Colleagues say I have exceptional empathy combined with sharp clinical thinking",
        ]
    },
    "Psychologist": {
        "problems": [
            "I love understanding why people behave the way they do in different situations",
            "I get deeply engaged when helping someone untangle complex emotional patterns",
            "I enjoy studying the connection between thoughts feelings and human behavior",
            "I feel fulfilled when I help someone break through a mental barrier holding them back",
            "I love designing research studies that reveal truths about human psychology",
        ],
        "dreams": [
            "I would make mental health care accessible and affordable for absolutely everyone",
            "I would research the psychology of happiness and what makes humans truly flourish",
            "I would work with schools to build emotional intelligence programs for all children",
            "I would write books that help people understand and genuinely improve their mental health",
            "I would create therapy approaches that help people recover faster from trauma",
        ],
        "skills": [
            "People say I listen deeply and make them feel truly heard and understood always",
            "Friends always come to me with their personal problems and emotional struggles",
            "I am known for my patience empathy and completely non judgmental approach to people",
            "People say I can read emotions and sense how someone is feeling without any words",
            "Colleagues say I can build therapeutic rapport with clients unusually quickly",
        ]
    },
    "Lawyer": {
        "problems": [
            "I love constructing logical arguments and finding flaws in opposing positions",
            "I get excited by complex legal puzzles where the answer requires deep research",
            "I enjoy the challenge of advocating for someone who cannot speak for themselves",
            "I love studying how laws shape society and influence human behavior at scale",
            "I enjoy finding the one legal precedent that changes the outcome of an entire case",
        ],
        "dreams": [
            "I would run a public interest law firm fighting for human rights and social justice",
            "I would specialize in technology law as AI reshapes legal and ethical boundaries",
            "I would become a judge who interprets laws with fairness and deep legal wisdom",
            "I would advise governments on policy to create more equitable legal systems globally",
            "I would build a legal aid organization that gives everyone access to quality defense",
        ],
        "skills": [
            "People say I am an exceptionally persuasive and logically structured communicator",
            "Friends always ask me to help them understand contracts and complex legal documents",
            "I am known for my ability to research deeply and build completely airtight arguments",
            "People say I stay calm and sharp under pressure in the most high stakes situations",
            "Colleagues say I can find the strongest argument for any position extremely quickly",
        ]
    },
    "Educator": {
        "problems": [
            "I love finding new ways to explain difficult concepts until they finally click",
            "I get deep satisfaction when I see the moment a student truly understands something",
            "I enjoy designing curriculum and learning experiences that genuinely inspire curiosity",
            "I love the challenge of reaching students who have struggled with traditional methods",
            "I enjoy creating assessments that actually measure understanding not just memorization",
        ],
        "dreams": [
            "I would build a school that makes every student feel seen valued and truly capable",
            "I would create free online courses that educate millions of people around the world",
            "I would reform education systems to focus on creativity and critical thinking skills",
            "I would mentor underprivileged youth and help them access world class education",
            "I would design a curriculum that prepares students for jobs that do not exist yet",
        ],
        "skills": [
            "People say I have a rare gift for explaining complex ideas in very simple terms",
            "Students always say I am the teacher who made them finally believe they could learn",
            "I am known for my patience encouragement and belief in every single persons potential",
            "Friends say I naturally take on a teaching role in every group I am ever part of",
            "People say I can make even the most boring topic feel genuinely exciting and relevant",
        ]
    },
    "Architect": {
        "problems": [
            "I love solving the tension between beautiful design and real functional constraints",
            "I get excited when I can design a space that changes how people feel and move",
            "I enjoy the technical challenge of making a building structurally sound and stunning",
            "I love designing spaces that bring communities together and serve real human needs",
            "I enjoy finding creative solutions when budget and structural limitations conflict",
        ],
        "dreams": [
            "I would design sustainable cities that work in harmony with the natural environment",
            "I would create affordable housing that is beautiful dignified and genuinely livable",
            "I would design iconic public spaces that become lasting symbols of their cities",
            "I would build schools and hospitals in developing regions that inspire their users",
            "I would create buildings that use zero energy and still feel warm and beautiful",
        ],
        "skills": [
            "People say I have a remarkable ability to visualize complex three dimensional spaces",
            "Friends always ask me to help redesign their homes and reimagine their living spaces",
            "I am known for my ability to blend artistic vision with very precise technical detail",
            "My peers say I can see the complete picture while still managing every small detail",
            "People say I can communicate spatial ideas through drawings that anyone can understand",
        ]
    },
    "Mechanical Engineer": {
        "problems": [
            "I love designing physical systems and watching them actually work in the real world",
            "I get excited by the challenge of making mechanical systems dramatically more efficient",
            "I enjoy the process of prototyping testing and iterating on physical product designs",
            "I love solving engineering problems where physics and creativity must work together",
            "I enjoy analyzing why a mechanical system failed and redesigning it to be stronger",
        ],
        "dreams": [
            "I would design the next generation of electric vehicles that transform transportation",
            "I would build manufacturing systems that produce goods with absolutely zero waste",
            "I would design medical devices that improve quality of life for millions of people",
            "I would work on space exploration hardware that expands human reach in the universe",
            "I would create renewable energy systems that make fossil fuels completely obsolete",
        ],
        "skills": [
            "People say I have an exceptional ability to visualize exactly how physical systems work",
            "Friends always ask me to fix mechanical things because I can figure absolutely anything out",
            "I am known for my precision and complete zero tolerance for errors in physical systems",
            "Colleagues say I can spot a design flaw in a mechanical system almost instantly",
            "People say I have an unusual ability to understand how things break before they do",
        ]
    },
    "Civil Engineer": {
        "problems": [
            "I love designing infrastructure that millions of people depend on every single day",
            "I get excited by large scale construction challenges that require truly creative solutions",
            "I enjoy calculating structural loads and ensuring absolute safety in everything I design",
            "I love the challenge of building in very difficult environments with severe constraints",
            "I enjoy finding ways to build infrastructure that will last for hundreds of years",
        ],
        "dreams": [
            "I would design bridges and infrastructure in countries that need them most urgently",
            "I would build flood resistant cities that protect communities from severe climate change",
            "I would design sustainable water systems for regions facing desperate water scarcity",
            "I would lead construction of the most ambitious infrastructure project ever attempted",
            "I would create transportation networks that connect isolated communities to opportunity",
        ],
        "skills": [
            "People say I am exceptionally detail oriented and absolutely never cut corners on safety",
            "Friends say I can look at a construction site and immediately see what is wrong",
            "I am known for my ability to manage extremely complex projects across many moving parts",
            "Colleagues say my structural calculations are always the most thorough on any team",
            "People say I have unusual ability to anticipate construction problems before they occur",
        ]
    },
    "Research Scientist": {
        "problems": [
            "I love asking questions that nobody has answered yet and designing experiments",
            "I get deeply excited by the possibility of discovering something completely new to humanity",
            "I enjoy the rigorous process of forming a hypothesis and testing it very systematically",
            "I love reading research papers and finding gaps that my own work could meaningfully fill",
            "I enjoy the challenge of designing experiments that eliminate all possible confounding factors",
        ],
        "dreams": [
            "I would run a lab researching cures for diseases that still have absolutely no treatment",
            "I would dedicate my life to understanding the fundamental nature of the universe itself",
            "I would research renewable energy solutions to help solve the global climate crisis",
            "I would publish research that completely reshapes what humanity knows about the brain",
            "I would create a research institute where scientists work on only the hardest problems",
        ],
        "skills": [
            "People say I have an extraordinary ability to focus deeply and intensely for very long periods",
            "My professors said I ask the sharpest and most probing questions in any class or seminar",
            "I am known for my methodical approach and complete obsession with accuracy and precision",
            "Friends say I never accept a surface level answer and always need to dig much deeper",
            "People say I can design an elegant experiment that gets to the truth very efficiently",
        ]
    },
    "HR Manager": {
        "problems": [
            "I love solving the challenge of building teams where every person truly thrives together",
            "I get excited by designing systems that make organizations genuinely fair and just",
            "I enjoy mediating conflicts and turning workplace tension into productive team dynamics",
            "I love the challenge of attracting and retaining exceptional talent for organizations",
            "I enjoy designing performance systems that motivate people rather than just evaluate them",
        ],
        "dreams": [
            "I would build company cultures where every single employee feels valued and heard",
            "I would redesign hiring processes to completely eliminate bias and find true talent",
            "I would create employee development programs that genuinely transform careers at scale",
            "I would consult for organizations to build truly inclusive workplaces around the world",
            "I would make workplace wellbeing a business priority not just a nice to have benefit",
        ],
        "skills": [
            "People say I have a natural gift for making absolutely everyone feel welcome and included",
            "Friends always ask me to help resolve conflicts because I am fair calm and very balanced",
            "I am known for my ability to understand what truly motivates very different types of people",
            "Colleagues say I can sense team dynamics and address issues before they ever escalate",
            "People say I can have difficult conversations in a way that leaves everyone feeling respected",
        ]
    },
    "Content Creator": {
        "problems": [
            "I love finding the perfect angle on a story that makes people stop and pay close attention",
            "I get excited by building an audience through content that genuinely helps real people",
            "I enjoy the creative challenge of communicating complex ideas in very engaging formats",
            "I love experimenting with different content formats to see what truly resonates deeply",
            "I enjoy the puzzle of making educational content feel entertaining and completely irresistible",
        ],
        "dreams": [
            "I would build a media brand that educates and entertains millions of loyal followers",
            "I would create documentary content that changes how people see very important issues",
            "I would write a book series that helps young people navigate life with real confidence",
            "I would build the largest educational channel in my subject area anywhere in the world",
            "I would create a content platform that gives a voice to stories that are never heard",
        ],
        "skills": [
            "People say I have a natural storytelling ability that genuinely keeps everyone engaged",
            "Friends say my writing voice is very distinctive and they can always recognize my work",
            "I am known for my consistency and discipline in producing very high quality content",
            "Colleagues say I have an instinct for what audiences want even before they know it",
            "People say I can make any topic feel fascinating and worth sharing with everyone",
        ]
    },
    "Biotechnologist": {
        "problems": [
            "I love engineering biological systems to solve problems that medicine cannot yet solve",
            "I get excited by the possibility of using biology to create entirely new materials and fuels",
            "I enjoy designing experiments that push the absolute boundaries of what living cells can do",
            "I love the intersection of biology chemistry and engineering in every single project",
            "I enjoy troubleshooting biological systems that behave in completely unexpected ways",
        ],
        "dreams": [
            "I would develop gene therapies that cure genetic diseases once thought completely incurable",
            "I would engineer crops that grow in harsh conditions and feed far more people globally",
            "I would create biodegradable materials that completely replace plastic in every product",
            "I would run a biotech startup that brings a life saving treatment successfully to market",
            "I would develop probiotics and microbiome therapies that transform how we treat disease",
        ],
        "skills": [
            "People say I have exceptional patience for the very slow and meticulous laboratory work",
            "My professors praised my ability to design clean and perfectly reproducible experiments",
            "I am known for my ability to connect fundamental biological principles to real world problems",
            "Colleagues say I can troubleshoot failed experiments far better than anyone on the team",
            "People say I have an unusual ability to see potential applications in basic research findings",
        ]
    },
    "Environmental Scientist": {
        "problems": [
            "I love studying complex ecosystems and understanding how human activity deeply affects them",
            "I get passionate about finding real solutions to pollution and environmental degradation",
            "I enjoy collecting field data and translating it into actionable policy recommendations",
            "I love the challenge of communicating environmental science to completely non scientific audiences",
            "I enjoy designing monitoring systems that detect environmental change before it becomes crisis",
        ],
        "dreams": [
            "I would lead climate research that directly informs the most important global environmental policy",
            "I would restore degraded ecosystems and bring endangered species back from the absolute brink",
            "I would build monitoring systems that give early warning of approaching environmental disasters",
            "I would advise governments on science based environmental protection legislation worldwide",
            "I would create nature based solutions that fight climate change while restoring biodiversity",
        ],
        "skills": [
            "People say I have an extraordinary passion for the natural world and its urgent protection",
            "Friends say I notice environmental details in every single place I visit completely automatically",
            "I am known for my ability to communicate urgent scientific issues in a very persuasive way",
            "Colleagues say my field data collection is always the most thorough and reliable on any team",
            "People say I can find practical environmental solutions that work within real world constraints",
        ]
    },
    "Entrepreneur": {
        "problems": [
            "I love identifying gaps in the market and imagining products that could perfectly fill them",
            "I get excited by building something from nothing and growing it through sheer persistent effort",
            "I enjoy the challenge of severe resource constraints and finding very creative solutions fast",
            "I love the risk and reward dynamic of betting everything on my own ideas and executing them",
            "I enjoy the chaos of early stage companies where every day brings completely new challenges",
        ],
        "dreams": [
            "I would build a company that disrupts an entire industry and creates thousands of good jobs",
            "I would start multiple ventures across different domains I am genuinely passionate about",
            "I would build a social enterprise that generates real profit and creates massive positive impact",
            "I would create a startup ecosystem in my city that produces the next generation of founders",
            "I would build a company whose culture and products I would be proud of for my entire life",
        ],
        "skills": [
            "People say I have an exceptional ability to sell ideas and inspire others to join my vision",
            "Friends say I turn every single problem I encounter into a potential business opportunity",
            "I am known for my resilience and ability to bounce back much stronger after every setback",
            "Colleagues say I can make important decisions very quickly with incomplete information",
            "People say I have an unusual ability to see business potential where everyone else sees problems",
        ]
    },
    "Business Consultant": {
        "problems": [
            "I love diagnosing what is fundamentally wrong with an organization and prescribing the right fix",
            "I get excited by the variety of industries and complex problems I get to work on each month",
            "I enjoy building frameworks that simplify very complex business problems into clear choices",
            "I love the challenge of influencing senior leaders to adopt genuinely better ways of working",
            "I enjoy finding the one change in an organization that unlocks dramatic performance improvement",
        ],
        "dreams": [
            "I would advise Fortune 500 companies on their most critical and difficult strategic challenges",
            "I would specialize in digital transformation and help traditional companies genuinely evolve",
            "I would start my own consulting firm completely focused on sustainable business practices",
            "I would use strategy consulting skills to dramatically improve how governments serve citizens",
            "I would build a consultancy that only works with companies creating genuine positive impact",
        ],
        "skills": [
            "People say I have an exceptional ability to structure very messy problems into completely clear logic",
            "Colleagues say my slide decks and presentations are always the clearest in every single room",
            "I am known for asking the one question in a meeting that changes the entire strategic direction",
            "Friends say I can analyze any situation very quickly and immediately identify the core issue",
            "People say I can build trust with senior executives and influence them without any formal authority",
        ]
    },
    "Supply Chain Manager": {
        "problems": [
            "I love optimizing complex networks and finding costly inefficiencies that others miss completely",
            "I get excited by the challenge of delivering the right thing to the right place at the right time",
            "I enjoy building resilient systems that do not break when very unexpected disruptions suddenly hit",
            "I love the data driven side of logistics where every single decision has a very measurable impact",
            "I enjoy finding the bottleneck in a supply chain that is silently costing millions every month",
        ],
        "dreams": [
            "I would design supply chains that are completely transparent and entirely ethically sourced",
            "I would build logistics systems for humanitarian aid that genuinely save lives during crises",
            "I would use AI to create self optimizing supply networks that adapt in completely real time",
            "I would revolutionize last mile delivery to make it fast cheap and genuinely sustainable",
            "I would create supply chains so efficient they make products affordable for everyone globally",
        ],
        "skills": [
            "People say I have an exceptional ability to coordinate many complex moving parts simultaneously",
            "Colleagues say I can spot a supply chain bottleneck long before it ever becomes a serious crisis",
            "I am known for my very systematic thinking and ability to optimize extremely complex processes",
            "Friends say I am the most thoroughly organized person they have ever known in every area of life",
            "People say I can model supply chain scenarios and predict disruptions before they actually happen",
        ]
    },
}

FALLBACK_RIASEC = {
    "Software Engineer":       [3.5,5.5,2.5,2.5,3.0,3.5],
    "Data Scientist":          [3.0,6.0,2.5,2.5,3.0,4.0],
    "AI/ML Engineer":          [3.5,6.0,2.5,2.0,3.0,3.5],
    "UX Designer":             [2.5,4.0,5.5,4.5,3.0,3.0],
    "Graphic Designer":        [2.5,2.5,6.5,3.0,3.5,3.0],
    "Product Manager":         [3.0,4.5,3.5,4.5,5.0,3.5],
    "Cybersecurity Analyst":   [4.0,5.5,2.0,2.5,3.5,4.0],
    "Marketing Manager":       [2.0,3.5,4.5,4.5,5.5,3.0],
    "Financial Analyst":       [2.5,4.5,2.0,3.0,4.5,5.5],
    "Doctor":                  [3.5,5.5,2.5,5.0,3.5,3.5],
    "Psychologist":            [2.0,5.0,3.5,6.0,3.0,3.0],
    "Lawyer":                  [2.0,4.5,3.0,4.5,5.5,4.0],
    "Educator":                [2.5,4.0,4.0,6.0,3.5,3.5],
    "Architect":               [4.5,4.5,5.5,3.0,4.0,4.0],
    "Mechanical Engineer":     [5.5,5.0,2.5,2.5,3.5,4.0],
    "Civil Engineer":          [5.5,4.5,2.5,3.0,3.5,4.5],
    "Research Scientist":      [3.5,6.5,3.0,3.0,3.0,4.0],
    "HR Manager":              [2.0,3.5,3.0,6.0,4.5,4.5],
    "Content Creator":         [2.0,3.0,6.0,4.5,4.5,2.5],
    "Biotechnologist":         [4.0,6.0,2.5,3.0,3.0,4.0],
    "Environmental Scientist": [4.5,5.5,3.0,4.0,3.0,3.5],
    "Entrepreneur":            [3.5,4.0,4.0,4.0,6.5,3.0],
    "Business Consultant":     [2.5,4.5,3.0,4.5,5.5,4.0],
    "Supply Chain Manager":    [4.0,4.0,2.0,3.5,4.5,5.5],
}

DEFAULT_SKILLS = {
    "Software Engineer":       ["Python","JavaScript","Data Structures","Algorithms","System Design","Git","SQL","Problem Solving"],
    "Data Scientist":          ["Python","Statistics","Machine Learning","SQL","Data Visualization","Pandas","Communication","NumPy"],
    "AI/ML Engineer":          ["Python","Deep Learning","PyTorch","TensorFlow","MLOps","Mathematics","Research","Cloud Platforms"],
    "UX Designer":             ["User Research","Figma","Prototyping","Wireframing","Usability Testing","Empathy","Design Thinking","Communication"],
    "Graphic Designer":        ["Adobe Creative Suite","Typography","Color Theory","Branding","Illustration","Layout Design","Creativity","Visual Communication"],
    "Product Manager":         ["Product Strategy","Roadmapping","User Research","Data Analysis","Communication","Prioritization","Agile","Stakeholder Management"],
    "Cybersecurity Analyst":   ["Network Security","Ethical Hacking","SIEM Tools","Risk Assessment","Python","Incident Response","Cryptography","Threat Intelligence"],
    "Marketing Manager":       ["Digital Marketing","SEO","Data Analytics","Content Strategy","Social Media","Brand Management","Communication","CRM Tools"],
    "Financial Analyst":       ["Financial Modeling","Excel","Valuation","Accounting","Statistics","Bloomberg","Communication","Risk Analysis"],
    "Doctor":                  ["Clinical Knowledge","Diagnosis","Patient Communication","Medical Research","Decision Making","Anatomy","Empathy","Attention to Detail"],
    "Psychologist":            ["Clinical Assessment","Therapy Techniques","Research Methods","Empathy","Communication","DSM Knowledge","Ethics","Report Writing"],
    "Lawyer":                  ["Legal Research","Argumentation","Contract Drafting","Negotiation","Critical Thinking","Writing","Ethics","Case Analysis"],
    "Educator":                ["Curriculum Design","Communication","Classroom Management","Assessment","Patience","Subject Expertise","Technology","Mentoring"],
    "Architect":               ["AutoCAD","3D Modeling","Structural Engineering","Urban Planning","Creativity","Project Management","Building Codes","Sustainability"],
    "Mechanical Engineer":     ["CAD Software","Thermodynamics","Materials Science","Prototyping","MATLAB","Manufacturing","Problem Solving","Technical Drawing"],
    "Civil Engineer":          ["Structural Analysis","AutoCAD","Project Management","Geotechnical Engineering","Building Codes","Mathematics","Safety Standards","Reporting"],
    "Research Scientist":      ["Research Design","Statistical Analysis","Scientific Writing","Lab Techniques","Critical Thinking","Grant Writing","Data Analysis","Peer Review"],
    "HR Manager":              ["Recruitment","Employee Relations","Performance Management","Labor Law","Communication","Training","HRIS Systems","Conflict Resolution"],
    "Content Creator":         ["Content Strategy","Video Production","Writing","SEO","Social Media","Analytics","Storytelling","Adobe Premiere"],
    "Biotechnologist":         ["Molecular Biology","PCR","Cell Culture","CRISPR","Data Analysis","Lab Safety","Scientific Writing","Bioinformatics"],
    "Environmental Scientist": ["Environmental Assessment","GIS","Field Research","Data Analysis","Report Writing","Ecology","Policy Knowledge","Statistical Analysis"],
    "Entrepreneur":            ["Business Strategy","Financial Literacy","Leadership","Sales","Networking","Product Development","Risk Management","Resilience"],
    "Business Consultant":     ["Strategic Analysis","Problem Solving","Data Analysis","Presentation","Project Management","Industry Knowledge","Communication","Change Management"],
    "Supply Chain Manager":    ["Logistics Management","ERP Systems","Data Analysis","Vendor Management","Inventory Control","Process Optimization","Negotiation","Risk Management"],
}

BLS_FALLBACK = {
    "Software Engineer":       {"annual_salary":130160,"total_employment":1847900},
    "Data Scientist":          {"annual_salary":108020,"total_employment":192000},
    "AI/ML Engineer":          {"annual_salary":136620,"total_employment":31000},
    "UX Designer":             {"annual_salary":95640, "total_employment":91770},
    "Graphic Designer":        {"annual_salary":58910, "total_employment":253000},
    "Product Manager":         {"annual_salary":169510,"total_employment":482000},
    "Cybersecurity Analyst":   {"annual_salary":102600,"total_employment":168900},
    "Marketing Manager":       {"annual_salary":171520,"total_employment":384980},
    "Financial Analyst":       {"annual_salary":83660, "total_employment":371920},
    "Doctor":                  {"annual_salary":229300,"total_employment":756800},
    "Psychologist":            {"annual_salary":81040, "total_employment":181600},
    "Lawyer":                  {"annual_salary":145760,"total_employment":813900},
    "Educator":                {"annual_salary":84380, "total_employment":1394000},
    "Architect":               {"annual_salary":93310, "total_employment":128830},
    "Mechanical Engineer":     {"annual_salary":96310, "total_employment":303400},
    "Civil Engineer":          {"annual_salary":88050, "total_employment":329800},
    "Research Scientist":      {"annual_salary":99490, "total_employment":136400},
    "HR Manager":              {"annual_salary":136350,"total_employment":185400},
    "Content Creator":         {"annual_salary":73690, "total_employment":165000},
    "Biotechnologist":         {"annual_salary":102270,"total_employment":37400},
    "Environmental Scientist": {"annual_salary":76480, "total_employment":97000},
    "Entrepreneur":            {"annual_salary":129420,"total_employment":3240000},
    "Business Consultant":     {"annual_salary":99410, "total_employment":1000000},
    "Supply Chain Manager":    {"annual_salary":99600, "total_employment":182800},
}


# ─────────────────────────────────────────
# LOADERS
# ─────────────────────────────────────────
def load_onet():
    print("\n📂 Loading O*NET...")
    try:
        interests   = pd.read_csv('onet_data/Interests.txt', sep='\t')
        skills      = pd.read_csv('onet_data/Skills.txt', sep='\t')
        occupations = pd.read_csv('onet_data/Occupation Data.txt', sep='\t')
        print(f"✅ Interests:{len(interests)} Skills:{len(skills)} Occupations:{len(occupations)}")
        return interests, skills, occupations, True
    except Exception as e:
        print(f"⚠️  {e} — using fallback RIASEC")
        return None, None, None, False


def build_riasec_table(interests, occupations):
    riasec = interests[interests['Scale ID'] == 'OI']
    pivot  = riasec.pivot_table(index='O*NET-SOC Code', columns='Element Name', values='Data Value', aggfunc='mean').reset_index()
    pivot  = pivot.merge(occupations[['O*NET-SOC Code','Title']], on='O*NET-SOC Code', how='left')
    pivot['career'] = pivot['Title'].apply(lambda t: next((v for k,v in TARGET_CAREERS.items() if not pd.isna(t) and k.lower() in str(t).lower()), None))
    pivot  = pivot.dropna(subset=['career'])
    for c in RIASEC_COLS:
        if c not in pivot.columns: pivot[c] = 3.0
    return pivot.dropna(subset=RIASEC_COLS)


def get_onet_skills(skills, occupations, career):
    kws   = [k for k,v in TARGET_CAREERS.items() if v == career]
    codes = occupations[occupations['Title'].apply(lambda t: any(k.lower() in str(t).lower() for k in kws))]['O*NET-SOC Code'].tolist()
    if not codes: return DEFAULT_SKILLS.get(career, [])
    top = skills[skills['O*NET-SOC Code'].isin(codes)].groupby('Element Name')['Data Value'].mean().sort_values(ascending=False).head(8).index.tolist()
    return top if top else DEFAULT_SKILLS.get(career, [])


def load_bls():
    print("\n📂 Loading BLS (all_data_M_2024.xlsx)...")
    BLS_MAP = {
        "Software Engineer":       "Software Developers",
        "Data Scientist":          "Data Scientists",
        "AI/ML Engineer":          "Computer and Information Research Scientists",
        "UX Designer":             "Web Developers",
        "Graphic Designer":        "Graphic Designers",
        "Product Manager":         "Computer and Information Systems Managers",
        "Cybersecurity Analyst":   "Information Security Analysts",
        "Marketing Manager":       "Marketing Managers",
        "Financial Analyst":       "Financial Analysts",
        "Doctor":                  "Physicians",
        "Psychologist":            "Psychologists",
        "Lawyer":                  "Lawyers",
        "Educator":                "Postsecondary Teachers",
        "Architect":               "Architects",
        "Mechanical Engineer":     "Mechanical Engineers",
        "Civil Engineer":          "Civil Engineers",
        "Research Scientist":      "Medical Scientists",
        "HR Manager":              "Human Resources Managers",
        "Content Creator":         "Writers and Authors",
        "Biotechnologist":         "Biochemists and Biophysicists",
        "Environmental Scientist": "Environmental Scientists",
        "Entrepreneur":            "General and Operations Managers",
        "Business Consultant":     "Management Analysts",
        "Supply Chain Manager":    "Logisticians",
    }
    try:
        bls = pd.read_excel('all_data_M_2024.xlsx')
        bls.columns = bls.columns.str.strip()
        if 'O_GROUP' in bls.columns:
            bls = bls[bls['O_GROUP'] == 'detailed']
        bls['A_MEAN']  = pd.to_numeric(bls['A_MEAN'],  errors='coerce')
        bls['TOT_EMP'] = pd.to_numeric(bls['TOT_EMP'], errors='coerce')
        bls = bls.dropna(subset=['A_MEAN'])
        result = {}
        for career, keyword in BLS_MAP.items():
            match = bls[bls['OCC_TITLE'].str.contains(keyword, case=False, na=False)]
            if len(match) > 0:
                result[career] = {
                    "annual_salary":    int(match['A_MEAN'].iloc[0]),
                    "total_employment": int(match['TOT_EMP'].iloc[0]) if not pd.isna(match['TOT_EMP'].iloc[0]) else 0
                }
        print(f"✅ BLS matched: {len(result)} careers")
        return result
    except Exception as e:
        print(f"⚠️  {e} — using fallback salaries")
        return BLS_FALLBACK


# ─────────────────────────────────────────
# FEATURE HELPERS
# ─────────────────────────────────────────
def get_skill_score(career, skill):
    high = {
        "math":   ["Software Engineer","Data Scientist","AI/ML Engineer","Financial Analyst","Research Scientist","Mechanical Engineer","Civil Engineer","Cybersecurity Analyst","Biotechnologist"],
        "comm":   ["Lawyer","Educator","HR Manager","Marketing Manager","Content Creator","Business Consultant","Doctor","Psychologist","Product Manager"],
        "tech":   ["Software Engineer","AI/ML Engineer","Cybersecurity Analyst","Data Scientist","Mechanical Engineer","Civil Engineer","Biotechnologist"],
        "design": ["Graphic Designer","UX Designer","Architect","Content Creator"],
    }
    med = {
        "math":   ["Doctor","Architect","Environmental Scientist","Product Manager","Business Consultant","Supply Chain Manager"],
        "comm":   ["Software Engineer","Data Scientist","UX Designer","Research Scientist","Environmental Scientist","Supply Chain Manager","Financial Analyst"],
        "tech":   ["UX Designer","Product Manager","Environmental Scientist","Research Scientist","Supply Chain Manager","Architect"],
        "design": ["Marketing Manager","Product Manager","Educator","Entrepreneur","Software Engineer"],
    }
    if career in high.get(skill,[]): return int(np.random.choice([4,5],p=[0.4,0.6]))
    if career in med.get(skill,[]):  return int(np.random.choice([3,4],p=[0.5,0.5]))
    return int(np.random.choice([1,2,3],p=[0.3,0.5,0.2]))


def get_pref(career, pref):
    prefs = {
        "env":    {"Office":["Financial Analyst","Lawyer","HR Manager","Business Consultant","Marketing Manager"],"Remote":["Software Engineer","Data Scientist","Content Creator","AI/ML Engineer","Graphic Designer"],"Lab":["Research Scientist","Biotechnologist","Doctor","Environmental Scientist"],"Outdoor":["Civil Engineer","Environmental Scientist"],"Flexible":["Product Manager","UX Designer","Educator","Entrepreneur","Psychologist","Supply Chain Manager","Mechanical Engineer","Architect"]},
        "team":   {"Solo":["Research Scientist","Content Creator","Graphic Designer","Cybersecurity Analyst"],"Small (2-5)":["Software Engineer","Data Scientist","UX Designer","AI/ML Engineer","Biotechnologist"],"Medium (6-20)":["Product Manager","Marketing Manager","Architect","Mechanical Engineer","Civil Engineer"],"Large (20+)":["Doctor","HR Manager","Business Consultant","Supply Chain Manager","Educator","Lawyer","Entrepreneur","Financial Analyst","Psychologist","Environmental Scientist"]},
        "risk":   {"Low":["Doctor","Lawyer","Civil Engineer","Financial Analyst","Research Scientist","Educator"],"Medium":["Software Engineer","Data Scientist","Marketing Manager","HR Manager","UX Designer","Psychologist","Environmental Scientist","Mechanical Engineer","Biotechnologist"],"High":["Entrepreneur","Content Creator","AI/ML Engineer","Cybersecurity Analyst","Product Manager","Business Consultant","Architect","Supply Chain Manager","Graphic Designer"]},
        "pace":   {"Slow and steady":["Research Scientist","Biotechnologist","Environmental Scientist","Educator"],"Moderate":["Doctor","Lawyer","Financial Analyst","Civil Engineer","Mechanical Engineer","HR Manager","Architect","Psychologist"],"Fast-paced":["Software Engineer","AI/ML Engineer","Cybersecurity Analyst","Marketing Manager","Entrepreneur","Product Manager","Supply Chain Manager","Business Consultant"],"Varies":["Content Creator","UX Designer","Data Scientist","Graphic Designer"]},
        "values": {"High salary":["Financial Analyst","Lawyer","Software Engineer","Business Consultant","AI/ML Engineer"],"Making impact":["Doctor","Educator","Psychologist","Environmental Scientist","Biotechnologist","Research Scientist"],"Creative freedom":["Graphic Designer","UX Designer","Content Creator","Architect","Entrepreneur"],"Job stability":["Civil Engineer","Mechanical Engineer","HR Manager","Supply Chain Manager"],"Fame/recognition":["Marketing Manager","Content Creator","Entrepreneur","Product Manager"]},
        "prefers":{"People":["Doctor","Psychologist","HR Manager","Educator","Lawyer","Marketing Manager"],"Data":["Data Scientist","Financial Analyst","Research Scientist","AI/ML Engineer","Cybersecurity Analyst"],"Ideas":["Software Engineer","Architect","Entrepreneur","Business Consultant","Product Manager","UX Designer"],"Physical things":["Mechanical Engineer","Civil Engineer","Biotechnologist","Environmental Scientist"],"Mix of all":["Content Creator","Graphic Designer","Supply Chain Manager"]},
        "indoor": {"Strongly indoor":["Software Engineer","Data Scientist","Financial Analyst","AI/ML Engineer","Cybersecurity Analyst","Graphic Designer","Content Creator","HR Manager"],"Mostly indoor":["Doctor","Lawyer","Research Scientist","Biotechnologist","Educator","Psychologist","Product Manager","Marketing Manager","Business Consultant","UX Designer","Supply Chain Manager"],"Both equally":["Architect","Mechanical Engineer","Civil Engineer","Environmental Scientist","Entrepreneur"],"Mostly outdoor":["Civil Engineer","Environmental Scientist"],"Strongly outdoor":[]},
    }
    for val, careers in prefs[pref].items():
        if career in careers: return val
    return list(prefs[pref].keys())[0]


def get_subject(career):
    if career in ["Software Engineer","Data Scientist","AI/ML Engineer","Research Scientist","Doctor","Biotechnologist","Environmental Scientist","Mechanical Engineer","Civil Engineer"]: return "Science/Math"
    if career in ["Graphic Designer","Content Creator","Educator","Psychologist","Lawyer","UX Designer"]: return "Arts/Humanities"
    if career in ["Financial Analyst","Marketing Manager","HR Manager","Business Consultant","Supply Chain Manager","Entrepreneur","Product Manager"]: return "Commerce/Business"
    return "Mixed"


def get_coding(career):
    if career in ["Software Engineer","AI/ML Engineer"]: return "Expert"
    if career in ["Data Scientist","Cybersecurity Analyst"]: return "Advanced"
    if career in ["Product Manager","UX Designer","Research Scientist","Biotechnologist"]: return "Intermediate"
    if career in ["Marketing Manager","Financial Analyst","Environmental Scientist","Supply Chain Manager"]: return "Basic"
    return "Never"


def build_rows(career, riasec_base, n=50):
    """Build n rows with TEXT VARIATION to prevent overfitting"""
    text = TEXT_PROFILES.get(career, TEXT_PROFILES["Software Engineer"])
    n_vars = len(text["problems"])
    rows = []

    for i in range(n):
        scores = np.clip(np.array(riasec_base) + np.random.normal(0, 0.5, 6), 1, 7)

        # KEY FIX: rotate through 5 different text answers
        idx = i % n_vars

        rows.append({
            "career":           career,
            "Q1_realistic":     round(scores[0],2),
            "Q2_investigative": round(scores[1],2),
            "Q3_artistic":      round(scores[2],2),
            "Q4_social":        round(scores[3],2),
            "Q5_enterprising":  round(scores[4],2),
            "Q6_conventional":  round(scores[5],2),
            "Q7_math":          get_skill_score(career,"math"),
            "Q8_communication": get_skill_score(career,"comm"),
            "Q9_technical":     get_skill_score(career,"tech"),
            "Q10_design":       get_skill_score(career,"design"),
            "Q11_work_env":     get_pref(career,"env"),
            "Q12_team_size":    get_pref(career,"team"),
            "Q13_risk":         get_pref(career,"risk"),
            "Q14_pace":         get_pref(career,"pace"),
            "Q15_values":       get_pref(career,"values"),
            "Q16_prefers":      get_pref(career,"prefers"),
            "Q17_balance":      np.random.choice(["Extremely","Very","Somewhat","Not"],p=[0.3,0.4,0.2,0.1]),
            "Q18_education":    np.random.choice(["HighSchool","Pursuing","Bachelors","Masters","PhD"],p=[0.05,0.25,0.40,0.20,0.10]),
            "Q19_subjects":     get_subject(career),
            "Q20_coding":       get_coding(career),
            "Q21_indoor":       get_pref(career,"indoor"),
            "Q22_age":          np.random.choice(["Under 18","18-22","23-27","28-35","35+"],p=[0.05,0.35,0.35,0.20,0.05]),
            # 5 DIFFERENT text answers rotating per row
            "Q23_problem_text": text["problems"][idx],
            "Q24_dream_text":   text["dreams"][idx],
            "Q25_skill_text":   text["skills"][idx],
        })
    return rows


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
def main():
    print("="*55)
    print("  CAREER DATASET BUILDER (Fixed - No Overfitting)")
    print("="*55)

    interests, skills, occupations, onet_ok = load_onet()
    bls_data = load_bls()

    if onet_ok:
        riasec_table = build_riasec_table(interests, occupations)
    else:
        riasec_table = pd.DataFrame([{"career":c,**dict(zip(RIASEC_COLS,v))} for c,v in FALLBACK_RIASEC.items()])

    print("\n🏗️  Building rows with text variation...")
    all_rows, skills_ref = [], {}

    for career in set(TARGET_CAREERS.values()):
        match = riasec_table[riasec_table['career']==career]
        riasec_base = match[RIASEC_COLS].mean().tolist() if len(match)>0 else FALLBACK_RIASEC.get(career,[3.0]*6)
        source = "O*NET" if len(match)>0 else "Estimated"

        career_skills = get_onet_skills(skills, occupations, career) if onet_ok else DEFAULT_SKILLS.get(career,[])
        skills_ref[career] = career_skills

        # 50 rows per career = 1200 total
        rows = build_rows(career, riasec_base, n=50)
        bls  = bls_data.get(career, {"annual_salary":80000,"total_employment":50000})
        for r in rows:
            r["annual_salary"]    = bls["annual_salary"]
            r["total_employment"] = bls["total_employment"]

        all_rows.extend(rows)
        print(f"  ✅ {career:<30} {source} | ${bls['annual_salary']:,}/yr")

    df = pd.DataFrame(all_rows).sample(frac=1,random_state=42).reset_index(drop=True)
    df['required_skills'] = df['career'].map(lambda c:" | ".join(skills_ref.get(c,[])))

    df.to_csv("model_artifacts/career_master_dataset.csv", index=False)
    with open("model_artifacts/career_skills_reference.json","w") as f:
        json.dump(skills_ref, f, indent=2)

    print(f"\n{'='*55}")
    print(f"  ✅ Dataset saved!")
    print(f"  Rows:    {len(df)}")
    print(f"  Careers: {df['career'].nunique()}")
    print(f"  Text variations: 5 per career (fixes overfitting)")
    print(f"\n  Next → python train_model.py")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()