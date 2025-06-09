# File Structure

```bash
workout-tracker/
├── backend/                 # AWS Lambda (Python)
│   ├── handlers/
│   ├── tests/
│   └── requirements.txt
├── web/                     # Next.js (TypeScript)
│   ├── app/
│   ├── components/
│   ├── tests/
│   └── package.json
├── ios/                     # Swift + SwiftUI
│   ├── WorkoutApp/
│   ├── WorkoutAppTests/
│   └── .xcodeproj
├── .github/workflows/       # GitHub Actions for CI/CD
│   ├── web.yml
│   ├── backend.yml
│   └── ios.yml
├── README.md                # Top-level project overview
└── docs/                    # Architecture diagrams, API docs, etc.
```