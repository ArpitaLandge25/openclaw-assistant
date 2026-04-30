import os

def generate_resume_points(folder):
    points = []

    for file in os.listdir(folder):
        if file.endswith(".py"):
            points.append(f"Developed Python project: {file}")
        elif file.endswith(".pdf"):
            points.append(f"Completed certification: {file}")

    # Print output
    print("\nGenerated Resume Points:\n")
    for p in points:
        print("•", p)

    # Save to file
    with open("data/resume_points.txt", "w") as f:
        for p in points:
            f.write("• " + p + "\n")

    print("\nSaved to data/resume_points.txt ✅")