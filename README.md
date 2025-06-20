# Lift Ledger Workout Tracker

A modern, serverless full-stack web application for tracking workouts, personal bests, workout plans, and user metrics.

## 🧱 STACK DETAILS
### 🌐 Web
- **Frontend:** React
- **Styling:** TailwindCSS + Daisy UI
- **Testing:**
  - **Unit:** Jest + React Testing Library
  - **E2E:** Cypress
- **Auth:** Auth.js (email provider)
- **Deployment:** AWS Amplify or Vercel
### 📱 iOS Frontend
- **Language:** Swift 5+
- **UI Framework:** SwiftUI
- **Networking:** URLSession or Alamofire
- **Data Models:** Codable + Async/Await
- **Auth:** Token-based (store in Keychain)
- **Testing:**
  - **Unit:** XCTest
  - **UI:** XCUITest
- **CI/CD:** GitHub Actions + `xcodebuild`
### 🔙 Backend
- **Compute:** AWS Lambda (Python)
- **API Layer:** AWS API Gateway (REST)
- **Data:** DynamoDB
- **Storage:** S3 (for profile pics or workout images/videos)
- **Auth:** JWT verification (Amazon Cognito optional)
- **Framework:** AWS Lambda Powertools = FastAPI or pure AWS Lambda handlers

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

## 🚦 CI/CD
| Workflow | Trigger | Descriptions
| --- | --- | --- |
| `web.yml` | `push` to `web/` | Builds, tests, and deploys web app |
| `ios.yml` | `push` to `ios/` | Builds and runs tests in Xcode     |
| `backend.yml` | `push` to `backend/` | Runs tests and deploys to Lambda |

## 📦 Setup Instructions
### Web
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
### iOS
Open `LiftledgerApp.xcodeproj` in Xcode and run the app using the iOS Simulator.

## 🧪 Testing
### pytest
1. Be inside the `backend/` directory
2. Start the Python virtual environment
```bash
source venv/bin/activate
```
3. Run the pytests
```bash
pytest
```
4. End the Python virtual environment
```bash
deactivate
```

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