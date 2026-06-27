# Social Media Platform

A full-stack social media application built with **Django** and **JavaScript**, allowing users to connect, share posts, and engage with content in real-time.

## 🚀 Features
* **User Authentication**: Secure signup, login, and logout functionality.
* **User Profiles**: Personalized profiles showcasing user details and their posts.
* **Post Management**: Full capability to create, view, edit, and delete posts.
* **Engagement System**: Interactive **Like** button and **Comments** section for every post.
* **Social Graph**: Follow/Unfollow mechanism to build a custom user network.
* **Live Search**: Dynamic, real-time search bar powered by JavaScript to find users instantly.

## 🛠️ Tech Stack
* **Backend**: Django (Python)
* **Frontend**: HTML5, CSS3, JavaScript
* **Database**: SQLite (Default development database)

## 📂 Project Structure
```text
SOCIALMEDIAPLATFORM/
├── accounts/       # Handles registration, login, and user profile logic
├── posts/          # Handles posts, likes, comments, and followers
├── media/          # Stores uploaded profile pictures and post images
└── socialmedia/    # Core configuration, settings, and main routing
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dikshasingh9259-create/codealpha_tasks/tree/main/codealpha_socialmediaplatform
   cd socialmediaplatform
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Environment**
   * **Windows**: `venv\Scripts\activate`
   * **Mac/Linux**: `source venv/bin/activate`

4. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0`.
