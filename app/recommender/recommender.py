from app.catalog.catalog_manager import CatalogManager


class Recommender:

    def __init__(self):
        self.catalog = CatalogManager()

    def recommend(self, requirements, top_k=10):

        results = []

        for assessment in self.catalog.assessments:

            score = 0

            description = assessment.get("description", "").lower()
            name = assessment.get("name", "").lower()

            job_levels = [
                level.lower()
                for level in assessment.get("job_levels", [])
            ]

            categories = [
                key.lower()
                for key in assessment.get("keys", [])
            ]

            # -----------------------
            # Role
            # -----------------------

            if requirements["role"]:

                if requirements["role"].lower() in description:

                    score += 10

            # -----------------------
            # Skills
            # -----------------------

            for skill in requirements["skills"]:

                if skill.lower() in description:

                    score += 8

            # -----------------------
            # Job Level
            # -----------------------

            if requirements["job_level"]:

                if requirements["job_level"].lower() in job_levels:

                    score += 6

            # -----------------------
            # Assessment Type
            # -----------------------

            if requirements["assessment_type"]:

                keyword = requirements["assessment_type"].lower()

                if any(keyword in c for c in categories):

                    score += 5

            # -----------------------
            # Name bonus
            # -----------------------

            for skill in requirements["skills"]:

                if skill.lower() in name:

                    score += 6

            # -----------------------

            if score > 0:

                results.append((score, assessment))

        results.sort(reverse=True, key=lambda x: x[0])

        return [
            item[1]
            for item in results[:top_k]
        ]