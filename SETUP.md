# AutoPCB GitHub Repository Setup

## Quick Start

1. **Create the repo on GitHub:**
   - Go to https://github.com/new
   - Name: `autopcb`
   - Description: "Automated PCB design from JSON specs to KiCad projects"
   - Visibility: Public
   - Add a README (paste the README.md content below)
   - Click "Create repository"

2. **Push the code:**
   ```bash
   cd "C:\Jarvis\workshop\autopcb_marketing\autopcb_github"
   git init
   git add .
   git commit -m "Initial commit: AutoPCB demo repository"
   git remote add origin https://github.com/YOUR_USERNAME/autopcb.git
   git push -u origin main
   ```

3. **Share the link:**
   - GitHub URL: `https://github.com/YOUR_USERNAME/autopcb`
   - Link this in LinkedIn posts, Discord messages, etc.

## Repository Structure

```
autopcb/
├── README.md          # Project description & API docs
├── demo.py            # Demo script showing AutoPCB capabilities
├── .github/
│   └── workflows/
│       └── demo.yml   # GitHub Actions demo workflow
└── LICENSE            # MIT License
```

## Next Steps

After pushing to GitHub:
1. Add to your GitHub profile README
2. Link from LinkedIn posts
3. Share in KiCad Discord server
4. Submit to Hackaday as a project story

## Alternative: No Git

If you don't want to use git:
1. Create the repo manually on GitHub (as above)
2. Download the ZIP from the repo
3. Upload the ZIP to the repo via GitHub's web interface
4. Done!
