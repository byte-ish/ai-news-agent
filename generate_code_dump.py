import os

# Define the output file name
OUTPUT_FILE = "output.txt"
EXCLUDE_DIRS = {
    ".venv",
    "venv",
    "__pycache__",
    "logs",
    "tests",
    ".git",
    ".idea",
}  # Directories to ignore


def collect_python_files(directory):
    """
    Recursively collects all Python files (.py) in the given directory.
    Excludes specified directories like .venv and __pycache__.
    """
    python_files = []
    for root, _, files in os.walk(directory):
        # Skip excluded directories
        if any(excluded in root.split(os.sep) for excluded in EXCLUDE_DIRS):
            continue
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def generate_code_dump(project_root):
    """
    Reads all Python files in the project and writes them to output.txt
    with file paths as comments.
    """
    python_files = collect_python_files(project_root)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        for file_path in python_files:
            try:
                # Write the file path as a comment
                output.write(f"# ====== File: {file_path} ======\n\n")
                with open(file_path, "r", encoding="utf-8") as file:
                    output.write(file.read() + "\n\n" + "=" * 80 + "\n\n")
            except Exception as e:
                print(f"⚠️ Skipping {file_path}: {e}")

    print(f"✅ Code dump created successfully in {OUTPUT_FILE}")


if __name__ == "__main__":
    # Change '.' to your project root if needed
    generate_code_dump(".")
