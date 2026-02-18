f"""
Comprehensive Roadmap Data - roadmap.sh style
Contains detailed learning paths for each career track
"""

ROADMAPS = {
    "frontend_internship": {
        "name": "Frontend Development",
        "description": "Complete roadmap to become a Frontend Developer",
        "nodes": [
            # Internet & Web Basics
            {
                "id": "internet",
                "title": "Internet",
                "type": "topic",
                "description": "How does the internet work?",
                "position": {"x": 50, "y": 10},
                "children": ["http", "browsers", "dns", "domain"]
            },
            {
                "id": "http",
                "title": "HTTP/HTTPS",
                "type": "subtopic",
                "description": "Understanding HTTP protocol",
                "position": {"x": 30, "y": 20},
                "children": ["html"]
            },
            {
                "id": "browsers",
                "title": "Browsers",
                "type": "subtopic",
                "description": "How browsers work",
                "position": {"x": 50, "y": 20},
                "children": ["html"]
            },
            {
                "id": "dns",
                "title": "DNS",
                "type": "subtopic",
                "description": "Domain Name System",
                "position": {"x": 70, "y": 20},
                "children": ["html"]
            },
            {
                "id": "domain",
                "title": "Domain Names",
                "type": "subtopic",
                "description": "Understanding domains",
                "position": {"x": 90, "y": 20},
                "children": ["html"]
            },
            
            # HTML
            {
                "id": "html",
                "title": "HTML",
                "type": "topic",
                "description": "Learn HTML basics",
                "position": {"x": 50, "y": 30},
                "children": ["semantic-html", "forms", "accessibility", "seo"]
            },
            {
                "id": "semantic-html",
                "title": "Semantic HTML",
                "type": "subtopic",
                "description": "Meaningful HTML tags",
                "position": {"x": 30, "y": 40},
                "children": ["css"]
            },
            {
                "id": "forms",
                "title": "Forms & Validations",
                "type": "subtopic",
                "description": "HTML forms",
                "position": {"x": 50, "y": 40},
                "children": ["css"]
            },
            {
                "id": "accessibility",
                "title": "Accessibility",
                "type": "subtopic",
                "description": "Web accessibility basics",
                "position": {"x": 70, "y": 40},
                "children": ["css"]
            },
            {
                "id": "seo",
                "title": "SEO Basics",
                "type": "subtopic",
                "description": "Search Engine Optimization",
                "position": {"x": 90, "y": 40},
                "children": ["css"]
            },
            
            # CSS
            {
                "id": "css",
                "title": "CSS",
                "type": "topic",
                "description": "Learn CSS styling",
                "position": {"x": 50, "y": 50},
                "children": ["layouts", "responsive", "css-frameworks"]
            },
            {
                "id": "layouts",
                "title": "Layouts",
                "type": "subtopic",
                "description": "Flexbox, Grid, Positioning",
                "position": {"x": 30, "y": 60},
                "children": ["javascript"]
            },
            {
                "id": "responsive",
                "title": "Responsive Design",
                "type": "subtopic",
                "description": "Mobile-first design",
                "position": {"x": 50, "y": 60},
                "children": ["javascript"]
            },
            {
                "id": "css-frameworks",
                "title": "CSS Frameworks",
                "type": "optional",
                "description": "Tailwind, Bootstrap",
                "position": {"x": 70, "y": 60},
                "children": ["javascript"]
            },
            
            # JavaScript
            {
                "id": "javascript",
                "title": "JavaScript",
                "type": "topic",
                "description": "Learn JavaScript fundamentals",
                "position": {"x": 50, "y": 70},
                "children": ["dom", "fetch", "es6", "async"]
            },
            {
                "id": "dom",
                "title": "DOM Manipulation",
                "type": "subtopic",
                "description": "Working with the DOM",
                "position": {"x": 25, "y": 80},
                "children": ["version-control"]
            },
            {
                "id": "fetch",
                "title": "Fetch API",
                "type": "subtopic",
                "description": "Making HTTP requests",
                "position": {"x": 45, "y": 80},
                "children": ["version-control"]
            },
            {
                "id": "es6",
                "title": "ES6+ Features",
                "type": "subtopic",
                "description": "Modern JavaScript",
                "position": {"x": 65, "y": 80},
                "children": ["version-control"]
            },
            {
                "id": "async",
                "title": "Async JavaScript",
                "type": "subtopic",
                "description": "Promises, Async/Await",
                "position": {"x": 85, "y": 80},
                "children": ["version-control"]
            },
            
            # Version Control
            {
                "id": "version-control",
                "title": "Version Control",
                "type": "topic",
                "description": "Git & GitHub",
                "position": {"x": 50, "y": 90},
                "children": ["package-managers"]
            },
            
            # Package Managers
            {
                "id": "package-managers",
                "title": "Package Managers",
                "type": "topic",
                "description": "npm, yarn, pnpm",
                "position": {"x": 50, "y": 100},
                "children": ["react", "build-tools"]
            },
            
            # Build Tools
            {
                "id": "build-tools",
                "title": "Build Tools",
                "type": "optional",
                "description": "Vite, Webpack, Parcel",
                "position": {"x": 30, "y": 110},
                "children": ["testing"]
            },
            
            # React
            {
                "id": "react",
                "title": "React",
                "type": "topic",
                "description": "Learn React library",
                "position": {"x": 70, "y": 110},
                "children": ["components", "hooks", "routing"]
            },
            {
                "id": "components",
                "title": "Components",
                "type": "subtopic",
                "description": "React components",
                "position": {"x": 60, "y": 120},
                "children": ["state-management"]
            },
            {
                "id": "hooks",
                "title": "Hooks",
                "type": "subtopic",
                "description": "useState, useEffect, etc",
                "position": {"x": 75, "y": 120},
                "children": ["state-management"]
            },
            {
                "id": "routing",
                "title": "React Router",
                "type": "subtopic",
                "description": "Client-side routing",
                "position": {"x": 90, "y": 120},
                "children": ["state-management"]
            },
            
            # State Management
            {
                "id": "state-management",
                "title": "State Management",
                "type": "topic",
                "description": "Context API, Redux",
                "position": {"x": 75, "y": 130},
                "children": ["testing"]
            },
            
            # Testing
            {
                "id": "testing",
                "title": "Testing",
                "type": "topic",
                "description": "Jest, React Testing Library",
                "position": {"x": 50, "y": 140},
                "children": ["typescript", "deployment"]
            },
            
            # TypeScript
            {
                "id": "typescript",
                "title": "TypeScript",
                "type": "optional",
                "description": "Static typing for JavaScript",
                "position": {"x": 30, "y": 150},
                "children": ["portfolio"]
            },
            
            # Deployment
            {
                "id": "deployment",
                "title": "Deployment",
                "type": "topic",
                "description": "Vercel, Netlify, GitHub Pages",
                "position": {"x": 70, "y": 150},
                "children": ["portfolio"]
            },
            
            # Portfolio
            {
                "id": "portfolio",
                "title": "Build Portfolio",
                "type": "milestone",
                "description": "Create 3-5 projects",
                "position": {"x": 50, "y": 160},
                "children": []
            }
        ]
    },
    
    "backend_dsa": {
        "name": "Backend + DSA",
        "description": "Complete roadmap for Backend Development with DSA",
        "nodes": [
            # Programming Language
            {
                "id": "programming-lang",
                "title": "Programming Language",
                "type": "topic",
                "description": "Python, Java, or JavaScript",
                "position": {"x": 50, "y": 10},
                "children": ["oop", "data-structures"]
            },
            {
                "id": "oop",
                "title": "OOP Concepts",
                "type": "subtopic",
                "description": "Object-Oriented Programming",
                "position": {"x": 30, "y": 20},
                "children": ["data-structures"]
            },
            
            # Data Structures
            {
                "id": "data-structures",
                "title": "Data Structures",
                "type": "topic",
                "description": "Arrays, LinkedLists, Trees, Graphs",
                "position": {"x": 50, "y": 30},
                "children": ["arrays", "linked-lists", "trees", "graphs"]
            },
            {
                "id": "arrays",
                "title": "Arrays & Strings",
                "type": "subtopic",
                "description": "Array manipulation",
                "position": {"x": 25, "y": 40},
                "children": ["algorithms"]
            },
            {
                "id": "linked-lists",
                "title": "Linked Lists",
                "type": "subtopic",
                "description": "Singly, Doubly linked lists",
                "position": {"x": 45, "y": 40},
                "children": ["algorithms"]
            },
            {
                "id": "trees",
                "title": "Trees",
                "type": "subtopic",
                "description": "Binary trees, BST, AVL",
                "position": {"x": 65, "y": 40},
                "children": ["algorithms"]
            },
            {
                "id": "graphs",
                "title": "Graphs",
                "type": "subtopic",
                "description": "Graph representations",
                "position": {"x": 85, "y": 40},
                "children": ["algorithms"]
            },
            
            # Algorithms
            {
                "id": "algorithms",
                "title": "Algorithms",
                "type": "topic",
                "description": "Sorting, Searching, DP",
                "position": {"x": 50, "y": 50},
                "children": ["sorting", "searching", "dp", "greedy"]
            },
            {
                "id": "sorting",
                "title": "Sorting",
                "type": "subtopic",
                "description": "QuickSort, MergeSort",
                "position": {"x": 25, "y": 60},
                "children": ["databases"]
            },
            {
                "id": "searching",
                "title": "Searching",
                "type": "subtopic",
                "description": "Binary Search, BFS, DFS",
                "position": {"x": 45, "y": 60},
                "children": ["databases"]
            },
            {
                "id": "dp",
                "title": "Dynamic Programming",
                "type": "subtopic",
                "description": "DP patterns",
                "position": {"x": 65, "y": 60},
                "children": ["databases"]
            },
            {
                "id": "greedy",
                "title": "Greedy Algorithms",
                "type": "subtopic",
                "description": "Greedy approach",
                "position": {"x": 85, "y": 60},
                "children": ["databases"]
            },
            
            # Databases
            {
                "id": "databases",
                "title": "Databases",
                "type": "topic",
                "description": "SQL & NoSQL",
                "position": {"x": 50, "y": 70},
                "children": ["sql", "nosql"]
            },
            {
                "id": "sql",
                "title": "SQL",
                "type": "subtopic",
                "description": "PostgreSQL, MySQL",
                "position": {"x": 35, "y": 80},
                "children": ["apis"]
            },
            {
                "id": "nosql",
                "title": "NoSQL",
                "type": "subtopic",
                "description": "MongoDB, Redis",
                "position": {"x": 65, "y": 80},
                "children": ["apis"]
            },
            
            # APIs
            {
                "id": "apis",
                "title": "APIs",
                "type": "topic",
                "description": "REST, GraphQL",
                "position": {"x": 50, "y": 90},
                "children": ["rest", "graphql"]
            },
            {
                "id": "rest",
                "title": "REST APIs",
                "type": "subtopic",
                "description": "RESTful services",
                "position": {"x": 35, "y": 100},
                "children": ["authentication"]
            },
            {
                "id": "graphql",
                "title": "GraphQL",
                "type": "optional",
                "description": "Query language",
                "position": {"x": 65, "y": 100},
                "children": ["authentication"]
            },
            
            # Authentication
            {
                "id": "authentication",
                "title": "Authentication",
                "type": "topic",
                "description": "JWT, OAuth, Sessions",
                "position": {"x": 50, "y": 110},
                "children": ["caching"]
            },
            
            # Caching
            {
                "id": "caching",
                "title": "Caching",
                "type": "topic",
                "description": "Redis, Memcached",
                "position": {"x": 50, "y": 120},
                "children": ["testing-backend"]
            },
            
            # Testing
            {
                "id": "testing-backend",
                "title": "Testing",
                "type": "topic",
                "description": "Unit, Integration tests",
                "position": {"x": 50, "y": 130},
                "children": ["docker"]
            },
            
            # Docker
            {
                "id": "docker",
                "title": "Docker",
                "type": "topic",
                "description": "Containerization",
                "position": {"x": 50, "y": 140},
                "children": ["system-design"]
            },
            
            # System Design
            {
                "id": "system-design",
                "title": "System Design",
                "type": "topic",
                "description": "Scalability, Load Balancing",
                "position": {"x": 50, "y": 150},
                "children": ["projects"]
            },
            
            # Projects
            {
                "id": "projects",
                "title": "Build Projects",
                "type": "milestone",
                "description": "Create 3-5 backend projects",
                "position": {"x": 50, "y": 160},
                "children": []
            }
        ]
    },
    
    "data_analyst": {
        "name": "Data Analyst",
        "description": "Complete roadmap to become a Data Analyst",
        "nodes": [
            # Statistics & Math
            {
                "id": "statistics",
                "title": "Statistics",
                "type": "topic",
                "description": "Descriptive & Inferential Statistics",
                "position": {"x": 50, "y": 10},
                "children": ["probability", "hypothesis-testing"]
            },
            {
                "id": "probability",
                "title": "Probability",
                "type": "subtopic",
                "description": "Probability theory basics",
                "position": {"x": 35, "y": 20},
                "children": ["excel"]
            },
            {
                "id": "hypothesis-testing",
                "title": "Hypothesis Testing",
                "type": "subtopic",
                "description": "Statistical testing",
                "position": {"x": 65, "y": 20},
                "children": ["excel"]
            },
            
            # Excel
            {
                "id": "excel",
                "title": "Excel",
                "type": "topic",
                "description": "Advanced Excel skills",
                "position": {"x": 50, "y": 30},
                "children": ["pivot-tables", "vlookup", "charts"]
            },
            {
                "id": "pivot-tables",
                "title": "Pivot Tables",
                "type": "subtopic",
                "description": "Data summarization",
                "position": {"x": 30, "y": 40},
                "children": ["sql"]
            },
            {
                "id": "vlookup",
                "title": "VLOOKUP/XLOOKUP",
                "type": "subtopic",
                "description": "Data lookup functions",
                "position": {"x": 50, "y": 40},
                "children": ["sql"]
            },
            {
                "id": "charts",
                "title": "Charts & Graphs",
                "type": "subtopic",
                "description": "Data visualization in Excel",
                "position": {"x": 70, "y": 40},
                "children": ["sql"]
            },
            
            # SQL
            {
                "id": "sql",
                "title": "SQL",
                "type": "topic",
                "description": "Database querying",
                "position": {"x": 50, "y": 50},
                "children": ["joins", "aggregations", "subqueries"]
            },
            {
                "id": "joins",
                "title": "SQL Joins",
                "type": "subtopic",
                "description": "Combining tables",
                "position": {"x": 30, "y": 60},
                "children": ["python-basics"]
            },
            {
                "id": "aggregations",
                "title": "Aggregations",
                "type": "subtopic",
                "description": "GROUP BY, COUNT, SUM",
                "position": {"x": 50, "y": 60},
                "children": ["python-basics"]
            },
            {
                "id": "subqueries",
                "title": "Subqueries",
                "type": "subtopic",
                "description": "Nested queries",
                "position": {"x": 70, "y": 60},
                "children": ["python-basics"]
            },
            
            # Python
            {
                "id": "python-basics",
                "title": "Python",
                "type": "topic",
                "description": "Python for data analysis",
                "position": {"x": 50, "y": 70},
                "children": ["pandas", "numpy"]
            },
            {
                "id": "pandas",
                "title": "Pandas",
                "type": "subtopic",
                "description": "Data manipulation library",
                "position": {"x": 35, "y": 80},
                "children": ["visualization"]
            },
            {
                "id": "numpy",
                "title": "NumPy",
                "type": "subtopic",
                "description": "Numerical computing",
                "position": {"x": 65, "y": 80},
                "children": ["visualization"]
            },
            
            # Visualization
            {
                "id": "visualization",
                "title": "Data Visualization",
                "type": "topic",
                "description": "Creating visual insights",
                "position": {"x": 50, "y": 90},
                "children": ["matplotlib", "tableau", "powerbi"]
            },
            {
                "id": "matplotlib",
                "title": "Matplotlib/Seaborn",
                "type": "subtopic",
                "description": "Python visualization",
                "position": {"x": 30, "y": 100},
                "children": ["ml-basics"]
            },
            {
                "id": "tableau",
                "title": "Tableau",
                "type": "subtopic",
                "description": "BI tool",
                "position": {"x": 50, "y": 100},
                "children": ["ml-basics"]
            },
            {
                "id": "powerbi",
                "title": "Power BI",
                "type": "optional",
                "description": "Microsoft BI tool",
                "position": {"x": 70, "y": 100},
                "children": ["ml-basics"]
            },
            
            # Machine Learning Basics
            {
                "id": "ml-basics",
                "title": "ML Basics",
                "type": "optional",
                "description": "Introduction to ML",
                "position": {"x": 50, "y": 110},
                "children": ["regression", "classification"]
            },
            {
                "id": "regression",
                "title": "Regression",
                "type": "subtopic",
                "description": "Linear/Logistic regression",
                "position": {"x": 35, "y": 120},
                "children": ["portfolio-da"]
            },
            {
                "id": "classification",
                "title": "Classification",
                "type": "subtopic",
                "description": "Classification algorithms",
                "position": {"x": 65, "y": 120},
                "children": ["portfolio-da"]
            },
            
            # Portfolio
            {
                "id": "portfolio-da",
                "title": "Build Portfolio",
                "type": "milestone",
                "description": "Create 3-5 data analysis projects",
                "position": {"x": 50, "y": 130},
                "children": []
            }
        ]
    },
    
    "fullstack_web": {
        "name": "Full Stack Web Development",
        "description": "Complete roadmap for Full Stack Developer",
        "nodes": [
            # Frontend Basics
            {
                "id": "html-css-js",
                "title": "HTML/CSS/JS",
                "type": "topic",
                "description": "Frontend fundamentals",
                "position": {"x": 50, "y": 10},
                "children": ["responsive-design", "javascript-advanced"]
            },
            {
                "id": "responsive-design",
                "title": "Responsive Design",
                "type": "subtopic",
                "description": "Mobile-first approach",
                "position": {"x": 35, "y": 20},
                "children": ["react-fullstack"]
            },
            {
                "id": "javascript-advanced",
                "title": "Advanced JavaScript",
                "type": "subtopic",
                "description": "ES6+, Async/Await",
                "position": {"x": 65, "y": 20},
                "children": ["react-fullstack"]
            },
            
            # React
            {
                "id": "react-fullstack",
                "title": "React",
                "type": "topic",
                "description": "Frontend framework",
                "position": {"x": 50, "y": 30},
                "children": ["react-hooks", "react-router"]
            },
            {
                "id": "react-hooks",
                "title": "React Hooks",
                "type": "subtopic",
                "description": "Modern React patterns",
                "position": {"x": 35, "y": 40},
                "children": ["nodejs"]
            },
            {
                "id": "react-router",
                "title": "React Router",
                "type": "subtopic",
                "description": "Client-side routing",
                "position": {"x": 65, "y": 40},
                "children": ["nodejs"]
            },
            
            # Node.js
            {
                "id": "nodejs",
                "title": "Node.js",
                "type": "topic",
                "description": "Backend JavaScript runtime",
                "position": {"x": 50, "y": 50},
                "children": ["express", "npm"]
            },
            {
                "id": "express",
                "title": "Express.js",
                "type": "subtopic",
                "description": "Web framework",
                "position": {"x": 35, "y": 60},
                "children": ["databases-fullstack"]
            },
            {
                "id": "npm",
                "title": "NPM/Yarn",
                "type": "subtopic",
                "description": "Package management",
                "position": {"x": 65, "y": 60},
                "children": ["databases-fullstack"]
            },
            
            # Databases
            {
                "id": "databases-fullstack",
                "title": "Databases",
                "type": "topic",
                "description": "SQL & NoSQL",
                "position": {"x": 50, "y": 70},
                "children": ["mongodb", "postgresql"]
            },
            {
                "id": "mongodb",
                "title": "MongoDB",
                "type": "subtopic",
                "description": "NoSQL database",
                "position": {"x": 35, "y": 80},
                "children": ["rest-apis"]
            },
            {
                "id": "postgresql",
                "title": "PostgreSQL",
                "type": "subtopic",
                "description": "Relational database",
                "position": {"x": 65, "y": 80},
                "children": ["rest-apis"]
            },
            
            # APIs
            {
                "id": "rest-apis",
                "title": "REST APIs",
                "type": "topic",
                "description": "Building RESTful services",
                "position": {"x": 50, "y": 90},
                "children": ["crud", "middleware"]
            },
            {
                "id": "crud",
                "title": "CRUD Operations",
                "type": "subtopic",
                "description": "Create, Read, Update, Delete",
                "position": {"x": 35, "y": 100},
                "children": ["auth-fullstack"]
            },
            {
                "id": "middleware",
                "title": "Middleware",
                "type": "subtopic",
                "description": "Request/Response handling",
                "position": {"x": 65, "y": 100},
                "children": ["auth-fullstack"]
            },
            
            # Authentication
            {
                "id": "auth-fullstack",
                "title": "Authentication",
                "type": "topic",
                "description": "JWT, OAuth, Sessions",
                "position": {"x": 50, "y": 110},
                "children": ["jwt", "oauth"]
            },
            {
                "id": "jwt",
                "title": "JWT",
                "type": "subtopic",
                "description": "JSON Web Tokens",
                "position": {"x": 35, "y": 120},
                "children": ["deployment-fullstack"]
            },
            {
                "id": "oauth",
                "title": "OAuth",
                "type": "optional",
                "description": "Third-party auth",
                "position": {"x": 65, "y": 120},
                "children": ["deployment-fullstack"]
            },
            
            # Deployment
            {
                "id": "deployment-fullstack",
                "title": "Deployment",
                "type": "topic",
                "description": "Deploy full stack apps",
                "position": {"x": 50, "y": 130},
                "children": ["heroku", "docker-fullstack"]
            },
            {
                "id": "heroku",
                "title": "Heroku/Railway",
                "type": "subtopic",
                "description": "Cloud platforms",
                "position": {"x": 35, "y": 140},
                "children": ["portfolio-fullstack"]
            },
            {
                "id": "docker-fullstack",
                "title": "Docker",
                "type": "optional",
                "description": "Containerization",
                "position": {"x": 65, "y": 140},
                "children": ["portfolio-fullstack"]
            },
            
            # Portfolio
            {
                "id": "portfolio-fullstack",
                "title": "Build Portfolio",
                "type": "milestone",
                "description": "Create 3-5 full stack projects",
                "position": {"x": 50, "y": 150},
                "children": []
            }
        ]
    },
    
    "ui_ux_design": {
        "name": "UI/UX Design",
        "description": "Complete roadmap to become a UI/UX Designer",
        "nodes": [
            # Design Fundamentals
            {
                "id": "design-fundamentals",
                "title": "Design Fundamentals",
                "type": "topic",
                "description": "Basic design principles",
                "position": {"x": 50, "y": 10},
                "children": ["color-theory", "typography", "layout"]
            },
            {
                "id": "color-theory",
                "title": "Color Theory",
                "type": "subtopic",
                "description": "Understanding colors",
                "position": {"x": 30, "y": 20},
                "children": ["figma"]
            },
            {
                "id": "typography",
                "title": "Typography",
                "type": "subtopic",
                "description": "Font selection & pairing",
                "position": {"x": 50, "y": 20},
                "children": ["figma"]
            },
            {
                "id": "layout",
                "title": "Layout & Composition",
                "type": "subtopic",
                "description": "Visual hierarchy",
                "position": {"x": 70, "y": 20},
                "children": ["figma"]
            },
            
            # Figma
            {
                "id": "figma",
                "title": "Figma",
                "type": "topic",
                "description": "Design tool mastery",
                "position": {"x": 50, "y": 30},
                "children": ["components-design", "prototyping"]
            },
            {
                "id": "components-design",
                "title": "Components",
                "type": "subtopic",
                "description": "Reusable design elements",
                "position": {"x": 35, "y": 40},
                "children": ["user-research"]
            },
            {
                "id": "prototyping",
                "title": "Prototyping",
                "type": "subtopic",
                "description": "Interactive prototypes",
                "position": {"x": 65, "y": 40},
                "children": ["user-research"]
            },
            
            # User Research
            {
                "id": "user-research",
                "title": "User Research",
                "type": "topic",
                "description": "Understanding users",
                "position": {"x": 50, "y": 50},
                "children": ["personas", "user-interviews"]
            },
            {
                "id": "personas",
                "title": "User Personas",
                "type": "subtopic",
                "description": "Creating user profiles",
                "position": {"x": 35, "y": 60},
                "children": ["wireframing"]
            },
            {
                "id": "user-interviews",
                "title": "User Interviews",
                "type": "subtopic",
                "description": "Gathering insights",
                "position": {"x": 65, "y": 60},
                "children": ["wireframing"]
            },
            
            # Wireframing
            {
                "id": "wireframing",
                "title": "Wireframing",
                "type": "topic",
                "description": "Low-fidelity designs",
                "position": {"x": 50, "y": 70},
                "children": ["lofi", "hifi"]
            },
            {
                "id": "lofi",
                "title": "Lo-Fi Wireframes",
                "type": "subtopic",
                "description": "Sketches & basic layouts",
                "position": {"x": 35, "y": 80},
                "children": ["ui-design"]
            },
            {
                "id": "hifi",
                "title": "Hi-Fi Wireframes",
                "type": "subtopic",
                "description": "Detailed mockups",
                "position": {"x": 65, "y": 80},
                "children": ["ui-design"]
            },
            
            # UI Design
            {
                "id": "ui-design",
                "title": "UI Design",
                "type": "topic",
                "description": "Visual interface design",
                "position": {"x": 50, "y": 90},
                "children": ["design-systems", "responsive-ui"]
            },
            {
                "id": "design-systems",
                "title": "Design Systems",
                "type": "subtopic",
                "description": "Consistent design language",
                "position": {"x": 35, "y": 100},
                "children": ["usability-testing"]
            },
            {
                "id": "responsive-ui",
                "title": "Responsive Design",
                "type": "subtopic",
                "description": "Mobile & desktop",
                "position": {"x": 65, "y": 100},
                "children": ["usability-testing"]
            },
            
            # Usability Testing
            {
                "id": "usability-testing",
                "title": "Usability Testing",
                "type": "topic",
                "description": "Testing with users",
                "position": {"x": 50, "y": 110},
                "children": ["ab-testing", "heuristics"]
            },
            {
                "id": "ab-testing",
                "title": "A/B Testing",
                "type": "subtopic",
                "description": "Comparing designs",
                "position": {"x": 35, "y": 120},
                "children": ["interaction-design"]
            },
            {
                "id": "heuristics",
                "title": "Heuristic Evaluation",
                "type": "subtopic",
                "description": "Expert review",
                "position": {"x": 65, "y": 120},
                "children": ["interaction-design"]
            },
            
            # Interaction Design
            {
                "id": "interaction-design",
                "title": "Interaction Design",
                "type": "topic",
                "description": "Micro-interactions & animations",
                "position": {"x": 50, "y": 130},
                "children": ["animations", "transitions"]
            },
            {
                "id": "animations",
                "title": "Animations",
                "type": "subtopic",
                "description": "Motion design",
                "position": {"x": 35, "y": 140},
                "children": ["portfolio-design"]
            },
            {
                "id": "transitions",
                "title": "Transitions",
                "type": "subtopic",
                "description": "Smooth state changes",
                "position": {"x": 65, "y": 140},
                "children": ["portfolio-design"]
            },
            
            # Portfolio
            {
                "id": "portfolio-design",
                "title": "Build Portfolio",
                "type": "milestone",
                "description": "Create 5-7 design case studies",
                "position": {"x": 50, "y": 150},
                "children": []
            }
        ]
    },
    
    "digital_marketing": {
        "name": "Digital Marketing",
        "description": "Complete roadmap for Digital Marketing Specialist",
        "nodes": [
            # Marketing Fundamentals
            {
                "id": "marketing-fundamentals",
                "title": "Marketing Fundamentals",
                "type": "topic",
                "description": "Basic marketing concepts",
                "position": {"x": 50, "y": 10},
                "children": ["4ps", "customer-journey"]
            },
            {
                "id": "4ps",
                "title": "4 Ps of Marketing",
                "type": "subtopic",
                "description": "Product, Price, Place, Promotion",
                "position": {"x": 35, "y": 20},
                "children": ["content-marketing"]
            },
            {
                "id": "customer-journey",
                "title": "Customer Journey",
                "type": "subtopic",
                "description": "Understanding buyer behavior",
                "position": {"x": 65, "y": 20},
                "children": ["content-marketing"]
            },
            
            # Content Marketing
            {
                "id": "content-marketing",
                "title": "Content Marketing",
                "type": "topic",
                "description": "Creating valuable content",
                "position": {"x": 50, "y": 30},
                "children": ["blogging", "copywriting"]
            },
            {
                "id": "blogging",
                "title": "Blogging",
                "type": "subtopic",
                "description": "Writing blog posts",
                "position": {"x": 35, "y": 40},
                "children": ["seo-marketing"]
            },
            {
                "id": "copywriting",
                "title": "Copywriting",
                "type": "subtopic",
                "description": "Persuasive writing",
                "position": {"x": 65, "y": 40},
                "children": ["seo-marketing"]
            },
            
            # SEO
            {
                "id": "seo-marketing",
                "title": "SEO",
                "type": "topic",
                "description": "Search Engine Optimization",
                "position": {"x": 50, "y": 50},
                "children": ["on-page-seo", "off-page-seo", "technical-seo"]
            },
            {
                "id": "on-page-seo",
                "title": "On-Page SEO",
                "type": "subtopic",
                "description": "Content optimization",
                "position": {"x": 30, "y": 60},
                "children": ["social-media"]
            },
            {
                "id": "off-page-seo",
                "title": "Off-Page SEO",
                "type": "subtopic",
                "description": "Link building",
                "position": {"x": 50, "y": 60},
                "children": ["social-media"]
            },
            {
                "id": "technical-seo",
                "title": "Technical SEO",
                "type": "subtopic",
                "description": "Site structure & speed",
                "position": {"x": 70, "y": 60},
                "children": ["social-media"]
            },
            
            # Social Media Marketing
            {
                "id": "social-media",
                "title": "Social Media Marketing",
                "type": "topic",
                "description": "Social platforms strategy",
                "position": {"x": 50, "y": 70},
                "children": ["facebook-ads", "instagram", "linkedin"]
            },
            {
                "id": "facebook-ads",
                "title": "Facebook Ads",
                "type": "subtopic",
                "description": "Paid social advertising",
                "position": {"x": 30, "y": 80},
                "children": ["email-marketing"]
            },
            {
                "id": "instagram",
                "title": "Instagram Marketing",
                "type": "subtopic",
                "description": "Visual content strategy",
                "position": {"x": 50, "y": 80},
                "children": ["email-marketing"]
            },
            {
                "id": "linkedin",
                "title": "LinkedIn Marketing",
                "type": "subtopic",
                "description": "B2B marketing",
                "position": {"x": 70, "y": 80},
                "children": ["email-marketing"]
            },
            
            # Email Marketing
            {
                "id": "email-marketing",
                "title": "Email Marketing",
                "type": "topic",
                "description": "Email campaigns",
                "position": {"x": 50, "y": 90},
                "children": ["email-automation", "newsletters"]
            },
            {
                "id": "email-automation",
                "title": "Email Automation",
                "type": "subtopic",
                "description": "Drip campaigns",
                "position": {"x": 35, "y": 100},
                "children": ["google-ads"]
            },
            {
                "id": "newsletters",
                "title": "Newsletters",
                "type": "subtopic",
                "description": "Regular email content",
                "position": {"x": 65, "y": 100},
                "children": ["google-ads"]
            },
            
            # Google Ads
            {
                "id": "google-ads",
                "title": "Google Ads",
                "type": "topic",
                "description": "PPC advertising",
                "position": {"x": 50, "y": 110},
                "children": ["search-ads", "display-ads"]
            },
            {
                "id": "search-ads",
                "title": "Search Ads",
                "type": "subtopic",
                "description": "Text-based ads",
                "position": {"x": 35, "y": 120},
                "children": ["analytics"]
            },
            {
                "id": "display-ads",
                "title": "Display Ads",
                "type": "subtopic",
                "description": "Banner advertising",
                "position": {"x": 65, "y": 120},
                "children": ["analytics"]
            },
            
            # Analytics
            {
                "id": "analytics",
                "title": "Analytics",
                "type": "topic",
                "description": "Measuring performance",
                "position": {"x": 50, "y": 130},
                "children": ["google-analytics", "conversion-tracking"]
            },
            {
                "id": "google-analytics",
                "title": "Google Analytics",
                "type": "subtopic",
                "description": "Website analytics",
                "position": {"x": 35, "y": 140},
                "children": ["portfolio-marketing"]
            },
            {
                "id": "conversion-tracking",
                "title": "Conversion Tracking",
                "type": "subtopic",
                "description": "ROI measurement",
                "position": {"x": 65, "y": 140},
                "children": ["portfolio-marketing"]
            },
            
            # Portfolio
            {
                "id": "portfolio-marketing",
                "title": "Build Portfolio",
                "type": "milestone",
                "description": "Create 3-5 marketing campaigns",
                "position": {"x": 50, "y": 150},
                "children": []
            }
        ]
    }
}

def get_roadmap(path_key):
    """Get roadmap data for a specific career path"""
    return ROADMAPS.get(path_key, {
        "name": "Generic Roadmap",
        "description": "Learning path",
        "nodes": []
    })
