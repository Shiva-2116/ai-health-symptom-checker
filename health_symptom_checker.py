def symptom_checker(symptom):
    symptom = symptom.lower()

    if symptom == "fever":
        return (
            "Possible cause: Viral fever\n"
            "Advice: Drink plenty of fluids, take rest.\n"
            "Warning: Consult a doctor if fever lasts more than 2 days."
        )

    elif symptom == "cold":
        return (
            "Possible cause: Common cold\n"
            "Advice: Warm fluids, steam inhalation, proper rest."
        )

    elif symptom == "headache":
        return (
            "Possible cause: Stress or dehydration\n"
            "Advice: Take rest and drink water.\n"
            "Warning: Consult a doctor if pain is severe."
        )

    elif symptom == "stomach pain":
        return (
            "Possible cause: Indigestion\n"
            "Advice: Avoid oily food and eat light meals.\n"
            "Warning: Consult a doctor if pain persists."
        )

    elif symptom == "cough":
        return (
            "Possible cause: Throat irritation or infection\n"
            "Advice: Warm water and rest.\n"
            "Warning: Consult a doctor if cough lasts more than a week."
        )

    else:
        return (
            "Symptom not recognized.\n"
            "Please consult a healthcare professional."
        )


if __name__ == "__main__":
    print("=== AI Health Symptom Checker ===")
    user_symptom = input("Enter your symptom: ")
    result = symptom_checker(user_symptom)
    print("\nResult:")
    print(result)
