"""
AI Career Guide Engine - Decision-Making System
A structured career recommendation engine that diagnoses profiles,
recommends paths, and generates 90-day roadmaps.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class CareerEngine:
    """Core engine for career path recommendation and roadmap generation"""
    
    def __init__(self):
        self.career_paths = self._initialize_career_paths()
        self.roadmap_templates = self._initialize_roadmap_templates()
    
    def _initialize_career_paths(self) -> Dict:
        """Define career path profiles with attribute vectors"""
        return {
            "software_engineer_backend": {
                "name": "Software Engineer (Backend/Systems)",
                "attributes": {
                    "logical_intensity": 0.9,
                    "creativity": 0.5,
                    "consistency": 0.8,
                    "ambiguity_tolerance": 0.6,
                    "self_learning": 0.8,
                    "time_to_reward": 0.5
                },
                "requirements": {
                    "min_time_per_week": 15,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Backend Developer", "Systems Engineer", "API Developer"]
            },
            "frontend_developer": {
                "name": "Frontend Developer",
                "attributes": {
                    "logical_intensity": 0.7,
                    "creativity": 0.8,
                    "consistency": 0.6,
                    "ambiguity_tolerance": 0.5,
                    "self_learning": 0.7,
                    "time_to_reward": 0.8
                },
                "requirements": {
                    "min_time_per_week": 10,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Frontend Developer", "UI Developer", "Web Developer"]
            },
            "fullstack_developer": {
                "name": "Full Stack Developer",
                "attributes": {
                    "logical_intensity": 0.8,
                    "creativity": 0.7,
                    "consistency": 0.7,
                    "ambiguity_tolerance": 0.6,
                    "self_learning": 0.8,
                    "time_to_reward": 0.7
                },
                "requirements": {
                    "min_time_per_week": 15,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Full Stack Developer", "Startup Roles", "Freelancing"]
            },
            "data_scientist": {
                "name": "Data Scientist/Analyst",
                "attributes": {
                    "logical_intensity": 0.8,
                    "creativity": 0.6,
                    "consistency": 0.7,
                    "ambiguity_tolerance": 0.7,
                    "self_learning": 0.7,
                    "time_to_reward": 0.7
                },
                "requirements": {
                    "min_time_per_week": 12,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Data Scientist", "Data Analyst", "Business Intelligence Analyst"]
            },
            "ui_ux_designer": {
                "name": "UI/UX Designer",
                "attributes": {
                    "logical_intensity": 0.5,
                    "creativity": 0.9,
                    "consistency": 0.6,
                    "ambiguity_tolerance": 0.7,
                    "self_learning": 0.7,
                    "time_to_reward": 0.8
                },
                "requirements": {
                    "min_time_per_week": 10,
                    "internet_required": True,
                    "financial_barrier": "medium"
                },
                "outcomes": ["UI/UX Designer", "Product Design", "Design Internship"]
            },
            "devops_engineer": {
                "name": "DevOps/Cloud Engineer",
                "attributes": {
                    "logical_intensity": 0.8,
                    "creativity": 0.5,
                    "consistency": 0.8,
                    "ambiguity_tolerance": 0.7,
                    "self_learning": 0.8,
                    "time_to_reward": 0.6
                },
                "requirements": {
                    "min_time_per_week": 15,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["DevOps Engineer", "Cloud Engineer", "Site Reliability Engineer"]
            },
            "mobile_developer": {
                "name": "Mobile App Developer",
                "attributes": {
                    "logical_intensity": 0.7,
                    "creativity": 0.7,
                    "consistency": 0.7,
                    "ambiguity_tolerance": 0.6,
                    "self_learning": 0.7,
                    "time_to_reward": 0.7
                },
                "requirements": {
                    "min_time_per_week": 12,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Mobile App Developer", "iOS/Android Developer", "Cross-platform Developer"]
            },
            "ai_ml_engineer": {
                "name": "AI/ML Engineer",
                "attributes": {
                    "logical_intensity": 0.9,
                    "creativity": 0.6,
                    "consistency": 0.8,
                    "ambiguity_tolerance": 0.7,
                    "self_learning": 0.9,
                    "time_to_reward": 0.5
                },
                "requirements": {
                    "min_time_per_week": 15,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["AI/ML Engineer", "Machine Learning Scientist", "AI Researcher"]
            },
            "cybersecurity": {
                "name": "Cybersecurity Specialist",
                "attributes": {
                    "logical_intensity": 0.8,
                    "creativity": 0.6,
                    "consistency": 0.8,
                    "ambiguity_tolerance": 0.7,
                    "self_learning": 0.8,
                    "time_to_reward": 0.6
                },
                "requirements": {
                    "min_time_per_week": 15,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Cybersecurity Analyst", "Security Engineer", "Penetration Tester"]
            },
            "product_manager": {
                "name": "Product Manager",
                "attributes": {
                    "logical_intensity": 0.7,
                    "creativity": 0.7,
                    "consistency": 0.7,
                    "ambiguity_tolerance": 0.8,
                    "self_learning": 0.7,
                    "time_to_reward": 0.7
                },
                "requirements": {
                    "min_time_per_week": 12,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Product Manager", "Technical Product Manager", "Product Owner"]
            },
            "digital_marketing": {
                "name": "Digital Marketing Specialist",
                "attributes": {
                    "logical_intensity": 0.6,
                    "creativity": 0.8,
                    "consistency": 0.7,
                    "ambiguity_tolerance": 0.8,
                    "self_learning": 0.7,
                    "time_to_reward": 0.7
                },
                "requirements": {
                    "min_time_per_week": 10,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Marketing Specialist", "Content Strategy", "SEO/SEM Roles"]
            },
            "business_analyst": {
                "name": "Business Analyst",
                "attributes": {
                    "logical_intensity": 0.7,
                    "creativity": 0.6,
                    "consistency": 0.7,
                    "ambiguity_tolerance": 0.7,
                    "self_learning": 0.7,
                    "time_to_reward": 0.7
                },
                "requirements": {
                    "min_time_per_week": 12,
                    "internet_required": True,
                    "financial_barrier": "low"
                },
                "outcomes": ["Business Analyst", "Systems Analyst", "Data Analyst"]
            }
        }
    
    def diagnose_profile(self, mcq_responses: List[int], constraints: Dict) -> Dict:
        """
        Convert MCQ responses into internal attribute scores
        
        Args:
            mcq_responses: List of 30 integers (1-5 scale)
            constraints: Dict with time_per_week, academic_year, financial, internet, device
        
        Returns:
            Dict with attribute scores (internal only, not shown to user)
        """
        # Map questions to attributes (30 questions)
        # Q1-5: Logical intensity (Analytical & Logical Thinking)
        # Q6-10: Creativity (Creativity & Innovation)
        # Q11-15: Consistency (Work Style & Persistence)
        # Q16-20: Self-learning (Learning & Adaptability)
        # Q21-25: Ambiguity tolerance (Social & Communication)
        # Q26-30: Time-to-reward preference (Work Environment Preferences)
        
        logical_intensity = sum(mcq_responses[0:5]) / 25.0  # Normalize to 0-1
        creativity = sum(mcq_responses[5:10]) / 25.0
        consistency = sum(mcq_responses[10:15]) / 25.0
        self_learning = sum(mcq_responses[15:20]) / 25.0
        ambiguity_tolerance = sum(mcq_responses[20:25]) / 25.0
        time_to_reward = sum(mcq_responses[25:30]) / 25.0
        
        profile = {
            "logical_intensity": round(logical_intensity, 2),
            "creativity": round(creativity, 2),
            "consistency": round(consistency, 2),
            "ambiguity_tolerance": round(ambiguity_tolerance, 2),
            "self_learning": round(self_learning, 2),
            "time_to_reward": round(time_to_reward, 2),
            "constraints": constraints
        }
        
        return profile
    
    def compute_compatibility(self, user_profile: Dict, path_key: str) -> float:
        """
        Compute compatibility score between user profile and career path
        
        Returns:
            Float between 0-100 representing compatibility percentage
        """
        path = self.career_paths[path_key]
        
        # Attribute matching score (70% weight)
        attribute_score = 0
        for attr, path_value in path["attributes"].items():
            user_value = user_profile.get(attr, 0.5)
            # Calculate similarity (1 - absolute difference)
            similarity = 1 - abs(user_value - path_value)
            attribute_score += similarity
        
        attribute_score = (attribute_score / len(path["attributes"])) * 70
        
        # Constraint matching score (30% weight)
        constraint_score = 30
        constraints = user_profile["constraints"]
        
        # Time availability check
        if constraints.get("time_per_week", 0) < path["requirements"]["min_time_per_week"]:
            constraint_score -= 15
        
        # Internet availability check
        if path["requirements"]["internet_required"] and not constraints.get("internet", True):
            constraint_score -= 10
        
        # Financial barrier check
        financial = constraints.get("financial", "medium")
        path_barrier = path["requirements"]["financial_barrier"]
        if financial == "low" and path_barrier == "high":
            constraint_score -= 5
        
        total_score = attribute_score + constraint_score
        return round(total_score, 1)
    
    def recommend_paths(self, user_profile: Dict) -> Tuple[Dict, Dict]:
        """
        Recommend exactly 1 primary and 1 secondary career path
        
        Returns:
            Tuple of (primary_path, secondary_path) with scores and rationale
        """
        # Compute compatibility for all paths
        scores = []
        for path_key in self.career_paths.keys():
            score = self.compute_compatibility(user_profile, path_key)
            scores.append((path_key, score))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Get top 2
        primary_key, primary_score = scores[0]
        secondary_key, secondary_score = scores[1]
        
        primary_path = {
            "key": primary_key,
            "name": self.career_paths[primary_key]["name"],
            "score": primary_score,
            "rationale": self._generate_rationale(user_profile, primary_key, "primary"),
            "outcomes": self.career_paths[primary_key]["outcomes"]
        }
        
        secondary_path = {
            "key": secondary_key,
            "name": self.career_paths[secondary_key]["name"],
            "score": secondary_score,
            "rationale": self._generate_rationale(user_profile, secondary_key, "secondary"),
            "outcomes": self.career_paths[secondary_key]["outcomes"]
        }
        
        return primary_path, secondary_path
    
    def _generate_rationale(self, user_profile: Dict, path_key: str, rank: str) -> str:
        """Generate human-readable rationale for path recommendation"""
        path = self.career_paths[path_key]
        
        # Find strongest matching attributes
        matches = []
        for attr, path_value in path["attributes"].items():
            user_value = user_profile.get(attr, 0.5)
            if abs(user_value - path_value) < 0.2:  # Strong match
                matches.append(attr.replace("_", " "))
        
        if rank == "primary":
            rationale = f"This path aligns strongly with your profile. "
        else:
            rationale = f"This is a solid fallback option. "
        
        if matches:
            rationale += f"Your strengths in {', '.join(matches[:2])} match well with this track. "
        
        # Add constraint-based insights
        time_available = user_profile["constraints"].get("time_per_week", 0)
        time_required = path["requirements"]["min_time_per_week"]
        
        if time_available >= time_required + 5:
            rationale += "You have sufficient time to excel in this path."
        elif time_available >= time_required:
            rationale += "Your available time meets the minimum requirements."
        else:
            rationale += "Note: This path requires more time than you currently have available."
        
        return rationale
    
    def _initialize_roadmap_templates(self) -> Dict:
        """Initialize 90-day roadmap templates for each career path"""
        return {
            "frontend_developer": {
                "phase1": {
                    "name": "Foundation (Weeks 1-4)",
                    "weeks": [
                        {
                            "week": 1,
                            "goal": "HTML & CSS Fundamentals",
                            "skills": ["HTML5 semantic tags", "CSS selectors", "Flexbox basics"],
                            "outcomes": ["Build 3 static web pages", "Complete HTML/CSS course"],
                            "resources": ["freeCodeCamp HTML/CSS", "MDN Web Docs"]
                        },
                        {
                            "week": 2,
                            "goal": "Advanced CSS & Responsive Design",
                            "skills": ["CSS Grid", "Media queries", "Mobile-first design"],
                            "outcomes": ["Create responsive portfolio page", "Clone 2 website layouts"],
                            "resources": ["CSS Grid Garden", "Responsive Web Design course"]
                        },
                        {
                            "week": 3,
                            "goal": "JavaScript Basics",
                            "skills": ["Variables & data types", "Functions", "DOM manipulation"],
                            "outcomes": ["Build calculator app", "Create interactive form"],
                            "resources": ["JavaScript.info", "Eloquent JavaScript"]
                        },
                        {
                            "week": 4,
                            "goal": "JavaScript ES6+ Features",
                            "skills": ["Arrow functions", "Promises", "Async/await"],
                            "outcomes": ["Build weather app using API", "Complete JS challenges"],
                            "resources": ["ES6 course", "JavaScript30 challenges"]
                        }
                    ]
                },
                "phase2": {
                    "name": "Application (Weeks 5-8)",
                    "weeks": [
                        {
                            "week": 5,
                            "goal": "React Fundamentals",
                            "skills": ["Components", "Props & State", "Hooks basics"],
                            "outcomes": ["Build todo app in React", "Complete React tutorial"],
                            "resources": ["React official docs", "Scrimba React course"]
                        },
                        {
                            "week": 6,
                            "goal": "React Advanced Concepts",
                            "skills": ["useEffect", "Context API", "Custom hooks"],
                            "outcomes": ["Build movie search app", "Implement routing"],
                            "resources": ["React Router docs", "Advanced React patterns"]
                        },
                        {
                            "week": 7,
                            "goal": "State Management & APIs",
                            "skills": ["API integration", "Error handling", "Loading states"],
                            "outcomes": ["Build e-commerce product page", "Integrate payment UI"],
                            "resources": ["Axios documentation", "REST API tutorial"]
                        },
                        {
                            "week": 8,
                            "goal": "Styling & UI Libraries",
                            "skills": ["Tailwind CSS", "Material-UI", "Component libraries"],
                            "outcomes": ["Redesign previous projects", "Build design system"],
                            "resources": ["Tailwind docs", "Material-UI components"]
                        }
                    ]
                },
                "phase3": {
                    "name": "Proof of Work (Weeks 9-12)",
                    "weeks": [
                        {
                            "week": 9,
                            "goal": "Portfolio Project Planning",
                            "skills": ["Project planning", "Wireframing", "Git workflow"],
                            "outcomes": ["Define project scope", "Create wireframes", "Setup Git repo"],
                            "resources": ["Figma", "GitHub", "Project planning templates"]
                        },
                        {
                            "week": 10,
                            "goal": "Portfolio Project Development",
                            "skills": ["Full-stack integration", "Deployment", "Testing"],
                            "outcomes": ["Build 80% of portfolio project", "Write tests"],
                            "resources": ["Jest documentation", "React Testing Library"]
                        },
                        {
                            "week": 11,
                            "goal": "Polish & Deploy",
                            "skills": ["Performance optimization", "SEO basics", "Deployment"],
                            "outcomes": ["Deploy project to Vercel/Netlify", "Optimize performance"],
                            "resources": ["Vercel docs", "Lighthouse", "Web.dev"]
                        },
                        {
                            "week": 12,
                            "goal": "Job Applications & Interview Prep",
                            "skills": ["Resume building", "LinkedIn optimization", "Interview prep"],
                            "outcomes": ["Apply to 10 internships", "Complete mock interviews", "Update portfolio"],
                            "resources": ["AngelList", "Internshala", "LeetCode Easy"]
                        }
                    ]
                }
            },
            "software_engineer_backend": {
                "phase1": {
                    "name": "Foundation (Weeks 1-4)",
                    "weeks": [
                        {
                            "week": 1,
                            "goal": "Programming Language Mastery",
                            "skills": ["Python/Java syntax", "OOP concepts", "Standard library"],
                            "outcomes": ["Solve 20 basic problems", "Build CLI tool"],
                            "resources": ["LeetCode", "HackerRank", "Official docs"]
                        },
                        {
                            "week": 2,
                            "goal": "Arrays & Strings",
                            "skills": ["Two pointers", "Sliding window", "String manipulation"],
                            "outcomes": ["Solve 25 array problems", "Implement algorithms"],
                            "resources": ["LeetCode patterns", "Striver's SDE Sheet"]
                        },
                        {
                            "week": 3,
                            "goal": "Linked Lists & Stacks/Queues",
                            "skills": ["Linked list operations", "Stack/Queue implementation"],
                            "outcomes": ["Solve 20 problems", "Implement data structures"],
                            "resources": ["GeeksforGeeks", "LeetCode"]
                        },
                        {
                            "week": 4,
                            "goal": "Recursion & Backtracking",
                            "skills": ["Recursive thinking", "Backtracking patterns"],
                            "outcomes": ["Solve 15 recursion problems", "Master base cases"],
                            "resources": ["Recursion playlist", "LeetCode recursion tag"]
                        }
                    ]
                },
                "phase2": {
                    "name": "Application (Weeks 5-8)",
                    "weeks": [
                        {
                            "week": 5,
                            "goal": "Trees & Graphs",
                            "skills": ["Tree traversals", "BFS/DFS", "Graph algorithms"],
                            "outcomes": ["Solve 25 tree/graph problems", "Implement traversals"],
                            "resources": ["LeetCode", "Graph theory course"]
                        },
                        {
                            "week": 6,
                            "goal": "Dynamic Programming Basics",
                            "skills": ["Memoization", "Tabulation", "DP patterns"],
                            "outcomes": ["Solve 20 DP problems", "Master classic problems"],
                            "resources": ["DP patterns guide", "Aditya Verma DP"]
                        },
                        {
                            "week": 7,
                            "goal": "Backend Development Basics",
                            "skills": ["REST APIs", "Express.js/Flask", "Database basics"],
                            "outcomes": ["Build CRUD API", "Connect to database"],
                            "resources": ["Express docs", "MongoDB tutorial"]
                        },
                        {
                            "week": 8,
                            "goal": "Authentication & Security",
                            "skills": ["JWT", "Password hashing", "API security"],
                            "outcomes": ["Implement auth system", "Secure API endpoints"],
                            "resources": ["JWT.io", "OWASP guidelines"]
                        }
                    ]
                },
                "phase3": {
                    "name": "Proof of Work (Weeks 9-12)",
                    "weeks": [
                        {
                            "week": 9,
                            "goal": "System Design Basics",
                            "skills": ["Scalability", "Caching", "Load balancing"],
                            "outcomes": ["Design 3 systems", "Study case studies"],
                            "resources": ["System Design Primer", "Gaurav Sen videos"]
                        },
                        {
                            "week": 10,
                            "goal": "Full Stack Project",
                            "skills": ["API design", "Database schema", "Deployment"],
                            "outcomes": ["Build complete backend project", "Write documentation"],
                            "resources": ["Postman", "Swagger", "Railway/Render"]
                        },
                        {
                            "week": 11,
                            "goal": "Advanced DSA Practice",
                            "skills": ["Hard problems", "Optimization", "Time complexity"],
                            "outcomes": ["Solve 30 medium/hard problems", "Mock interviews"],
                            "resources": ["LeetCode", "InterviewBit"]
                        },
                        {
                            "week": 12,
                            "goal": "Interview Preparation",
                            "skills": ["Behavioral questions", "System design", "Coding rounds"],
                            "outcomes": ["Apply to 15 companies", "Complete 5 mock interviews"],
                            "resources": ["Pramp", "Interviewing.io", "LinkedIn"]
                        }
                    ]
                }
            },
            # Remaining 10 careers use generic templates - all have detailed visual roadmaps in roadmap_data.py
        }
    
    def generate_roadmap(self, path_key: str, user_level: str, time_per_week: int) -> Dict:
        """
        Generate personalized 90-day roadmap
        
        Args:
            path_key: Career path identifier
            user_level: "beginner", "intermediate", "advanced"
            time_per_week: Hours available per week
        
        Returns:
            Dict with phase-wise roadmap
        """
        template = self.roadmap_templates.get(path_key)
        
        if not template:
            # Return generic template if specific one not found
            return self._generate_generic_roadmap(path_key)
        
        # Adjust roadmap based on time availability
        roadmap = {
            "path_name": self.career_paths[path_key]["name"],
            "duration": "90 days",
            "time_commitment": f"{time_per_week} hours/week",
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d"),
            "phases": []
        }
        
        for phase_key in ["phase1", "phase2", "phase3"]:
            phase = template[phase_key]
            roadmap["phases"].append({
                "name": phase["name"],
                "weeks": phase["weeks"]
            })
        
        # Add current week focus
        roadmap["current_week"] = {
            "week": 1,
            "phase": "Foundation",
            "focus": template["phase1"]["weeks"][0]["goal"]
        }
        
        return roadmap
    
    def _generate_generic_roadmap(self, path_key: str) -> Dict:
        """Generate a generic roadmap for paths without specific templates"""
        return {
            "path_name": self.career_paths[path_key]["name"],
            "duration": "90 days",
            "phases": [
                {
                    "name": "Foundation (Weeks 1-4)",
                    "weeks": [
                        {"week": i, "goal": "Build foundational skills", "skills": [], "outcomes": []}
                        for i in range(1, 5)
                    ]
                },
                {
                    "name": "Application (Weeks 5-8)",
                    "weeks": [
                        {"week": i, "goal": "Apply skills to projects", "skills": [], "outcomes": []}
                        for i in range(5, 9)
                    ]
                },
                {
                    "name": "Proof of Work (Weeks 9-12)",
                    "weeks": [
                        {"week": i, "goal": "Build portfolio and apply", "skills": [], "outcomes": []}
                        for i in range(9, 13)
                    ]
                }
            ],
            "current_week": {"week": 1, "phase": "Foundation", "focus": "Getting started"}
        }
    
    def generate_diagnosis_summary(self, user_profile: Dict) -> str:
        """Generate human-readable diagnosis summary"""
        summary = "Based on your responses, here's your career profile:\n\n"
        
        # Identify top 2 strengths
        attributes = {k: v for k, v in user_profile.items() if k != "constraints"}
        sorted_attrs = sorted(attributes.items(), key=lambda x: x[1], reverse=True)
        
        top_attrs = sorted_attrs[:2]
        summary += f"Your strongest attributes are {top_attrs[0][0].replace('_', ' ')} "
        summary += f"and {top_attrs[1][0].replace('_', ' ')}. "
        
        # Add constraint insights
        constraints = user_profile["constraints"]
        time = constraints.get("time_per_week", 0)
        
        if time >= 15:
            summary += f"With {time} hours per week, you can pursue intensive tracks. "
        elif time >= 10:
            summary += f"With {time} hours per week, you have good flexibility for most paths. "
        else:
            summary += f"With {time} hours per week, focus on efficient, targeted learning. "
        
        return summary


# Utility function for integration
def process_career_recommendation(mcq_responses: List[int], constraints: Dict, 
                                  interest: str, experience_level: str) -> Dict:
    """
    Main function to process career recommendation request
    
    Args:
        mcq_responses: List of 30 MCQ responses (1-5)
        constraints: Dict with time_per_week, academic_year, financial, internet, device
        interest: "internship", "job", or "skill_building"
        experience_level: "beginner", "intermediate", "advanced"
    
    Returns:
        Complete recommendation output with diagnosis, paths, and roadmap
    """
    engine = CareerEngine()
    
    # Step 1: Diagnose profile
    user_profile = engine.diagnose_profile(mcq_responses, constraints)
    
    # Step 2: Generate diagnosis summary
    diagnosis_summary = engine.generate_diagnosis_summary(user_profile)
    
    # Step 3: Recommend paths
    primary_path, secondary_path = engine.recommend_paths(user_profile)
    
    # Step 4: Generate roadmap for primary path
    roadmap = engine.generate_roadmap(
        primary_path["key"],
        experience_level,
        constraints.get("time_per_week", 10)
    )
    
    # Step 5: Compile output
    output = {
        "diagnosis_summary": diagnosis_summary,
        "primary_path": primary_path,
        "secondary_path": secondary_path,
        "roadmap": roadmap,
        "current_week_focus": roadmap["current_week"],
        "timestamp": datetime.now().isoformat(),
        "requires_commitment": True,
        "commitment_duration": "90 days"
    }
    
    return output
