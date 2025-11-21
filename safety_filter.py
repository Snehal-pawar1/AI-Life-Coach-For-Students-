def is_unsafe(query: str) -> str | None:
    q = query.lower()

    # 1. Medical / Diagnosis
    medical = [
        "medicine", "prescribe", "diagnose", "chest pain", "fever", "covid",
        "treatment", "infection", "disease", "mental disorder"
    ]
    if any(w in q for w in medical):
        return "❌ I cannot give medical or health diagnoses. Please consult a doctor."

    # 2. Legal advice
    legal = ["court", "case", "lawsuit", "legal", "police complaint", "crime penalty"]
    if any(w in q for w in legal):
        return "❌ I cannot provide legal advice. Please contact a lawyer or legal authority."

    # 3. Financial investment
    finance = ["stock", "invest", "crypto", "bitcoin", "trading", "mutual fund"]
    if any(w in q for w in finance):
        return "❌ I cannot give investment or financial advice. Only general tips are allowed."

    # 4. Abuse, hate, harm
    harmful = ["kill", "hurt", "insult", "abuse", "bully", "criminal", "hack", "cheat"]
    if any(w in q for w in harmful):
        return "❌ I cannot help with harmful, abusive, or illegal actions."

    # 5. Suicidal or deep mental health
    suicide = ["suicide", "kill myself", "end my life", "self harm"]
    if any(w in q for w in suicide):
        return (
            "❌ I cannot help with this.\n"
            "Please reach out to someone immediately:\n"
            "📞 India Helpline: 9152987821\n"
            "You are not alone — please talk to a real professional."
        )

    # 6. Personal info / tracking
    personal_info = ["address", "track", "location", "hack phone", "data leak"]
    if any(w in q for w in personal_info):
        return "❌ I cannot access or share personal or private information."

    # 7. Adult content
    adult = ["sex", "porn", "adult", "hot girl", "relationship physical"]
    if any(w in q for w in adult):
        return "❌ I cannot talk about adult or inappropriate content."

    # 8. Political bias
    politics = ["political party", "vote", "election", "propaganda"]
    if any(w in q for w in politics):
        return "❌ I cannot give political advice or influence elections."

    # 9. Dangerous technical instructions
    dangerous = ["bomb", "explosive", "ransomware", "hack wifi", "virus program"]
    if any(w in q for w in dangerous):
        return "❌ I cannot help with dangerous or illegal technical instructions."

    return None  # Safe
