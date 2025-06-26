# 🛠️ Support Ticket System (Fullstack)

A full-stack support ticket management system that allows users to create, view, update, and filter tickets with real-time stats.

---

## 🔧 Tech Stack

- **Backend:** FastAPI (Python), SQLite, SQLAlchemy, Pydantic
- **Frontend:** React + Vite (JavaScript), Axios
- **Styling:** Custom CSS (no Tailwind or Bootstrap)
- **Others:** CORS, modern component breakdown, RESTful principles

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd support-ticket-system
```

### 2. Start Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

📌 FastAPI Docs: http://localhost:8000/docs

### 3. Start Frontend

```bash
cd support-ticket-frontend
npm install
npm run dev
```

📌 React App: http://localhost:5173

---

## 🌟 Features

- Create new support tickets with title, description, and optional assignee
- View all tickets with filtering by status (All, Open, In Progress, Closed)
- Update status of tickets via dropdown or by ID
- Ticket summary with color-coded status boxes
- Beautiful, modern responsive UI using plain CSS
- Input validation and proper error handling with HTTPExceptions
- OpenAPI docs for backend testing

---

## 🤖 AI Usage

### Tools Used

- **ChatGPT** – primary assistant for backend and frontend design
- **GitHub Copilot** – minor autocomplete assistance

### Prompts Asked

- *"use enum for the status in schema classes"*
- *"create endpoints, use HTTPExceptions for proper errors, do proper validations and use Pydantic for response models"*
- *"make UI aesthetic and modern with card layout"*
- *"create a short README with tech stack and run instructions"*
- *"center the layout and show ticket by ID before updating"*

### Modifications to AI Output

- UI styling was manually refined (colors, sizing, spacing)
- React code was customized to eliminate unused code and structure pages clearly
- Backend routes were adjusted for filtering, validation, and database interaction

---

## 📝 Notes

- Tested on Python 3.10+ and Node.js 18+
- Database: `tickets.db` auto-generated on run
- All endpoints follow RESTful standards

---

## 📷 UI Preview

> Check `/view`, `/create`, `/update` for full UX walkthrough.
