# Scoutly — Project Planning Document

---

## 1. Why am I building Scoutly?

To improve a business function in need of efficiency gains. Also to learn about basic web development.

## 2. Who is the Project for?

Sales teams and their potential clients.

## 3. What is gonna make it valuable?

To help sales teams find higher quality leads by matching individuals with prospects based off business, local, and personal commonalities. The same can be said for potential clients on the platform who need specific services with specific personalities involved. The overall time, effort, and effectiveness of matching services with clients will be improved. Increase the ease leaning on similarity-attraction effect factor.

---

## 4. Functional and Non-Functional Sales User Needs

- Input lead files and return a snapshot of best matches on a dashboard
    - Should be able to filter best matches based on personal, business, and/or local needs
    - Should be able to adjust display of matches as list ranking
    - Dashboard should display most common traits between leads and Sales user
        - Should also display most common traits of leads not found with Sales user
- When lead files are input from another Sales user
    - If commonalities metric is over a certain threshold, all respective Sales users shall be notified via email or text.
        - This can be adjusted to only the best fit (or range of Sales users) Sales user is notified
- Sales user should be able to access a newly created lead profile and identify best matched traits
    - Should also be given a rating for likelihood a Sales user's services are needed
- Leads given from an enterprise should be able to be stored along with their embeddings as well as updated if they are requested again.
- The data of leads should be updated in a specified time range.
- Secure Login and Logout functionality

---

## 5. Data Models

### Sales User
| Field            | Type     | Notes                                      |
|------------------|----------|--------------------------------------------|
| Name             | String   |      (MVP 1)                                 |
| Picture          | Image    | Profile photo (MVP 1?)                        |
| Business         | String   | Company name  (MVP 1)                        |
| Role             | String   | Job title     (MVP 1)                        |
| Age              | Integer  |                                            |
| Work Location    | String   | City / Region                              |
| Industry         | String   |                                            |
| Product          | String   | What they sell / offer                     |
| Years Experience | Integer  |                                            |
| Hobbies          | List     |                                            |
| Teams            | List     | Sports teams, clubs, orgs                  |
| Other Facts      | Text     | Free-form notes                            |

### Client Rep (Lead)
| Field                          | Type     | Notes                                                        |
|--------------------------------|----------|--------------------------------------------------------------|
| Name                           | String   | (MVP1)                                                             |
| Picture(s)                     | Image(s) | (MVP1)                                                             |
| Business                       | String   |  (MVP1)                                                            |
| Role                           | String   |        (MVP1)                                                      |
| Age                            | Integer  |                                                              |
| Work Location                  | String   |                                                              |
| Industry                       | String   |                                                              |
| Product                        | String   |                                                              |
| Years Experience               | Integer  |                                                              |
| Hobbies                        | List     |                                                              |
| Teams                          | List     |                                                              |
| Other Facts                    | Text     |                                                              |
| Last_Update_Info               | DateTime |                                                              |
| Lead_Status                    | Enum     | New, Contacted, Qualified, Converted, Lost                   |
| Last_Reach_Out                 | DateTime |                                                              |
| Likelihood_for_business_rating | Integer  | 1–5 rating from rep who last contacted + online signal data  |
| Similarity_Score               | Float    | Computed from embedding comparison                           |
| Key_Similarities_List          | List     | Ranked by importance to the lead                             |
| Profile_Update_Interval        | String   | How often to re-scrape/refresh (e.g., weekly, monthly)       |

### Enterprise (Organization)
| Field       | Type     | Notes                                           |
|-------------|----------|-------------------------------------------------|
| Name        | String   | Company or team name                            |
| Admin Users | List     | Sales Users with admin privileges               |
| Members     | List     | All Sales Users under this org                  |
| Lead Pool   | List     | All Client Reps uploaded by this enterprise     |
| Created_At  | DateTime |                                                 |

> **Why Enterprise?** Your requirements mention "leads given from an enterprise" — this model lets you group Sales Users and their shared Lead Pools under one roof, which sets you up for multi-tenancy later.

---

## 6. Data Relationship Map

```
Enterprise (1) ──────< (Many) Sales User
    │
    └───────────────< (Many) Lead Upload Batch

Sales User (1) ──────< (Many) Lead Match
                                  │
Client Rep (1) ──────< (Many) Lead Match

Lead Upload Batch (1) ──< (Many) Client Rep
```

**Key Relationships:**
- An Enterprise has many Sales Users (members).
- A Sales User belongs to one Enterprise.
- A Sales User can have many Lead Matches (each linking them to a Client Rep with a Similarity Score).
- A Client Rep can be matched to many Sales Users (many-to-many through Lead Match).
- A Lead Upload Batch groups Client Reps that were uploaded together, tied to an Enterprise.
- Lead Match is the join table — it holds the Similarity_Score, Key_Similarities_List, and the relationship between a specific Sales User and a specific Client Rep.

> **Why a join table (Lead Match)?** The same lead could be a great fit for one Sales User and a poor fit for another. The match data (score, similarities) is specific to the *pair*, not to either person alone.

---

## 7. MVP — Absolute Minimum

- [ ] Sales User can create an account and log in securely
- [ ] Sales User can fill out their own profile (name, industry, hobbies, location, etc.)
- [ ] Sales User can upload a lead file (CSV) containing basic Client Rep info
- [ ] System processes the file: enriches data via public scraping, generates embeddings, computes Similarity Scores
- [ ] Dashboard displays ranked list of best-matched leads with Key Similarities highlighted
- [ ] Sales User can filter matches by personal, business, and/or local traits
- [ ] Sales User can click into a lead profile to see full details and match reasoning
- [ ] Lead data and embeddings are stored and retrievable

**What is NOT in MVP:**
- No notifications (email/text)
- No multi-user matching across Sales Users
- No auto-refresh of lead data on intervals
- No statistics/charts beyond the ranked list
- No Lead Map
- No enterprise admin settings

> **Why strip it this far?** You want to validate that the core loop works — upload leads, get ranked matches, see why. Everything else is enhancement. If this core isn't valuable, none of the extras matter.

---

## 8. Wireframes — UX-First Thinking

### Screen 1: Login / Sign Up
- Simple email + password form
- "Create Account" flow that leads into profile setup

### Screen 2: Profile Setup / Edit
- Form with all Sales User fields
- This is critical to matching quality — the more a Sales User fills out, the better their results

### Screen 3: Dashboard (Home)
- Upload area (drag-and-drop CSV or file picker)
- After processing: ranked list of leads with Similarity Score badge, top 3 Key Similarities shown inline
- Filter bar: checkboxes or toggles for Personal / Business / Local
- Sort toggle: by score, by name, by status

### Screen 4: Lead Profile Detail
- Full Client Rep info
- Similarity Score prominently displayed
- Key Similarities listed and ranked
- Likelihood for Business rating (if available)
- Lead Status selector (New → Contacted → Qualified → etc.)
- Last Reach Out date (editable)

> **UX priority:** The dashboard-to-lead-detail flow is the main loop. Keep it to two clicks max: upload → see ranked list → click a lead → see why they're a match. Don't over-design screens that aren't in the MVP.

---

## 9. The Future of the Project

- Notifications of lead matches and/or likelihood-for-business scores (email/text)
- Statistics-based data presentation (charts, trends over time)
- Lead Map (geographic visualization of leads)
- Settings for Scoutly User profiles (preferences, notification thresholds)
- More robust UI to allow for widgets and customization of Overview Screen
- Cross-Sales-User matching (when a lead uploaded by one user is a better fit for another)
- Auto-refresh of lead data on configurable intervals
- Enterprise admin panel

> **Timeline expectation:** MVP will take months. This is healthy — you're learning web dev while building a real product. Don't rush to features before the core is solid.

---

## 10. Project Presentation

- WebApp — users access through the browser
- A desktop app may be provided sometime in the future
- Mobile-responsive design so Sales Users can check matches on their phones

---

## 11. Tech Stack

| Layer              | Choice                  | Why                                                                                      |
|--------------------|-------------------------|------------------------------------------------------------------------------------------|
| **Backend**        | Python FastAPI          | Async-first (critical for scraping + LLM calls), built-in Pydantic validation for your data models, auto-generated API docs for testing |
| **Frontend**       | React.js               | Component-based (dashboard, lead cards, filters map well to components), huge ecosystem for charts (Recharts) and tables |
| **Database**       | PostgreSQL + pgvector + (Redis vs Mongo DB?) | Relational structure fits your data models cleanly; pgvector extension stores and queries embeddings without needing a separate vector DB; NEED TO DECIDE ON STORING UNSTRUCTURED DATA FROM SCRAPING| 
| **Auth**           | JWT tokens (via FastAPI) | Simple, stateless, well-documented for learning                                         |
| **Scraping**       | BeautifulSoup + Playwright | BS4 for simple HTML pages, Playwright for JS-rendered sites; start simple, scale up as needed |
| **AI / Matching**  | distilbert-base-uncased (Similarity Scoring)/Claude API (Data Enrichment)  | Claude enriches scraped data into structured profiles and powers the "why" behind each match while dsitlbert calculates similarity scoring with low cost and overhead |
| **Embeddings**     | sentence-transformers   | Free, local, fast; generates vectors for semantic similarity scoring                     |
| **Task Queue**     | Celery + Redis          | Scraping and enrichment are slow — offload to background workers so the UI stays responsive |
| **Deployment**     | Docker + Railway or Render | Containerized for consistency; Railway/Render are simple to deploy for a solo dev without DevOps overhead |

> **Decision rationale:** Every choice optimizes for "can a college student learn this, deploy this, and maintain this solo?" Flask was considered but FastAPI teaches better modern patterns (async, type hints) and handles the concurrent scraping workload your app demands. PostgreSQL over a NoSQL option because your data is clearly relational (Sales Users ↔ Leads ↔ Matches). Docker because it makes deployment reproducible — you set it up once and don't fight environment issues.

---

## 12. The Development Process

### Phase 1: Bare Bones Setup
- **Folder Structure:**
```
scoutly/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── models/              # Pydantic + SQLAlchemy models
│   │   ├── routes/              # API endpoint files
│   │   ├── services/            # Business logic (scraping, matching, enrichment)
│   │   ├── workers/             # Celery task definitions
│   │   └── config.py            # Environment config
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/          # Reusable UI pieces (LeadCard, FilterBar, etc.)
│   │   ├── pages/               # Dashboard, LeadDetail, Login, Profile
│   │   ├── services/            # API call functions
│   │   └── App.jsx
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml           # Postgres + Redis + Backend + Frontend
└── README.md
```
- **Naming Conventions:** snake_case for Python, camelCase for JS/React, PascalCase for React components
- **Dev Environment:** Docker Compose for local dev (Postgres, Redis, backend, frontend all in one command)
- **Version Control:** Git + GitHub. Commit early, commit often. Use branches for features.

### Phase 2: Database & Data Models
- Define SQLAlchemy models for Sales User, Client Rep, Enterprise, Lead Match, Lead Upload Batch
- Write and run Alembic migrations
- Seed with test data (fake Sales Users and Leads) to develop against
- **Test:** Verify models create/read/update/delete correctly via Python shell or simple scripts

### Phase 3: Backend Routes (API Endpoints)
- `POST /auth/register` — create account
- `POST /auth/login` — return JWT
- `GET /users/me` — get current user profile
- `PUT /users/me` — update profile
- `POST /leads/upload` — accept CSV, kick off processing
- `GET /leads` — list leads for current user (with filters + sort)
- `GET /leads/{id}` — single lead detail with match data
- `PUT /leads/{id}` — update lead status, reach out date
- **Test:** Use FastAPI's auto-generated `/docs` Swagger UI to test every endpoint manually. Write basic pytest tests for critical paths.

### Phase 4: Frontend
- Set up React with Vite
- Build pages in order of the user flow: Login → Profile Setup → Dashboard → Lead Detail
- Connect to backend API using fetch or axios
- Keep styling minimal at first (basic CSS or Tailwind) — function over aesthetics for MVP

### Phase 5: Integration & Matching Pipeline
- Wire up the full flow: CSV upload → scraping workers → LLM enrichment → embedding generation → similarity scoring → results to dashboard
- This is the hardest phase — take it one piece at a time
- **Test:** Upload a real CSV of 5–10 leads and verify the full pipeline end-to-end

### Phase 6: Deployment
- Dockerize everything (backend, frontend, Postgres, Redis)
- Deploy to Railway or Render
- Set environment variables (API keys, DB connection strings)
- Verify it works in production with a small test batch

### Phase 7: CI/CD
- GitHub Actions for: linting, running tests on push, auto-deploy on merge to main
- Keep it simple — don't over-engineer the pipeline before the app is stable

> **Testing philosophy:** Test at every step, but don't aim for 100% coverage on an MVP. Focus tests on the matching logic (your core value) and auth (security). UI testing can wait.

---

## Appendix: Development Process Checklist Reference

This was the framework used to build this plan:

1. Start from your goal — define why, who, and what value
2. Write down user needs — features and guardrails, user-centric
3. Define data models — think about data and relationships, not databases
4. Nail an MVP — strip to absolute minimum
5. Wireframe for the most basic user — UX over UI, paper is cheap
6. Understand the future — plan for growth without over-engineering
7. Project presentation — how users interact dictates architecture
8. Tech stack — best tool for the project, not the other way around
9. Development process — structure, build, integrate, deploy, test at all steps
