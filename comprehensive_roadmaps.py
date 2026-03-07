"""
Comprehensive Roadmap Data - roadmap.sh style with nodes
Visual learning paths for all 24 ML careers with clickable nodes
"""

def get_roadmap(career_key):
    """Get detailed node-based roadmap for any career"""
    original_key = career_key
    career_key = career_key.lower().replace(' ', '_').replace('/', '_').replace('-', '_')
    
    roadmap_map = {
        "ai_ml_engineer": generate_ai_ml_roadmap,
        "aiml_engineer": generate_ai_ml_roadmap,
        "software_engineer": generate_software_engineer_roadmap,
        "software_developer": generate_software_engineer_roadmap,
        "data_scientist": generate_data_scientist_roadmap,
        "ux_designer": generate_ux_designer_roadmap,
        "ui_ux_designer": generate_ux_designer_roadmap,
        "cybersecurity_analyst": generate_cybersecurity_roadmap,
        "cyber_security_analyst": generate_cybersecurity_roadmap,
        "product_manager": generate_product_manager_roadmap,
        "marketing_manager": generate_marketing_manager_roadmap,
        "financial_analyst": generate_financial_analyst_roadmap,
        "graphic_designer": generate_graphic_designer_roadmap,
        "content_creator": generate_content_creator_roadmap,
        "entrepreneur": generate_entrepreneur_roadmap,
        "hr_manager": generate_hr_manager_roadmap,
        "human_resources_manager": generate_hr_manager_roadmap,
        "business_consultant": generate_business_consultant_roadmap,
        "mechanical_engineer": generate_mechanical_engineer_roadmap,
        "civil_engineer": generate_civil_engineer_roadmap,
        "architect": generate_architect_roadmap,
        "biotechnologist": generate_biotechnologist_roadmap,
        "environmental_scientist": generate_environmental_scientist_roadmap,
        "doctor": generate_doctor_roadmap,
        "educator": generate_educator_roadmap,
        "psychologist": generate_psychologist_roadmap,
        "lawyer": generate_lawyer_roadmap,
        "research_scientist": generate_research_scientist_roadmap,
        "supply_chain_manager": generate_supply_chain_manager_roadmap,
    }
    
    roadmap_func = roadmap_map.get(career_key)
    if roadmap_func:
        return roadmap_func()
    return generate_default_roadmap(original_key)


def generate_ai_ml_roadmap():
    return {
        "name": "AI/ML Engineer",
        "description": "Complete roadmap to become an AI/ML Engineer with hands-on projects",
        "nodes": [
            # Python Fundamentals
            {"id": "python", "title": "Python Basics", "type": "topic", "description": "Master Python programming fundamentals", "position": {"x": 50, "y": 5}, "children": ["python-syntax", "data-structures"]},
            {"id": "python-syntax", "title": "Syntax & Variables", "type": "subtopic", "description": "Variables, data types, operators", "position": {"x": 40, "y": 12}, "children": ["data-structures"]},
            {"id": "data-structures", "title": "Data Structures", "type": "subtopic", "description": "Lists, dicts, sets, tuples", "position": {"x": 60, "y": 12}, "children": ["numpy"]},
            
            # NumPy & Pandas
            {"id": "numpy", "title": "NumPy", "type": "topic", "description": "Numerical computing with arrays", "position": {"x": 50, "y": 20}, "children": ["arrays", "pandas"]},
            {"id": "arrays", "title": "Array Operations", "type": "subtopic", "description": "Creating, indexing, slicing arrays", "position": {"x": 40, "y": 27}, "children": ["pandas"]},
            {"id": "pandas", "title": "Pandas", "type": "topic", "description": "Data manipulation and analysis", "position": {"x": 60, "y": 27}, "children": ["dataframes", "data-cleaning"]},
            {"id": "dataframes", "title": "DataFrames", "type": "subtopic", "description": "Working with tabular data", "position": {"x": 50, "y": 34}, "children": ["data-cleaning"]},
            {"id": "data-cleaning", "title": "Data Cleaning", "type": "subtopic", "description": "Handling missing data, outliers", "position": {"x": 70, "y": 34}, "children": ["math"]},
            
            # Mathematics
            {"id": "math", "title": "Mathematics", "type": "topic", "description": "Essential math for ML", "position": {"x": 50, "y": 42}, "children": ["linear-algebra", "statistics"]},
            {"id": "linear-algebra", "title": "Linear Algebra", "type": "subtopic", "description": "Vectors, matrices, operations", "position": {"x": 40, "y": 49}, "children": ["ml-basics"]},
            {"id": "statistics", "title": "Statistics", "type": "subtopic", "description": "Probability, distributions, hypothesis testing", "position": {"x": 60, "y": 49}, "children": ["ml-basics"]},
            
            # Machine Learning Basics
            {"id": "ml-basics", "title": "ML Fundamentals", "type": "topic", "description": "Core machine learning concepts", "position": {"x": 50, "y": 57}, "children": ["supervised", "unsupervised"]},
            {"id": "supervised", "title": "Supervised Learning", "type": "subtopic", "description": "Regression, classification algorithms", "position": {"x": 35, "y": 64}, "children": ["regression", "classification"]},
            {"id": "regression", "title": "Regression", "type": "subtopic", "description": "Linear, polynomial, ridge, lasso", "position": {"x": 25, "y": 71}, "children": ["sklearn"]},
            {"id": "classification", "title": "Classification", "type": "subtopic", "description": "Logistic regression, decision trees, SVM", "position": {"x": 45, "y": 71}, "children": ["sklearn"]},
            {"id": "unsupervised", "title": "Unsupervised Learning", "type": "subtopic", "description": "Clustering, dimensionality reduction", "position": {"x": 65, "y": 64}, "children": ["clustering", "pca"]},
            {"id": "clustering", "title": "Clustering", "type": "subtopic", "description": "K-means, DBSCAN, hierarchical", "position": {"x": 60, "y": 71}, "children": ["sklearn"]},
            {"id": "pca", "title": "PCA", "type": "subtopic", "description": "Principal Component Analysis", "position": {"x": 70, "y": 71}, "children": ["sklearn"]},
            
            # Scikit-learn
            {"id": "sklearn", "title": "Scikit-learn", "type": "topic", "description": "ML library for Python", "position": {"x": 50, "y": 79}, "children": ["model-training", "evaluation"]},
            {"id": "model-training", "title": "Model Training", "type": "subtopic", "description": "fit, predict, train-test split", "position": {"x": 40, "y": 86}, "children": ["evaluation"]},
            {"id": "evaluation", "title": "Model Evaluation", "type": "subtopic", "description": "Accuracy, precision, recall, F1, ROC-AUC", "position": {"x": 60, "y": 86}, "children": ["deep-learning"]},
            
            # Deep Learning
            {"id": "deep-learning", "title": "Deep Learning", "type": "topic", "description": "Neural networks and deep learning", "position": {"x": 50, "y": 94}, "children": ["neural-nets", "frameworks"]},
            {"id": "neural-nets", "title": "Neural Networks", "type": "subtopic", "description": "Perceptrons, activation functions, backprop", "position": {"x": 35, "y": 101}, "children": ["frameworks"]},
            {"id": "frameworks", "title": "DL Frameworks", "type": "subtopic", "description": "TensorFlow, PyTorch, Keras", "position": {"x": 65, "y": 101}, "children": ["tensorflow", "pytorch"]},
            {"id": "tensorflow", "title": "TensorFlow", "type": "optional", "description": "Google's ML framework", "position": {"x": 55, "y": 108}, "children": ["cnn"]},
            {"id": "pytorch", "title": "PyTorch", "type": "optional", "description": "Facebook's ML framework", "position": {"x": 75, "y": 108}, "children": ["cnn"]},
            
            # Computer Vision
            {"id": "cnn", "title": "CNNs", "type": "topic", "description": "Convolutional Neural Networks", "position": {"x": 35, "y": 116}, "children": ["conv-layers", "transfer-learning"]},
            {"id": "conv-layers", "title": "Conv Layers", "type": "subtopic", "description": "Convolution, pooling, padding", "position": {"x": 30, "y": 123}, "children": ["transfer-learning"]},
            {"id": "transfer-learning", "title": "Transfer Learning", "type": "subtopic", "description": "ResNet, VGG, EfficientNet", "position": {"x": 40, "y": 123}, "children": ["nlp"]},
            
            # NLP
            {"id": "nlp", "title": "NLP", "type": "topic", "description": "Natural Language Processing", "position": {"x": 65, "y": 116}, "children": ["text-processing", "transformers"]},
            {"id": "text-processing", "title": "Text Processing", "type": "subtopic", "description": "Tokenization, embeddings, word2vec", "position": {"x": 60, "y": 123}, "children": ["transformers"]},
            {"id": "transformers", "title": "Transformers", "type": "subtopic", "description": "BERT, GPT, attention mechanism", "position": {"x": 70, "y": 123}, "children": ["mlops"]},
            
            # MLOps
            {"id": "mlops", "title": "MLOps", "type": "topic", "description": "ML model deployment and operations", "position": {"x": 50, "y": 131}, "children": ["docker", "apis"]},
            {"id": "docker", "title": "Docker", "type": "subtopic", "description": "Containerization for ML apps", "position": {"x": 40, "y": 138}, "children": ["deployment"]},
            {"id": "apis", "title": "REST APIs", "type": "subtopic", "description": "FastAPI, Flask for model serving", "position": {"x": 60, "y": 138}, "children": ["deployment"]},
            {"id": "deployment", "title": "Cloud Deployment", "type": "milestone", "description": "Deploy ML models to AWS, GCP, Azure", "position": {"x": 50, "y": 145}, "children": ["capstone"]},
            
            # Capstone
            {"id": "capstone", "title": "Capstone Project", "type": "milestone", "description": "Build and deploy end-to-end ML project", "position": {"x": 50, "y": 153}, "children": []},
        ]
    }


def generate_software_engineer_roadmap():
    return {
        "name": "Software Engineer",
        "description": "Complete roadmap to become a Software Engineer",
        "nodes": [
            # Programming Basics
            {"id": "programming", "title": "Programming Basics", "type": "topic", "description": "Learn programming fundamentals", "position": {"x": 50, "y": 5}, "children": ["variables", "control-flow"]},
            {"id": "variables", "title": "Variables & Types", "type": "subtopic", "description": "Data types, variables, operators", "position": {"x": 40, "y": 12}, "children": ["control-flow"]},
            {"id": "control-flow", "title": "Control Flow", "type": "subtopic", "description": "if/else, loops, functions", "position": {"x": 60, "y": 12}, "children": ["data-structures"]},
            
            # Data Structures
            {"id": "data-structures", "title": "Data Structures", "type": "topic", "description": "Essential data structures", "position": {"x": 50, "y": 20}, "children": ["arrays", "linked-lists", "trees"]},
            {"id": "arrays", "title": "Arrays", "type": "subtopic", "description": "Arrays, dynamic arrays", "position": {"x": 30, "y": 27}, "children": ["algorithms"]},
            {"id": "linked-lists", "title": "Linked Lists", "type": "subtopic", "description": "Singly, doubly linked lists", "position": {"x": 50, "y": 27}, "children": ["algorithms"]},
            {"id": "trees", "title": "Trees & Graphs", "type": "subtopic", "description": "Binary trees, BST, graphs", "position": {"x": 70, "y": 27}, "children": ["algorithms"]},
            
            # Algorithms
            {"id": "algorithms", "title": "Algorithms", "type": "topic", "description": "Common algorithms", "position": {"x": 50, "y": 35}, "children": ["sorting", "searching", "recursion"]},
            {"id": "sorting", "title": "Sorting", "type": "subtopic", "description": "Quick, merge, heap sort", "position": {"x": 35, "y": 42}, "children": ["oop"]},
            {"id": "searching", "title": "Searching", "type": "subtopic", "description": "Binary search, DFS, BFS", "position": {"x": 50, "y": 42}, "children": ["oop"]},
            {"id": "recursion", "title": "Recursion", "type": "subtopic", "description": "Recursive algorithms, dynamic programming", "position": {"x": 65, "y": 42}, "children": ["oop"]},
            
            # OOP
            {"id": "oop", "title": "OOP", "type": "topic", "description": "Object-Oriented Programming", "position": {"x": 50, "y": 50}, "children": ["classes", "inheritance", "polymorphism"]},
            {"id": "classes", "title": "Classes & Objects", "type": "subtopic", "description": "Classes, objects, methods", "position": {"x": 35, "y": 57}, "children": ["web-basics"]},
            {"id": "inheritance", "title": "Inheritance", "type": "subtopic", "description": "Inheritance, composition", "position": {"x": 50, "y": 57}, "children": ["web-basics"]},
            {"id": "polymorphism", "title": "Polymorphism", "type": "subtopic", "description": "Polymorphism, interfaces", "position": {"x": 65, "y": 57}, "children": ["web-basics"]},
            
            # Web Development
            {"id": "web-basics", "title": "Web Basics", "type": "topic", "description": "HTML, CSS, JavaScript", "position": {"x": 50, "y": 65}, "children": ["html", "css", "javascript"]},
            {"id": "html", "title": "HTML", "type": "subtopic", "description": "HTML5, semantic HTML", "position": {"x": 35, "y": 72}, "children": ["frontend"]},
            {"id": "css", "title": "CSS", "type": "subtopic", "description": "CSS3, flexbox, grid", "position": {"x": 50, "y": 72}, "children": ["frontend"]},
            {"id": "javascript", "title": "JavaScript", "type": "subtopic", "description": "ES6+, DOM, async/await", "position": {"x": 65, "y": 72}, "children": ["frontend"]},
            
            # Frontend Framework
            {"id": "frontend", "title": "Frontend Framework", "type": "topic", "description": "React, Vue, or Angular", "position": {"x": 35, "y": 80}, "children": ["react", "state-mgmt"]},
            {"id": "react", "title": "React", "type": "optional", "description": "Components, hooks, JSX", "position": {"x": 30, "y": 87}, "children": ["backend"]},
            {"id": "state-mgmt", "title": "State Management", "type": "subtopic", "description": "Redux, Context API", "position": {"x": 40, "y": 87}, "children": ["backend"]},
            
            # Backend
            {"id": "backend", "title": "Backend Development", "type": "topic", "description": "Server-side programming", "position": {"x": 65, "y": 80}, "children": ["nodejs", "apis"]},
            {"id": "nodejs", "title": "Node.js/Python", "type": "subtopic", "description": "Express, Flask, FastAPI", "position": {"x": 60, "y": 87}, "children": ["databases"]},
            {"id": "apis", "title": "REST APIs", "type": "subtopic", "description": "RESTful design, HTTP methods", "position": {"x": 70, "y": 87}, "children": ["databases"]},
            
            # Databases
            {"id": "databases", "title": "Databases", "type": "topic", "description": "SQL and NoSQL databases", "position": {"x": 50, "y": 95}, "children": ["sql", "nosql"]},
            {"id": "sql", "title": "SQL", "type": "subtopic", "description": "PostgreSQL, MySQL, queries", "position": {"x": 40, "y": 102}, "children": ["git"]},
            {"id": "nosql", "title": "NoSQL", "type": "subtopic", "description": "MongoDB, Redis, Firebase", "position": {"x": 60, "y": 102}, "children": ["git"]},
            
            # Version Control
            {"id": "git", "title": "Git & GitHub", "type": "topic", "description": "Version control system", "position": {"x": 50, "y": 110}, "children": ["git-basics", "github"]},
            {"id": "git-basics", "title": "Git Basics", "type": "subtopic", "description": "commit, push, pull, branch", "position": {"x": 40, "y": 117}, "children": ["testing"]},
            {"id": "github", "title": "GitHub", "type": "subtopic", "description": "Pull requests, code review", "position": {"x": 60, "y": 117}, "children": ["testing"]},
            
            # Testing
            {"id": "testing", "title": "Testing", "type": "topic", "description": "Unit, integration, E2E testing", "position": {"x": 50, "y": 125}, "children": ["unit-tests", "integration-tests"]},
            {"id": "unit-tests", "title": "Unit Testing", "type": "subtopic", "description": "Jest, pytest, unittest", "position": {"x": 40, "y": 132}, "children": ["devops"]},
            {"id": "integration-tests", "title": "Integration Testing", "type": "subtopic", "description": "API testing, E2E testing", "position": {"x": 60, "y": 132}, "children": ["devops"]},
            
            # DevOps
            {"id": "devops", "title": "DevOps", "type": "topic", "description": "Deployment and CI/CD", "position": {"x": 50, "y": 140}, "children": ["docker", "cicd"]},
            {"id": "docker", "title": "Docker", "type": "subtopic", "description": "Containers, images, compose", "position": {"x": 40, "y": 147}, "children": ["deployment"]},
            {"id": "cicd", "title": "CI/CD", "type": "subtopic", "description": "GitHub Actions, Jenkins", "position": {"x": 60, "y": 147}, "children": ["deployment"]},
            {"id": "deployment", "title": "Cloud Deployment", "type": "milestone", "description": "Deploy to AWS, Heroku, Vercel", "position": {"x": 50, "y": 154}, "children": ["capstone"]},
            
            # Capstone
            {"id": "capstone", "title": "Full Stack Project", "type": "milestone", "description": "Build complete web application", "position": {"x": 50, "y": 162}, "children": []},
        ]
    }


def generate_career_roadmap_template(career_name, topics):
    """Generate a roadmap template for any career with custom topics"""
    nodes = []
    y_pos = 5
    node_id_counter = 0
    
    for i, topic in enumerate(topics):
        topic_id = f"topic-{node_id_counter}"
        node_id_counter += 1
        
        # Create main topic node
        children_ids = []
        for j in range(3):  # 3 subtopics per topic
            subtopic_id = f"subtopic-{node_id_counter}"
            children_ids.append(subtopic_id)
            node_id_counter += 1
        
        nodes.append({
            "id": topic_id,
            "title": topic,
            "type": "topic",
            "description": f"Learn {topic}",
            "position": {"x": 50, "y": y_pos},
            "children": children_ids
        })
        
        # Create subtopic nodes
        for j, subtopic_id in enumerate(children_ids):
            x_pos = 30 + (j * 20)
            next_topic_id = f"topic-{node_id_counter}" if i < len(topics) - 1 else None
            
            nodes.append({
                "id": subtopic_id,
                "title": f"{topic} - Part {j+1}",
                "type": "subtopic",
                "description": f"Master {topic} fundamentals - Part {j+1}",
                "position": {"x": x_pos, "y": y_pos + 7},
                "children": [next_topic_id] if next_topic_id and j == 1 else []
            })
        
        y_pos += 15
    
    # Add capstone project
    nodes.append({
        "id": "capstone",
        "title": "Capstone Project",
        "type": "milestone",
        "description": f"Complete {career_name} portfolio project",
        "position": {"x": 50, "y": y_pos},
        "children": []
    })
    
    return {
        "name": career_name,
        "description": f"Complete roadmap to become a {career_name}",
        "nodes": nodes
    }

# Data Scientist
def generate_data_scientist_roadmap():
    topics = ["Python & Statistics", "Data Analysis", "Machine Learning", "Data Visualization", "Big Data Tools", "ML Deployment"]
    return generate_career_roadmap_template("Data Scientist", topics)

# UX Designer
def generate_ux_designer_roadmap():
    topics = ["Design Principles", "User Research", "Wireframing", "Prototyping", "UI Design", "Usability Testing"]
    return generate_career_roadmap_template("UX Designer", topics)

# Cybersecurity Analyst
def generate_cybersecurity_roadmap():
    topics = ["Network Fundamentals", "Security Basics", "Ethical Hacking", "Penetration Testing", "Security Tools", "Incident Response"]
    return generate_career_roadmap_template("Cybersecurity Analyst", topics)

# Product Manager
def generate_product_manager_roadmap():
    topics = ["Product Strategy", "User Research", "Roadmap Planning", "Agile/Scrum", "Data Analysis", "Stakeholder Management"]
    return generate_career_roadmap_template("Product Manager", topics)

# Marketing Manager
def generate_marketing_manager_roadmap():
    topics = ["Marketing Fundamentals", "Digital Marketing", "SEO & SEM", "Social Media", "Analytics", "Campaign Management"]
    return generate_career_roadmap_template("Marketing Manager", topics)

# Financial Analyst
def generate_financial_analyst_roadmap():
    topics = ["Financial Accounting", "Financial Modeling", "Excel & Tools", "Valuation", "Financial Analysis", "Reporting"]
    return generate_career_roadmap_template("Financial Analyst", topics)

# Graphic Designer
def generate_graphic_designer_roadmap():
    topics = ["Design Principles", "Adobe Creative Suite", "Typography", "Color Theory", "Branding", "Portfolio Building"]
    return generate_career_roadmap_template("Graphic Designer", topics)

# Content Creator
def generate_content_creator_roadmap():
    topics = ["Content Strategy", "Writing Skills", "Video Production", "Social Media", "SEO", "Monetization"]
    return generate_career_roadmap_template("Content Creator", topics)

# Entrepreneur
def generate_entrepreneur_roadmap():
    topics = ["Business Fundamentals", "Market Research", "Business Planning", "Funding", "Product Development", "Growth Strategies"]
    return generate_career_roadmap_template("Entrepreneur", topics)

# HR Manager
def generate_hr_manager_roadmap():
    topics = ["HR Fundamentals", "Recruitment", "Employee Relations", "Performance Management", "HR Analytics", "Strategic HR"]
    return generate_career_roadmap_template("HR Manager", topics)

# Business Consultant
def generate_business_consultant_roadmap():
    topics = ["Business Analysis", "Strategy", "Problem Solving", "Data Analysis", "Client Management", "Presentation Skills"]
    return generate_career_roadmap_template("Business Consultant", topics)

# Mechanical Engineer
def generate_mechanical_engineer_roadmap():
    topics = ["Engineering Fundamentals", "CAD Software", "Thermodynamics", "Mechanics", "Materials Science", "Design Projects"]
    return generate_career_roadmap_template("Mechanical Engineer", topics)

# Civil Engineer
def generate_civil_engineer_roadmap():
    topics = ["Engineering Basics", "Structural Analysis", "CAD Tools", "Construction Management", "Materials", "Project Design"]
    return generate_career_roadmap_template("Civil Engineer", topics)

# Architect
def generate_architect_roadmap():
    topics = ["Architecture Fundamentals", "Design Principles", "CAD & BIM", "Building Codes", "Sustainability", "Portfolio"]
    return generate_career_roadmap_template("Architect", topics)

# Biotechnologist
def generate_biotechnologist_roadmap():
    topics = ["Biology Fundamentals", "Molecular Biology", "Lab Techniques", "Genetics", "Bioinformatics", "Research Methods"]
    return generate_career_roadmap_template("Biotechnologist", topics)

# Environmental Scientist
def generate_environmental_scientist_roadmap():
    topics = ["Environmental Science", "Ecology", "Research Methods", "Data Analysis", "Policy", "Sustainability"]
    return generate_career_roadmap_template("Environmental Scientist", topics)

# Doctor
def generate_doctor_roadmap():
    topics = ["Medical Fundamentals", "Anatomy & Physiology", "Pathology", "Clinical Skills", "Diagnostics", "Patient Care"]
    return generate_career_roadmap_template("Doctor", topics)

# Educator
def generate_educator_roadmap():
    topics = ["Teaching Fundamentals", "Curriculum Design", "Classroom Management", "Assessment", "Educational Technology", "Professional Development"]
    return generate_career_roadmap_template("Educator", topics)

# Psychologist
def generate_psychologist_roadmap():
    topics = ["Psychology Fundamentals", "Research Methods", "Clinical Psychology", "Counseling Techniques", "Assessment", "Ethics"]
    return generate_career_roadmap_template("Psychologist", topics)

# Lawyer
def generate_lawyer_roadmap():
    topics = ["Legal Fundamentals", "Contract Law", "Case Analysis", "Legal Research", "Court Procedures", "Legal Writing"]
    return generate_career_roadmap_template("Lawyer", topics)

# Research Scientist
def generate_research_scientist_roadmap():
    topics = ["Scientific Method", "Research Design", "Data Analysis", "Lab Techniques", "Publication", "Grant Writing"]
    return generate_career_roadmap_template("Research Scientist", topics)

# Supply Chain Manager
def generate_supply_chain_manager_roadmap():
    topics = ["Supply Chain Basics", "Logistics", "Inventory Management", "Procurement", "Analytics", "Strategy"]
    return generate_career_roadmap_template("Supply Chain Manager", topics)

# Default fallback
def generate_default_roadmap(career_key):
    career_name = career_key.replace('_', ' ').title()
    topics = ["Fundamentals", "Core Skills", "Advanced Topics", "Tools & Technologies", "Best Practices", "Real Projects"]
    return generate_career_roadmap_template(career_name, topics)
