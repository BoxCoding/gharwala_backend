# GitHub Setup Instructions

## Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. Enter repository name (e.g., `gharwala_backend`)
3. Choose public or private
4. **DO NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

## Step 2: Connect Local Repository to GitHub

After creating the repository on GitHub, run these commands:

```bash
# Add remote repository (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Or if using SSH:
git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Update Git Email (Optional but Recommended)

To set your GitHub email globally:
```bash
git config --global user.email "your-github-email@example.com"
```

## Quick Commands Reference

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Pull from GitHub
git pull
```



