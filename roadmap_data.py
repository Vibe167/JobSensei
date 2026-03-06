f"""
Comprehensive Roadmap Data - roadmap.sh style
Contains detailed learning paths for each career track
"""

ROADMAPS = {
    "frontend_developer": {
        "name": "Frontend Development",
        "description": "Complete roadmap to become a Frontend Developer",
        "nodes": [
            # Internet & Web Basics
            {"id": "internet", "title": "Internet", "type": "topic", "description": "How does the internet work?", "position": {"x": 50, "y": 5}, "children": ["http", "browsers", "dns", "domain"]},
            {"id": "http", "title": "HTTP/HTTPS", "type": "subtopic", "description": "Understanding HTTP protocol", "position": {"x": 20, "y": 12}, "children": ["http-methods", "status-codes"]},
            {"id": "http-methods", "title": "HTTP Methods", "type": "subtopic", "description": "GET, POST, PUT, DELETE", "position": {"x": 15, "y": 18}, "children": ["html"]},
            {"id": "status-codes", "title": "Status Codes", "type": "subtopic", "description": "200, 404, 500, etc", "position": {"x": 25, "y": 18}, "children": ["html"]},
            {"id": "browsers", "title": "Browsers", "type": "subtopic", "description": "How browsers work", "position": {"x": 40, "y": 12}, "children": ["rendering", "dev-tools"]},
            {"id": "rendering", "title": "Rendering Engine", "type": "subtopic", "description": "DOM, CSSOM, Render Tree", "position": {"x": 35, "y": 18}, "children": ["html"]},
            {"id": "dev-tools", "title": "Dev Tools", "type": "subtopic", "description": "Chrome DevTools, Firefox DevTools", "position": {"x": 45, "y": 18}, "children": ["html"]},
            {"id": "dns", "title": "DNS", "type": "subtopic", "description": "Domain Name System", "position": {"x": 60, "y": 12}, "children": ["html"]},
            {"id": "domain", "title": "Domain Names", "type": "subtopic", "description": "Understanding domains", "position": {"x": 80, "y": 12}, "children": ["html"]},
            
            # HTML - Expanded
            {"id": "html", "title": "HTML", "type": "topic", "description": "Learn HTML basics", "position": {"x": 50, "y": 25}, "children": ["html-basics", "semantic-html", "forms", "accessibility", "seo"]},
            {"id": "html-basics", "title": "HTML Basics", "type": "subtopic", "description": "Tags, elements, attributes", "position": {"x": 20, "y": 32}, "children": ["html-structure", "html-text"]},
            {"id": "html-structure", "title": "Document Structure", "type": "subtopic", "description": "DOCTYPE, head, body", "position": {"x": 15, "y": 38}, "children": ["semantic-html"]},
            {"id": "html-text", "title": "Text Elements", "type": "subtopic", "description": "h1-h6, p, span, div", "position": {"x": 25, "y": 38}, "children": ["semantic-html"]},
            {"id": "semantic-html", "title": "Semantic HTML", "type": "subtopic", "description": "header, nav, main, article, section", "position": {"x": 40, "y": 32}, "children": ["html-media", "html-lists"]},
            {"id": "html-media", "title": "Media Elements", "type": "subtopic", "description": "img, video, audio, picture", "position": {"x": 35, "y": 38}, "children": ["forms"]},
            {"id": "html-lists", "title": "Lists & Tables", "type": "subtopic", "description": "ul, ol, table", "position": {"x": 45, "y": 38}, "children": ["forms"]},
            {"id": "forms", "title": "Forms & Validations", "type": "subtopic", "description": "input, textarea, select, validation", "position": {"x": 60, "y": 32}, "children": ["form-types", "form-validation"]},
            {"id": "form-types", "title": "Input Types", "type": "subtopic", "description": "text, email, password, checkbox", "position": {"x": 55, "y": 38}, "children": ["accessibility"]},
            {"id": "form-validation", "title": "Form Validation", "type": "subtopic", "description": "required, pattern, custom validation", "position": {"x": 65, "y": 38}, "children": ["accessibility"]},
            {"id": "accessibility", "title": "Accessibility", "type": "subtopic", "description": "ARIA, semantic HTML, keyboard nav", "position": {"x": 75, "y": 32}, "children": ["aria", "wcag"]},
            {"id": "aria", "title": "ARIA", "type": "subtopic", "description": "Accessible Rich Internet Applications", "position": {"x": 72, "y": 38}, "children": ["seo"]},
            {"id": "wcag", "title": "WCAG", "type": "subtopic", "description": "Web Content Accessibility Guidelines", "position": {"x": 78, "y": 38}, "children": ["seo"]},
            {"id": "seo", "title": "SEO Basics", "type": "subtopic", "description": "meta tags, Open Graph, structured data", "position": {"x": 85, "y": 32}, "children": ["css"]},
            
            # CSS - Expanded
            {"id": "css", "title": "CSS", "type": "topic", "description": "Learn CSS styling", "position": {"x": 50, "y": 45}, "children": ["css-basics", "selectors", "box-model", "layouts", "responsive", "css-frameworks"]},
            {"id": "css-basics", "title": "CSS Basics", "type": "subtopic", "description": "Syntax, properties, values", "position": {"x": 15, "y": 52}, "children": ["colors", "units"]},
            {"id": "colors", "title": "Colors", "type": "subtopic", "description": "hex, rgb, hsl, named colors", "position": {"x": 12, "y": 58}, "children": ["selectors"]},
            {"id": "units", "title": "Units", "type": "subtopic", "description": "px, em, rem, %, vw, vh", "position": {"x": 18, "y": 58}, "children": ["selectors"]},
            {"id": "selectors", "title": "Selectors", "type": "subtopic", "description": "class, id, attribute, pseudo", "position": {"x": 28, "y": 52}, "children": ["specificity", "combinators"]},
            {"id": "specificity", "title": "Specificity", "type": "subtopic", "description": "Selector priority rules", "position": {"x": 25, "y": 58}, "children": ["box-model"]},
            {"id": "combinators", "title": "Combinators", "type": "subtopic", "description": "descendant, child, sibling", "position": {"x": 31, "y": 58}, "children": ["box-model"]},
            {"id": "box-model", "title": "Box Model", "type": "subtopic", "description": "margin, border, padding, content", "position": {"x": 40, "y": 52}, "children": ["display", "positioning"]},
            {"id": "display", "title": "Display", "type": "subtopic", "description": "block, inline, inline-block, none", "position": {"x": 37, "y": 58}, "children": ["layouts"]},
            {"id": "positioning", "title": "Positioning", "type": "subtopic", "description": "static, relative, absolute, fixed, sticky", "position": {"x": 43, "y": 58}, "children": ["layouts"]},
            {"id": "layouts", "title": "Layouts", "type": "subtopic", "description": "Flexbox, Grid, Float", "position": {"x": 52, "y": 52}, "children": ["flexbox", "grid"]},
            {"id": "flexbox", "title": "Flexbox", "type": "subtopic", "description": "flex container, flex items, alignment", "position": {"x": 49, "y": 58}, "children": ["responsive"]},
            {"id": "grid", "title": "CSS Grid", "type": "subtopic", "description": "grid template, areas, auto-placement", "position": {"x": 55, "y": 58}, "children": ["responsive"]},
            {"id": "responsive", "title": "Responsive Design", "type": "subtopic", "description": "Media queries, mobile-first", "position": {"x": 64, "y": 52}, "children": ["media-queries", "breakpoints"]},
            {"id": "media-queries", "title": "Media Queries", "type": "subtopic", "description": "@media, min-width, max-width", "position": {"x": 61, "y": 58}, "children": ["css-frameworks"]},
            {"id": "breakpoints", "title": "Breakpoints", "type": "subtopic", "description": "Mobile, tablet, desktop sizes", "position": {"x": 67, "y": 58}, "children": ["css-frameworks"]},
            {"id": "css-frameworks", "title": "CSS Frameworks", "type": "optional", "description": "Tailwind, Bootstrap, Material UI", "position": {"x": 76, "y": 52}, "children": ["tailwind", "bootstrap"]},
            {"id": "tailwind", "title": "Tailwind CSS", "type": "optional", "description": "Utility-first CSS framework", "position": {"x": 73, "y": 58}, "children": ["javascript"]},
            {"id": "bootstrap", "title": "Bootstrap", "type": "optional", "description": "Component-based framework", "position": {"x": 79, "y": 58}, "children": ["javascript"]},
            
            # JavaScript - Expanded
            {"id": "javascript", "title": "JavaScript", "type": "topic", "description": "Learn JavaScript fundamentals", "position": {"x": 50, "y": 65}, "children": ["js-basics", "dom", "fetch", "es6", "async"]},
            {"id": "js-basics", "title": "JS Basics", "type": "subtopic", "description": "Variables, data types, operators", "position": {"x": 15, "y": 72}, "children": ["variables", "data-types"]},
            {"id": "variables", "title": "Variables", "type": "subtopic", "description": "var, let, const, scope", "position": {"x": 12, "y": 78}, "children": ["dom"]},
            {"id": "data-types", "title": "Data Types", "type": "subtopic", "description": "string, number, boolean, object, array", "position": {"x": 18, "y": 78}, "children": ["dom"]},
            {"id": "dom", "title": "DOM Manipulation", "type": "subtopic", "description": "querySelector, createElement, events", "position": {"x": 28, "y": 72}, "children": ["dom-selection", "dom-events"]},
            {"id": "dom-selection", "title": "DOM Selection", "type": "subtopic", "description": "getElementById, querySelector", "position": {"x": 25, "y": 78}, "children": ["fetch"]},
            {"id": "dom-events", "title": "Event Handling", "type": "subtopic", "description": "addEventListener, event bubbling", "position": {"x": 31, "y": 78}, "children": ["fetch"]},
            {"id": "fetch", "title": "Fetch API", "type": "subtopic", "description": "Making HTTP requests, REST APIs", "position": {"x": 40, "y": 72}, "children": ["fetch-methods", "json"]},
            {"id": "fetch-methods", "title": "Fetch Methods", "type": "subtopic", "description": "GET, POST, PUT, DELETE", "position": {"x": 37, "y": 78}, "children": ["es6"]},
            {"id": "json", "title": "JSON", "type": "subtopic", "description": "Parse, stringify, working with APIs", "position": {"x": 43, "y": 78}, "children": ["es6"]},
            {"id": "es6", "title": "ES6+ Features", "type": "subtopic", "description": "Arrow functions, destructuring, spread", "position": {"x": 52, "y": 72}, "children": ["arrow-functions", "destructuring"]},
            {"id": "arrow-functions", "title": "Arrow Functions", "type": "subtopic", "description": "() => {}, this binding", "position": {"x": 49, "y": 78}, "children": ["async"]},
            {"id": "destructuring", "title": "Destructuring", "type": "subtopic", "description": "Array & object destructuring", "position": {"x": 55, "y": 78}, "children": ["async"]},
            {"id": "async", "title": "Async JavaScript", "type": "subtopic", "description": "Promises, async/await, callbacks", "position": {"x": 64, "y": 72}, "children": ["promises", "async-await"]},
            {"id": "promises", "title": "Promises", "type": "subtopic", "description": "then, catch, finally, Promise.all", "position": {"x": 61, "y": 78}, "children": ["version-control"]},
            {"id": "async-await", "title": "Async/Await", "type": "subtopic", "description": "Modern async syntax, try/catch", "position": {"x": 67, "y": 78}, "children": ["version-control"]},
            
            # Version Control & Tools
            {"id": "version-control", "title": "Version Control", "type": "topic", "description": "Git & GitHub", "position": {"x": 50, "y": 85}, "children": ["git-basics", "github"]},
            {"id": "git-basics", "title": "Git Basics", "type": "subtopic", "description": "init, add, commit, push, pull", "position": {"x": 45, "y": 92}, "children": ["package-managers"]},
            {"id": "github", "title": "GitHub", "type": "subtopic", "description": "Repositories, branches, PRs", "position": {"x": 55, "y": 92}, "children": ["package-managers"]},
            
            # Package Managers
            {"id": "package-managers", "title": "Package Managers", "type": "topic", "description": "npm, yarn, pnpm", "position": {"x": 50, "y": 98}, "children": ["npm", "build-tools"]},
            {"id": "npm", "title": "NPM", "type": "subtopic", "description": "install, scripts, package.json", "position": {"x": 45, "y": 105}, "children": ["build-tools"]},
            
            # Build Tools
            {"id": "build-tools", "title": "Build Tools", "type": "optional", "description": "Vite, Webpack, Parcel", "position": {"x": 30, "y": 112}, "children": ["vite", "webpack"]},
            {"id": "vite", "title": "Vite", "type": "optional", "description": "Fast build tool", "position": {"x": 27, "y": 118}, "children": ["testing"]},
            {"id": "webpack", "title": "Webpack", "type": "optional", "description": "Module bundler", "position": {"x": 33, "y": 118}, "children": ["testing"]},
            
            # React - Expanded
            {"id": "react", "title": "React", "type": "topic", "description": "Learn React library", "position": {"x": 70, "y": 112}, "children": ["react-basics", "components", "hooks", "routing"]},
            {"id": "react-basics", "title": "React Basics", "type": "subtopic", "description": "JSX, components, props", "position": {"x": 60, "y": 118}, "children": ["jsx", "props"]},
            {"id": "jsx", "title": "JSX", "type": "subtopic", "description": "JavaScript XML syntax", "position": {"x": 57, "y": 124}, "children": ["components"]},
            {"id": "props", "title": "Props", "type": "subtopic", "description": "Passing data to components", "position": {"x": 63, "y": 124}, "children": ["components"]},
            {"id": "components", "title": "Components", "type": "subtopic", "description": "Functional & class components", "position": {"x": 70, "y": 118}, "children": ["functional-components", "lifecycle"]},
            {"id": "functional-components", "title": "Functional Components", "type": "subtopic", "description": "Modern React components", "position": {"x": 67, "y": 124}, "children": ["hooks"]},
            {"id": "lifecycle", "title": "Lifecycle", "type": "subtopic", "description": "Component lifecycle methods", "position": {"x": 73, "y": 124}, "children": ["hooks"]},
            {"id": "hooks", "title": "Hooks", "type": "subtopic", "description": "useState, useEffect, custom hooks", "position": {"x": 80, "y": 118}, "children": ["useState", "useEffect"]},
            {"id": "useState", "title": "useState", "type": "subtopic", "description": "State management hook", "position": {"x": 77, "y": 124}, "children": ["routing"]},
            {"id": "useEffect", "title": "useEffect", "type": "subtopic", "description": "Side effects hook", "position": {"x": 83, "y": 124}, "children": ["routing"]},
            {"id": "routing", "title": "React Router", "type": "subtopic", "description": "Client-side routing, navigation", "position": {"x": 90, "y": 118}, "children": ["state-management"]},
            
            # State Management
            {"id": "state-management", "title": "State Management", "type": "topic", "description": "Context API, Redux, Zustand", "position": {"x": 75, "y": 130}, "children": ["context-api", "redux"]},
            {"id": "context-api", "title": "Context API", "type": "subtopic", "description": "React built-in state management", "position": {"x": 70, "y": 136}, "children": ["testing"]},
            {"id": "redux", "title": "Redux", "type": "optional", "description": "Predictable state container", "position": {"x": 80, "y": 136}, "children": ["testing"]},
            
            # Testing
            {"id": "testing", "title": "Testing", "type": "topic", "description": "Jest, React Testing Library, Vitest", "position": {"x": 50, "y": 142}, "children": ["unit-testing", "integration-testing"]},
            {"id": "unit-testing", "title": "Unit Testing", "type": "subtopic", "description": "Testing individual components", "position": {"x": 45, "y": 148}, "children": ["typescript"]},
            {"id": "integration-testing", "title": "Integration Testing", "type": "subtopic", "description": "Testing component interactions", "position": {"x": 55, "y": 148}, "children": ["typescript"]},
            
            # TypeScript
            {"id": "typescript", "title": "TypeScript", "type": "optional", "description": "Static typing for JavaScript", "position": {"x": 30, "y": 155}, "children": ["ts-basics", "ts-react"]},
            {"id": "ts-basics", "title": "TS Basics", "type": "optional", "description": "Types, interfaces, generics", "position": {"x": 27, "y": 161}, "children": ["deployment"]},
            {"id": "ts-react", "title": "TS with React", "type": "optional", "description": "Typing React components", "position": {"x": 33, "y": 161}, "children": ["deployment"]},
            
            # Deployment
            {"id": "deployment", "title": "Deployment", "type": "topic", "description": "Vercel, Netlify, GitHub Pages", "position": {"x": 70, "y": 155}, "children": ["vercel", "netlify", "ci-cd"]},
            {"id": "vercel", "title": "Vercel", "type": "subtopic", "description": "Deploy React apps", "position": {"x": 65, "y": 161}, "children": ["portfolio"]},
            {"id": "netlify", "title": "Netlify", "type": "subtopic", "description": "Continuous deployment", "position": {"x": 70, "y": 161}, "children": ["portfolio"]},
            {"id": "ci-cd", "title": "CI/CD", "type": "subtopic", "description": "GitHub Actions, automated testing", "position": {"x": 75, "y": 161}, "children": ["portfolio"]},
            
            # Portfolio
            {"id": "portfolio", "title": "Build Portfolio", "type": "milestone", "description": "Create 3-5 projects showcasing skills", "position": {"x": 50, "y": 168}, "children": []}
        ]
    },
    
    "software_engineer_backend": {
        "name": "Software Engineer (Backend/Systems)",
        "description": "Complete roadmap for Backend Development with DSA",
        "nodes": [
            # Programming Language Fundamentals
            {"id": "programming-lang", "title": "Programming Language", "type": "topic", "description": "Choose: Python, Java, Go, or Node.js", "position": {"x": 50, "y": 5}, "children": ["syntax", "oop"]},
            {"id": "syntax", "title": "Syntax & Basics", "type": "subtopic", "description": "Variables, loops, conditionals", "position": {"x": 35, "y": 12}, "children": ["oop"]},
            {"id": "oop", "title": "OOP Concepts", "type": "subtopic", "description": "Classes, inheritance, polymorphism", "position": {"x": 50, "y": 12}, "children": ["design-patterns", "solid"]},
            {"id": "design-patterns", "title": "Design Patterns", "type": "subtopic", "description": "Singleton, Factory, Observer", "position": {"x": 45, "y": 18}, "children": ["data-structures"]},
            {"id": "solid", "title": "SOLID Principles", "type": "subtopic", "description": "Software design principles", "position": {"x": 55, "y": 18}, "children": ["data-structures"]},
            
            # Data Structures - Expanded
            {"id": "data-structures", "title": "Data Structures", "type": "topic", "description": "Core data structures", "position": {"x": 50, "y": 25}, "children": ["arrays", "linked-lists", "stacks-queues", "hash-tables"]},
            {"id": "arrays", "title": "Arrays & Strings", "type": "subtopic", "description": "Array manipulation, string algorithms", "position": {"x": 20, "y": 32}, "children": ["array-techniques"]},
            {"id": "array-techniques", "title": "Array Techniques", "type": "subtopic", "description": "Two pointers, sliding window", "position": {"x": 17, "y": 38}, "children": ["trees"]},
            {"id": "linked-lists", "title": "Linked Lists", "type": "subtopic", "description": "Singly, doubly, circular", "position": {"x": 35, "y": 32}, "children": ["ll-operations"]},
            {"id": "ll-operations", "title": "LL Operations", "type": "subtopic", "description": "Reversal, cycle detection", "position": {"x": 32, "y": 38}, "children": ["trees"]},
            {"id": "stacks-queues", "title": "Stacks & Queues", "type": "subtopic", "description": "LIFO, FIFO structures", "position": {"x": 50, "y": 32}, "children": ["stack-applications"]},
            {"id": "stack-applications", "title": "Stack Applications", "type": "subtopic", "description": "Expression evaluation, backtracking", "position": {"x": 47, "y": 38}, "children": ["trees"]},
            {"id": "hash-tables", "title": "Hash Tables", "type": "subtopic", "description": "Hash maps, collision handling", "position": {"x": 65, "y": 32}, "children": ["hashing-techniques"]},
            {"id": "hashing-techniques", "title": "Hashing Techniques", "type": "subtopic", "description": "Chaining, open addressing", "position": {"x": 62, "y": 38}, "children": ["trees"]},
            {"id": "trees", "title": "Trees", "type": "subtopic", "description": "Binary trees, BST, AVL, Red-Black", "position": {"x": 80, "y": 32}, "children": ["tree-traversal", "balanced-trees"]},
            {"id": "tree-traversal", "title": "Tree Traversal", "type": "subtopic", "description": "Inorder, preorder, postorder, level-order", "position": {"x": 77, "y": 38}, "children": ["graphs"]},
            {"id": "balanced-trees", "title": "Balanced Trees", "type": "subtopic", "description": "AVL, Red-Black trees", "position": {"x": 83, "y": 38}, "children": ["graphs"]},
            {"id": "graphs", "title": "Graphs", "type": "subtopic", "description": "Adjacency list/matrix, directed/undirected", "position": {"x": 50, "y": 44}, "children": ["graph-traversal", "graph-algorithms"]},
            {"id": "graph-traversal", "title": "Graph Traversal", "type": "subtopic", "description": "BFS, DFS", "position": {"x": 45, "y": 50}, "children": ["algorithms"]},
            {"id": "graph-algorithms", "title": "Graph Algorithms", "type": "subtopic", "description": "Dijkstra, Bellman-Ford, Floyd-Warshall", "position": {"x": 55, "y": 50}, "children": ["algorithms"]},
            
            # Algorithms - Expanded
            {"id": "algorithms", "title": "Algorithms", "type": "topic", "description": "Algorithm design & analysis", "position": {"x": 50, "y": 57}, "children": ["sorting", "searching", "recursion", "dp"]},
            {"id": "sorting", "title": "Sorting Algorithms", "type": "subtopic", "description": "QuickSort, MergeSort, HeapSort", "position": {"x": 20, "y": 64}, "children": ["sorting-advanced"]},
            {"id": "sorting-advanced", "title": "Advanced Sorting", "type": "subtopic", "description": "Counting sort, radix sort", "position": {"x": 17, "y": 70}, "children": ["databases"]},
            {"id": "searching", "title": "Searching", "type": "subtopic", "description": "Binary search, interpolation search", "position": {"x": 35, "y": 64}, "children": ["search-variations"]},
            {"id": "search-variations", "title": "Search Variations", "type": "subtopic", "description": "Search in rotated array, 2D matrix", "position": {"x": 32, "y": 70}, "children": ["databases"]},
            {"id": "recursion", "title": "Recursion & Backtracking", "type": "subtopic", "description": "Recursive problem solving", "position": {"x": 50, "y": 64}, "children": ["backtracking-problems"]},
            {"id": "backtracking-problems", "title": "Backtracking Problems", "type": "subtopic", "description": "N-Queens, Sudoku solver", "position": {"x": 47, "y": 70}, "children": ["databases"]},
            {"id": "dp", "title": "Dynamic Programming", "type": "subtopic", "description": "Memoization, tabulation", "position": {"x": 65, "y": 64}, "children": ["dp-patterns"]},
            {"id": "dp-patterns", "title": "DP Patterns", "type": "subtopic", "description": "Knapsack, LCS, LIS", "position": {"x": 62, "y": 70}, "children": ["databases"]},
            {"id": "greedy", "title": "Greedy Algorithms", "type": "subtopic", "description": "Activity selection, Huffman coding", "position": {"x": 80, "y": 64}, "children": ["greedy-problems"]},
            {"id": "greedy-problems", "title": "Greedy Problems", "type": "subtopic", "description": "Interval scheduling, fractional knapsack", "position": {"x": 77, "y": 70}, "children": ["databases"]},
            
            # Databases - Expanded
            {"id": "databases", "title": "Databases", "type": "topic", "description": "SQL & NoSQL databases", "position": {"x": 50, "y": 77}, "children": ["sql", "nosql", "db-design"]},
            {"id": "sql", "title": "SQL Databases", "type": "subtopic", "description": "PostgreSQL, MySQL, SQLite", "position": {"x": 30, "y": 84}, "children": ["sql-queries", "joins"]},
            {"id": "sql-queries", "title": "SQL Queries", "type": "subtopic", "description": "SELECT, INSERT, UPDATE, DELETE", "position": {"x": 25, "y": 90}, "children": ["apis"]},
            {"id": "joins", "title": "SQL Joins", "type": "subtopic", "description": "INNER, LEFT, RIGHT, FULL", "position": {"x": 35, "y": 90}, "children": ["apis"]},
            {"id": "nosql", "title": "NoSQL Databases", "type": "subtopic", "description": "MongoDB, Redis, Cassandra", "position": {"x": 50, "y": 84}, "children": ["document-db", "key-value"]},
            {"id": "document-db", "title": "Document Databases", "type": "subtopic", "description": "MongoDB, CouchDB", "position": {"x": 47, "y": 90}, "children": ["apis"]},
            {"id": "key-value", "title": "Key-Value Stores", "type": "subtopic", "description": "Redis, Memcached", "position": {"x": 53, "y": 90}, "children": ["apis"]},
            {"id": "db-design", "title": "Database Design", "type": "subtopic", "description": "Normalization, indexing, transactions", "position": {"x": 70, "y": 84}, "children": ["normalization", "indexing"]},
            {"id": "normalization", "title": "Normalization", "type": "subtopic", "description": "1NF, 2NF, 3NF, BCNF", "position": {"x": 67, "y": 90}, "children": ["apis"]},
            {"id": "indexing", "title": "Indexing", "type": "subtopic", "description": "B-tree, hash indexes", "position": {"x": 73, "y": 90}, "children": ["apis"]},
            
            # APIs - Expanded
            {"id": "apis", "title": "API Development", "type": "topic", "description": "Building robust APIs", "position": {"x": 50, "y": 97}, "children": ["rest", "graphql", "api-design"]},
            {"id": "rest", "title": "REST APIs", "type": "subtopic", "description": "RESTful principles, HTTP methods", "position": {"x": 30, "y": 104}, "children": ["rest-best-practices"]},
            {"id": "rest-best-practices", "title": "REST Best Practices", "type": "subtopic", "description": "Versioning, pagination, filtering", "position": {"x": 27, "y": 110}, "children": ["authentication"]},
            {"id": "graphql", "title": "GraphQL", "type": "optional", "description": "Query language for APIs", "position": {"x": 50, "y": 104}, "children": ["graphql-schema"]},
            {"id": "graphql-schema", "title": "GraphQL Schema", "type": "optional", "description": "Types, queries, mutations", "position": {"x": 47, "y": 110}, "children": ["authentication"]},
            {"id": "api-design", "title": "API Design", "type": "subtopic", "description": "Documentation, error handling", "position": {"x": 70, "y": 104}, "children": ["api-docs", "error-handling"]},
            {"id": "api-docs", "title": "API Documentation", "type": "subtopic", "description": "Swagger, OpenAPI", "position": {"x": 67, "y": 110}, "children": ["authentication"]},
            {"id": "error-handling", "title": "Error Handling", "type": "subtopic", "description": "Status codes, error responses", "position": {"x": 73, "y": 110}, "children": ["authentication"]},
            
            # Authentication & Security
            {"id": "authentication", "title": "Authentication & Security", "type": "topic", "description": "Securing backend systems", "position": {"x": 50, "y": 117}, "children": ["jwt", "oauth", "security"]},
            {"id": "jwt", "title": "JWT", "type": "subtopic", "description": "JSON Web Tokens", "position": {"x": 35, "y": 124}, "children": ["caching"]},
            {"id": "oauth", "title": "OAuth 2.0", "type": "subtopic", "description": "Authorization framework", "position": {"x": 50, "y": 124}, "children": ["caching"]},
            {"id": "security", "title": "Security Best Practices", "type": "subtopic", "description": "HTTPS, CORS, rate limiting", "position": {"x": 65, "y": 124}, "children": ["caching"]},
            
            # Caching & Performance
            {"id": "caching", "title": "Caching", "type": "topic", "description": "Performance optimization", "position": {"x": 50, "y": 131}, "children": ["redis-cache", "cdn", "cache-strategies"]},
            {"id": "redis-cache", "title": "Redis", "type": "subtopic", "description": "In-memory data store", "position": {"x": 35, "y": 138}, "children": ["message-queues"]},
            {"id": "cdn", "title": "CDN", "type": "subtopic", "description": "Content delivery networks", "position": {"x": 50, "y": 138}, "children": ["message-queues"]},
            {"id": "cache-strategies", "title": "Cache Strategies", "type": "subtopic", "description": "LRU, LFU, write-through", "position": {"x": 65, "y": 138}, "children": ["message-queues"]},
            
            # Message Queues & Async
            {"id": "message-queues", "title": "Message Queues", "type": "topic", "description": "Asynchronous processing", "position": {"x": 50, "y": 145}, "children": ["rabbitmq", "kafka"]},
            {"id": "rabbitmq", "title": "RabbitMQ", "type": "subtopic", "description": "Message broker", "position": {"x": 40, "y": 152}, "children": ["testing-backend"]},
            {"id": "kafka", "title": "Apache Kafka", "type": "subtopic", "description": "Distributed streaming", "position": {"x": 60, "y": 152}, "children": ["testing-backend"]},
            
            # Testing
            {"id": "testing-backend", "title": "Testing", "type": "topic", "description": "Test-driven development", "position": {"x": 50, "y": 159}, "children": ["unit-tests", "integration-tests", "e2e-tests"]},
            {"id": "unit-tests", "title": "Unit Testing", "type": "subtopic", "description": "Testing individual functions", "position": {"x": 35, "y": 166}, "children": ["docker"]},
            {"id": "integration-tests", "title": "Integration Testing", "type": "subtopic", "description": "Testing component interactions", "position": {"x": 50, "y": 166}, "children": ["docker"]},
            {"id": "e2e-tests", "title": "E2E Testing", "type": "subtopic", "description": "End-to-end testing", "position": {"x": 65, "y": 166}, "children": ["docker"]},
            
            # Docker & Containers
            {"id": "docker", "title": "Docker", "type": "topic", "description": "Containerization", "position": {"x": 50, "y": 173}, "children": ["dockerfile", "docker-compose"]},
            {"id": "dockerfile", "title": "Dockerfile", "type": "subtopic", "description": "Creating container images", "position": {"x": 40, "y": 180}, "children": ["microservices"]},
            {"id": "docker-compose", "title": "Docker Compose", "type": "subtopic", "description": "Multi-container applications", "position": {"x": 60, "y": 180}, "children": ["microservices"]},
            
            # Microservices
            {"id": "microservices", "title": "Microservices", "type": "topic", "description": "Service-oriented architecture", "position": {"x": 50, "y": 187}, "children": ["service-communication", "api-gateway"]},
            {"id": "service-communication", "title": "Service Communication", "type": "subtopic", "description": "REST, gRPC, message queues", "position": {"x": 40, "y": 194}, "children": ["system-design"]},
            {"id": "api-gateway", "title": "API Gateway", "type": "subtopic", "description": "Request routing, load balancing", "position": {"x": 60, "y": 194}, "children": ["system-design"]},
            
            # System Design
            {"id": "system-design", "title": "System Design", "type": "topic", "description": "Scalable system architecture", "position": {"x": 50, "y": 201}, "children": ["scalability", "load-balancing", "db-sharding"]},
            {"id": "scalability", "title": "Scalability", "type": "subtopic", "description": "Horizontal vs vertical scaling", "position": {"x": 30, "y": 208}, "children": ["projects"]},
            {"id": "load-balancing", "title": "Load Balancing", "type": "subtopic", "description": "Distributing traffic", "position": {"x": 50, "y": 208}, "children": ["projects"]},
            {"id": "db-sharding", "title": "Database Sharding", "type": "subtopic", "description": "Partitioning data", "position": {"x": 70, "y": 208}, "children": ["projects"]},
            
            # Projects
            {"id": "projects", "title": "Build Projects", "type": "milestone", "description": "Create 3-5 backend projects with system design", "position": {"x": 50, "y": 215}, "children": []}
        ]
    },
    
    "data_scientist": {
        "name": "Data Scientist/Analyst",
        "description": "Complete roadmap to become a Data Scientist",
        "nodes": [
            # Mathematics & Statistics - Expanded
            {"id": "mathematics", "title": "Mathematics", "type": "topic", "description": "Mathematical foundations", "position": {"x": 50, "y": 5}, "children": ["linear-algebra", "calculus", "statistics"]},
            {"id": "linear-algebra", "title": "Linear Algebra", "type": "subtopic", "description": "Vectors, matrices, eigenvalues", "position": {"x": 30, "y": 12}, "children": ["statistics"]},
            {"id": "calculus", "title": "Calculus", "type": "subtopic", "description": "Derivatives, gradients, optimization", "position": {"x": 50, "y": 12}, "children": ["statistics"]},
            {"id": "statistics", "title": "Statistics", "type": "subtopic", "description": "Descriptive & inferential statistics", "position": {"x": 70, "y": 12}, "children": ["probability", "distributions"]},
            {"id": "probability", "title": "Probability Theory", "type": "subtopic", "description": "Probability distributions, Bayes theorem", "position": {"x": 60, "y": 18}, "children": ["excel"]},
            {"id": "distributions", "title": "Statistical Distributions", "type": "subtopic", "description": "Normal, binomial, Poisson", "position": {"x": 70, "y": 18}, "children": ["excel"]},
            {"id": "hypothesis-testing", "title": "Hypothesis Testing", "type": "subtopic", "description": "t-tests, chi-square, ANOVA", "position": {"x": 80, "y": 18}, "children": ["excel"]},
            
            # Excel - Expanded
            {"id": "excel", "title": "Excel", "type": "topic", "description": "Advanced Excel for data analysis", "position": {"x": 50, "y": 25}, "children": ["excel-basics", "pivot-tables", "excel-functions"]},
            {"id": "excel-basics", "title": "Excel Basics", "type": "subtopic", "description": "Formulas, formatting, data entry", "position": {"x": 30, "y": 32}, "children": ["sql"]},
            {"id": "pivot-tables", "title": "Pivot Tables", "type": "subtopic", "description": "Data summarization & analysis", "position": {"x": 45, "y": 32}, "children": ["sql"]},
            {"id": "excel-functions", "title": "Excel Functions", "type": "subtopic", "description": "VLOOKUP, INDEX-MATCH, SUMIFS", "position": {"x": 60, "y": 32}, "children": ["sql"]},
            {"id": "charts", "title": "Charts & Dashboards", "type": "subtopic", "description": "Data visualization in Excel", "position": {"x": 75, "y": 32}, "children": ["sql"]},
            
            # SQL - Expanded
            {"id": "sql", "title": "SQL", "type": "topic", "description": "Database querying & management", "position": {"x": 50, "y": 39}, "children": ["sql-basics", "joins", "advanced-sql"]},
            {"id": "sql-basics", "title": "SQL Basics", "type": "subtopic", "description": "SELECT, WHERE, ORDER BY", "position": {"x": 25, "y": 46}, "children": ["python-basics"]},
            {"id": "joins", "title": "SQL Joins", "type": "subtopic", "description": "INNER, LEFT, RIGHT, FULL joins", "position": {"x": 40, "y": 46}, "children": ["python-basics"]},
            {"id": "aggregations", "title": "Aggregations", "type": "subtopic", "description": "GROUP BY, COUNT, SUM, AVG", "position": {"x": 55, "y": 46}, "children": ["python-basics"]},
            {"id": "advanced-sql", "title": "Advanced SQL", "type": "subtopic", "description": "Window functions, CTEs, subqueries", "position": {"x": 70, "y": 46}, "children": ["python-basics"]},
            {"id": "sql-optimization", "title": "Query Optimization", "type": "subtopic", "description": "Indexes, execution plans", "position": {"x": 85, "y": 46}, "children": ["python-basics"]},
            
            # Python - Expanded
            {"id": "python-basics", "title": "Python Programming", "type": "topic", "description": "Python for data science", "position": {"x": 50, "y": 53}, "children": ["python-fundamentals", "pandas", "numpy"]},
            {"id": "python-fundamentals", "title": "Python Fundamentals", "type": "subtopic", "description": "Syntax, data types, control flow", "position": {"x": 25, "y": 60}, "children": ["data-cleaning"]},
            {"id": "numpy", "title": "NumPy", "type": "subtopic", "description": "Numerical computing, arrays", "position": {"x": 40, "y": 60}, "children": ["data-cleaning"]},
            {"id": "pandas", "title": "Pandas", "type": "subtopic", "description": "DataFrames, data manipulation", "position": {"x": 55, "y": 60}, "children": ["data-cleaning"]},
            {"id": "pandas-advanced", "title": "Advanced Pandas", "type": "subtopic", "description": "Merge, groupby, pivot, time series", "position": {"x": 70, "y": 60}, "children": ["data-cleaning"]},
            
            # Data Cleaning & Preprocessing
            {"id": "data-cleaning", "title": "Data Cleaning", "type": "topic", "description": "Data preprocessing & wrangling", "position": {"x": 50, "y": 67}, "children": ["missing-data", "outliers", "feature-engineering"]},
            {"id": "missing-data", "title": "Missing Data", "type": "subtopic", "description": "Imputation techniques", "position": {"x": 35, "y": 74}, "children": ["visualization"]},
            {"id": "outliers", "title": "Outlier Detection", "type": "subtopic", "description": "Identifying & handling outliers", "position": {"x": 50, "y": 74}, "children": ["visualization"]},
            {"id": "feature-engineering", "title": "Feature Engineering", "type": "subtopic", "description": "Creating & transforming features", "position": {"x": 65, "y": 74}, "children": ["visualization"]},
            
            # Data Visualization - Expanded
            {"id": "visualization", "title": "Data Visualization", "type": "topic", "description": "Visual storytelling with data", "position": {"x": 50, "y": 81}, "children": ["matplotlib", "seaborn", "plotly", "tableau"]},
            {"id": "matplotlib", "title": "Matplotlib", "type": "subtopic", "description": "Basic plotting library", "position": {"x": 25, "y": 88}, "children": ["ml-basics"]},
            {"id": "seaborn", "title": "Seaborn", "type": "subtopic", "description": "Statistical visualizations", "position": {"x": 40, "y": 88}, "children": ["ml-basics"]},
            {"id": "plotly", "title": "Plotly", "type": "subtopic", "description": "Interactive visualizations", "position": {"x": 55, "y": 88}, "children": ["ml-basics"]},
            {"id": "tableau", "title": "Tableau", "type": "subtopic", "description": "Business intelligence tool", "position": {"x": 70, "y": 88}, "children": ["ml-basics"]},
            {"id": "powerbi", "title": "Power BI", "type": "optional", "description": "Microsoft BI platform", "position": {"x": 85, "y": 88}, "children": ["ml-basics"]},
            
            # Machine Learning - Expanded
            {"id": "ml-basics", "title": "Machine Learning", "type": "topic", "description": "ML algorithms & techniques", "position": {"x": 50, "y": 95}, "children": ["supervised-learning", "unsupervised-learning", "sklearn"]},
            {"id": "supervised-learning", "title": "Supervised Learning", "type": "subtopic", "description": "Regression & classification", "position": {"x": 30, "y": 102}, "children": ["regression", "classification"]},
            {"id": "regression", "title": "Regression", "type": "subtopic", "description": "Linear, polynomial, ridge, lasso", "position": {"x": 25, "y": 108}, "children": ["model-evaluation"]},
            {"id": "classification", "title": "Classification", "type": "subtopic", "description": "Logistic, decision trees, SVM, random forest", "position": {"x": 35, "y": 108}, "children": ["model-evaluation"]},
            {"id": "unsupervised-learning", "title": "Unsupervised Learning", "type": "subtopic", "description": "Clustering & dimensionality reduction", "position": {"x": 55, "y": 102}, "children": ["clustering", "pca"]},
            {"id": "clustering", "title": "Clustering", "type": "subtopic", "description": "K-means, hierarchical, DBSCAN", "position": {"x": 52, "y": 108}, "children": ["model-evaluation"]},
            {"id": "pca", "title": "PCA", "type": "subtopic", "description": "Principal component analysis", "position": {"x": 58, "y": 108}, "children": ["model-evaluation"]},
            {"id": "sklearn", "title": "Scikit-learn", "type": "subtopic", "description": "ML library for Python", "position": {"x": 75, "y": 102}, "children": ["model-evaluation"]},
            
            # Model Evaluation
            {"id": "model-evaluation", "title": "Model Evaluation", "type": "topic", "description": "Assessing model performance", "position": {"x": 50, "y": 115}, "children": ["metrics", "cross-validation", "hyperparameter-tuning"]},
            {"id": "metrics", "title": "Evaluation Metrics", "type": "subtopic", "description": "Accuracy, precision, recall, F1, RMSE", "position": {"x": 35, "y": 122}, "children": ["deep-learning"]},
            {"id": "cross-validation", "title": "Cross-Validation", "type": "subtopic", "description": "K-fold, stratified CV", "position": {"x": 50, "y": 122}, "children": ["deep-learning"]},
            {"id": "hyperparameter-tuning", "title": "Hyperparameter Tuning", "type": "subtopic", "description": "Grid search, random search", "position": {"x": 65, "y": 122}, "children": ["deep-learning"]},
            
            # Deep Learning - Optional
            {"id": "deep-learning", "title": "Deep Learning", "type": "optional", "description": "Neural networks & deep learning", "position": {"x": 50, "y": 129}, "children": ["neural-networks", "tensorflow-keras"]},
            {"id": "neural-networks", "title": "Neural Networks", "type": "optional", "description": "Perceptrons, backpropagation", "position": {"x": 40, "y": 136}, "children": ["deployment-ds"]},
            {"id": "tensorflow-keras", "title": "TensorFlow/Keras", "type": "optional", "description": "Deep learning frameworks", "position": {"x": 60, "y": 136}, "children": ["deployment-ds"]},
            
            # Deployment & MLOps
            {"id": "deployment-ds", "title": "Model Deployment", "type": "topic", "description": "Deploying ML models", "position": {"x": 50, "y": 143}, "children": ["flask-api", "docker-ds", "cloud-ds"]},
            {"id": "flask-api", "title": "Flask/FastAPI", "type": "subtopic", "description": "Creating ML APIs", "position": {"x": 35, "y": 150}, "children": ["portfolio-da"]},
            {"id": "docker-ds", "title": "Docker", "type": "optional", "description": "Containerizing models", "position": {"x": 50, "y": 150}, "children": ["portfolio-da"]},
            {"id": "cloud-ds", "title": "Cloud Platforms", "type": "optional", "description": "AWS, GCP, Azure ML", "position": {"x": 65, "y": 150}, "children": ["portfolio-da"]},
            
            # Portfolio
            {"id": "portfolio-da", "title": "Build Portfolio", "type": "milestone", "description": "Create 5-7 data science projects with end-to-end ML pipelines", "position": {"x": 50, "y": 157}, "children": []}
        ]
    },
    
    "fullstack_developer": {
        "name": "Full Stack Web Development",
        "description": "Complete roadmap for Full Stack Developer",
        "nodes": [
            # Frontend Fundamentals - Expanded
            {"id": "html-basics", "title": "HTML", "type": "topic", "description": "HTML fundamentals", "position": {"x": 30, "y": 5}, "children": ["html-semantic", "html-forms"]},
            {"id": "html-semantic", "title": "Semantic HTML", "type": "subtopic", "description": "header, nav, main, article", "position": {"x": 25, "y": 12}, "children": ["css-basics"]},
            {"id": "html-forms", "title": "Forms & Validation", "type": "subtopic", "description": "Input types, validation", "position": {"x": 35, "y": 12}, "children": ["css-basics"]},
            
            {"id": "css-basics", "title": "CSS", "type": "topic", "description": "Styling fundamentals", "position": {"x": 50, "y": 5}, "children": ["css-flexbox", "css-grid", "responsive-design"]},
            {"id": "css-flexbox", "title": "Flexbox", "type": "subtopic", "description": "Flexible layouts", "position": {"x": 45, "y": 12}, "children": ["javascript-basics"]},
            {"id": "css-grid", "title": "CSS Grid", "type": "subtopic", "description": "Grid layouts", "position": {"x": 50, "y": 12}, "children": ["javascript-basics"]},
            {"id": "responsive-design", "title": "Responsive Design", "type": "subtopic", "description": "Media queries, mobile-first", "position": {"x": 55, "y": 12}, "children": ["javascript-basics"]},
            
            {"id": "javascript-basics", "title": "JavaScript", "type": "topic", "description": "JS fundamentals", "position": {"x": 70, "y": 5}, "children": ["js-dom", "js-es6", "javascript-advanced"]},
            {"id": "js-dom", "title": "DOM Manipulation", "type": "subtopic", "description": "querySelector, events", "position": {"x": 65, "y": 12}, "children": ["react-fullstack"]},
            {"id": "js-es6", "title": "ES6+ Features", "type": "subtopic", "description": "Arrow functions, destructuring", "position": {"x": 70, "y": 12}, "children": ["react-fullstack"]},
            {"id": "javascript-advanced", "title": "Advanced JS", "type": "subtopic", "description": "Async/await, promises, closures", "position": {"x": 75, "y": 12}, "children": ["react-fullstack"]},
            
            # React - Expanded
            {"id": "react-fullstack", "title": "React", "type": "topic", "description": "Frontend framework", "position": {"x": 50, "y": 19}, "children": ["react-basics", "react-hooks", "react-router"]},
            {"id": "react-basics", "title": "React Basics", "type": "subtopic", "description": "Components, props, JSX", "position": {"x": 35, "y": 26}, "children": ["nodejs"]},
            {"id": "react-hooks", "title": "React Hooks", "type": "subtopic", "description": "useState, useEffect, custom hooks", "position": {"x": 50, "y": 26}, "children": ["nodejs"]},
            {"id": "react-router", "title": "React Router", "type": "subtopic", "description": "Client-side routing", "position": {"x": 65, "y": 26}, "children": ["nodejs"]},
            {"id": "react-state", "title": "State Management", "type": "subtopic", "description": "Context API, Redux", "position": {"x": 80, "y": 26}, "children": ["nodejs"]},
            
            # Backend - Node.js Expanded
            {"id": "nodejs", "title": "Node.js", "type": "topic", "description": "Backend JavaScript runtime", "position": {"x": 50, "y": 33}, "children": ["node-basics", "express", "npm"]},
            {"id": "node-basics", "title": "Node.js Basics", "type": "subtopic", "description": "Modules, file system, events", "position": {"x": 35, "y": 40}, "children": ["databases-fullstack"]},
            {"id": "express", "title": "Express.js", "type": "subtopic", "description": "Web framework, routing, middleware", "position": {"x": 50, "y": 40}, "children": ["databases-fullstack"]},
            {"id": "npm", "title": "NPM/Yarn", "type": "subtopic", "description": "Package management", "position": {"x": 65, "y": 40}, "children": ["databases-fullstack"]},
            
            # Databases - Expanded
            {"id": "databases-fullstack", "title": "Databases", "type": "topic", "description": "SQL & NoSQL", "position": {"x": 50, "y": 47}, "children": ["mongodb", "postgresql", "orm"]},
            {"id": "mongodb", "title": "MongoDB", "type": "subtopic", "description": "NoSQL document database", "position": {"x": 30, "y": 54}, "children": ["rest-apis"]},
            {"id": "mongoose", "title": "Mongoose", "type": "subtopic", "description": "MongoDB ODM", "position": {"x": 40, "y": 54}, "children": ["rest-apis"]},
            {"id": "postgresql", "title": "PostgreSQL", "type": "subtopic", "description": "Relational database", "position": {"x": 55, "y": 54}, "children": ["rest-apis"]},
            {"id": "orm", "title": "ORM/Query Builders", "type": "subtopic", "description": "Sequelize, Prisma", "position": {"x": 70, "y": 54}, "children": ["rest-apis"]},
            
            # APIs - Expanded
            {"id": "rest-apis", "title": "REST APIs", "type": "topic", "description": "Building RESTful services", "position": {"x": 50, "y": 61}, "children": ["crud", "middleware", "api-design"]},
            {"id": "crud", "title": "CRUD Operations", "type": "subtopic", "description": "Create, Read, Update, Delete", "position": {"x": 30, "y": 68}, "children": ["auth-fullstack"]},
            {"id": "middleware", "title": "Middleware", "type": "subtopic", "description": "Request/response processing", "position": {"x": 45, "y": 68}, "children": ["auth-fullstack"]},
            {"id": "api-design", "title": "API Design", "type": "subtopic", "description": "RESTful principles, versioning", "position": {"x": 60, "y": 68}, "children": ["auth-fullstack"]},
            {"id": "error-handling-fs", "title": "Error Handling", "type": "subtopic", "description": "Try-catch, error middleware", "position": {"x": 75, "y": 68}, "children": ["auth-fullstack"]},
            
            # Authentication & Security - Expanded
            {"id": "auth-fullstack", "title": "Authentication", "type": "topic", "description": "User authentication & authorization", "position": {"x": 50, "y": 75}, "children": ["jwt", "sessions", "oauth"]},
            {"id": "jwt", "title": "JWT", "type": "subtopic", "description": "JSON Web Tokens", "position": {"x": 30, "y": 82}, "children": ["testing-fullstack"]},
            {"id": "sessions", "title": "Sessions & Cookies", "type": "subtopic", "description": "Session management", "position": {"x": 45, "y": 82}, "children": ["testing-fullstack"]},
            {"id": "oauth", "title": "OAuth 2.0", "type": "optional", "description": "Third-party authentication", "position": {"x": 60, "y": 82}, "children": ["testing-fullstack"]},
            {"id": "security-fs", "title": "Security", "type": "subtopic", "description": "HTTPS, CORS, helmet, rate limiting", "position": {"x": 75, "y": 82}, "children": ["testing-fullstack"]},
            
            # Testing - Expanded
            {"id": "testing-fullstack", "title": "Testing", "type": "topic", "description": "Frontend & backend testing", "position": {"x": 50, "y": 89}, "children": ["unit-test-fs", "integration-test-fs", "e2e-test-fs"]},
            {"id": "unit-test-fs", "title": "Unit Testing", "type": "subtopic", "description": "Jest, Mocha, Chai", "position": {"x": 35, "y": 96}, "children": ["version-control-fs"]},
            {"id": "integration-test-fs", "title": "Integration Testing", "type": "subtopic", "description": "API testing, Supertest", "position": {"x": 50, "y": 96}, "children": ["version-control-fs"]},
            {"id": "e2e-test-fs", "title": "E2E Testing", "type": "subtopic", "description": "Cypress, Playwright", "position": {"x": 65, "y": 96}, "children": ["version-control-fs"]},
            
            # Version Control & DevOps
            {"id": "version-control-fs", "title": "Version Control", "type": "topic", "description": "Git & GitHub", "position": {"x": 50, "y": 103}, "children": ["git-fs", "github-fs"]},
            {"id": "git-fs", "title": "Git", "type": "subtopic", "description": "Branching, merging, rebasing", "position": {"x": 40, "y": 110}, "children": ["deployment-fullstack"]},
            {"id": "github-fs", "title": "GitHub", "type": "subtopic", "description": "Pull requests, code review", "position": {"x": 60, "y": 110}, "children": ["deployment-fullstack"]},
            
            # Deployment - Expanded
            {"id": "deployment-fullstack", "title": "Deployment", "type": "topic", "description": "Deploy full stack applications", "position": {"x": 50, "y": 117}, "children": ["hosting", "docker-fullstack", "cicd-fs"]},
            {"id": "hosting", "title": "Hosting Platforms", "type": "subtopic", "description": "Vercel, Netlify, Heroku, Railway", "position": {"x": 30, "y": 124}, "children": ["portfolio-fullstack"]},
            {"id": "docker-fullstack", "title": "Docker", "type": "optional", "description": "Containerization", "position": {"x": 50, "y": 124}, "children": ["portfolio-fullstack"]},
            {"id": "cicd-fs", "title": "CI/CD", "type": "optional", "description": "GitHub Actions, automated deployment", "position": {"x": 70, "y": 124}, "children": ["portfolio-fullstack"]},
            
            # Advanced Topics
            {"id": "advanced-fs", "title": "Advanced Topics", "type": "optional", "description": "Performance & scalability", "position": {"x": 50, "y": 131}, "children": ["caching-fs", "websockets", "graphql-fs"]},
            {"id": "caching-fs", "title": "Caching", "type": "optional", "description": "Redis, CDN", "position": {"x": 35, "y": 138}, "children": ["portfolio-fullstack"]},
            {"id": "websockets", "title": "WebSockets", "type": "optional", "description": "Real-time communication", "position": {"x": 50, "y": 138}, "children": ["portfolio-fullstack"]},
            {"id": "graphql-fs", "title": "GraphQL", "type": "optional", "description": "Alternative to REST", "position": {"x": 65, "y": 138}, "children": ["portfolio-fullstack"]},
            
            # Portfolio
            {"id": "portfolio-fullstack", "title": "Build Portfolio", "type": "milestone", "description": "Create 4-6 full stack projects (MERN/PERN stack)", "position": {"x": 50, "y": 145}, "children": []}
        ]
    },
    
    "ui_ux_designer": {
        "name": "UI/UX Design",
        "description": "Complete roadmap to become a UI/UX Designer",
        "nodes": [
            # Design Fundamentals - Expanded
            {"id": "design-fundamentals", "title": "Design Fundamentals", "type": "topic", "description": "Core design principles", "position": {"x": 50, "y": 5}, "children": ["color-theory", "typography", "layout", "gestalt"]},
            {"id": "color-theory", "title": "Color Theory", "type": "subtopic", "description": "Color wheel, harmony, psychology", "position": {"x": 25, "y": 12}, "children": ["figma"]},
            {"id": "typography", "title": "Typography", "type": "subtopic", "description": "Font selection, hierarchy, readability", "position": {"x": 40, "y": 12}, "children": ["figma"]},
            {"id": "layout", "title": "Layout & Composition", "type": "subtopic", "description": "Grid systems, visual hierarchy", "position": {"x": 55, "y": 12}, "children": ["figma"]},
            {"id": "gestalt", "title": "Gestalt Principles", "type": "subtopic", "description": "Proximity, similarity, closure", "position": {"x": 70, "y": 12}, "children": ["figma"]},
            {"id": "whitespace", "title": "Whitespace", "type": "subtopic", "description": "Negative space, breathing room", "position": {"x": 85, "y": 12}, "children": ["figma"]},
            
            # Design Tools - Figma Expanded
            {"id": "figma", "title": "Figma", "type": "topic", "description": "Industry-standard design tool", "position": {"x": 50, "y": 19}, "children": ["figma-basics", "components-design", "prototyping", "auto-layout"]},
            {"id": "figma-basics", "title": "Figma Basics", "type": "subtopic", "description": "Frames, layers, shapes, text", "position": {"x": 25, "y": 26}, "children": ["user-research"]},
            {"id": "components-design", "title": "Components & Variants", "type": "subtopic", "description": "Reusable design elements", "position": {"x": 40, "y": 26}, "children": ["user-research"]},
            {"id": "prototyping", "title": "Prototyping", "type": "subtopic", "description": "Interactive prototypes, animations", "position": {"x": 55, "y": 26}, "children": ["user-research"]},
            {"id": "auto-layout", "title": "Auto Layout", "type": "subtopic", "description": "Responsive components", "position": {"x": 70, "y": 26}, "children": ["user-research"]},
            {"id": "design-systems-tool", "title": "Design Systems", "type": "subtopic", "description": "Building component libraries", "position": {"x": 85, "y": 26}, "children": ["user-research"]},
            
            # User Research - Expanded
            {"id": "user-research", "title": "User Research", "type": "topic", "description": "Understanding user needs", "position": {"x": 50, "y": 33}, "children": ["research-methods", "personas", "user-interviews", "surveys"]},
            {"id": "research-methods", "title": "Research Methods", "type": "subtopic", "description": "Qualitative vs quantitative", "position": {"x": 25, "y": 40}, "children": ["information-architecture"]},
            {"id": "personas", "title": "User Personas", "type": "subtopic", "description": "Creating user profiles", "position": {"x": 40, "y": 40}, "children": ["information-architecture"]},
            {"id": "user-interviews", "title": "User Interviews", "type": "subtopic", "description": "Conducting interviews, gathering insights", "position": {"x": 55, "y": 40}, "children": ["information-architecture"]},
            {"id": "surveys", "title": "Surveys & Questionnaires", "type": "subtopic", "description": "Collecting user feedback", "position": {"x": 70, "y": 40}, "children": ["information-architecture"]},
            {"id": "empathy-maps", "title": "Empathy Maps", "type": "subtopic", "description": "Understanding user emotions", "position": {"x": 85, "y": 40}, "children": ["information-architecture"]},
            
            # Information Architecture
            {"id": "information-architecture", "title": "Information Architecture", "type": "topic", "description": "Organizing content & navigation", "position": {"x": 50, "y": 47}, "children": ["site-maps", "user-flows", "card-sorting"]},
            {"id": "site-maps", "title": "Site Maps", "type": "subtopic", "description": "Content structure", "position": {"x": 35, "y": 54}, "children": ["wireframing"]},
            {"id": "user-flows", "title": "User Flows", "type": "subtopic", "description": "User journey mapping", "position": {"x": 50, "y": 54}, "children": ["wireframing"]},
            {"id": "card-sorting", "title": "Card Sorting", "type": "subtopic", "description": "Content organization", "position": {"x": 65, "y": 54}, "children": ["wireframing"]},
            
            # Wireframing - Expanded
            {"id": "wireframing", "title": "Wireframing", "type": "topic", "description": "Low to high fidelity designs", "position": {"x": 50, "y": 61}, "children": ["lofi", "hifi", "sketching"]},
            {"id": "sketching", "title": "Sketching", "type": "subtopic", "description": "Paper prototyping, rapid ideation", "position": {"x": 30, "y": 68}, "children": ["ui-design"]},
            {"id": "lofi", "title": "Lo-Fi Wireframes", "type": "subtopic", "description": "Basic layouts, structure", "position": {"x": 45, "y": 68}, "children": ["ui-design"]},
            {"id": "hifi", "title": "Hi-Fi Wireframes", "type": "subtopic", "description": "Detailed mockups", "position": {"x": 60, "y": 68}, "children": ["ui-design"]},
            {"id": "annotations", "title": "Annotations", "type": "subtopic", "description": "Documenting design decisions", "position": {"x": 75, "y": 68}, "children": ["ui-design"]},
            
            # UI Design - Expanded
            {"id": "ui-design", "title": "UI Design", "type": "topic", "description": "Visual interface design", "position": {"x": 50, "y": 75}, "children": ["design-systems", "responsive-ui", "mobile-design", "web-design"]},
            {"id": "design-systems", "title": "Design Systems", "type": "subtopic", "description": "Consistent design language", "position": {"x": 25, "y": 82}, "children": ["accessibility-design"]},
            {"id": "responsive-ui", "title": "Responsive Design", "type": "subtopic", "description": "Adaptive layouts", "position": {"x": 40, "y": 82}, "children": ["accessibility-design"]},
            {"id": "mobile-design", "title": "Mobile Design", "type": "subtopic", "description": "iOS & Android patterns", "position": {"x": 55, "y": 82}, "children": ["accessibility-design"]},
            {"id": "web-design", "title": "Web Design", "type": "subtopic", "description": "Desktop interfaces", "position": {"x": 70, "y": 82}, "children": ["accessibility-design"]},
            {"id": "iconography", "title": "Iconography", "type": "subtopic", "description": "Icon design & usage", "position": {"x": 85, "y": 82}, "children": ["accessibility-design"]},
            
            # Accessibility
            {"id": "accessibility-design", "title": "Accessibility", "type": "topic", "description": "Inclusive design", "position": {"x": 50, "y": 89}, "children": ["wcag", "aria-design", "contrast"]},
            {"id": "wcag", "title": "WCAG Guidelines", "type": "subtopic", "description": "Web accessibility standards", "position": {"x": 35, "y": 96}, "children": ["usability-testing"]},
            {"id": "aria-design", "title": "ARIA", "type": "subtopic", "description": "Accessible labels & roles", "position": {"x": 50, "y": 96}, "children": ["usability-testing"]},
            {"id": "contrast", "title": "Color Contrast", "type": "subtopic", "description": "Readability & accessibility", "position": {"x": 65, "y": 96}, "children": ["usability-testing"]},
            
            # Usability Testing - Expanded
            {"id": "usability-testing", "title": "Usability Testing", "type": "topic", "description": "Testing with real users", "position": {"x": 50, "y": 103}, "children": ["test-planning", "ab-testing", "heuristics", "analytics-design"]},
            {"id": "test-planning", "title": "Test Planning", "type": "subtopic", "description": "Creating test scenarios", "position": {"x": 30, "y": 110}, "children": ["interaction-design"]},
            {"id": "ab-testing", "title": "A/B Testing", "type": "subtopic", "description": "Comparing design variants", "position": {"x": 45, "y": 110}, "children": ["interaction-design"]},
            {"id": "heuristics", "title": "Heuristic Evaluation", "type": "subtopic", "description": "Expert review, Nielsen's heuristics", "position": {"x": 60, "y": 110}, "children": ["interaction-design"]},
            {"id": "analytics-design", "title": "Analytics", "type": "subtopic", "description": "Measuring user behavior", "position": {"x": 75, "y": 110}, "children": ["interaction-design"]},
            
            # Interaction Design - Expanded
            {"id": "interaction-design", "title": "Interaction Design", "type": "topic", "description": "Micro-interactions & animations", "position": {"x": 50, "y": 117}, "children": ["animations", "transitions", "micro-interactions", "motion-principles"]},
            {"id": "animations", "title": "Animations", "type": "subtopic", "description": "Motion design, easing", "position": {"x": 30, "y": 124}, "children": ["design-handoff"]},
            {"id": "transitions", "title": "Transitions", "type": "subtopic", "description": "Smooth state changes", "position": {"x": 45, "y": 124}, "children": ["design-handoff"]},
            {"id": "micro-interactions", "title": "Micro-interactions", "type": "subtopic", "description": "Button states, hover effects", "position": {"x": 60, "y": 124}, "children": ["design-handoff"]},
            {"id": "motion-principles", "title": "Motion Principles", "type": "subtopic", "description": "Timing, choreography", "position": {"x": 75, "y": 124}, "children": ["design-handoff"]},
            
            # Design Handoff & Collaboration
            {"id": "design-handoff", "title": "Design Handoff", "type": "topic", "description": "Developer collaboration", "position": {"x": 50, "y": 131}, "children": ["design-specs", "dev-collaboration", "design-tokens"]},
            {"id": "design-specs", "title": "Design Specifications", "type": "subtopic", "description": "Documenting designs", "position": {"x": 35, "y": 138}, "children": ["portfolio-design"]},
            {"id": "dev-collaboration", "title": "Developer Collaboration", "type": "subtopic", "description": "Working with developers", "position": {"x": 50, "y": 138}, "children": ["portfolio-design"]},
            {"id": "design-tokens", "title": "Design Tokens", "type": "subtopic", "description": "Design-to-code workflow", "position": {"x": 65, "y": 138}, "children": ["portfolio-design"]},
            
            # Portfolio
            {"id": "portfolio-design", "title": "Build Portfolio", "type": "milestone", "description": "Create 5-7 case studies with full design process", "position": {"x": 50, "y": 145}, "children": []}
        ]
    },
    
    "digital_marketing": {
        "name": "Digital Marketing",
        "description": "Complete roadmap for Digital Marketing Specialist",
        "nodes": [
            # Marketing Fundamentals - Expanded
            {"id": "marketing-fundamentals", "title": "Marketing Fundamentals", "type": "topic", "description": "Core marketing concepts", "position": {"x": 50, "y": 5}, "children": ["4ps", "customer-journey", "marketing-strategy"]},
            {"id": "4ps", "title": "4 Ps of Marketing", "type": "subtopic", "description": "Product, Price, Place, Promotion", "position": {"x": 30, "y": 12}, "children": ["content-marketing"]},
            {"id": "customer-journey", "title": "Customer Journey", "type": "subtopic", "description": "Awareness, consideration, decision", "position": {"x": 50, "y": 12}, "children": ["content-marketing"]},
            {"id": "marketing-strategy", "title": "Marketing Strategy", "type": "subtopic", "description": "Target audience, positioning", "position": {"x": 70, "y": 12}, "children": ["content-marketing"]},
            
            # Content Marketing - Expanded
            {"id": "content-marketing", "title": "Content Marketing", "type": "topic", "description": "Creating valuable content", "position": {"x": 50, "y": 19}, "children": ["blogging", "copywriting", "content-strategy", "storytelling"]},
            {"id": "blogging", "title": "Blogging", "type": "subtopic", "description": "Writing engaging blog posts", "position": {"x": 25, "y": 26}, "children": ["seo-marketing"]},
            {"id": "copywriting", "title": "Copywriting", "type": "subtopic", "description": "Persuasive writing, CTAs", "position": {"x": 40, "y": 26}, "children": ["seo-marketing"]},
            {"id": "content-strategy", "title": "Content Strategy", "type": "subtopic", "description": "Content calendar, planning", "position": {"x": 55, "y": 26}, "children": ["seo-marketing"]},
            {"id": "storytelling", "title": "Storytelling", "type": "subtopic", "description": "Brand narratives", "position": {"x": 70, "y": 26}, "children": ["seo-marketing"]},
            {"id": "video-content", "title": "Video Content", "type": "subtopic", "description": "YouTube, TikTok, Reels", "position": {"x": 85, "y": 26}, "children": ["seo-marketing"]},
            
            # SEO - Expanded
            {"id": "seo-marketing", "title": "SEO", "type": "topic", "description": "Search Engine Optimization", "position": {"x": 50, "y": 33}, "children": ["keyword-research", "on-page-seo", "off-page-seo", "technical-seo"]},
            {"id": "keyword-research", "title": "Keyword Research", "type": "subtopic", "description": "Finding search terms", "position": {"x": 20, "y": 40}, "children": ["social-media"]},
            {"id": "on-page-seo", "title": "On-Page SEO", "type": "subtopic", "description": "Content optimization, meta tags", "position": {"x": 35, "y": 40}, "children": ["social-media"]},
            {"id": "off-page-seo", "title": "Off-Page SEO", "type": "subtopic", "description": "Link building, backlinks", "position": {"x": 50, "y": 40}, "children": ["social-media"]},
            {"id": "technical-seo", "title": "Technical SEO", "type": "subtopic", "description": "Site speed, mobile-friendly", "position": {"x": 65, "y": 40}, "children": ["social-media"]},
            {"id": "local-seo", "title": "Local SEO", "type": "subtopic", "description": "Google My Business", "position": {"x": 80, "y": 40}, "children": ["social-media"]},
            
            # Social Media Marketing - Expanded
            {"id": "social-media", "title": "Social Media Marketing", "type": "topic", "description": "Social platforms strategy", "position": {"x": 50, "y": 47}, "children": ["facebook-marketing", "instagram", "linkedin", "twitter", "tiktok"]},
            {"id": "facebook-marketing", "title": "Facebook Marketing", "type": "subtopic", "description": "Organic & paid strategies", "position": {"x": 20, "y": 54}, "children": ["email-marketing"]},
            {"id": "instagram", "title": "Instagram Marketing", "type": "subtopic", "description": "Visual content, stories, reels", "position": {"x": 35, "y": 54}, "children": ["email-marketing"]},
            {"id": "linkedin", "title": "LinkedIn Marketing", "type": "subtopic", "description": "B2B marketing, networking", "position": {"x": 50, "y": 54}, "children": ["email-marketing"]},
            {"id": "twitter", "title": "Twitter/X Marketing", "type": "subtopic", "description": "Real-time engagement", "position": {"x": 65, "y": 54}, "children": ["email-marketing"]},
            {"id": "tiktok", "title": "TikTok Marketing", "type": "subtopic", "description": "Short-form video content", "position": {"x": 80, "y": 54}, "children": ["email-marketing"]},
            
            # Email Marketing - Expanded
            {"id": "email-marketing", "title": "Email Marketing", "type": "topic", "description": "Email campaigns & automation", "position": {"x": 50, "y": 61}, "children": ["email-list", "email-automation", "newsletters", "email-design"]},
            {"id": "email-list", "title": "List Building", "type": "subtopic", "description": "Growing email subscribers", "position": {"x": 30, "y": 68}, "children": ["paid-advertising"]},
            {"id": "email-automation", "title": "Email Automation", "type": "subtopic", "description": "Drip campaigns, workflows", "position": {"x": 45, "y": 68}, "children": ["paid-advertising"]},
            {"id": "newsletters", "title": "Newsletters", "type": "subtopic", "description": "Regular email content", "position": {"x": 60, "y": 68}, "children": ["paid-advertising"]},
            {"id": "email-design", "title": "Email Design", "type": "subtopic", "description": "Templates, responsive design", "position": {"x": 75, "y": 68}, "children": ["paid-advertising"]},
            
            # Paid Advertising - Expanded
            {"id": "paid-advertising", "title": "Paid Advertising", "type": "topic", "description": "PPC & social ads", "position": {"x": 50, "y": 75}, "children": ["google-ads", "facebook-ads", "display-ads", "retargeting"]},
            {"id": "google-ads", "title": "Google Ads", "type": "subtopic", "description": "Search & display campaigns", "position": {"x": 25, "y": 82}, "children": ["analytics"]},
            {"id": "facebook-ads", "title": "Facebook/Instagram Ads", "type": "subtopic", "description": "Social media advertising", "position": {"x": 40, "y": 82}, "children": ["analytics"]},
            {"id": "display-ads", "title": "Display Advertising", "type": "subtopic", "description": "Banner ads, GDN", "position": {"x": 55, "y": 82}, "children": ["analytics"]},
            {"id": "retargeting", "title": "Retargeting", "type": "subtopic", "description": "Pixel tracking, remarketing", "position": {"x": 70, "y": 82}, "children": ["analytics"]},
            {"id": "ad-copywriting", "title": "Ad Copywriting", "type": "subtopic", "description": "Writing compelling ads", "position": {"x": 85, "y": 82}, "children": ["analytics"]},
            
            # Analytics & Measurement - Expanded
            {"id": "analytics", "title": "Analytics & Measurement", "type": "topic", "description": "Measuring marketing performance", "position": {"x": 50, "y": 89}, "children": ["google-analytics", "conversion-tracking", "kpis", "data-analysis"]},
            {"id": "google-analytics", "title": "Google Analytics", "type": "subtopic", "description": "Website analytics, GA4", "position": {"x": 25, "y": 96}, "children": ["marketing-automation"]},
            {"id": "conversion-tracking", "title": "Conversion Tracking", "type": "subtopic", "description": "Goals, funnels, ROI", "position": {"x": 40, "y": 96}, "children": ["marketing-automation"]},
            {"id": "kpis", "title": "Marketing KPIs", "type": "subtopic", "description": "CTR, CPC, ROAS, CAC", "position": {"x": 55, "y": 96}, "children": ["marketing-automation"]},
            {"id": "data-analysis", "title": "Data Analysis", "type": "subtopic", "description": "Excel, dashboards, reporting", "position": {"x": 70, "y": 96}, "children": ["marketing-automation"]},
            {"id": "ab-testing-marketing", "title": "A/B Testing", "type": "subtopic", "description": "Testing campaigns", "position": {"x": 85, "y": 96}, "children": ["marketing-automation"]},
            
            # Marketing Automation & CRM
            {"id": "marketing-automation", "title": "Marketing Automation", "type": "topic", "description": "Automation tools & CRM", "position": {"x": 50, "y": 103}, "children": ["hubspot", "mailchimp", "crm"]},
            {"id": "hubspot", "title": "HubSpot", "type": "optional", "description": "Marketing automation platform", "position": {"x": 35, "y": 110}, "children": ["influencer-marketing"]},
            {"id": "mailchimp", "title": "Mailchimp", "type": "optional", "description": "Email marketing platform", "position": {"x": 50, "y": 110}, "children": ["influencer-marketing"]},
            {"id": "crm", "title": "CRM Systems", "type": "subtopic", "description": "Customer relationship management", "position": {"x": 65, "y": 110}, "children": ["influencer-marketing"]},
            
            # Advanced Topics
            {"id": "influencer-marketing", "title": "Influencer Marketing", "type": "optional", "description": "Collaborating with influencers", "position": {"x": 30, "y": 117}, "children": ["portfolio-marketing"]},
            {"id": "affiliate-marketing", "title": "Affiliate Marketing", "type": "optional", "description": "Partner programs", "position": {"x": 50, "y": 117}, "children": ["portfolio-marketing"]},
            {"id": "conversion-optimization", "title": "Conversion Rate Optimization", "type": "optional", "description": "CRO strategies", "position": {"x": 70, "y": 117}, "children": ["portfolio-marketing"]},
            
            # Portfolio
            {"id": "portfolio-marketing", "title": "Build Portfolio", "type": "milestone", "description": "Create 4-6 marketing campaigns with measurable results", "position": {"x": 50, "y": 124}, "children": []}
        ]
    },
    
    "devops_engineer": {
        "name": "DevOps/Cloud Engineer",
        "description": "Complete roadmap to become a DevOps/Cloud Engineer",
        "nodes": [
            # Linux & OS Fundamentals - Expanded
            {"id": "linux", "title": "Linux Fundamentals", "type": "topic", "description": "Master Linux command line", "position": {"x": 50, "y": 5}, "children": ["linux-basics", "linux-commands", "file-system"]},
            {"id": "linux-basics", "title": "Linux Basics", "type": "subtopic", "description": "Distributions, shell, terminal", "position": {"x": 35, "y": 12}, "children": ["networking"]},
            {"id": "linux-commands", "title": "Linux Commands", "type": "subtopic", "description": "grep, awk, sed, find", "position": {"x": 50, "y": 12}, "children": ["networking"]},
            {"id": "file-system", "title": "File System", "type": "subtopic", "description": "Permissions, ownership, directories", "position": {"x": 65, "y": 12}, "children": ["networking"]},
            
            # Networking - Expanded
            {"id": "networking", "title": "Networking", "type": "topic", "description": "Network fundamentals", "position": {"x": 50, "y": 19}, "children": ["tcp-ip", "dns", "http-https", "load-balancers"]},
            {"id": "tcp-ip", "title": "TCP/IP", "type": "subtopic", "description": "Network protocols", "position": {"x": 30, "y": 26}, "children": ["scripting"]},
            {"id": "dns", "title": "DNS", "type": "subtopic", "description": "Domain name system", "position": {"x": 45, "y": 26}, "children": ["scripting"]},
            {"id": "http-https", "title": "HTTP/HTTPS", "type": "subtopic", "description": "Web protocols, SSL/TLS", "position": {"x": 60, "y": 26}, "children": ["scripting"]},
            {"id": "load-balancers", "title": "Load Balancers", "type": "subtopic", "description": "Nginx, HAProxy", "position": {"x": 75, "y": 26}, "children": ["scripting"]},
            
            # Scripting & Programming - Expanded
            {"id": "scripting", "title": "Scripting", "type": "topic", "description": "Automation scripting", "position": {"x": 50, "y": 33}, "children": ["bash", "python-devops", "yaml"]},
            {"id": "bash", "title": "Bash Scripting", "type": "subtopic", "description": "Shell scripts, automation", "position": {"x": 35, "y": 40}, "children": ["git"]},
            {"id": "python-devops", "title": "Python", "type": "subtopic", "description": "Python for automation", "position": {"x": 50, "y": 40}, "children": ["git"]},
            {"id": "yaml", "title": "YAML/JSON", "type": "subtopic", "description": "Configuration formats", "position": {"x": 65, "y": 40}, "children": ["git"]},
            
            # Version Control - Expanded
            {"id": "git", "title": "Git & Version Control", "type": "topic", "description": "Source control management", "position": {"x": 50, "y": 47}, "children": ["git-basics", "git-workflows", "github-gitlab"]},
            {"id": "git-basics", "title": "Git Basics", "type": "subtopic", "description": "commit, push, pull, branch", "position": {"x": 35, "y": 54}, "children": ["docker"]},
            {"id": "git-workflows", "title": "Git Workflows", "type": "subtopic", "description": "GitFlow, trunk-based", "position": {"x": 50, "y": 54}, "children": ["docker"]},
            {"id": "github-gitlab", "title": "GitHub/GitLab", "type": "subtopic", "description": "Remote repositories", "position": {"x": 65, "y": 54}, "children": ["docker"]},
            
            # Containers - Docker Expanded
            {"id": "docker", "title": "Docker", "type": "topic", "description": "Containerization platform", "position": {"x": 50, "y": 61}, "children": ["docker-basics", "dockerfile", "docker-compose", "docker-networking"]},
            {"id": "docker-basics", "title": "Docker Basics", "type": "subtopic", "description": "Images, containers, volumes", "position": {"x": 25, "y": 68}, "children": ["kubernetes"]},
            {"id": "dockerfile", "title": "Dockerfile", "type": "subtopic", "description": "Building custom images", "position": {"x": 40, "y": 68}, "children": ["kubernetes"]},
            {"id": "docker-compose", "title": "Docker Compose", "type": "subtopic", "description": "Multi-container apps", "position": {"x": 55, "y": 68}, "children": ["kubernetes"]},
            {"id": "docker-networking", "title": "Docker Networking", "type": "subtopic", "description": "Container networking", "position": {"x": 70, "y": 68}, "children": ["kubernetes"]},
            {"id": "docker-registry", "title": "Docker Registry", "type": "subtopic", "description": "Docker Hub, private registries", "position": {"x": 85, "y": 68}, "children": ["kubernetes"]},
            
            # Kubernetes - Expanded
            {"id": "kubernetes", "title": "Kubernetes", "type": "topic", "description": "Container orchestration", "position": {"x": 50, "y": 75}, "children": ["k8s-basics", "pods", "services", "deployments"]},
            {"id": "k8s-basics", "title": "K8s Basics", "type": "subtopic", "description": "Clusters, nodes, kubectl", "position": {"x": 25, "y": 82}, "children": ["cicd"]},
            {"id": "pods", "title": "Pods", "type": "subtopic", "description": "Container groups", "position": {"x": 40, "y": 82}, "children": ["cicd"]},
            {"id": "services", "title": "Services", "type": "subtopic", "description": "Networking, load balancing", "position": {"x": 55, "y": 82}, "children": ["cicd"]},
            {"id": "deployments", "title": "Deployments", "type": "subtopic", "description": "Rolling updates, scaling", "position": {"x": 70, "y": 82}, "children": ["cicd"]},
            {"id": "configmaps-secrets", "title": "ConfigMaps & Secrets", "type": "subtopic", "description": "Configuration management", "position": {"x": 85, "y": 82}, "children": ["cicd"]},
            
            # CI/CD - Expanded
            {"id": "cicd", "title": "CI/CD", "type": "topic", "description": "Continuous integration & deployment", "position": {"x": 50, "y": 89}, "children": ["jenkins", "github-actions", "gitlab-ci", "cicd-pipelines"]},
            {"id": "jenkins", "title": "Jenkins", "type": "subtopic", "description": "Automation server", "position": {"x": 25, "y": 96}, "children": ["cloud"]},
            {"id": "github-actions", "title": "GitHub Actions", "type": "subtopic", "description": "GitHub CI/CD", "position": {"x": 40, "y": 96}, "children": ["cloud"]},
            {"id": "gitlab-ci", "title": "GitLab CI", "type": "subtopic", "description": "GitLab pipelines", "position": {"x": 55, "y": 96}, "children": ["cloud"]},
            {"id": "cicd-pipelines", "title": "Pipeline Design", "type": "subtopic", "description": "Build, test, deploy stages", "position": {"x": 70, "y": 96}, "children": ["cloud"]},
            {"id": "argocd", "title": "ArgoCD", "type": "optional", "description": "GitOps continuous delivery", "position": {"x": 85, "y": 96}, "children": ["cloud"]},
            
            # Cloud Platforms - Expanded
            {"id": "cloud", "title": "Cloud Platforms", "type": "topic", "description": "Cloud infrastructure", "position": {"x": 50, "y": 103}, "children": ["aws", "azure", "gcp", "cloud-services"]},
            {"id": "aws", "title": "AWS", "type": "subtopic", "description": "EC2, S3, RDS, Lambda", "position": {"x": 25, "y": 110}, "children": ["iac"]},
            {"id": "azure", "title": "Azure", "type": "optional", "description": "Microsoft cloud platform", "position": {"x": 40, "y": 110}, "children": ["iac"]},
            {"id": "gcp", "title": "GCP", "type": "optional", "description": "Google Cloud Platform", "position": {"x": 55, "y": 110}, "children": ["iac"]},
            {"id": "cloud-services", "title": "Cloud Services", "type": "subtopic", "description": "Compute, storage, networking", "position": {"x": 70, "y": 110}, "children": ["iac"]},
            {"id": "serverless", "title": "Serverless", "type": "optional", "description": "Lambda, Cloud Functions", "position": {"x": 85, "y": 110}, "children": ["iac"]},
            
            # Infrastructure as Code - Expanded
            {"id": "iac", "title": "Infrastructure as Code", "type": "topic", "description": "Automated infrastructure", "position": {"x": 50, "y": 117}, "children": ["terraform", "ansible", "cloudformation"]},
            {"id": "terraform", "title": "Terraform", "type": "subtopic", "description": "Infrastructure provisioning", "position": {"x": 30, "y": 124}, "children": ["monitoring"]},
            {"id": "ansible", "title": "Ansible", "type": "subtopic", "description": "Configuration management", "position": {"x": 50, "y": 124}, "children": ["monitoring"]},
            {"id": "cloudformation", "title": "CloudFormation", "type": "optional", "description": "AWS infrastructure as code", "position": {"x": 70, "y": 124}, "children": ["monitoring"]},
            
            # Monitoring & Logging - Expanded
            {"id": "monitoring", "title": "Monitoring & Logging", "type": "topic", "description": "Observability & alerting", "position": {"x": 50, "y": 131}, "children": ["prometheus", "grafana", "elk", "alerting"]},
            {"id": "prometheus", "title": "Prometheus", "type": "subtopic", "description": "Metrics collection", "position": {"x": 25, "y": 138}, "children": ["security-devops"]},
            {"id": "grafana", "title": "Grafana", "type": "subtopic", "description": "Visualization & dashboards", "position": {"x": 40, "y": 138}, "children": ["security-devops"]},
            {"id": "elk", "title": "ELK Stack", "type": "subtopic", "description": "Elasticsearch, Logstash, Kibana", "position": {"x": 55, "y": 138}, "children": ["security-devops"]},
            {"id": "alerting", "title": "Alerting", "type": "subtopic", "description": "PagerDuty, Slack alerts", "position": {"x": 70, "y": 138}, "children": ["security-devops"]},
            {"id": "apm", "title": "APM Tools", "type": "optional", "description": "Application performance monitoring", "position": {"x": 85, "y": 138}, "children": ["security-devops"]},
            
            # Security & Best Practices
            {"id": "security-devops", "title": "Security", "type": "topic", "description": "DevSecOps practices", "position": {"x": 50, "y": 145}, "children": ["secrets-management", "security-scanning", "compliance"]},
            {"id": "secrets-management", "title": "Secrets Management", "type": "subtopic", "description": "Vault, AWS Secrets Manager", "position": {"x": 35, "y": 152}, "children": ["portfolio-devops"]},
            {"id": "security-scanning", "title": "Security Scanning", "type": "subtopic", "description": "Vulnerability scanning, SAST/DAST", "position": {"x": 50, "y": 152}, "children": ["portfolio-devops"]},
            {"id": "compliance", "title": "Compliance", "type": "subtopic", "description": "Security standards, auditing", "position": {"x": 65, "y": 152}, "children": ["portfolio-devops"]},
            
            # Portfolio
            {"id": "portfolio-devops", "title": "Build Portfolio", "type": "milestone", "description": "Create 3-5 DevOps projects with CI/CD pipelines", "position": {"x": 50, "y": 159}, "children": []}
        ]
    },
    
    "mobile_developer": {
        "name": "Mobile App Developer",
        "description": "Complete roadmap to become a Mobile App Developer",
        "nodes": [
            # Mobile Fundamentals - Expanded
            {"id": "mobile-basics", "title": "Mobile Development Basics", "type": "topic", "description": "iOS vs Android concepts", "position": {"x": 50, "y": 5}, "children": ["mobile-platforms", "mobile-design-patterns", "app-lifecycle"]},
            {"id": "mobile-platforms", "title": "Platform Differences", "type": "subtopic", "description": "iOS vs Android ecosystems", "position": {"x": 35, "y": 12}, "children": ["programming"]},
            {"id": "mobile-design-patterns", "title": "Mobile Design Patterns", "type": "subtopic", "description": "Navigation, gestures, patterns", "position": {"x": 50, "y": 12}, "children": ["programming"]},
            {"id": "app-lifecycle", "title": "App Lifecycle", "type": "subtopic", "description": "App states, background tasks", "position": {"x": 65, "y": 12}, "children": ["programming"]},
            
            # Programming Languages - Expanded
            {"id": "programming", "title": "Programming Language", "type": "topic", "description": "Choose your stack", "position": {"x": 50, "y": 19}, "children": ["react-native", "swift", "kotlin", "flutter"]},
            {"id": "react-native", "title": "React Native", "type": "subtopic", "description": "Cross-platform with JavaScript", "position": {"x": 25, "y": 26}, "children": ["ui-components"]},
            {"id": "swift", "title": "Swift", "type": "subtopic", "description": "iOS native development", "position": {"x": 40, "y": 26}, "children": ["ui-components"]},
            {"id": "kotlin", "title": "Kotlin", "type": "subtopic", "description": "Android native development", "position": {"x": 55, "y": 26}, "children": ["ui-components"]},
            {"id": "flutter", "title": "Flutter", "type": "optional", "description": "Cross-platform with Dart", "position": {"x": 70, "y": 26}, "children": ["ui-components"]},
            {"id": "java-android", "title": "Java", "type": "optional", "description": "Traditional Android development", "position": {"x": 85, "y": 26}, "children": ["ui-components"]},
            
            # UI Components - Expanded
            {"id": "ui-components", "title": "UI Components", "type": "topic", "description": "Building user interfaces", "position": {"x": 50, "y": 33}, "children": ["views-layouts", "navigation", "styling", "responsive-mobile"]},
            {"id": "views-layouts", "title": "Views & Layouts", "type": "subtopic", "description": "Text, Image, Button, ScrollView", "position": {"x": 25, "y": 40}, "children": ["state-management"]},
            {"id": "navigation", "title": "Navigation", "type": "subtopic", "description": "Stack, tab, drawer navigation", "position": {"x": 40, "y": 40}, "children": ["state-management"]},
            {"id": "styling", "title": "Styling", "type": "subtopic", "description": "StyleSheet, themes, colors", "position": {"x": 55, "y": 40}, "children": ["state-management"]},
            {"id": "responsive-mobile", "title": "Responsive Design", "type": "subtopic", "description": "Different screen sizes", "position": {"x": 70, "y": 40}, "children": ["state-management"]},
            {"id": "animations-mobile", "title": "Animations", "type": "subtopic", "description": "Animated API, transitions", "position": {"x": 85, "y": 40}, "children": ["state-management"]},
            
            # State Management - Expanded
            {"id": "state-management", "title": "State Management", "type": "topic", "description": "Managing app state", "position": {"x": 50, "y": 47}, "children": ["local-state", "redux-mobile", "context-api-mobile", "mobx"]},
            {"id": "local-state", "title": "Local State", "type": "subtopic", "description": "useState, component state", "position": {"x": 30, "y": 54}, "children": ["networking-mobile"]},
            {"id": "redux-mobile", "title": "Redux", "type": "subtopic", "description": "Global state management", "position": {"x": 45, "y": 54}, "children": ["networking-mobile"]},
            {"id": "context-api-mobile", "title": "Context API", "type": "subtopic", "description": "React Context", "position": {"x": 60, "y": 54}, "children": ["networking-mobile"]},
            {"id": "mobx", "title": "MobX", "type": "optional", "description": "Observable state", "position": {"x": 75, "y": 54}, "children": ["networking-mobile"]},
            
            # Networking - Expanded
            {"id": "networking-mobile", "title": "Networking", "type": "topic", "description": "API integration", "position": {"x": 50, "y": 61}, "children": ["rest-mobile", "graphql-mobile", "axios-fetch", "websockets-mobile"]},
            {"id": "rest-mobile", "title": "REST APIs", "type": "subtopic", "description": "RESTful services", "position": {"x": 30, "y": 68}, "children": ["local-storage"]},
            {"id": "graphql-mobile", "title": "GraphQL", "type": "optional", "description": "GraphQL queries", "position": {"x": 45, "y": 68}, "children": ["local-storage"]},
            {"id": "axios-fetch", "title": "Axios/Fetch", "type": "subtopic", "description": "HTTP clients", "position": {"x": 60, "y": 68}, "children": ["local-storage"]},
            {"id": "websockets-mobile", "title": "WebSockets", "type": "optional", "description": "Real-time communication", "position": {"x": 75, "y": 68}, "children": ["local-storage"]},
            
            # Local Storage - Expanded
            {"id": "local-storage", "title": "Local Storage", "type": "topic", "description": "Data persistence", "position": {"x": 50, "y": 75}, "children": ["asyncstorage", "sqlite", "realm", "secure-storage"]},
            {"id": "asyncstorage", "title": "AsyncStorage", "type": "subtopic", "description": "Key-value storage", "position": {"x": 30, "y": 82}, "children": ["native-features"]},
            {"id": "sqlite", "title": "SQLite", "type": "subtopic", "description": "Local database", "position": {"x": 45, "y": 82}, "children": ["native-features"]},
            {"id": "realm", "title": "Realm", "type": "optional", "description": "Mobile database", "position": {"x": 60, "y": 82}, "children": ["native-features"]},
            {"id": "secure-storage", "title": "Secure Storage", "type": "subtopic", "description": "Encrypted storage", "position": {"x": 75, "y": 82}, "children": ["native-features"]},
            
            # Native Features - Expanded
            {"id": "native-features", "title": "Native Features", "type": "topic", "description": "Device capabilities", "position": {"x": 50, "y": 89}, "children": ["camera", "gps", "notifications", "permissions", "biometrics"]},
            {"id": "camera", "title": "Camera", "type": "subtopic", "description": "Photo & video capture", "position": {"x": 20, "y": 96}, "children": ["testing-mobile"]},
            {"id": "gps", "title": "GPS/Location", "type": "subtopic", "description": "Geolocation services", "position": {"x": 35, "y": 96}, "children": ["testing-mobile"]},
            {"id": "notifications", "title": "Push Notifications", "type": "subtopic", "description": "FCM, APNs", "position": {"x": 50, "y": 96}, "children": ["testing-mobile"]},
            {"id": "permissions", "title": "Permissions", "type": "subtopic", "description": "Runtime permissions", "position": {"x": 65, "y": 96}, "children": ["testing-mobile"]},
            {"id": "biometrics", "title": "Biometrics", "type": "subtopic", "description": "Face ID, Touch ID", "position": {"x": 80, "y": 96}, "children": ["testing-mobile"]},
            
            # Testing - Expanded
            {"id": "testing-mobile", "title": "Testing", "type": "topic", "description": "Mobile app testing", "position": {"x": 50, "y": 103}, "children": ["unit-testing-mobile", "integration-testing-mobile", "e2e-mobile"]},
            {"id": "unit-testing-mobile", "title": "Unit Testing", "type": "subtopic", "description": "Jest, testing library", "position": {"x": 35, "y": 110}, "children": ["performance-mobile"]},
            {"id": "integration-testing-mobile", "title": "Integration Testing", "type": "subtopic", "description": "Component testing", "position": {"x": 50, "y": 110}, "children": ["performance-mobile"]},
            {"id": "e2e-mobile", "title": "E2E Testing", "type": "subtopic", "description": "Detox, Appium", "position": {"x": 65, "y": 110}, "children": ["performance-mobile"]},
            
            # Performance & Optimization
            {"id": "performance-mobile", "title": "Performance", "type": "topic", "description": "App optimization", "position": {"x": 50, "y": 117}, "children": ["memory-management", "lazy-loading", "code-splitting"]},
            {"id": "memory-management", "title": "Memory Management", "type": "subtopic", "description": "Preventing memory leaks", "position": {"x": 35, "y": 124}, "children": ["deployment-mobile"]},
            {"id": "lazy-loading", "title": "Lazy Loading", "type": "subtopic", "description": "Loading optimization", "position": {"x": 50, "y": 124}, "children": ["deployment-mobile"]},
            {"id": "code-splitting", "title": "Code Splitting", "type": "subtopic", "description": "Bundle optimization", "position": {"x": 65, "y": 124}, "children": ["deployment-mobile"]},
            
            # Deployment - Expanded
            {"id": "deployment-mobile", "title": "App Deployment", "type": "topic", "description": "Publishing apps", "position": {"x": 50, "y": 131}, "children": ["app-store", "play-store", "code-signing", "app-updates"]},
            {"id": "app-store", "title": "App Store", "type": "subtopic", "description": "iOS app submission", "position": {"x": 30, "y": 138}, "children": ["portfolio-mobile"]},
            {"id": "play-store", "title": "Play Store", "type": "subtopic", "description": "Android app submission", "position": {"x": 45, "y": 138}, "children": ["portfolio-mobile"]},
            {"id": "code-signing", "title": "Code Signing", "type": "subtopic", "description": "Certificates, provisioning", "position": {"x": 60, "y": 138}, "children": ["portfolio-mobile"]},
            {"id": "app-updates", "title": "App Updates", "type": "subtopic", "description": "OTA updates, versioning", "position": {"x": 75, "y": 138}, "children": ["portfolio-mobile"]},
            
            # Portfolio
            {"id": "portfolio-mobile", "title": "Build Portfolio", "type": "milestone", "description": "Create 3-5 mobile apps and publish to stores", "position": {"x": 50, "y": 145}, "children": []}
        ]
    },
    
    "ai_ml_engineer": {
        "name": "AI/ML Engineer",
        "description": "Complete roadmap to become an AI/ML Engineer",
        "nodes": [
            # Python & Programming - Expanded
            {"id": "python-ml", "title": "Python for ML", "type": "topic", "description": "Python fundamentals", "position": {"x": 50, "y": 5}, "children": ["python-basics-ml", "numpy", "pandas-ml", "matplotlib-ml"]},
            {"id": "python-basics-ml", "title": "Python Basics", "type": "subtopic", "description": "Syntax, data structures, OOP", "position": {"x": 25, "y": 12}, "children": ["math-ml"]},
            {"id": "numpy", "title": "NumPy", "type": "subtopic", "description": "Numerical computing, arrays", "position": {"x": 40, "y": 12}, "children": ["math-ml"]},
            {"id": "pandas-ml", "title": "Pandas", "type": "subtopic", "description": "Data manipulation", "position": {"x": 55, "y": 12}, "children": ["math-ml"]},
            {"id": "matplotlib-ml", "title": "Matplotlib/Seaborn", "type": "subtopic", "description": "Data visualization", "position": {"x": 70, "y": 12}, "children": ["math-ml"]},
            {"id": "jupyter", "title": "Jupyter Notebooks", "type": "subtopic", "description": "Interactive development", "position": {"x": 85, "y": 12}, "children": ["math-ml"]},
            
            # Mathematics - Expanded
            {"id": "math-ml", "title": "Mathematics", "type": "topic", "description": "Mathematical foundations", "position": {"x": 50, "y": 19}, "children": ["linear-algebra-ml", "calculus-ml", "statistics-ml", "probability-ml"]},
            {"id": "linear-algebra-ml", "title": "Linear Algebra", "type": "subtopic", "description": "Vectors, matrices, eigenvalues", "position": {"x": 25, "y": 26}, "children": ["ml-basics"]},
            {"id": "calculus-ml", "title": "Calculus", "type": "subtopic", "description": "Derivatives, gradients, optimization", "position": {"x": 40, "y": 26}, "children": ["ml-basics"]},
            {"id": "statistics-ml", "title": "Statistics", "type": "subtopic", "description": "Distributions, hypothesis testing", "position": {"x": 55, "y": 26}, "children": ["ml-basics"]},
            {"id": "probability-ml", "title": "Probability", "type": "subtopic", "description": "Bayes theorem, conditional probability", "position": {"x": 70, "y": 26}, "children": ["ml-basics"]},
            
            # ML Fundamentals - Expanded
            {"id": "ml-basics", "title": "ML Fundamentals", "type": "topic", "description": "Machine learning basics", "position": {"x": 50, "y": 33}, "children": ["supervised-ml", "unsupervised-ml", "ml-workflow"]},
            {"id": "supervised-ml", "title": "Supervised Learning", "type": "subtopic", "description": "Regression, classification", "position": {"x": 30, "y": 40}, "children": ["sklearn"]},
            {"id": "unsupervised-ml", "title": "Unsupervised Learning", "type": "subtopic", "description": "Clustering, dimensionality reduction", "position": {"x": 50, "y": 40}, "children": ["sklearn"]},
            {"id": "ml-workflow", "title": "ML Workflow", "type": "subtopic", "description": "Data prep, training, evaluation", "position": {"x": 70, "y": 40}, "children": ["sklearn"]},
            
            # Scikit-learn - Expanded
            {"id": "sklearn", "title": "Scikit-learn", "type": "topic", "description": "Classical ML algorithms", "position": {"x": 50, "y": 47}, "children": ["regression-ml", "classification-ml", "clustering-ml", "model-selection"]},
            {"id": "regression-ml", "title": "Regression", "type": "subtopic", "description": "Linear, polynomial, ridge, lasso", "position": {"x": 25, "y": 54}, "children": ["deep-learning"]},
            {"id": "classification-ml", "title": "Classification", "type": "subtopic", "description": "Logistic, SVM, decision trees, random forest", "position": {"x": 40, "y": 54}, "children": ["deep-learning"]},
            {"id": "clustering-ml", "title": "Clustering", "type": "subtopic", "description": "K-means, DBSCAN, hierarchical", "position": {"x": 55, "y": 54}, "children": ["deep-learning"]},
            {"id": "model-selection", "title": "Model Selection", "type": "subtopic", "description": "Cross-validation, hyperparameter tuning", "position": {"x": 70, "y": 54}, "children": ["deep-learning"]},
            {"id": "ensemble-methods", "title": "Ensemble Methods", "type": "subtopic", "description": "Bagging, boosting, stacking", "position": {"x": 85, "y": 54}, "children": ["deep-learning"]},
            
            # Deep Learning - Expanded
            {"id": "deep-learning", "title": "Deep Learning", "type": "topic", "description": "Neural networks", "position": {"x": 50, "y": 61}, "children": ["neural-networks-ml", "activation-functions", "backpropagation", "optimization"]},
            {"id": "neural-networks-ml", "title": "Neural Networks", "type": "subtopic", "description": "Perceptrons, MLPs", "position": {"x": 25, "y": 68}, "children": ["tensorflow"]},
            {"id": "activation-functions", "title": "Activation Functions", "type": "subtopic", "description": "ReLU, sigmoid, tanh, softmax", "position": {"x": 40, "y": 68}, "children": ["tensorflow"]},
            {"id": "backpropagation", "title": "Backpropagation", "type": "subtopic", "description": "Gradient descent, chain rule", "position": {"x": 55, "y": 68}, "children": ["tensorflow"]},
            {"id": "optimization", "title": "Optimization", "type": "subtopic", "description": "SGD, Adam, RMSprop", "position": {"x": 70, "y": 68}, "children": ["tensorflow"]},
            {"id": "regularization", "title": "Regularization", "type": "subtopic", "description": "Dropout, L1/L2, batch norm", "position": {"x": 85, "y": 68}, "children": ["tensorflow"]},
            
            # Deep Learning Frameworks - Expanded
            {"id": "tensorflow", "title": "TensorFlow/Keras", "type": "topic", "description": "Deep learning frameworks", "position": {"x": 30, "y": 75}, "children": ["keras-basics", "tensorflow-basics"]},
            {"id": "keras-basics", "title": "Keras", "type": "subtopic", "description": "High-level API", "position": {"x": 25, "y": 82}, "children": ["cnn"]},
            {"id": "tensorflow-basics", "title": "TensorFlow", "type": "subtopic", "description": "Low-level operations", "position": {"x": 35, "y": 82}, "children": ["cnn"]},
            
            {"id": "pytorch", "title": "PyTorch", "type": "optional", "description": "Alternative DL framework", "position": {"x": 70, "y": 75}, "children": ["pytorch-basics"]},
            {"id": "pytorch-basics", "title": "PyTorch Basics", "type": "optional", "description": "Tensors, autograd, nn.Module", "position": {"x": 70, "y": 82}, "children": ["cnn"]},
            
            # Computer Vision - Expanded
            {"id": "cnn", "title": "Computer Vision", "type": "topic", "description": "Image processing & CNNs", "position": {"x": 50, "y": 89}, "children": ["cnn-architectures", "image-processing", "object-detection", "image-segmentation"]},
            {"id": "cnn-architectures", "title": "CNN Architectures", "type": "subtopic", "description": "VGG, ResNet, Inception", "position": {"x": 25, "y": 96}, "children": ["nlp"]},
            {"id": "image-processing", "title": "Image Processing", "type": "subtopic", "description": "OpenCV, augmentation", "position": {"x": 40, "y": 96}, "children": ["nlp"]},
            {"id": "object-detection", "title": "Object Detection", "type": "subtopic", "description": "YOLO, R-CNN, SSD", "position": {"x": 55, "y": 96}, "children": ["nlp"]},
            {"id": "image-segmentation", "title": "Image Segmentation", "type": "subtopic", "description": "U-Net, Mask R-CNN", "position": {"x": 70, "y": 96}, "children": ["nlp"]},
            {"id": "transfer-learning", "title": "Transfer Learning", "type": "subtopic", "description": "Pre-trained models, fine-tuning", "position": {"x": 85, "y": 96}, "children": ["nlp"]},
            
            # NLP - Expanded
            {"id": "nlp", "title": "Natural Language Processing", "type": "topic", "description": "Text processing & NLP", "position": {"x": 50, "y": 103}, "children": ["text-preprocessing", "word-embeddings", "transformers", "llms"]},
            {"id": "text-preprocessing", "title": "Text Preprocessing", "type": "subtopic", "description": "Tokenization, stemming, lemmatization", "position": {"x": 25, "y": 110}, "children": ["mlops"]},
            {"id": "word-embeddings", "title": "Word Embeddings", "type": "subtopic", "description": "Word2Vec, GloVe, FastText", "position": {"x": 40, "y": 110}, "children": ["mlops"]},
            {"id": "transformers", "title": "Transformers", "type": "subtopic", "description": "BERT, GPT, attention mechanism", "position": {"x": 55, "y": 110}, "children": ["mlops"]},
            {"id": "llms", "title": "Large Language Models", "type": "subtopic", "description": "GPT-4, LLaMA, fine-tuning", "position": {"x": 70, "y": 110}, "children": ["mlops"]},
            {"id": "huggingface", "title": "Hugging Face", "type": "subtopic", "description": "Transformers library", "position": {"x": 85, "y": 110}, "children": ["mlops"]},
            
            # MLOps - Expanded
            {"id": "mlops", "title": "MLOps", "type": "topic", "description": "ML in production", "position": {"x": 50, "y": 117}, "children": ["model-deployment", "model-monitoring", "ml-pipelines", "experiment-tracking"]},
            {"id": "model-deployment", "title": "Model Deployment", "type": "subtopic", "description": "Flask, FastAPI, Docker", "position": {"x": 25, "y": 124}, "children": ["portfolio-ml"]},
            {"id": "model-monitoring", "title": "Model Monitoring", "type": "subtopic", "description": "Performance tracking, drift detection", "position": {"x": 40, "y": 124}, "children": ["portfolio-ml"]},
            {"id": "ml-pipelines", "title": "ML Pipelines", "type": "subtopic", "description": "Airflow, Kubeflow", "position": {"x": 55, "y": 124}, "children": ["portfolio-ml"]},
            {"id": "experiment-tracking", "title": "Experiment Tracking", "type": "subtopic", "description": "MLflow, Weights & Biases", "position": {"x": 70, "y": 124}, "children": ["portfolio-ml"]},
            {"id": "cloud-ml", "title": "Cloud ML", "type": "optional", "description": "AWS SageMaker, GCP AI Platform", "position": {"x": 85, "y": 124}, "children": ["portfolio-ml"]},
            
            # Portfolio
            {"id": "portfolio-ml", "title": "Build Portfolio", "type": "milestone", "description": "Create 4-6 ML projects with deployed models", "position": {"x": 50, "y": 131}, "children": []}
        ]
    },
    
    "cybersecurity": {
        "name": "Cybersecurity Specialist",
        "description": "Complete roadmap to become a Cybersecurity Specialist",
        "nodes": [
            # Security Fundamentals - Expanded
            {"id": "security-basics", "title": "Security Fundamentals", "type": "topic", "description": "Core security concepts", "position": {"x": 50, "y": 5}, "children": ["cia-triad", "threat-models", "security-principles"]},
            {"id": "cia-triad", "title": "CIA Triad", "type": "subtopic", "description": "Confidentiality, Integrity, Availability", "position": {"x": 35, "y": 12}, "children": ["networking-security"]},
            {"id": "threat-models", "title": "Threat Modeling", "type": "subtopic", "description": "STRIDE, attack trees", "position": {"x": 50, "y": 12}, "children": ["networking-security"]},
            {"id": "security-principles", "title": "Security Principles", "type": "subtopic", "description": "Least privilege, defense in depth", "position": {"x": 65, "y": 12}, "children": ["networking-security"]},
            
            # Network Security - Expanded
            {"id": "networking-security", "title": "Network Security", "type": "topic", "description": "Securing networks", "position": {"x": 50, "y": 19}, "children": ["firewalls", "vpn", "ids-ips", "network-protocols"]},
            {"id": "firewalls", "title": "Firewalls", "type": "subtopic", "description": "Packet filtering, stateful inspection", "position": {"x": 25, "y": 26}, "children": ["os-security"]},
            {"id": "vpn", "title": "VPN", "type": "subtopic", "description": "Virtual private networks", "position": {"x": 40, "y": 26}, "children": ["os-security"]},
            {"id": "ids-ips", "title": "IDS/IPS", "type": "subtopic", "description": "Intrusion detection/prevention", "position": {"x": 55, "y": 26}, "children": ["os-security"]},
            {"id": "network-protocols", "title": "Network Protocols", "type": "subtopic", "description": "TCP/IP, DNS, DHCP security", "position": {"x": 70, "y": 26}, "children": ["os-security"]},
            {"id": "wireless-security", "title": "Wireless Security", "type": "subtopic", "description": "WPA2, WPA3, WiFi attacks", "position": {"x": 85, "y": 26}, "children": ["os-security"]},
            
            # OS Security - Expanded
            {"id": "os-security", "title": "OS Security", "type": "topic", "description": "Operating system hardening", "position": {"x": 50, "y": 33}, "children": ["linux-security", "windows-security", "access-control"]},
            {"id": "linux-security", "title": "Linux Security", "type": "subtopic", "description": "SELinux, AppArmor, hardening", "position": {"x": 35, "y": 40}, "children": ["cryptography"]},
            {"id": "windows-security", "title": "Windows Security", "type": "subtopic", "description": "Active Directory, Group Policy", "position": {"x": 50, "y": 40}, "children": ["cryptography"]},
            {"id": "access-control", "title": "Access Control", "type": "subtopic", "description": "RBAC, MAC, DAC", "position": {"x": 65, "y": 40}, "children": ["cryptography"]},
            
            # Cryptography - Expanded
            {"id": "cryptography", "title": "Cryptography", "type": "topic", "description": "Encryption & hashing", "position": {"x": 50, "y": 47}, "children": ["symmetric-crypto", "asymmetric-crypto", "hashing", "pki"]},
            {"id": "symmetric-crypto", "title": "Symmetric Encryption", "type": "subtopic", "description": "AES, DES, 3DES", "position": {"x": 25, "y": 54}, "children": ["web-security"]},
            {"id": "asymmetric-crypto", "title": "Asymmetric Encryption", "type": "subtopic", "description": "RSA, ECC", "position": {"x": 40, "y": 54}, "children": ["web-security"]},
            {"id": "hashing", "title": "Hashing", "type": "subtopic", "description": "SHA, MD5, bcrypt", "position": {"x": 55, "y": 54}, "children": ["web-security"]},
            {"id": "pki", "title": "PKI", "type": "subtopic", "description": "Public Key Infrastructure, certificates", "position": {"x": 70, "y": 54}, "children": ["web-security"]},
            {"id": "ssl-tls", "title": "SSL/TLS", "type": "subtopic", "description": "Secure communication protocols", "position": {"x": 85, "y": 54}, "children": ["web-security"]},
            
            # Web Security - Expanded
            {"id": "web-security", "title": "Web Security", "type": "topic", "description": "Web application security", "position": {"x": 50, "y": 61}, "children": ["owasp-top10", "xss", "sql-injection", "csrf"]},
            {"id": "owasp-top10", "title": "OWASP Top 10", "type": "subtopic", "description": "Top web vulnerabilities", "position": {"x": 20, "y": 68}, "children": ["pentesting"]},
            {"id": "xss", "title": "XSS", "type": "subtopic", "description": "Cross-site scripting", "position": {"x": 35, "y": 68}, "children": ["pentesting"]},
            {"id": "sql-injection", "title": "SQL Injection", "type": "subtopic", "description": "Database injection attacks", "position": {"x": 50, "y": 68}, "children": ["pentesting"]},
            {"id": "csrf", "title": "CSRF", "type": "subtopic", "description": "Cross-site request forgery", "position": {"x": 65, "y": 68}, "children": ["pentesting"]},
            {"id": "authentication-security", "title": "Authentication Security", "type": "subtopic", "description": "OAuth, JWT, session management", "position": {"x": 80, "y": 68}, "children": ["pentesting"]},
            
            # Penetration Testing - Expanded
            {"id": "pentesting", "title": "Penetration Testing", "type": "topic", "description": "Ethical hacking", "position": {"x": 50, "y": 75}, "children": ["recon", "exploitation", "metasploit", "burp-suite"]},
            {"id": "recon", "title": "Reconnaissance", "type": "subtopic", "description": "Information gathering, OSINT", "position": {"x": 25, "y": 82}, "children": ["incident-response"]},
            {"id": "exploitation", "title": "Exploitation", "type": "subtopic", "description": "Exploiting vulnerabilities", "position": {"x": 40, "y": 82}, "children": ["incident-response"]},
            {"id": "metasploit", "title": "Metasploit", "type": "subtopic", "description": "Exploitation framework", "position": {"x": 55, "y": 82}, "children": ["incident-response"]},
            {"id": "burp-suite", "title": "Burp Suite", "type": "subtopic", "description": "Web application testing", "position": {"x": 70, "y": 82}, "children": ["incident-response"]},
            {"id": "privilege-escalation", "title": "Privilege Escalation", "type": "subtopic", "description": "Gaining higher privileges", "position": {"x": 85, "y": 82}, "children": ["incident-response"]},
            
            # Incident Response - Expanded
            {"id": "incident-response", "title": "Incident Response", "type": "topic", "description": "Handling security incidents", "position": {"x": 50, "y": 89}, "children": ["forensics", "malware-analysis", "incident-handling"]},
            {"id": "forensics", "title": "Digital Forensics", "type": "subtopic", "description": "Evidence collection, analysis", "position": {"x": 35, "y": 96}, "children": ["security-tools"]},
            {"id": "malware-analysis", "title": "Malware Analysis", "type": "subtopic", "description": "Static & dynamic analysis", "position": {"x": 50, "y": 96}, "children": ["security-tools"]},
            {"id": "incident-handling", "title": "Incident Handling", "type": "subtopic", "description": "Response procedures, containment", "position": {"x": 65, "y": 96}, "children": ["security-tools"]},
            
            # Security Tools - Expanded
            {"id": "security-tools", "title": "Security Tools", "type": "topic", "description": "Essential security tools", "position": {"x": 50, "y": 103}, "children": ["wireshark", "nmap", "kali-linux", "siem"]},
            {"id": "wireshark", "title": "Wireshark", "type": "subtopic", "description": "Network protocol analyzer", "position": {"x": 25, "y": 110}, "children": ["compliance"]},
            {"id": "nmap", "title": "Nmap", "type": "subtopic", "description": "Network scanning", "position": {"x": 40, "y": 110}, "children": ["compliance"]},
            {"id": "kali-linux", "title": "Kali Linux", "type": "subtopic", "description": "Penetration testing distribution", "position": {"x": 55, "y": 110}, "children": ["compliance"]},
            {"id": "siem", "title": "SIEM", "type": "subtopic", "description": "Security information & event management", "position": {"x": 70, "y": 110}, "children": ["compliance"]},
            {"id": "vulnerability-scanners", "title": "Vulnerability Scanners", "type": "subtopic", "description": "Nessus, OpenVAS", "position": {"x": 85, "y": 110}, "children": ["compliance"]},
            
            # Compliance & Standards - Expanded
            {"id": "compliance", "title": "Compliance & Standards", "type": "topic", "description": "Security frameworks", "position": {"x": 50, "y": 117}, "children": ["iso27001", "gdpr", "pci-dss", "nist"]},
            {"id": "iso27001", "title": "ISO 27001", "type": "subtopic", "description": "Information security management", "position": {"x": 25, "y": 124}, "children": ["portfolio-security"]},
            {"id": "gdpr", "title": "GDPR", "type": "subtopic", "description": "Data protection regulation", "position": {"x": 40, "y": 124}, "children": ["portfolio-security"]},
            {"id": "pci-dss", "title": "PCI DSS", "type": "subtopic", "description": "Payment card security", "position": {"x": 55, "y": 124}, "children": ["portfolio-security"]},
            {"id": "nist", "title": "NIST Framework", "type": "subtopic", "description": "Cybersecurity framework", "position": {"x": 70, "y": 124}, "children": ["portfolio-security"]},
            {"id": "risk-management", "title": "Risk Management", "type": "subtopic", "description": "Risk assessment, mitigation", "position": {"x": 85, "y": 124}, "children": ["portfolio-security"]},
            
            # Portfolio
            {"id": "portfolio-security", "title": "Build Portfolio", "type": "milestone", "description": "Create 3-5 security projects & certifications (CEH, OSCP)", "position": {"x": 50, "y": 131}, "children": []}
        ]
    },
    
    "product_manager": {
        "name": "Product Manager",
        "description": "Complete roadmap to become a Product Manager",
        "nodes": [
            # PM Fundamentals - Expanded
            {"id": "pm-basics", "title": "PM Fundamentals", "type": "topic", "description": "Product management basics", "position": {"x": 50, "y": 5}, "children": ["product-lifecycle", "product-strategy", "pm-frameworks"]},
            {"id": "product-lifecycle", "title": "Product Lifecycle", "type": "subtopic", "description": "Introduction, growth, maturity, decline", "position": {"x": 35, "y": 12}, "children": ["user-research"]},
            {"id": "product-strategy", "title": "Product Strategy", "type": "subtopic", "description": "Vision, mission, goals", "position": {"x": 50, "y": 12}, "children": ["user-research"]},
            {"id": "pm-frameworks", "title": "PM Frameworks", "type": "subtopic", "description": "Jobs-to-be-done, lean startup", "position": {"x": 65, "y": 12}, "children": ["user-research"]},
            
            # User Research - Expanded
            {"id": "user-research", "title": "User Research", "type": "topic", "description": "Understanding users", "position": {"x": 50, "y": 19}, "children": ["user-interviews-pm", "surveys-pm", "personas-pm", "user-testing"]},
            {"id": "user-interviews-pm", "title": "User Interviews", "type": "subtopic", "description": "Conducting interviews", "position": {"x": 25, "y": 26}, "children": ["market-analysis"]},
            {"id": "surveys-pm", "title": "Surveys", "type": "subtopic", "description": "Quantitative research", "position": {"x": 40, "y": 26}, "children": ["market-analysis"]},
            {"id": "personas-pm", "title": "User Personas", "type": "subtopic", "description": "Creating user profiles", "position": {"x": 55, "y": 26}, "children": ["market-analysis"]},
            {"id": "user-testing", "title": "User Testing", "type": "subtopic", "description": "Usability testing", "position": {"x": 70, "y": 26}, "children": ["market-analysis"]},
            {"id": "customer-feedback", "title": "Customer Feedback", "type": "subtopic", "description": "Collecting & analyzing feedback", "position": {"x": 85, "y": 26}, "children": ["market-analysis"]},
            
            # Market Analysis - Expanded
            {"id": "market-analysis", "title": "Market Analysis", "type": "topic", "description": "Market research", "position": {"x": 50, "y": 33}, "children": ["competitive-analysis", "market-sizing", "swot"]},
            {"id": "competitive-analysis", "title": "Competitive Analysis", "type": "subtopic", "description": "Analyzing competitors", "position": {"x": 35, "y": 40}, "children": ["roadmapping"]},
            {"id": "market-sizing", "title": "Market Sizing", "type": "subtopic", "description": "TAM, SAM, SOM", "position": {"x": 50, "y": 40}, "children": ["roadmapping"]},
            {"id": "swot", "title": "SWOT Analysis", "type": "subtopic", "description": "Strengths, weaknesses, opportunities, threats", "position": {"x": 65, "y": 40}, "children": ["roadmapping"]},
            
            # Product Roadmapping - Expanded
            {"id": "roadmapping", "title": "Product Roadmapping", "type": "topic", "description": "Planning product development", "position": {"x": 50, "y": 47}, "children": ["prioritization", "okrs", "roadmap-tools"]},
            {"id": "prioritization", "title": "Prioritization", "type": "subtopic", "description": "RICE, MoSCoW, Kano model", "position": {"x": 30, "y": 54}, "children": ["wireframing"]},
            {"id": "okrs", "title": "OKRs", "type": "subtopic", "description": "Objectives & key results", "position": {"x": 45, "y": 54}, "children": ["wireframing"]},
            {"id": "roadmap-tools", "title": "Roadmap Tools", "type": "subtopic", "description": "Aha!, ProductPlan", "position": {"x": 60, "y": 54}, "children": ["wireframing"]},
            {"id": "feature-definition", "title": "Feature Definition", "type": "subtopic", "description": "Writing feature specs", "position": {"x": 75, "y": 54}, "children": ["wireframing"]},
            
            # Wireframing & Design - Expanded
            {"id": "wireframing", "title": "Wireframing & Prototyping", "type": "topic", "description": "Product design basics", "position": {"x": 50, "y": 61}, "children": ["figma-pm", "user-flows-pm", "mockups"]},
            {"id": "figma-pm", "title": "Figma Basics", "type": "subtopic", "description": "Design tool for PMs", "position": {"x": 35, "y": 68}, "children": ["agile-pm"]},
            {"id": "user-flows-pm", "title": "User Flows", "type": "subtopic", "description": "Mapping user journeys", "position": {"x": 50, "y": 68}, "children": ["agile-pm"]},
            {"id": "mockups", "title": "Mockups", "type": "subtopic", "description": "Low & high fidelity designs", "position": {"x": 65, "y": 68}, "children": ["agile-pm"]},
            
            # Agile Methodologies - Expanded
            {"id": "agile-pm", "title": "Agile Methodologies", "type": "topic", "description": "Agile product management", "position": {"x": 50, "y": 75}, "children": ["scrum", "kanban", "sprints", "backlog"]},
            {"id": "scrum", "title": "Scrum", "type": "subtopic", "description": "Scrum framework", "position": {"x": 25, "y": 82}, "children": ["metrics"]},
            {"id": "kanban", "title": "Kanban", "type": "subtopic", "description": "Kanban boards", "position": {"x": 40, "y": 82}, "children": ["metrics"]},
            {"id": "sprints", "title": "Sprint Planning", "type": "subtopic", "description": "Planning sprints", "position": {"x": 55, "y": 82}, "children": ["metrics"]},
            {"id": "backlog", "title": "Backlog Management", "type": "subtopic", "description": "Grooming & prioritizing", "position": {"x": 70, "y": 82}, "children": ["metrics"]},
            {"id": "user-stories", "title": "User Stories", "type": "subtopic", "description": "Writing user stories", "position": {"x": 85, "y": 82}, "children": ["metrics"]},
            
            # Product Metrics - Expanded
            {"id": "metrics", "title": "Product Metrics", "type": "topic", "description": "Measuring success", "position": {"x": 50, "y": 89}, "children": ["kpis-pm", "analytics-pm", "ab-testing-pm", "cohort-analysis"]},
            {"id": "kpis-pm", "title": "KPIs", "type": "subtopic", "description": "Key performance indicators", "position": {"x": 25, "y": 96}, "children": ["stakeholder"]},
            {"id": "analytics-pm", "title": "Product Analytics", "type": "subtopic", "description": "Google Analytics, Mixpanel, Amplitude", "position": {"x": 40, "y": 96}, "children": ["stakeholder"]},
            {"id": "ab-testing-pm", "title": "A/B Testing", "type": "subtopic", "description": "Experimentation", "position": {"x": 55, "y": 96}, "children": ["stakeholder"]},
            {"id": "cohort-analysis", "title": "Cohort Analysis", "type": "subtopic", "description": "User retention analysis", "position": {"x": 70, "y": 96}, "children": ["stakeholder"]},
            {"id": "funnel-analysis", "title": "Funnel Analysis", "type": "subtopic", "description": "Conversion funnels", "position": {"x": 85, "y": 96}, "children": ["stakeholder"]},
            
            # Stakeholder Management - Expanded
            {"id": "stakeholder", "title": "Stakeholder Management", "type": "topic", "description": "Communication & collaboration", "position": {"x": 50, "y": 103}, "children": ["communication-pm", "presentations", "negotiation"]},
            {"id": "communication-pm", "title": "Communication", "type": "subtopic", "description": "Effective communication", "position": {"x": 35, "y": 110}, "children": ["technical-pm"]},
            {"id": "presentations", "title": "Presentations", "type": "subtopic", "description": "Presenting to stakeholders", "position": {"x": 50, "y": 110}, "children": ["technical-pm"]},
            {"id": "negotiation", "title": "Negotiation", "type": "subtopic", "description": "Conflict resolution", "position": {"x": 65, "y": 110}, "children": ["technical-pm"]},
            
            # Technical Knowledge - Expanded
            {"id": "technical-pm", "title": "Technical Knowledge", "type": "topic", "description": "Understanding technology", "position": {"x": 50, "y": 117}, "children": ["apis-pm", "databases-pm", "architecture-pm", "sql-pm"]},
            {"id": "apis-pm", "title": "APIs", "type": "subtopic", "description": "REST, GraphQL basics", "position": {"x": 25, "y": 124}, "children": ["go-to-market"]},
            {"id": "databases-pm", "title": "Databases", "type": "subtopic", "description": "SQL, NoSQL basics", "position": {"x": 40, "y": 124}, "children": ["go-to-market"]},
            {"id": "architecture-pm", "title": "System Architecture", "type": "subtopic", "description": "Frontend, backend, infrastructure", "position": {"x": 55, "y": 124}, "children": ["go-to-market"]},
            {"id": "sql-pm", "title": "SQL Basics", "type": "subtopic", "description": "Querying data", "position": {"x": 70, "y": 124}, "children": ["go-to-market"]},
            
            # Go-to-Market
            {"id": "go-to-market", "title": "Go-to-Market Strategy", "type": "optional", "description": "Product launches", "position": {"x": 50, "y": 131}, "children": ["launch-planning", "pricing"]},
            {"id": "launch-planning", "title": "Launch Planning", "type": "optional", "description": "Product launch strategy", "position": {"x": 40, "y": 138}, "children": ["portfolio-pm"]},
            {"id": "pricing", "title": "Pricing Strategy", "type": "optional", "description": "Pricing models", "position": {"x": 60, "y": 138}, "children": ["portfolio-pm"]},
            
            # Portfolio
            {"id": "portfolio-pm", "title": "Build Portfolio", "type": "milestone", "description": "Create 3-5 product case studies with metrics", "position": {"x": 50, "y": 145}, "children": []}
        ]
    },
    
    "business_analyst": {
        "name": "Business Analyst",
        "description": "Complete roadmap to become a Business Analyst",
        "nodes": [
            # BA Fundamentals - Expanded
            {"id": "ba-fundamentals", "title": "BA Fundamentals", "type": "topic", "description": "Business analysis basics", "position": {"x": 50, "y": 5}, "children": ["requirements-gathering", "documentation", "ba-techniques"]},
            {"id": "requirements-gathering", "title": "Requirements Gathering", "type": "subtopic", "description": "Elicitation techniques", "position": {"x": 35, "y": 12}, "children": ["business-process"]},
            {"id": "documentation", "title": "Documentation", "type": "subtopic", "description": "BRD, FRD, SRS", "position": {"x": 50, "y": 12}, "children": ["business-process"]},
            {"id": "ba-techniques", "title": "BA Techniques", "type": "subtopic", "description": "Interviews, workshops, observation", "position": {"x": 65, "y": 12}, "children": ["business-process"]},
            
            # Business Process Modeling - Expanded
            {"id": "business-process", "title": "Business Process Modeling", "type": "topic", "description": "Process analysis & design", "position": {"x": 50, "y": 19}, "children": ["bpmn", "process-flows", "process-improvement"]},
            {"id": "bpmn", "title": "BPMN", "type": "subtopic", "description": "Business Process Model & Notation", "position": {"x": 35, "y": 26}, "children": ["requirements"]},
            {"id": "process-flows", "title": "Process Flows", "type": "subtopic", "description": "Flowcharts, swimlane diagrams", "position": {"x": 50, "y": 26}, "children": ["requirements"]},
            {"id": "process-improvement", "title": "Process Improvement", "type": "subtopic", "description": "Six Sigma, Lean", "position": {"x": 65, "y": 26}, "children": ["requirements"]},
            
            # Requirements Analysis - Expanded
            {"id": "requirements", "title": "Requirements Analysis", "type": "topic", "description": "Analyzing requirements", "position": {"x": 50, "y": 33}, "children": ["functional-requirements", "non-functional-requirements", "requirements-validation"]},
            {"id": "functional-requirements", "title": "Functional Requirements", "type": "subtopic", "description": "What the system should do", "position": {"x": 30, "y": 40}, "children": ["data-analysis-ba"]},
            {"id": "non-functional-requirements", "title": "Non-Functional Requirements", "type": "subtopic", "description": "Performance, security, usability", "position": {"x": 50, "y": 40}, "children": ["data-analysis-ba"]},
            {"id": "requirements-validation", "title": "Requirements Validation", "type": "subtopic", "description": "Verifying requirements", "position": {"x": 70, "y": 40}, "children": ["data-analysis-ba"]},
            
            # Data Analysis - Expanded
            {"id": "data-analysis-ba", "title": "Data Analysis", "type": "topic", "description": "Analyzing business data", "position": {"x": 50, "y": 47}, "children": ["excel-ba", "sql-ba", "data-visualization-ba", "statistics-ba"]},
            {"id": "excel-ba", "title": "Excel", "type": "subtopic", "description": "Advanced Excel, pivot tables, formulas", "position": {"x": 25, "y": 54}, "children": ["uml"]},
            {"id": "sql-ba", "title": "SQL", "type": "subtopic", "description": "Database querying", "position": {"x": 40, "y": 54}, "children": ["uml"]},
            {"id": "data-visualization-ba", "title": "Data Visualization", "type": "subtopic", "description": "Charts, dashboards, Tableau", "position": {"x": 55, "y": 54}, "children": ["uml"]},
            {"id": "statistics-ba", "title": "Statistics", "type": "subtopic", "description": "Basic statistical analysis", "position": {"x": 70, "y": 54}, "children": ["uml"]},
            {"id": "power-query", "title": "Power Query", "type": "subtopic", "description": "Data transformation", "position": {"x": 85, "y": 54}, "children": ["uml"]},
            
            # UML & Modeling - Expanded
            {"id": "uml", "title": "UML Diagrams", "type": "topic", "description": "Unified Modeling Language", "position": {"x": 50, "y": 61}, "children": ["use-cases", "sequence-diagrams", "class-diagrams", "activity-diagrams"]},
            {"id": "use-cases", "title": "Use Case Diagrams", "type": "subtopic", "description": "System interactions", "position": {"x": 25, "y": 68}, "children": ["agile-ba"]},
            {"id": "sequence-diagrams", "title": "Sequence Diagrams", "type": "subtopic", "description": "Interaction flows", "position": {"x": 40, "y": 68}, "children": ["agile-ba"]},
            {"id": "class-diagrams", "title": "Class Diagrams", "type": "subtopic", "description": "System structure", "position": {"x": 55, "y": 68}, "children": ["agile-ba"]},
            {"id": "activity-diagrams", "title": "Activity Diagrams", "type": "subtopic", "description": "Workflow modeling", "position": {"x": 70, "y": 68}, "children": ["agile-ba"]},
            {"id": "er-diagrams", "title": "ER Diagrams", "type": "subtopic", "description": "Entity-relationship diagrams", "position": {"x": 85, "y": 68}, "children": ["agile-ba"]},
            
            # Agile BA - Expanded
            {"id": "agile-ba", "title": "Agile BA", "type": "topic", "description": "BA in agile environments", "position": {"x": 50, "y": 75}, "children": ["user-stories-ba", "acceptance-criteria", "backlog-refinement"]},
            {"id": "user-stories-ba", "title": "User Stories", "type": "subtopic", "description": "Writing user stories", "position": {"x": 35, "y": 82}, "children": ["tools-ba"]},
            {"id": "acceptance-criteria", "title": "Acceptance Criteria", "type": "subtopic", "description": "Defining done", "position": {"x": 50, "y": 82}, "children": ["tools-ba"]},
            {"id": "backlog-refinement", "title": "Backlog Refinement", "type": "subtopic", "description": "Grooming stories", "position": {"x": 65, "y": 82}, "children": ["tools-ba"]},
            
            # BA Tools - Expanded
            {"id": "tools-ba", "title": "BA Tools", "type": "topic", "description": "Essential BA tools", "position": {"x": 50, "y": 89}, "children": ["jira-ba", "confluence", "visio", "lucidchart"]},
            {"id": "jira-ba", "title": "Jira", "type": "subtopic", "description": "Issue tracking, agile boards", "position": {"x": 25, "y": 96}, "children": ["stakeholder-ba"]},
            {"id": "confluence", "title": "Confluence", "type": "subtopic", "description": "Documentation & collaboration", "position": {"x": 40, "y": 96}, "children": ["stakeholder-ba"]},
            {"id": "visio", "title": "Visio", "type": "subtopic", "description": "Diagramming tool", "position": {"x": 55, "y": 96}, "children": ["stakeholder-ba"]},
            {"id": "lucidchart", "title": "Lucidchart", "type": "subtopic", "description": "Online diagramming", "position": {"x": 70, "y": 96}, "children": ["stakeholder-ba"]},
            {"id": "miro", "title": "Miro", "type": "subtopic", "description": "Collaborative whiteboard", "position": {"x": 85, "y": 96}, "children": ["stakeholder-ba"]},
            
            # Stakeholder Communication - Expanded
            {"id": "stakeholder-ba", "title": "Stakeholder Communication", "type": "topic", "description": "Effective communication", "position": {"x": 50, "y": 103}, "children": ["presentations-ba", "workshops-ba", "facilitation"]},
            {"id": "presentations-ba", "title": "Presentations", "type": "subtopic", "description": "Presenting findings", "position": {"x": 35, "y": 110}, "children": ["testing-ba"]},
            {"id": "workshops-ba", "title": "Workshops", "type": "subtopic", "description": "Facilitating workshops", "position": {"x": 50, "y": 110}, "children": ["testing-ba"]},
            {"id": "facilitation", "title": "Facilitation", "type": "subtopic", "description": "Meeting facilitation", "position": {"x": 65, "y": 110}, "children": ["testing-ba"]},
            
            # Testing & QA - Expanded
            {"id": "testing-ba", "title": "Testing & QA", "type": "topic", "description": "Quality assurance", "position": {"x": 50, "y": 117}, "children": ["uat", "test-cases", "test-planning"]},
            {"id": "uat", "title": "UAT", "type": "subtopic", "description": "User acceptance testing", "position": {"x": 30, "y": 124}, "children": ["domain-knowledge"]},
            {"id": "test-cases", "title": "Test Cases", "type": "subtopic", "description": "Writing test cases", "position": {"x": 45, "y": 124}, "children": ["domain-knowledge"]},
            {"id": "test-planning", "title": "Test Planning", "type": "subtopic", "description": "Test strategy & planning", "position": {"x": 60, "y": 124}, "children": ["domain-knowledge"]},
            {"id": "defect-tracking", "title": "Defect Tracking", "type": "subtopic", "description": "Bug reporting & tracking", "position": {"x": 75, "y": 124}, "children": ["domain-knowledge"]},
            
            # Domain Knowledge
            {"id": "domain-knowledge", "title": "Domain Knowledge", "type": "optional", "description": "Industry-specific knowledge", "position": {"x": 50, "y": 131}, "children": ["finance-domain", "healthcare-domain", "ecommerce-domain"]},
            {"id": "finance-domain", "title": "Finance Domain", "type": "optional", "description": "Banking, fintech", "position": {"x": 30, "y": 138}, "children": ["portfolio-ba"]},
            {"id": "healthcare-domain", "title": "Healthcare Domain", "type": "optional", "description": "Healthcare systems", "position": {"x": 50, "y": 138}, "children": ["portfolio-ba"]},
            {"id": "ecommerce-domain", "title": "E-commerce Domain", "type": "optional", "description": "Retail, e-commerce", "position": {"x": 70, "y": 138}, "children": ["portfolio-ba"]},
            
            # Portfolio
            {"id": "portfolio-ba", "title": "Build Portfolio", "type": "milestone", "description": "Create 3-5 BA case studies with documentation", "position": {"x": 50, "y": 145}, "children": []}
        ]
    },
    
    "software_engineer_backend": {
        "name": "Software Engineer (Backend/Systems)",
        "description": "Complete roadmap for Backend Software Engineering",
        "nodes": [
            {"id": "backend-lang", "title": "Backend Language", "type": "topic", "description": "Python, Java, Go, or Node.js", "position": {"x": 50, "y": 10}, "children": ["data-structures"]},
            {"id": "data-structures", "title": "Data Structures & Algorithms", "type": "topic", "description": "Arrays, trees, graphs, sorting", "position": {"x": 50, "y": 20}, "children": ["databases-backend"]},
            {"id": "databases-backend", "title": "Databases", "type": "topic", "description": "SQL, NoSQL, database design", "position": {"x": 50, "y": 30}, "children": ["apis-backend"]},
            {"id": "apis-backend", "title": "API Development", "type": "topic", "description": "REST, GraphQL, API design", "position": {"x": 50, "y": 40}, "children": ["authentication"]},
            {"id": "authentication", "title": "Authentication & Security", "type": "topic", "description": "JWT, OAuth, encryption", "position": {"x": 50, "y": 50}, "children": ["caching"]},
            {"id": "caching", "title": "Caching", "type": "topic", "description": "Redis, Memcached", "position": {"x": 50, "y": 60}, "children": ["message-queues"]},
            {"id": "message-queues", "title": "Message Queues", "type": "topic", "description": "RabbitMQ, Kafka", "position": {"x": 50, "y": 70}, "children": ["microservices"]},
            {"id": "microservices", "title": "Microservices", "type": "topic", "description": "Service architecture, communication", "position": {"x": 50, "y": 80}, "children": ["system-design"]},
            {"id": "system-design", "title": "System Design", "type": "topic", "description": "Scalability, load balancing", "position": {"x": 50, "y": 90}, "children": []}
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
