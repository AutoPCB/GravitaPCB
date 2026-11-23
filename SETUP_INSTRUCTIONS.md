# AutoPCB GitHub Repository Setup

## Quick Start (No Git Required)

### Option 1: Create Repo Manually on GitHub.com (Recommended)

1. **Go to:** https://github.com/new
2. **Fill in:**
   - Repository name: `autopcb`
   - Description: "Automated PCB design from JSON specs to KiCad projects"
   - Visibility: `Public`
   - Check "Add a README file"
   - Click "Create repository"
3. **Upload files:**
   - Go to the repo you just created
   - Click "uploading an existing file"
   - Drag and drop all files from `C:\Jarvis\workshop\autopcb_marketing\autopcb_github\`
   - Commit the changes
4. **Done!** Your repo is live at: `https://github.com/YOUR_USERNAME/autopcb`

### Option 2: Use Git (If you have GitHub credentials)

```bash
cd "C:\Jarvis\workshop\autopcb_marketing\autopcb_github"
git add .
git commit -m "Initial commit: AutoPCB demo repository"
git remote add origin https://github.com/YOUR_USERNAME/autopcb.git
git push -u origin main
```

## Repository Contents

- **README.md** - Project description & API documentation
- **demo.py** - Demo script showing AutoPCB capabilities
- **index.html** - Landing page for the project
- **.github/workflows/demo.yml** - GitHub Actions demo workflow
- **SETUP.md** - Setup instructions
- **LICENSE** - MIT License

## Share Your Repo

Once created, share this link:
- GitHub: `https://github.com/YOUR_USERNAME/autopcb`
- LinkedIn posts
- KiCad Discord server
- Hackaday submission

## Next Steps

After creating the repo:
1. Share the link in LinkedIn posts
2. Post in KiCad Discord server (#general or #showcase)
3. Submit to Hackaday as a project story
4. Add to your GitHub profile README
