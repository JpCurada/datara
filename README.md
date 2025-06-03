# DataCamp Database Management System for Organization Admins
<div align="center">

![Status](https://img.shields.io/badge/Status-Ongoing-blue)
![DataCamp](https://img.shields.io/badge/Platform-DataCamp-brightgreen?logo=datacamp&logoColor=white)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Ready-FF9900?logo=amazon-aws&logoColor=white)

</div>

## Team Members
**Group 1 of BS CS 2-5**
- ACO, Cris Jericho DL.
- CURADA, John Paul M.
- GRAGAS, Nethan Edry L.
- NADONGA, Solomon M.
- RIMON, Jairus Chrisnie R.

---

## About DataCamp

DataCamp is a leading online learning platform specializing in data science, analytics, and AI education through interactive courses, projects, and assessments. With a mission to democratize data skills globally, DataCamp offers comprehensive training from beginner to advanced levels across programming languages like Python, R, SQL, and various data tools. Through DataCamp Donates, the company extends its impact by providing free access to underserved communities, educational institutions, and nonprofit organizations worldwide.

### DataCamp Donates Impact:
- **40K+** one-year scholarships donated (valued at $15M+)
- **199** partner organizations (new and returning)
- **2.8K+** active universities and secondary schools
- **10K+** active educators
- **205K+** students actively learning with DataCamp
- **160** Teacher Ambassadors leading change across 180 countries

In Polytechnic University of the Philippines (PUP), DataCamp partners with organizations like Google Developer Group On Campus PUP and Amazon Web Service Cloud Club PUP, which cater to students passionate about data science and AI.

---

## The Challenge

Organization admins like JP and Jen of GDG On Campus PUP manage substantial scholarship programs (1,000 scholars, with 500 from PUP and 500 from other institutions or underserved communities) using cobbled-together solutions not designed for this purpose.

### Current administrative challenges include:
- Manual issuance and processing of application forms
- Inefficient tracking of scholar demographics and progress
- Time-consuming evaluation of scholarship applications
- Complex management of waitlisted applicants
- Difficulty tracking applicants who abandon the process at various stages
- Manual email communications for acceptances and waitlist notifications
- Cumbersome processes for Memorandum of Agreement (MoA) signing
- Data security and privacy concerns with current spreadsheet solutions

These pain points aren't unique to PUP—they're shared across all 199 DataCamp partner organizations globally, creating a significant inefficiency in program administration.

> What if there was a purpose-built platform where DataCamp admins could efficiently manage scholarship applications—a centralized system designed and maintained by DataCamp specifically for program administrators?

---

## The Solution: DataCamp Admin Portal

<div align="center">
<img src="https://img.shields.io/badge/Proposed%20Solution-DataCamp%20Admin%20Portal-green" alt="Solution" width="350">
</div>

Our proposed Database Management System would transform how scholarship programs are administered by creating a unified, secure platform with:

### Key Features:

#### Application Management System
- Customizable application forms with DataCamp branding
- Multi-stage application workflow management
- Built-in screening mechanisms and eligibility filters
- Automated application status tracking

#### Scholar Database
- Comprehensive demographic data collection and visualization
- Privacy-compliant data storage with role-based access controls
- Custom tagging and segmentation capabilities
- Integration with DataCamp learning progress metrics

#### Communication Center
- Templated email communications for each application stage
- Automated notifications for acceptance, waitlisting, and requirements
- Bulk and individual messaging capabilities
- Communication history tracking

#### Document Management
- Digital MoA signing and storage
- Secure document repository for program requirements
- Certificate generation and distribution

#### Analytics Dashboard
- Program performance metrics
- Completion rates and engagement statistics
- Demographic reports and diversity tracking
- Custom reporting options

### Benefits:
- **Efficiency & Scale:** Reduce administrative time by 70%, allowing organizations to focus on scholar support rather than paperwork.
- **Data Security & Compliance:** Enterprise-grade security protocols protect sensitive applicant data, ensuring GDPR and local data privacy compliance.
- **Program Insights:** Rich analytics enable organizations to understand applicant demographics, program effectiveness, and areas for improvement.
- **Consistent Experience:** Standardized processes create a professional application experience reflecting DataCamp's quality.
- **Global Community:** A unified platform connects program administrators across 199 organizations, facilitating knowledge sharing and best practices.

---

## Conclusion

The DataCamp Admin Portal represents an opportunity to solve a critical pain point faced by all 199 partner organizations while significantly enhancing the impact of the DataCamp Donates program. By investing in this infrastructure, DataCamp can demonstrate its commitment to partners, improve program effectiveness, and ultimately extend its educational reach to more deserving students worldwide.

This isn't just an administrative tool—it's a catalyst for expanding data literacy in underserved communities and educational institutions globally.

---

## Developer Setup Guide

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed (includes Docker and Docker Compose)
- [Git](https://git-scm.com/downloads) for cloning the repository
- (Optional) [pgAdmin](https://www.pgadmin.org/download/) for database GUI

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/JpCurada/datacamp-scholarship-dbms.git
   cd datacamp-scholarship-dbms
   ```

2. **Set up environment files**
   - You will need the `env/db` and `env/web` files with database credentials
   - These files will be shared separately in the group chat to maintain security
   - Place them in the `env/` directory of the project

3. **First-time build and setup**
   ```bash
   # Build and start all services
   docker-compose -f docker-compose-dev.yml up --build
   ```

4. **Run database migrations**
   ```bash
   # In a new terminal
   docker-compose -f docker-compose-dev.yml exec web python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   docker-compose -f docker-compose-dev.yml exec web python manage.py createsuperuser
   ```

### Running the Project (After Initial Setup)

#### Option 1: Run all services together
```bash
docker-compose -f docker-compose-dev.yml up
```

#### Option 2: Run services separately (recommended for development)
```bash
# Start the database first
docker-compose -f docker-compose-dev.yml up db

# Wait ~10 seconds for the database to initialize
# Then in a new terminal, start the web service
docker-compose -f docker-compose-dev.yml up web
```

#### Run in detached mode (background)
```bash
docker-compose -f docker-compose-dev.yml up -d
```

### Stopping the Project
```bash
# If running in the foreground, use Ctrl+C
# If running in detached mode:
docker-compose -f docker-compose-dev.yml down
```

### Connecting to the Database with pgAdmin

1. **Open pgAdmin** (install if not already installed)
2. **Add a new server**:
   - Right-click on "Servers" and select "Create" → "Server..."
   - General tab:
     - Name: `Docker PostgreSQL` (or any name you prefer)
   - Connection tab:
     - Host name/address: `localhost`
     - Port: `5433` (the port mapped in docker-compose-dev.yml)
     - Maintenance database: `postgres`
     - Username: `postgres` (or as specified in your env/db file)
     - Password: (the password from your env/db file)
   - Click "Save"

3. **Navigate to your database**:
   - Expand the server you just created
   - Expand "Databases"
   - You should see the `datacamp-db` database (or whatever name is set in your env/db file)

### Common Commands

```bash
# View running containers
docker ps

# View logs
docker-compose -f docker-compose-dev.yml logs

# Follow logs for a specific service
docker-compose -f docker-compose-dev.yml logs -f web

# Restart a specific service
docker-compose -f docker-compose-dev.yml restart web

# Run Django management commands
docker-compose -f docker-compose-dev.yml exec web python manage.py [command]
```

### Troubleshooting

- **Port conflicts**: If you get a "port is already allocated" error, change the port mapping in `docker-compose-dev.yml`
- **Database connection issues**: Ensure the database service is fully started before launching the web service
- **Missing environment files**: Check that you've received and properly placed the `env/db` and `env/web` files


## Task & Development Workflow

We use **task tracking** to manage development work and assignments. Follow these steps when working on tasks:

#### 2. Create a Branch

- Use the [branching convention](#branching--git-workflow).
- Start coding!

#### 3. Submit a Pull Request (PR)

- Reference the task in the PR description (e.g., `Completes Task #123`).
- Mark the task as "In Review" on your tracking system.

#### 4. Code Review & Merge

- Once approved, the PR gets merged into `develop`.
- The task is marked as "Completed."

---

## Branching & Git Workflow

### Branch Naming Convention

| Branch Type     | Naming Convention               | Example                 |
| --------------- | ------------------------------- | ----------------------- |
| **Main**        | `main`                          | `main`                  |
| **Development** | `dev`                           | `dev`                   |
| **Feature**     | `feature/TASK-ID-feature-name`  | `feature/123-add-auth`  |
| **Bugfix**      | `bugfix/TASK-ID-bug-name`       | `bugfix/234-fix-footer` |
| **Hotfix**      | `hotfix/TASK-ID-critical-fix`   | `hotfix/345-fix-login`  |

#### 1. Switch to develop branch

```bash
git checkout dev
git pull origin dev
```

#### 2. Create a feature branch linked to a task

```bash
git checkout -b feature/TASK-ID-feature-name
```

Example:

```bash
git checkout -b feature/123-add-login-auth
```

#### 3. Make your changes in the code

#### 4. Once you're done with your changes, commit

```bash
git add .
git commit -m "feat(auth): add login authentication (Completes Task #123)"
```

#### 5. Push to remote branch

```bash
git push origin feature/TASK-ID-feature-name
```

#### 6. Create a pull request (PR)

- Go to your repository
- Open a new PR from feature/TASK-ID-feature-name → develop
- Use the [PR Template](#pull-request-description-format) below

---

## Commit Message Guidelines

### Commit Message Format

```
<type>(<scope>): <description>
```

### Allowed Commit Types

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

| Type         | Description                                           |
| ------------ | ----------------------------------------------------- |
| **feat**     | A new feature                                         |
| **fix**      | A bug fix                                             |
| **docs**     | Documentation changes                                 |
| **style**    | Code style changes (formatting, etc.)                |
| **refactor** | Code changes that neither fix a bug nor add a feature |
| **perf**     | Performance improvements                              |
| **test**     | Adding or modifying tests                             |
| **chore**    | Maintenance and other minor tasks                     |

#### Examples

```bash
git commit -m "feat(auth): add user authentication with JWT"
git commit -m "fix(navbar): resolve mobile responsiveness issue"
git commit -m "docs(readme): update contribution guide"
```

---

## 📋 Pull Request Guidelines

### PR Title Format:

```
<type>(<scope>): <short description>
```

Example

```
feat(auth): add user login functionality
fix(navbar): resolve mobile responsiveness issue
```

### PR Description Template

```
✨ What's New?
- [x] Briefly explain what was added

📷 Screenshots of application (IMPORTANT)
_Add relevant screenshots/gifs_

🔗 Related Tasks
Completes Task #TASK_NUMBER

✅ Checklist (from task)
- [ ] Code follows project conventions
- [ ] Linted & formatted
- [ ] Tested locally
```
