class IntentDetector:

    def detect(self, messages):

        text = " ".join(
            m["content"].lower()
            for m in messages
            if m["role"] == "user"
        )

        if "compare" in text:
            return "compare"

        if "difference" in text:
            return "compare"

        if "add" in text:
            return "refine"

        if "remove" in text:
            return "refine"

        return "recommend"