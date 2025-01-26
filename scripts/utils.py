def save_results(results, filepath):
    """Save results to a file."""
    with open(filepath, 'w') as file:
        file.write(results)
