PromptStore – Sell & Buy Prompts/Apps/Templates

A full-stack production-ready application built using Django REST Framework + React, featuring:

✔ JWT authentication
✔ Secure CRUD operations
✔ Role-based restrictions (owner-only edits/deletes)
✔ Marketplace browsing
✔ Stripe-based checkout flow
✔ Deployment-ready setup (Render + Vercel)

🚀 Demo Links

🔹 Frontend Live → https://promptstore-five.vercel.app/
🔹 Backend API → https://promptstore.onrender.com/admin/login/?next=/admin/

🔥 Features
👤 Authentication & Authorization

Register/Login using JWT

Automatic token storage and token refresh

Access-protected endpoints

Logout support

🛒 Prompt Marketplace

Browse all listed prompts

Search/filter ready

View detailed description and price

Secure purchase flow

✍️ CRUD for Authors

Create, update and delete your own prompts

Publish/unpublish feature

Auto ownership mapping on creation

💳 Payment Flow

Stripe checkout session per item

Redirect automatically to payment

Post-payment success page

Ready for webhooks integration

🧰 Tech Stack
Frontend

React (Vite)

React Router

Axios

Vercel deployment

Backend

Django

Django REST Framework

JWT (SimpleJWT)

Stripe Python SDK

PostgreSQL (recommended)

Deployment

Render (Backend + DB)

Vercel / Netlify (Frontend)



🚀 Local Development Setup
📌 Backend Setup
bash
Copy code
cd backend
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
👉 API now runs on http://localhost:8000

🔐 Environment Variables (Backend)
Create .env in backend/

ini
Copy code
SECRET_KEY=<your-secret-key>
DATABASE_URL=<postgres-url-or-empty-for-sqlite>
STRIPE_SECRET_KEY=<stripe-key>
FRONTEND_URL=http://localhost:5173
DEBUG=True
🌐 Frontend Setup
bash
Copy code
cd frontend
npm install
npm run dev
👉 App runs at http://localhost:5173

🧠 Frontend Environment Variables
Create .env in frontend/

ini
Copy code
VITE_API_URL=http://localhost:8000
🛠 Build Commands
Frontend Production Build:
bash
Copy code
npm run build
Collect static files for backend:
bash
Copy code
python manage.py collectstatic

🌍 Deployment Guide
🚀 Backend Deployment – Render

Push backend to GitHub

Create a Render Web Service

Set:

Start Command = gunicorn backend.wsgi
Build Command = pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput


Add environment variables

⚠️ Remember to attach PostgreSQL service on Render

🚀 Frontend Deployment – Vercel

Import GitHub repo

Set root folder to frontend

Set environment:

VITE_API_URL = https://your-backend-url.com


