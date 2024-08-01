def load_payloads(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(f"Error loading payloads: {e}")
        return []
