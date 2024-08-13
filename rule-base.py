def diagnose(symptoms):
    # Rule 1: If the patient has a fever and cough, then they may have the flu.
    if 'fever' in symptoms and 'cough' in symptoms:
        return "You might have the flu."

    # Rule 2: If the patient has a headache and fever, then they may have a migraine.
    if 'headache' in symptoms and 'fever' in symptoms:
        return "You might have a migraine."

    # Rule 3: If the patient has a sore throat and cough, then they may have a cold.
    if 'sore throat' in symptoms and 'cough' in symptoms:
        return "You might have a cold."

    # Rule 4: If the patient has a runny nose and sneezing, then they may have allergies.
    if 'runny nose' in symptoms and 'sneezing' in symptoms:
        return "You might have allergies."

    # Default Rule: If no rules match, then the diagnosis is unknown.
    return "Diagnosis unclear, please consult a doctor."

# Main function to run the diagnosis
def main():
    # List of symptoms provided by the user
    symptoms = []

    # Asking the user for symptoms
    print("Enter your symptoms (type 'done' when finished):")
    while True:
        symptom = input("Symptom: ").lower()
        if symptom == 'done':
            break
        symptoms.append(symptom)

    # Diagnosing based on the given symptoms
    diagnosis = diagnose(symptoms)
    print(diagnosis)

# Run the main function
main()
