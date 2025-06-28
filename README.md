# Home
# Naresh Kumar Medicinal Chemistry Research Group Website

This is the official website for the Naresh Kumar Medicinal Chemistry Research Group at UNSW Sydney. The website is built using Jekyll, a static site generator that transforms plain text files into a complete website.

## Project Structure

```
.
├── _config.yml          # Main configuration file
├── _layouts/           # Layout templates
│   └── default.html    # Default page layout
├── _posts/            # Blog posts and news
│   └── 2025-05-26-welcome-to-jekyll.markdown
├── _site/             # Generated site (do not edit)
├── assets/            # Static assets
│   ├── css/          # Stylesheets
│   │   └── main.scss
│   ├── js/           # JavaScript files
│   │   └── main.js
│   └── images/       # Image files
├── about.md          # About page content
├── contact.md        # Contact page content
├── Gemfile          # Ruby dependencies
├── Gemfile.lock     # Locked Ruby dependencies
├── index.md         # Homepage content
├── people.md        # Team members page
├── publications.md  # Publications page
├── research.md      # Research page
├── 404.html         # Custom 404 page
├── package.json     # Node.js dependencies and scripts
└── .gitignore       # Git ignore rules
```

## Technologies Used

| Technology | Purpose | Details |
|------------|---------|---------|
| Jekyll | Static Site Generator | Version 4.4.1 |
| Ruby | Backend | Version 3.2.2 |
| SCSS/CSS | Styling | Custom responsive design |
| JavaScript | Interactivity | Modern ES6+ features |
| Liquid | Templating | Jekyll's template language |
| YAML | Configuration | Site settings and metadata |
| Node.js | Development Tools | ESLint, security scanning |

## Key Features

1. **Responsive Design**
   - Mobile-first approach
   - Adaptive layouts for all devices
   - Smooth navigation experience

2. **Modern UI Components**
   - Clean and professional design
   - Interactive elements
   - Smooth animations and transitions
   - Custom 404 page

3. **Research Showcase**
   - Detailed research areas
   - Project descriptions
   - Interactive project sections
   - Media integration (images, videos)

4. **Team Profiles**
   - Comprehensive member profiles
   - Research interests
   - Professional achievements
   - Dynamic team sections

5. **Publication Management**
   - Organized publication list
   - Filtering capabilities
   - Citation information
   - DOI links

6. **Contact System**
   - Interactive contact form
   - Location map
   - Social media integration
   - Direct email links

## Setup Instructions

### Prerequisites

- Ruby (version 3.2.2 or later)
- Bundler
- Node.js (for development tools)
- Conda (for environment management)

### Installation

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd website
   ```

2. **Set up Ruby environment**
   ```bash
   conda create -n jekyll-env ruby=3.2.2
   conda activate jekyll-env
   ```

3. **Install Ruby dependencies**
   ```bash
   bundle install
   ```

4. **Install Node.js dependencies (optional, for development)**
   ```bash
   npm install
   ```

5. **Start the development server**
   ```bash
   bundle exec jekyll serve
   ```

The site will be available at `http://localhost:4000`

## Development Guidelines

### Adding New Content

1. **Pages**: Create new `.md` files in the project root with front matter
2. **Posts**: Add new `.md` files in `_posts/` with format `YYYY-MM-DD-title.md`
3. **Team Members**: Update `people.md` with new member information
4. **Publications**: Add new publications in `publications.md`
5. **Research**: Update `research.md` with new projects and findings

### Styling

- Main styles: `assets/css/main.scss`
- Custom styles: Add to existing SCSS files
- Responsive design: Mobile-first approach
- Color scheme: Defined in SCSS variables

### Images and Media

- Location: `assets/images/`
- Formats: JPG, PNG, SVG
- Optimization: Use appropriate compression
- Lazy loading: Enabled for better performance

### Development Tools

The project includes several development tools:

```bash
# Security audit
npm run security-audit

# Check for dependency updates
npm run check-deps

# Lint code
npm run lint

# Run all security checks
npm run security-scan
```

## Deployment

The site can be deployed to various platforms:

1. **GitHub Pages**
   - Enable GitHub Pages in repository settings
   - Set source to main branch
   - Configure custom domain if needed

2. **Netlify**
   - Connect repository to Netlify
   - Configure build settings:
     - Build command: `bundle exec jekyll build`
     - Publish directory: `_site`

3. **Custom Server**
   - Build the site: `bundle exec jekyll build`
   - Deploy `_site` directory to your server

## Contributing

1. Create a new branch for your changes
2. Make your changes
3. Run development tools to ensure quality
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions about the website, please contact:

- **Email**: n.kumar@unsw.edu.au
- **Address**: School of Chemistry, UNSW Sydney, NSW 2052, Australia
- **Social Media**:
  - ResearchGate: [Naresh Kumar](https://www.researchgate.net/profile/Naresh-Kumar-100)
  - LinkedIn: [Profile Link]
  - Twitter: [@handle]
 






_This entire pipeline is made publicly available as open-source software, intended solely for educational. The developer assumes no responsibility or liability for any misuse, errors, or damages arising from the use of this code. for further enquiry reach out to admin_ 
