# Lift Ledger Workout Tracker

A modern, serverless full-stack web application for tracking workouts, personal bests, workout plans, and user metrics.

## 🧰 Built with:
- **Frontend:** Next.js (App Router)
- **Backend:** Next.js API routes for simple logic, AWS Lambda via API Gateway for complex operations
- **Database:** DynamoDB
- **Caching:** Upstach Redis
- **File Storage:** S3
- **Authentication:** Auth.js with JWT
- **Hosting:** Vercel (frontend + API) + AWS Lambda (heavy backend)
- **CI/CD:** GitHub Actions
- **Testing:** Jest
- **UI/UX:** TailwindCSS + Daisy UI

## 🚀 Features
- User authentication (Sign up / Sign in with email)
- Create and track workouts
- Save reusable exercises
- Track personal history for each exercise
- Responsive and mobile-friendly design

## 🗺️ API Routes
| Method | Endpoint | Description
| --- | --- | --- |
| `POST` | `/api/auth/signup`            | Create a new user account                |
| `GET`  | `/api/workouts`               | Fetch all workout for the signed-in user |
| `POST` | `/api/workouts`               | Create a new workout                     |
| `GET`  | `/api/exercises`              | Fetch an exercise                        |
| `POST` | `/api/exercises`              | Create a new exercise                    |
| `GET`  | `/api/exercises/search-names` | Searches exercises during search         |
| `PUT`  | `/api/user/[id]`              | Edit the user profile data               |
| `GET`  | `/api/userMetrics`            | Fetch a user's metrics                   |

## 🔒 Authentication
- Sessions are managed using **Auth JWT tokens.**
- Protected API routes require authentication to access user data.

## 📦 Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/josh-peters-99/liftledger.git
cd kratos-ts
```
2. Install dependencies
```bash
npm install
```
3. Set up environment variables
  - Create a `.env.local` file in the root directory with the following:
```bash
NEXTAUTH_SECRET=your_nextauth_secret
NEXTAUTH_URL=http://localhost:3000
```
4. Run the app locally
```bash
npm run dev
```
5. Visit [http://localhost:3000](http://localhost:3000) to view the app.

## 🧪 Testing
🚧 Under Construction

## 📚 Future Improvements
- Advanced workout analytics and graphs
- Save reusable workout templates
- Plan structured weekly workouts
- Track total workouts (weekly, mongthly, yearly, all-time)
- Social fetaures
- Workout history calendar view
- Notifications/reminders for planned workouts

## ☁️ Live Application
🚧 Under Construction

## 📄 License
This project is licensed under the MIT license.