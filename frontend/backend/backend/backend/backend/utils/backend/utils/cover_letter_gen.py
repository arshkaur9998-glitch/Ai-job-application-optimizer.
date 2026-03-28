from transformers import pipeline
import re

def generate_cover_letter(resume_text, job_description):
    """
    Generate a tailored cover letter based on resume and job description
    """
    try:
        # Extract key information from resume
        name = extract_name(resume_text)
        skills = extract_skills(resume_text)
        experience = extract_experience(resume_text)
        
        # Extract job requirements
        job_requirements = extract_job_requirements(job_description)
        
        # Match skills with requirements
        matched_skills = match_skills(skills, job_requirements)
        
        # Generate cover letter
        cover_letter = create_cover_letter(
            name=name,
            job_title=extract_job_title(job_description),
            matched_skills=matched_skills,
            experience=experience,
            job_description=job_description
        )
        
        return cover_letter
    except Exception as e:
        return f"Error generating cover letter: {str(e)}"

def extract_name(resume_text):
    """Extract name from resume"""
    # Look for name at the beginning or after "Name:"
    lines = resume_text.split('\n')
    for line in lines[:5]:  # Check first 5 lines
        line = line.strip()
        if line and not any(x in line.lower() for x in ['email', 'phone', 'address']):
            return line
    return "Applicant"

def extract_skills(resume_text):
    """Extract skills from resume"""
    skills = []
    
    # Common skill keywords
    skill_patterns = [
        r'(?:python|java|javascript|c\+\+|sql|react|node|aws|docker|git)',
        r'(?:leadership|communication|teamwork|problem.solving)',
        r'(?:machine learning|data analysis|web development|mobile development)'
    ]
    
    text_lower = resume_text.lower()
    for pattern in skill_patterns:
        matches = re.findall(pattern, text_lower, re.IGNORECASE)
        skills.extend(matches)
    
    return list(set(skills))

def extract_experience(resume_text):
    """Extract work experience from resume"""
    # Look for job titles and companies
    experience = []
    
    job_title_pattern = r'(?:Software Engineer|Developer|Manager|Analyst|Designer)'
    matches = re.findall(job_title_pattern, resume_text, re.IGNORECASE)
    
    if matches:
        experience.append(matches[0])
    
    return experience

def extract_job_requirements(job_description):
    """Extract requirements from job description"""
    requirements = []
    
    # Look for "Required", "Must have", "

