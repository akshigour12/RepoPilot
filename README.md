# 🚀 RepoPilot

RepoPilot is a Flask-based GitHub Repository Management application that helps developers perform bulk operations on multiple GitHub repositories from a simple web interface.

Instead of visiting every repository individually, RepoPilot allows you to manage repositories with just a few clicks.

---

## ✨ Features

### Repository Management

- ✅ List all GitHub repositories
- ✅ View repository details
- ✅ Search repositories
- ✅ Multi-select repositories

### Bulk Operations

- 🔒 Change repository visibility (Public / Private)
- 📦 Archive repositories
- 📂 Unarchive repositories
- ✏️ Rename repositories
- 🏷️ Add repository topics
- 📄 Create README.md
- ⚖️ Add MIT LICENSE
- 🗑️ Delete repositories

### Dashboard

- Repository search
- Repository details page
- Bulk action result page
- Success / Failure status for every operation

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- GitHub REST API

---

## 📂 Project Structure

```
RepoPilot/
│
├── app.py
├── github_client.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── details.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── .env
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/RepoPilot.git
```

Go to the project folder

```bash
cd RepoPilot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project root.

```env
GITHUB_TOKEN=your_personal_access_token
GITHUB_OWNER=your_github_username
```

> Never commit your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📷 Application Screens

- Dashboard
- Repository Details
- Bulk Action Results

*(Screenshots can be added here.)*

---

## 🔐 GitHub Permissions

RepoPilot requires a GitHub Personal Access Token (Classic) with:

- repo
- delete_repo (optional, required for delete)

or an equivalent Fine-grained Token with repository administration permissions.

---

## 🚧 Future Enhancements

- GitHub OAuth Login
- Docker Support
- GitHub Actions Integration
- Repository Analytics Dashboard
- Bulk Collaborator Management
- Bulk Branch Protection
- Repository Templates
- Export Reports (CSV / Excel)
- Dark Mode

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Akshita Gour**

GitHub: https://github.com/akshigour12

---

⭐ If you found this project useful, consider giving it a star.
