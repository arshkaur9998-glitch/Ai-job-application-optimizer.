from transformers import pipeline
import re

def analyze_resume(resume_text):
    """
    Analyze resume and provide improvement suggestions
    """
    try:
        # Initialize NLP pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
        # Extract key sections
        sections = extract_sections(resume_text)
        
        # Analyze each section
        analysis_results = {
            "sections_found": list(sections.keys()),
            "resume_score": calculate_score(resume_text),
            "strengths": extract_strengths(resume_text),
            "improvements": get_improvements(resume_text),
            "missing_sections": find_missing_sections(sections),
            "keyword_analysis": analyze_keywords(resume_text)
        }
        
        return analysis_results
    except Exception as e:
        return {"error": str(e)}

def extract_sections(resume_text):
    """Extract main sections from resume"""
    sections = {}
    section_patterns = {
        'contact': r'(contact|email|phone)',
        'summary': r'(professional summary|objective)',
        'experience': r'(work experience|employment|professional)',
        'education': r'(education|degree|university)',
        'skills': r'(skills|technical|proficiency)',
        'projects': r'(projects|portfolio)',
        'certifications': r'(certifications|courses|training)'
    }
    
    text_lower = resume_text.lower()
    for section, pattern in section_patterns.items():
        if re.search(pattern, text_lower):
            sections[section] = True
    
    return sections

def calculate_score(resume_text):
    """Calculate resume score (0-100)"""
    score = 0
    
    # Check for key elements
    if len(resume_text) > 500:
        score += 10
    if re.search(r'\d{4}-\d{4}|\d{4}-present', resume_text):
        score += 15  # Has dates
    if re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resume_text):
        score += 10  # Has email
    if re.search(r'\+?\d{10,}', resume_text):
        score += 10  # Has phone
    if re.search(r'github|linkedin|portfolio', resume_text, re.IGNORECASE):
        score += 15  # Has links
    if len(resume_text.split()) > 200:
        score += 20  # Good length
    if re.search(r'[A-Z][a-z]+\s+[A-Z][a-z]+', resume_text):
        score += 20  # Has proper formatting
    
    return min(score, 100)

def extract_strengths(resume_text):
    """Extract strengths from resume"""
    strengths = []
    
    if re.search(r'python|java|javascript|c\+\+|sql', resume_text, re.IGNORECASE):
        strengths.append("Has technical skills")
    if re.search(r'led|managed|organized|coordinated', resume_text, re.IGNORECASE):
        strengths.append("Shows leadership experience")
    if re.search(r'bachelor|master|phd', resume_text, re.IGNORECASE):
        strengths.append("Has formal education")
    if re.search(r'project|achievement|award', resume_text, re.IGNORECASE):
        strengths.append("Highlights achievements")
    
    return strengths

def get_improvements(resume_text):
    """Get improvement suggestions"""
    improvements = []
    
    if len(resume_text) < 300:
        improvements.append("Resume is too short. Aim for at least 300 words.")
    if not re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', resume_text):
        improvements.append("Add your email address")
    if not re.search(r'\+?\d{10,}', resume_text):
        improvements.append("Add your phone number")
    if not re.search(r'github|linkedin', resume_text, re.IGNORECASE):
        improvements.append("Add links to your portfolio or LinkedIn")
    if not re.search(r'\d{4}-\d{4}|\d{4}-present', resume_text):
        improvements.append("Add dates to your experience entries")
    
    return improvements

def find_missing_sections(sections):
    """Find missing sections"""
    all_sections = {'contact', 'summary', 'experience', 'education', 'skills', 'projects', 'certifications'}
    return list(all_sections - set(sections.keys()))

def analyze_keywords(resume_text):
    """Analyze keywords in resume"""
    keywords = {}
    
    tech_skills = ['python', 'java', 'javascript', 'react', 'node', 'sql', 'aws', 'docker']
    soft_skills = ['leadership', 'communication', 'teamwork', 'problem-solving']
    
    text_lower = resume_text.lower()
    
    for skill in tech_skills:
        if skill in text_lower:
            keywords[skill] = True
    
    for skill in soft_skills:
        if skill in text_lower:
            keywords[skill] = True
    
    return keywords
