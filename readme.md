# Study Strategy API Documentation

This API allows users to allocate study hours based on subject difficulty and suggest study techniques based on OCEAN personality traits.

## Base URL

The API runs locally on:
```
http://127.0.0.1:5000/
```

---

## Endpoints Overview

| HTTP Method | Endpoint                  | Description |
| ----------- | ------------------------- | ----------- |
| POST        | `/allocate_hours`          | Allocates study hours to subjects based on their difficulty and total available study hours. |
| POST        | `/calculate_ocean_scores`  | Calculates the OCEAN personality matrix from quiz responses. |
| POST        | `/suggest_techniques`      | Suggests study techniques based on OCEAN personality scores. |

---

## 1. **POST** `/allocate_hours`

### Description:
This endpoint takes a list of subjects with their difficulty levels and the total available study hours, then allocates hours to each subject proportionally based on difficulty.

### Request Body:
- **Content-Type:** `application/json`
- **Required Fields:**
  - `total_hours` (integer): The total number of hours available for study.
  - `subjects` (array of objects): A list of subjects, each with the following properties:
    - `name` (string): The name of the subject.
    - `difficulty` (integer): The difficulty rating of the subject (1-10).

### Example Request:
```json
{
  "total_hours": 40,
  "subjects": [
    {"name": "Math", "difficulty": 5},
    {"name": "Science", "difficulty": 3},
    {"name": "History", "difficulty": 7}
  ]
}
```

### Response:
- **Success Status:** `200 OK`
- **Response Format:** `application/json`
- **Response Fields:**
  - `message`: Success message.
  - `total_subjects`: Number of subjects provided.
  - `total_hours`: The total hours provided.
  - `subjects`: An array of subjects with the allocated study hours.

### Example Response:
```json
{
  "message": "Study hours allocated successfully",
  "total_subjects": 3,
  "total_hours": 40,
  "subjects": [
    {"name": "Math", "difficulty": 5, "allocated_hours": 15},
    {"name": "Science", "difficulty": 3, "allocated_hours": 9},
    {"name": "History", "difficulty": 7, "allocated_hours": 16}
  ]
}
```

### Errors:
- **Invalid Input:** Returns `400 Bad Request` if `total_hours` is not a positive integer or if subjects are not provided.
- **Unsupported Media Type:** Returns `415 Unsupported Media Type` if the content type is not `application/json`.

---

## 2. **POST** `/calculate_ocean_scores`

### Description:
This endpoint calculates OCEAN (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) personality scores based on quiz responses.

### Request Body:
- **Content-Type:** `application/json`
- **Required Fields:**
  - `quiz_responses` (array of objects): A list of quiz responses. Each response has:
    - `trait` (string): The trait name (one of: "openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism").
    - `score` (integer): The score for the trait (1-100).

### Example Request:
```json
{
  "quiz_responses": [
    {"trait": "openness", "score": 80},
    {"trait": "conscientiousness", "score": 75},
    {"trait": "extraversion", "score": 60},
    {"trait": "agreeableness", "score": 85},
    {"trait": "neuroticism", "score": 40}
  ]
}
```

### Response:
- **Success Status:** `200 OK`
- **Response Format:** `application/json`
- **Response Fields:**
  - `message`: Success message.
  - `ocean_scores`: An object with the calculated average scores for each trait.

### Example Response:
```json
{
  "message": "OCEAN personality scores calculated",
  "ocean_scores": {
    "openness": 80,
    "conscientiousness": 75,
    "extraversion": 60,
    "agreeableness": 85,
    "neuroticism": 40
  }
}
```

### Errors:
- **Invalid Input:** Returns `400 Bad Request` if quiz responses are not provided or invalid.
- **Unsupported Media Type:** Returns `415 Unsupported Media Type` if the content type is not `application/json`.

---

## 3. **POST** `/suggest_techniques`

### Description:
This endpoint suggests study techniques based on the user's OCEAN personality scores.

### Request Body:
- **Content-Type:** `application/json`
- **Required Fields:**
  - `ocean_scores` (object): The calculated OCEAN personality scores. Each trait must be included:
    - `openness` (integer): Openness score (1-100).
    - `conscientiousness` (integer): Conscientiousness score (1-100).
    - `extraversion` (integer): Extraversion score (1-100).
    - `agreeableness` (integer): Agreeableness score (1-100).
    - `neuroticism` (integer): Neuroticism score (1-100).

### Example Request:
```json
{
  "ocean_scores": {
    "openness": 80,
    "conscientiousness": 75,
    "extraversion": 60,
    "agreeableness": 85,
    "neuroticism": 40
  }
}
```

### Response:
- **Success Status:** `200 OK`
- **Response Format:** `application/json`
- **Response Fields:**
  - `message`: Success message.
  - `techniques`: A list of suggested study techniques based on the OCEAN scores.

### Example Response:
```json
{
  "message": "Study techniques suggested",
  "techniques": [
    "Mind mapping, creative summarization",
    "Pomodoro method, strict scheduling",
    "Solitary study, self-quizzing",
    "Collaborative projects, peer learning",
    "Frequent breaks, stress-relief exercises"
  ]
}
```

### Errors:
- **Invalid Input:** Returns `400 Bad Request` if OCEAN scores are incomplete or invalid.
- **Unsupported Media Type:** Returns `415 Unsupported Media Type` if the content type is not `application/json`.

---

## How to Run the API

1. **Install Dependencies**:
   Ensure you have Flask installed by running:
   ```bash
   pip install Flask
   ```

2. **Run the App**:
   Start the Flask server by running the app:
   ```bash
   python app.py
   ```

   The API will run on `http://127.0.0.1:5000/`.

---

Feel free to share this documentation with your front-end developer to help them understand how to interact with the API effectively!