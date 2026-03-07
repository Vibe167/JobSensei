"""
Course Recommendation API Service
Integrates YouTube Data API and Coursera API for personalized course recommendations
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json

class CourseRecommendationService:
    """Service to fetch courses from YouTube and Coursera"""
    
    def __init__(self):
        # API Keys - Store these in environment variables or config
        self.youtube_api_key = os.getenv('YOUTUBE_API_KEY', 'YOUR_YOUTUBE_API_KEY')
        self.youtube_base_url = 'https://www.googleapis.com/youtube/v3'
        
        # Coursera doesn't have a public API, so we'll use web scraping or alternative methods
        # For now, we'll use curated Coursera links
        
        # Career-specific search queries
        self.career_queries = {
            'software_engineer_backend': [
                'backend development tutorial',
                'system design course',
                'database design tutorial',
                'API development course',
                'microservices architecture'
            ],
            'frontend_developer': [
                'react tutorial',
                'javascript course',
                'html css tutorial',
                'frontend development',
                'web design course'
            ],
            'fullstack_developer': [
                'full stack development',
                'MERN stack tutorial',
                'web development bootcamp',
                'full stack course',
                'node.js tutorial'
            ],
            'data_scientist': [
                'data science tutorial',
                'machine learning course',
                'python for data science',
                'data analysis tutorial',
                'statistics for data science'
            ],
            'ui_ux_designer': [
                'UI UX design tutorial',
                'figma tutorial',
                'user experience design',
                'design thinking course',
                'prototyping tutorial'
            ],
            'devops_engineer': [
                'devops tutorial',
                'docker kubernetes course',
                'CI CD pipeline',
                'cloud computing tutorial',
                'AWS tutorial'
            ],
            'mobile_developer': [
                'react native tutorial',
                'flutter course',
                'mobile app development',
                'android development',
                'iOS development'
            ],
            'ai_ml_engineer': [
                'artificial intelligence course',
                'deep learning tutorial',
                'neural networks course',
                'tensorflow tutorial',
                'machine learning projects'
            ],
            'cybersecurity': [
                'cybersecurity tutorial',
                'ethical hacking course',
                'network security',
                'penetration testing',
                'security fundamentals'
            ],
            'product_manager': [
                'product management course',
                'agile scrum tutorial',
                'product strategy',
                'user research methods',
                'product roadmap'
            ],
            'digital_marketing': [
                'digital marketing course',
                'SEO tutorial',
                'social media marketing',
                'content marketing',
                'google analytics tutorial'
            ],
            'business_analyst': [
                'business analysis course',
                'data analytics tutorial',
                'SQL for business',
                'business intelligence',
                'requirements gathering'
            ]
        }
        
        # Curated Coursera courses by career path
        self.coursera_courses = {
            'software_engineer_backend': [
                {
                    'title': 'Python for Everybody Specialization',
                    'provider': 'University of Michigan',
                    'url': 'https://www.coursera.org/specializations/python',
                    'level': 'Beginner',
                    'duration': '8 months'
                },
                {
                    'title': 'Algorithms Specialization',
                    'provider': 'Stanford University',
                    'url': 'https://www.coursera.org/specializations/algorithms',
                    'level': 'Intermediate',
                    'duration': '4 months'
                },
                {
                    'title': 'Database Design and Basic SQL',
                    'provider': 'University of Michigan',
                    'url': 'https://www.coursera.org/learn/database-design',
                    'level': 'Beginner',
                    'duration': '4 weeks'
                }
            ],
            'frontend_developer': [
                {
                    'title': 'HTML, CSS, and Javascript for Web Developers',
                    'provider': 'Johns Hopkins University',
                    'url': 'https://www.coursera.org/learn/html-css-javascript-for-web-developers',
                    'level': 'Beginner',
                    'duration': '5 weeks'
                },
                {
                    'title': 'React Basics',
                    'provider': 'Meta',
                    'url': 'https://www.coursera.org/learn/react-basics',
                    'level': 'Intermediate',
                    'duration': '4 weeks'
                },
                {
                    'title': 'Advanced React',
                    'provider': 'Meta',
                    'url': 'https://www.coursera.org/learn/advanced-react',
                    'level': 'Advanced',
                    'duration': '4 weeks'
                }
            ],
            'fullstack_developer': [
                {
                    'title': 'Full-Stack Web Development with React',
                    'provider': 'Hong Kong University',
                    'url': 'https://www.coursera.org/specializations/full-stack-react',
                    'level': 'Intermediate',
                    'duration': '6 months'
                },
                {
                    'title': 'Server-side Development with NodeJS',
                    'provider': 'Hong Kong University',
                    'url': 'https://www.coursera.org/learn/server-side-nodejs',
                    'level': 'Intermediate',
                    'duration': '4 weeks'
                }
            ],
            'data_scientist': [
                {
                    'title': 'Data Science Specialization',
                    'provider': 'Johns Hopkins University',
                    'url': 'https://www.coursera.org/specializations/jhu-data-science',
                    'level': 'Intermediate',
                    'duration': '11 months'
                },
                {
                    'title': 'Machine Learning',
                    'provider': 'Stanford University',
                    'url': 'https://www.coursera.org/learn/machine-learning',
                    'level': 'Intermediate',
                    'duration': '11 weeks'
                },
                {
                    'title': 'Applied Data Science with Python',
                    'provider': 'University of Michigan',
                    'url': 'https://www.coursera.org/specializations/data-science-python',
                    'level': 'Intermediate',
                    'duration': '5 months'
                }
            ],
            'ui_ux_designer': [
                {
                    'title': 'Google UX Design Professional Certificate',
                    'provider': 'Google',
                    'url': 'https://www.coursera.org/professional-certificates/google-ux-design',
                    'level': 'Beginner',
                    'duration': '6 months'
                },
                {
                    'title': 'UI / UX Design Specialization',
                    'provider': 'CalArts',
                    'url': 'https://www.coursera.org/specializations/ui-ux-design',
                    'level': 'Beginner',
                    'duration': '4 months'
                }
            ],
            'devops_engineer': [
                {
                    'title': 'DevOps on AWS Specialization',
                    'provider': 'AWS',
                    'url': 'https://www.coursera.org/specializations/aws-devops',
                    'level': 'Intermediate',
                    'duration': '4 months'
                },
                {
                    'title': 'Docker and Kubernetes',
                    'provider': 'IBM',
                    'url': 'https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift',
                    'level': 'Intermediate',
                    'duration': '4 weeks'
                }
            ],
            'mobile_developer': [
                {
                    'title': 'Meta React Native Specialization',
                    'provider': 'Meta',
                    'url': 'https://www.coursera.org/specializations/meta-react-native',
                    'level': 'Intermediate',
                    'duration': '8 months'
                },
                {
                    'title': 'Android App Development',
                    'provider': 'Vanderbilt University',
                    'url': 'https://www.coursera.org/specializations/android-app-development',
                    'level': 'Intermediate',
                    'duration': '6 months'
                }
            ],
            'ai_ml_engineer': [
                {
                    'title': 'Deep Learning Specialization',
                    'provider': 'DeepLearning.AI',
                    'url': 'https://www.coursera.org/specializations/deep-learning',
                    'level': 'Intermediate',
                    'duration': '5 months'
                },
                {
                    'title': 'Machine Learning Engineering for Production',
                    'provider': 'DeepLearning.AI',
                    'url': 'https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops',
                    'level': 'Advanced',
                    'duration': '4 months'
                }
            ],
            'cybersecurity': [
                {
                    'title': 'Google Cybersecurity Professional Certificate',
                    'provider': 'Google',
                    'url': 'https://www.coursera.org/professional-certificates/google-cybersecurity',
                    'level': 'Beginner',
                    'duration': '6 months'
                },
                {
                    'title': 'Cybersecurity Specialization',
                    'provider': 'University of Maryland',
                    'url': 'https://www.coursera.org/specializations/cyber-security',
                    'level': 'Intermediate',
                    'duration': '6 months'
                }
            ],
            'product_manager': [
                {
                    'title': 'Digital Product Management Specialization',
                    'provider': 'University of Virginia',
                    'url': 'https://www.coursera.org/specializations/uva-darden-digital-product-management',
                    'level': 'Intermediate',
                    'duration': '5 months'
                },
                {
                    'title': 'Product Management Fundamentals',
                    'provider': 'University of Maryland',
                    'url': 'https://www.coursera.org/learn/umd-product-management-fundamentals',
                    'level': 'Beginner',
                    'duration': '4 weeks'
                }
            ],
            'digital_marketing': [
                {
                    'title': 'Google Digital Marketing & E-commerce',
                    'provider': 'Google',
                    'url': 'https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce',
                    'level': 'Beginner',
                    'duration': '6 months'
                },
                {
                    'title': 'Digital Marketing Specialization',
                    'provider': 'University of Illinois',
                    'url': 'https://www.coursera.org/specializations/digital-marketing',
                    'level': 'Beginner',
                    'duration': '8 months'
                }
            ],
            'business_analyst': [
                {
                    'title': 'Business Analytics Specialization',
                    'provider': 'University of Pennsylvania',
                    'url': 'https://www.coursera.org/specializations/business-analytics',
                    'level': 'Intermediate',
                    'duration': '8 months'
                },
                {
                    'title': 'Data Analysis and Visualization',
                    'provider': 'IBM',
                    'url': 'https://www.coursera.org/professional-certificates/ibm-data-analyst',
                    'level': 'Beginner',
                    'duration': '11 months'
                }
            ]
        }
    
    def get_youtube_courses(self, career_path: str, max_results: int = 10) -> List[Dict]:
        """
        Fetch YouTube courses/playlists for a specific career path
        
        Args:
            career_path: Career path key (e.g., 'frontend_developer')
            max_results: Maximum number of results to return
        
        Returns:
            List of course dictionaries
        """
        if self.youtube_api_key == 'YOUR_YOUTUBE_API_KEY':
            print("⚠️  YouTube API key not configured. Using sample data.")
            return self._get_sample_youtube_courses(career_path)
        
        queries = self.career_queries.get(career_path, ['programming tutorial'])
        all_courses = []
        
        for query in queries[:2]:  # Limit to 2 queries to avoid API quota
            try:
                # Search for playlists
                playlist_url = f"{self.youtube_base_url}/search"
                playlist_params = {
                    'part': 'snippet',
                    'q': query,
                    'type': 'playlist',
                    'maxResults': 3,
                    'key': self.youtube_api_key,
                    'order': 'relevance',
                    'relevanceLanguage': 'en'
                }
                
                response = requests.get(playlist_url, params=playlist_params)
                response.raise_for_status()
                data = response.json()
                
                for item in data.get('items', []):
                    course = {
                        'id': item['id']['playlistId'],
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'][:200] + '...',
                        'thumbnail': item['snippet']['thumbnails']['medium']['url'],
                        'channel': item['snippet']['channelTitle'],
                        'url': f"https://www.youtube.com/playlist?list={item['id']['playlistId']}",
                        'type': 'playlist',
                        'platform': 'YouTube',
                        'kind': 'youtube#playlist'
                    }
                    all_courses.append(course)
                
            except Exception as e:
                print(f"Error fetching YouTube courses: {e}")
                continue
        
        return all_courses[:max_results]
    
    def _get_sample_youtube_courses(self, career_path: str) -> List[Dict]:
        """Return sample YouTube courses when API key is not configured"""
        samples = {
            'frontend_developer': [
                {
                    'id': 'sample1',
                    'title': 'Complete React Course - Beginner to Advanced',
                    'description': 'Learn React from scratch with hands-on projects...',
                    'thumbnail': 'https://i.ytimg.com/vi/bMknfKXIFA8/mqdefault.jpg',
                    'channel': 'freeCodeCamp.org',
                    'url': 'https://www.youtube.com/watch?v=bMknfKXIFA8',
                    'type': 'video',
                    'platform': 'YouTube',
                    'kind': 'youtube#video'
                },
                {
                    'id': 'sample2',
                    'title': 'JavaScript Full Course',
                    'description': 'Complete JavaScript tutorial for beginners...',
                    'thumbnail': 'https://i.ytimg.com/vi/PkZNo7MFNFg/mqdefault.jpg',
                    'channel': 'freeCodeCamp.org',
                    'url': 'https://www.youtube.com/watch?v=PkZNo7MFNFg',
                    'type': 'video',
                    'platform': 'YouTube',
                    'kind': 'youtube#video'
                }
            ]
        }
        return samples.get(career_path, samples['frontend_developer'])
    
    def get_coursera_courses(self, career_path: str) -> List[Dict]:
        """
        Get curated Coursera courses for a specific career path
        
        Args:
            career_path: Career path key
        
        Returns:
            List of Coursera course dictionaries
        """
        courses = self.coursera_courses.get(career_path, [])
        
        # Add platform and type info
        for course in courses:
            course['platform'] = 'Coursera'
            course['type'] = 'course'
            course['thumbnail'] = 'https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-course-photos.s3.amazonaws.com/fb/36e9e0c91011e6b8f1d3c4e5e6f5e5/logo.png'
        
        return courses
    
    def get_all_recommendations(self, career_path: str, include_youtube: bool = True, 
                               include_coursera: bool = True) -> Dict:
        """
        Get comprehensive course recommendations from all platforms
        
        Args:
            career_path: Career path key
            include_youtube: Whether to include YouTube courses
            include_coursera: Whether to include Coursera courses
        
        Returns:
            Dictionary with courses from different platforms
        """
        recommendations = {
            'career_path': career_path,
            'youtube_courses': [],
            'coursera_courses': [],
            'total_courses': 0,
            'generated_at': datetime.now().isoformat()
        }
        
        if include_youtube:
            recommendations['youtube_courses'] = self.get_youtube_courses(career_path)
        
        if include_coursera:
            recommendations['coursera_courses'] = self.get_coursera_courses(career_path)
        
        recommendations['total_courses'] = (
            len(recommendations['youtube_courses']) + 
            len(recommendations['coursera_courses'])
        )
        
        return recommendations


# Utility function for Flask integration
def get_course_recommendations(career_path: str) -> Dict:
    """
    Main function to get course recommendations
    
    Args:
        career_path: Career path key
    
    Returns:
        Dictionary with course recommendations
    """
    service = CourseRecommendationService()
    return service.get_all_recommendations(career_path)


if __name__ == "__main__":
    # Test the service
    print("\n" + "="*60)
    print("🎓 TESTING COURSE RECOMMENDATION SERVICE")
    print("="*60)
    
    service = CourseRecommendationService()
    
    # Test with frontend developer
    print("\n📚 Fetching courses for Frontend Developer...")
    recommendations = service.get_all_recommendations('frontend_developer')
    
    print(f"\n✅ Found {recommendations['total_courses']} courses:")
    print(f"   - YouTube: {len(recommendations['youtube_courses'])} courses")
    print(f"   - Coursera: {len(recommendations['coursera_courses'])} courses")
    
    print("\n📺 Sample YouTube Course:")
    if recommendations['youtube_courses']:
        course = recommendations['youtube_courses'][0]
        print(f"   Title: {course['title']}")
        print(f"   Channel: {course['channel']}")
        print(f"   URL: {course['url']}")
    
    print("\n🎓 Sample Coursera Course:")
    if recommendations['coursera_courses']:
        course = recommendations['coursera_courses'][0]
        print(f"   Title: {course['title']}")
        print(f"   Provider: {course['provider']}")
        print(f"   URL: {course['url']}")
    
    print("\n" + "="*60)
