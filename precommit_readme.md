# 🔹 Using Pre-commit for Code Quality

## 📌 What is Pre-commit?
`pre-commit` is a **Git hook manager** that runs automatic **code quality checks** before allowing commits. It ensures **clean, formatted, and error-free code**.

## 📖 Setup Instructions

### ✅ **1. Install Pre-commit**
Ensure `pre-commit` is installed inside your virtual environment:
```bash
pip install pre-commit
```

### ✅ **2. Install Hooks**
Run the following command to install pre-commit hooks in your repository:
```bash
pre-commit install
```
This ensures that every time you run `git commit`, **code quality checks will run automatically**.

### ✅ **3. Run Pre-commit on All Files (First-Time Setup)**
To check and fix all files in the repository, run:
```bash
pre-commit run --all-files
```

---

## 🎯 **How Pre-commit Works**
1. When you **run `git commit -m "message"`**, pre-commit automatically:
   - **Formats the code** (Black, isort)
   - **Runs linting checks** (Flake8)
   - **Scans for security issues** (Bandit)
   - **Prevents committing large files**
   - **Checks for sensitive secrets (API keys, passwords)**

2. **If an issue is found**:
   - Pre-commit **automatically fixes** issues where possible.
   - If manual changes are needed, the commit will **fail**, and you must **fix the errors before retrying**.

---

## 🛠 **Troubleshooting**
### ❌ **1. Pre-commit Prevents Commit**
If `pre-commit` modifies files (like fixing imports), **you must re-stage the changes**:
```bash
git add .
git commit -m "Fix: Auto-formatted code"
```

### ❌ **2. Run Pre-commit Manually**
To manually check for issues before committing, run:
```bash
pre-commit run --all-files
```

### ❌ **3. Uninstall Pre-commit (If Needed)**
```bash
pre-commit uninstall
```

---

## 📜 **Pre-commit Hooks Used in This Project**
| **Hook**       | **Purpose** |
|---------------|------------|
| `black`       | Auto-formats Python code |
| `flake8`      | Lints Python code for errors |
| `isort`       | Ensures imports are structured properly |
| `bandit`      | Scans for security vulnerabilities |
| `detect-secrets` | Prevents committing API keys, passwords |
| `check-added-large-files` | Prevents adding large files (512KB+) |

---

### 🚀 **Now, You're Ready to Commit Code Like a Pro!**
With `pre-commit`, your **code remains clean, secure, and consistent** before every commit! 🛠✨
