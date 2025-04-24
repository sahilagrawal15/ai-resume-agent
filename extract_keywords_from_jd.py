from keybert import KeyBERT
import re

kw_model = KeyBERT()

# Fallback soft match hints for generalized terms in JDs
JD_SOFT_MATCH_HINTS = {
    "software development": ["java", "python", "software engineering", "oop", "git", "ci/cd", "unit testing", "design patterns", "rest apis"],
    "programming language": ["java", "python", "c++", "typescript", "go"],
    "design or architecture": ["system design", "microservices", "scalability", "low latency", "design patterns"],
    "development life cycle": ["code review", "git", "jenkins", "ci/cd", "unit testing", "release management"],
    "testing": ["unit testing", "integration testing", "jest", "junit", "pytest"],
    "operations": ["monitoring", "logging", "grafana", "prometheus", "datadog"],
    "agile": ["scrum", "sprints", "standups", "jira"],
    "cloud": ["aws", "gcp", "azure", "cloudformation", "terraform", "docker", "kubernetes"],
    "deployment": ["docker", "kubernetes", "jenkins", "helm", "ansible"],
    "source control": ["git", "github", "gitlab", "bitbucket"],
    "full stack": ["react", "node.js", "express", "graphql", "mongodb", "postgresql"],
    "backend": ["spring boot", "django", "flask", "express", "node.js", "java", "python"],
    "frontend": ["react", "angular", "vue", "typescript", "css", "html", "tailwind"],
    "database": ["postgresql", "mysql", "mongodb", "dynamodb", "redis", "sql"]
}

# Denylist: irrelevant or noisy words frequently extracted
DENYLIST_KEYWORDS = set([
    "alexa", "job", "yes", "true", "love", "career", "description", "enable", "make", "create",
    "see", "interact", "company", "services", "llc", "apply", "click", "workplace", "requirements",
    "responsibilities", "qualifications", "equal", "opportunity", "employer", "information",
    "hiring", "posting", "candidate", "support", "include", "location", "status", "external",
    "internal", "website", "visit", "how", "process", "range", "benefits", "content", "other",
    "region", "listed", "market", "pay", "amazon", "employment", "submit", "site", "submit"
])

def extract_keywords_from_jd(jd_text):
    jd_text_cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', jd_text)
    keywords = kw_model.extract_keywords(jd_text_cleaned, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=30)

    extracted = [
        kw[0].lower()
        for kw in keywords
        if not any(d in kw[0].lower() for d in DENYLIST_KEYWORDS)
    ]

    # Apply soft match inference
    fallback_skills = set()
    for trigger, implied_skills in JD_SOFT_MATCH_HINTS.items():
        if trigger in jd_text.lower():
            fallback_skills.update(implied_skills)

    final_keywords = list(set(extracted).union(fallback_skills))
    return final_keywords
