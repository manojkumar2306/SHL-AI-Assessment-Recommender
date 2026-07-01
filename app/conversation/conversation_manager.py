import re


class ConversationManager:
    """
    Extracts user requirements from conversation history.
    """

    def extract_requirements(self, messages):

        requirements = {
            "role": None,
            "skills": [],
            "experience": None,
            "job_level": None,
            "assessment_type": None
        }

        text = " ".join(
            message["content"]
            for message in messages
            if message["role"] == "user"
        ).lower()

        # -------------------------
        # Experience
        # -------------------------

        exp = re.search(r"(\d+)\s*(year|years)", text)

        if exp:
            requirements["experience"] = exp.group(1)

        # -------------------------
        # Skills
        # -------------------------

        skills = [
            "python",
            "java",
            "sql",
            "aws",
            "docker",
            "excel",
            "power bi",
            "communication",
            "leadership",
            "sales",
            "machine learning",
            "ai"
        ]

        for skill in skills:
            if skill in text:
                requirements["skills"].append(skill)

        # -------------------------
        # Roles
        # -------------------------

        roles = [
            "software engineer",
            "developer",
            "data analyst",
            "business analyst",
            "manager",
            "sales executive",
            "intern"
        ]

        for role in roles:
            if role in text:
                requirements["role"] = role
                break

        # -------------------------
        # Job Level
        # -------------------------

        job_levels = [
            "graduate",
            "entry-level",
            "mid-professional",
            "manager",
            "director",
            "executive",
            "supervisor"
        ]

        for level in job_levels:
            if level in text:
                requirements["job_level"] = level
                break

        # -------------------------
        # Assessment Type
        # -------------------------

        assessment_types = {
            "technical": "Technical",
            "personality": "Personality",
            "behavior": "Behavior",
            "behaviour": "Behavior",
            "cognitive": "Cognitive",
            "aptitude": "Aptitude"
        }

        for keyword, value in assessment_types.items():
            if keyword in text:
                requirements["assessment_type"] = value
                break

        return requirements

    def missing_information(self, requirements):

        missing = []

        if requirements["role"] is None:
            missing.append("role")

        if len(requirements["skills"]) == 0:
            missing.append("skills")

        return missing