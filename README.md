# Clone Docker Project from GitHub Repository

### This is a first lesson of learning about Git and GitHub

#### 1. Create GitHub repository
  - Set to repository to "public"
  - Add README file
  - Set ignore to node
  - Set security to node

#### 2. Clone GitHub repo using HTTPS method
  - Copy the HTTPS url from github repository
  - From your terminal type ```git clone <HTTPS url>```

#### 3. Try below Git commands on your terminal and use README.md file to do some changes and commit.
  ```
  git config --global user.name ""
  git config --global user.email ""
  git .status
  git add .
  git commit -m "Update README"
  git push
  ```

#### 4. Copy file from docker folder, follow the hand-on instruction too buid docker image
  |Files|
  |------|
  | .dockerignore|
  | gitignore|
  | app.py|
  | requirements.txt|
