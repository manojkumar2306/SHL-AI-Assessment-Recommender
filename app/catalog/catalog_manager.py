import json
from pathlib import Path


class CatalogManager:
    def __init__(self):
        self.catalog_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "shl_product_catalog.json"
        )

        self.assessments = self.load_catalog()

    def load_catalog(self):
        with open(self.catalog_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def total_assessments(self):
        return len(self.assessments)

    def search(self, query: str):
        """
        Search across multiple fields in the catalog.
        """
        query = query.lower().strip()
        results = []

        for assessment in self.assessments:

            searchable_text = " ".join([
                assessment.get("name", ""),
                assessment.get("description", ""),
                " ".join(assessment.get("job_levels", [])),
                " ".join(assessment.get("languages", [])),
                " ".join(assessment.get("keys", [])),
                assessment.get("duration", ""),
                assessment.get("remote", ""),
                assessment.get("adaptive", "")
            ]).lower()

            if query in searchable_text:
                results.append(assessment)

        return results


if __name__ == "__main__":
    catalog = CatalogManager()

    print(f"Loaded {catalog.total_assessments()} assessments.\n")

    while True:

        query = input("\nSearch (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        matches = catalog.search(query)

        print(f"\nFound {len(matches)} matching assessments.\n")

        for assessment in matches[:10]:

            print("=" * 60)
            print("Name :", assessment["name"])
            print("Job Levels :", ", ".join(assessment["job_levels"]))
            print("Categories :", ", ".join(assessment["keys"]))
            print("Remote :", assessment["remote"])
            print("Adaptive :", assessment["adaptive"])