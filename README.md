PromptStore – Sell & Buy Prompts/Apps/Templates

A full-stack production-ready application built using Django REST Framework + React, featuring:

✔ JWT authentication
✔ Secure CRUD operations
✔ Role-based restrictions (owner-only edits/deletes)
✔ Marketplace browsing
✔ Stripe-based checkout flow
✔ Deployment-ready setup (Render + Vercel)

🚀 Demo Links

🔹 Frontend Live → <your-vercel-link>
🔹 Backend API → <your-render-backend-link>

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

Netlify/Vercel deployment

Backend

Django

Django REST Framework

JWT (SimpleJWT)

Stripe Python SDK

PostgreSQL (recommended)

Deployment

Render (Backend + DB)

Vercel / Netlify (Frontend)

📁 Project Structure
promptstore/
│── backend/
│   ├── backend/           # Django project root
│   ├── prompts/           # Main app (CRUD + Payments)
│   ├── venv/              # Virtual environment (ignored)
│   └── manage.py
│
└── frontend/
    ├── src/
    │   ├── pages/         # Login, Register, PromptList, PromptForm
    │   ├── services/      # Axios API wrapper
    │   └── App.jsx
    └── vite.config.js

🚀 Local Development Setup
📌 Backend Setup
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

SECRET_KEY=<your-secret-key>
DATABASE_URL=<postgres-url-or-empty-for-sqlite>
STRIPE_SECRET_KEY=<stripe-key>
FRONTEND_URL=http://localhost:5173
DEBUG=True

🌐 Frontend Setup
cd frontend
npm install
npm run dev


👉 App runs at http://localhost:5173

🧠 Frontend Environment Variables

Create .env in frontend/

VITE_API_URL=http://localhost:8000

🛠 Build Commands
Frontend Production Build:
npm run build

Collect static files for backend:
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


Deploy

🔑 API Endpoints
Auth
Method	Endpoint	Description
POST	/api/auth/register/	Register user
POST	/api/auth/token/	Login & get tokens
POST	/api/auth/token/refresh/	Refresh access
Prompts
Method	Endpoint	Description
GET	/api/prompts/	List all prompts
POST	/api/prompts/	Create new prompt
GET	/api/prompts/{id}/	Fetch prompt
PUT/PATCH	/api/prompts/{id}/	Edit only if owner
DELETE	/api/prompts/{id}/	Delete only if owner
GET	/api/prompts/my_prompts/	Get logged-in user's prompts
Payments
Method	Endpoint	Description
POST	/api/payments/checkout/	Create payment session

Request:

{
  "prompt_id": 1
}


Response:

{
  "checkout_url": "https://checkout.stripe.com/..."
}

🧪 Testing Suggestions
For auth:

Test login → store JWT → GET protected resource

For CRUD:

Create prompt

GET prompts

PATCH prompt as owner

DELETE prompt as owner

DELETE prompt as non-owner (should fail)

For payments:

Hit /api/payments/checkout/

Validate redirect URL works

🧩 Future Improvements

💡 Add categories, tags, and search filters
💡 Add review & rating system
💡 Add webhook to store successful orders
💡 Allow authors to upload sample files
💡 Dashboard for seller sales analytics

📜 License

This project is open-sourced under the MIT License.
