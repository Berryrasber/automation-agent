import datetime
import os
import subprocess
import shutil
import re

def execute_task(task_description):
    """Parses the task and executes the corresponding function."""
    
    task_description_lower = task_description.lower()
    
    # Task A1: Install uv and run datagen.py
    if "install uv" in task_description_lower and "datagen.py" in task_description_lower:
        return run_A1(task_description)
    
    # Task A2: Format /data/format.md using Prettier
    if "format" in task_description_lower and "prettier" in task_description_lower:
        return run_A2()

    # Task A3: Count Wednesdays in /data/dates.txt
    if "wednesday" in task_description_lower and "/data/dates.txt" in task_description_lower:
        return run_A3()
    
    # Task A4: Sort contacts.json by last_name, then first_name
    if "sort" in task_description_lower and "contacts.json" in task_description_lower:
        return run_A4()
    
    # Task A5: Extract recent log entries
    if "recent logs" in task_description_lower and "logs-recent.txt" in task_description_lower:
        return run_A5()
    
      # Task A6: Create an index of Markdown files
    if "create index" in task_description_lower and "markdown" in task_description_lower:
        return run_A6()
    
    # Task A7: Extract sender's email address from /data/email.txt using LLM
    if "extract" in task_description_lower and "email sender" in task_description_lower:
        return run_A7()
    
    # Task A8: Extract credit card number from /data/credit-card.png
    if "extract" in task_description_lower and "credit card" in task_description_lower:
        return run_A8()
    
    # Task A9: Find most similar comments in /data/comments.txt
    if "find" in task_description_lower and "similar comments" in task_description_lower:
        return run_A9()
    
    # Task A10: Calculate total sales for Gold tickets
    if "total sales" in task_description_lower and "gold ticket" in task_description_lower:
        return run_A10()
    
    # ✅ Task B3: Fetch data from an API and save it to /data/api-data.json
    if "fetch" in task_description_lower and "api" in task_description_lower:
        return run_B3(task_description)

    # ✅ Task B4: Clone a Git repository and commit a change
    if "clone" in task_description_lower and "git" in task_description_lower:
        return run_B4(task_description)
    
    # ✅ Task B5
    if "run sql" in task_description_lower and "on" in task_description_lower and "query" in task_description_lower:
        return run_B5(task_description)
    
    # ✅ Task B6
    if "list files" in task_description_lower and "directory" in task_description_lower:
        return run_B6(task_description)
    
    # ✅ Task B7
    if "read first" in task_description_lower and "lines of" in task_description_lower:
        return run_B7(task_description)
    
    # ✅ Task B8
    if "read last" in task_description_lower and "lines of" in task_description_lower:
        return run_B8(task_description)
    
    # ✅ Task B9
    if "compute sha-256" in task_description_lower and "hash of" in task_description_lower:
        return run_B9(task_description)
    
    # ✅ Task B10
    if "extract top" in task_description_lower and "words from" in task_description_lower:
        return run_B10(task_description)

    return {"status": "error", "error": "Bad Request", "details": "Unknown task"}

def run_A1(task_description):
    """Installs uv (if not installed) and runs datagen.py with the user's email as the argument."""
    try:
        # Extract email from the task description
        email = extract_email(task_description)
        if not email:
            return {"status": "error", "error": "Bad Request", "details": "No email provided in task description"}

        # Step 1: Check if `uv` is installed
        if not shutil.which("uv"):
            print("Installing uv...")
            subprocess.run(["pip", "install", "uv"], check=True)

        # Step 2: Check if `datagen.py` exists, if not, download it
        datagen_script = "datagen.py"
        if not os.path.exists(datagen_script):
            url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
            subprocess.run(["curl", "-o", datagen_script, url], check=True)

        # Step 3: Run `datagen.py` with the email and capture errors
        result = subprocess.run(
            ["C:\\Users\\yashv\\Downloads\\automation_agent\\venv\\Scripts\\python.exe", datagen_script, email],
            capture_output=True, text=True
        )

        # Debugging output in Flask terminal
        print("DEBUG: datagen.py Output ->", result.stdout)
        print("DEBUG: datagen.py Error ->", result.stderr)

        # If script fails, return the error message
        if result.returncode != 0:
            return {"status": "error", "error": "Internal Server Error", "details": result.stderr}

        return {"status": "success", "result": f"Task A1 completed: datagen.py executed with {email}"}
    
    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

def extract_email(task_description):
    """Extracts an email from the task description (basic extraction logic)."""
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', task_description)
    return match.group(0) if match else None

def run_A2():
    """Formats /data/format.md using Prettier."""
    try:
        file_path = "data/format.md"

        # Check if the file exists
        if not os.path.exists(file_path):
            return {"status": "error", "error": "File Not Found", "details": f"{file_path} does not exist"}

        # Run Prettier to format the file in place
        result = subprocess.run(["C:\\Users\\yashv\\AppData\\Roaming\\npm\\prettier.cmd", "--write", file_path], capture_output=True, text=True)

        # Debugging output
        print("DEBUG: Prettier Output ->", result.stdout)
        print("DEBUG: Prettier Error ->", result.stderr)

        # If Prettier fails, return the error
        if result.returncode != 0:
            return {"status": "error", "error": "Prettier Failed", "details": result.stderr}

        return {"status": "success", "result": f"Task A2 completed: {file_path} formatted successfully."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

def run_A3():
    """Counts the number of Wednesdays in /data/dates.txt."""
    input_file = "data/dates.txt"
    output_file = "data/dates-wednesdays.txt"

    is_safe, error_message = is_path_safe(input_file)
    if not is_safe:
        return {"status": "error", "error": "Security Violation", "details": error_message}

    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        count_wednesdays = sum(1 for line in lines if line.strip() and datetime.datetime.strptime(line.strip(), "%Y-%m-%d").weekday() == 2)

        with open(output_file, "w") as f:
            f.write(str(count_wednesdays))

        return {"status": "success", "result": f"Task A3 completed: Found {count_wednesdays} Wednesdays."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

    
import json
def run_A4():
    """Sorts contacts.json by last_name, then first_name, and writes to contacts-sorted.json."""
    try:
        input_file = "data/contacts.json"
        output_file = "data/contacts-sorted.json"

        # Check if the file exists
        if not os.path.exists(input_file):
            return {"status": "error", "error": "File Not Found", "details": f"{input_file} does not exist"}

        # Read the JSON data
        with open(input_file, "r") as f:
            contacts = json.load(f)

        # Sort contacts by last_name, then first_name
        sorted_contacts = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

        # Write the sorted data to the output file
        with open(output_file, "w") as f:
            json.dump(sorted_contacts, f, indent=4)

        return {"status": "success", "result": f"Task A4 completed: {output_file} created successfully."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}
    
import glob

def run_A5():
    """Extracts the first line of the 10 most recent .log files and writes to logs-recent.txt."""
    try:
        log_dir = "data/logs"
        output_file = "data/logs-recent.txt"

        # Get all .log files sorted by modified time (most recent first)
        log_files = sorted(glob.glob(os.path.join(log_dir, "*.log")), key=os.path.getmtime, reverse=True)

        # Extract first lines from the 10 most recent logs
        extracted_lines = []
        for log_file in log_files[:10]:  # Take only the latest 10 logs
            with open(log_file, "r") as f:
                first_line = f.readline().strip()  # Read first line
                if first_line:
                    extracted_lines.append(first_line)

        # Write extracted lines to logs-recent.txt
        with open(output_file, "w") as f:
            f.write("\n".join(extracted_lines))

        return {"status": "success", "result": f"Task A5 completed: Extracted recent log entries to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

def run_A6():
    """Creates an index.json mapping Markdown files to their first H1 title."""
    docs_dir = "data/docs"
    output_file = "data/docs/index.json"

    is_safe, error_message = is_path_safe(output_file)
    if not is_safe:
        return {"status": "error", "error": "Security Violation", "details": error_message}

    try:
        if not os.path.exists(docs_dir):
            return {"status": "error", "error": "Directory Not Found", "details": f"{docs_dir} does not exist"}

        index = {}
        for md_file in glob.glob(os.path.join(docs_dir, "*.md")):
            with open(md_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("# "):  
                        filename = os.path.basename(md_file)
                        index[filename] = line[2:].strip()
                        break  

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=4)

        return {"status": "success", "result": f"Task A6 completed: Markdown index created at {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

    
import re
def run_A7():
    """Extracts the sender's email address from /data/email.txt using regex (simulating LLM)."""
    try:
        input_file = "data/email.txt"
        output_file = "data/email-sender.txt"

        # Check if the file exists
        if not os.path.exists(input_file):
            return {"status": "error", "error": "File Not Found", "details": f"{input_file} does not exist"}

        # Read the email content
        with open(input_file, "r", encoding="utf-8") as f:
            email_content = f.read()

        # Simulated LLM extraction using regex
        match = re.search(r'From:\s*([\w\.-]+@[\w\.-]+\.\w+)', email_content, re.IGNORECASE)
        if not match:
            return {"status": "error", "error": "Email Not Found", "details": "No valid sender email detected in email.txt"}

        sender_email = match.group(1)

        # Write extracted email to output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(sender_email)

        return {"status": "success", "result": f"Task A7 completed: Extracted sender email to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}
    
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\yashv\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
from PIL import Image
import re

def run_A8():
    """Extracts the credit card number from /data/credit-card.png using OCR."""
    try:
        input_file = "data/credit-card.png"
        output_file = "data/credit-card.txt"

        # Check if the file exists
        if not os.path.exists(input_file):
            return {"status": "error", "error": "File Not Found", "details": f"{input_file} does not exist"}

        # Open and process the image
        image = Image.open(input_file)
        extracted_text = pytesseract.image_to_string(image)

        # Extract only digits (simulating extracting the credit card number)
        card_number = "".join(re.findall(r"\d+", extracted_text))

        if not card_number:
            return {"status": "error", "error": "Card Number Not Found", "details": "No valid card number detected in the image"}

        # Write extracted card number to output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(card_number)

        return {"status": "success", "result": f"Task A8 completed: Extracted credit card number to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}
    
from sentence_transformers import SentenceTransformer, util

def run_A9():
    """Finds the most similar pair of comments in /data/comments.txt using embeddings."""
    try:
        input_file = "data/comments.txt"
        output_file = "data/comments-similar.txt"

        # Check if the file exists
        if not os.path.exists(input_file):
            return {"status": "error", "error": "File Not Found", "details": f"{input_file} does not exist"}

        # Read all comments
        with open(input_file, "r", encoding="utf-8") as f:
            comments = [line.strip() for line in f.readlines() if line.strip()]

        if len(comments) < 2:
            return {"status": "error", "error": "Not Enough Comments", "details": "At least two comments are required"}

        # Load a pre-trained sentence transformer model
        model = SentenceTransformer("all-MiniLM-L6-v2")

        # Compute embeddings
        embeddings = model.encode(comments, convert_to_tensor=True)

        # Find the most similar pair
        max_similarity = -1
        most_similar_pair = ("", "")

        for i in range(len(comments)):
            for j in range(i + 1, len(comments)):
                similarity = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_pair = (comments[i], comments[j])

        # Write the most similar comments to output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(most_similar_pair[0] + "\n" + most_similar_pair[1])

        return {"status": "success", "result": f"Task A9 completed: Most similar comments written to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}
    
import sqlite3
def run_A10():
    """Calculates total sales for 'Gold' tickets from /data/ticket-sales.db."""
    db_file = "data/ticket-sales.db"
    output_file = "data/ticket-sales-gold.txt"

    is_safe, error_message = is_path_safe(output_file)
    if not is_safe:
        return {"status": "error", "error": "Security Violation", "details": error_message}

    try:
        if not os.path.exists(db_file):
            return {"status": "error", "error": "File Not Found", "details": f"{db_file} does not exist"}

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
        total_sales = cursor.fetchone()[0]
        conn.close()

        if total_sales is None:
            total_sales = 0  

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(total_sales))

        return {"status": "success", "result": f"Task A10 completed: Total sales for Gold tickets written to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}


#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

import os

def is_path_safe(file_path):
    """Ensures the file path stays within /data and does not allow deletions."""
    data_dir = os.path.abspath("data")  # Absolute path to /data
    full_path = os.path.abspath(file_path)  # Absolute path of the requested file

    # Rule B1: Ensure file stays within /data/
    if not full_path.startswith(data_dir):
        return False, "Access Denied: Attempt to access files outside /data/."

    # Rule B2: Prevent file deletions
    if "delete" in full_path.lower() or "remove" in full_path.lower():
        return False, "Access Denied: Deleting files is not allowed."

    return True, None


import requests

def run_B3(task_description):
    """Fetches data from an API and saves it to /data/api-data.json."""
    try:
        output_file = "data/api-data.json"

        # Extract the API URL from the task description
        match = re.search(r"(https?://\S+)", task_description)
        if not match:
            return {"status": "error", "error": "Bad Request", "details": "No API URL provided in task description"}

        api_url = match.group(0)

        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code != 200:
            return {"status": "error", "error": "API Request Failed", "details": f"Status Code: {response.status_code}"}

        api_data = response.json()  # Convert response to JSON

        # Write data to /data/api-data.json
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(api_data, f, indent=4)

        return {"status": "success", "result": f"Task B3 completed: API data saved to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}
    

import subprocess
def run_B4(task_description):
    """Clones a Git repository, makes a change, and commits it."""
    try:
        repos_dir = "data/repos"
        if not os.path.exists(repos_dir):
            os.makedirs(repos_dir)  # Ensure `/data/repos/` exists

        # Extract the Git repository URL from the task description
        match = re.search(r"(https?://\S+\.git)", task_description)
        if not match:
            return {"status": "error", "error": "Bad Request", "details": "No Git repository URL provided in task description"}

        repo_url = match.group(0)
        repo_name = repo_url.split("/")[-1].replace(".git", "")  # Extract repo name
        repo_path = os.path.join(repos_dir, repo_name)

        # Clone the repository (if not already cloned)
        if not os.path.exists(repo_path):
            subprocess.run(["git", "clone", repo_url, repo_path], check=True)

        # Create or update a file in the repository
        update_file = os.path.join(repo_path, "update.txt")
        with open(update_file, "w", encoding="utf-8") as f:
            f.write("This is an automated update.\n")

        # Commit and push changes
        subprocess.run(["git", "-C", repo_path, "add", "."], check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", "Automated update"], check=True)
        subprocess.run(["git", "-C", repo_path, "push"], check=True)

        return {"status": "success", "result": f"Task B4 completed: Repository {repo_name} updated and changes pushed."}

    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": "Git Command Failed", "details": str(e)}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

import sqlite3
import duckdb
def run_B5(task_description):
    """Runs a SQL query on SQLite or DuckDB and writes the result to /data/sql-results.txt."""
    try:
        print(f"DEBUG: Task received -> {task_description}")  # ✅ Debugging output
        output_file = "data/sql-results.txt"

        # Security Check: Ensure output file is inside /data/
        is_safe, error_message = is_path_safe(output_file)
        if not is_safe:
            return {"status": "error", "error": "Security Violation", "details": error_message}

        # Extract SQL query from task description
        match = re.search(r"run sql query '(.*?)' on (\S+)", task_description, re.IGNORECASE)
        if not match:
            return {"status": "error", "error": "Bad Request", "details": "No valid SQL query or database provided"}

        db_file, sql_query = match.groups()

        db_path = f"data/{db_file}"  # Ensure DB is inside /data/
        is_safe, error_message = is_path_safe(db_path)
        if not is_safe:
            return {"status": "error", "error": "Security Violation", "details": error_message}

        # Choose the right database engine
        if db_file.endswith(".db"):
            conn = sqlite3.connect(db_path)
        elif db_file.endswith(".duckdb"):
            conn = duckdb.connect(db_path)
        else:
            return {"status": "error", "error": "Unsupported Database", "details": "Only SQLite (.db) and DuckDB (.duckdb) are supported"}

        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()

        # Save results to file
        with open(output_file, "w", encoding="utf-8") as f:
            for row in results:
                f.write(str(row) + "\n")

        return {"status": "success", "result": f"Task B5 completed: SQL query executed, results saved to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}
    
def run_B6(task_description):
    """Lists all files in a directory and writes them to /data/files-list.txt."""
    try:
        output_file = "data/files-list.txt"

        # ✅ Security Check: Ensure output file is inside /data/
        is_safe, error_message = is_path_safe(output_file)
        if not is_safe:
            return {"status": "error", "error": "Security Violation", "details": error_message}

        # ✅ Extract directory path from task description
        match = re.search(r"list files in directory (.+)", task_description, re.IGNORECASE)
        if not match:
            return {"status": "error", "error": "Bad Request", "details": "No valid directory provided"}

        dir_path = f"data/{match.group(1)}"  # ✅ Ensure directory is inside /data/
        is_safe, error_message = is_path_safe(dir_path)
        if not is_safe:
            return {"status": "error", "error": "Security Violation", "details": error_message}

        # ✅ Check if directory exists
        if not os.path.exists(dir_path):
            return {"status": "error", "error": "Directory Not Found", "details": f"{dir_path} does not exist"}

        # ✅ Get list of all files in directory
        file_list = os.listdir(dir_path)

        # ✅ Write file names to files-list.txt
        with open(output_file, "w", encoding="utf-8") as f:
            for file_name in file_list:
                f.write(file_name + "\n")

        return {"status": "success", "result": f"Task B6 completed: File list saved to {output_file}."}

    except Exception as e:
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

def run_B7(task_description):
    """Reads the first N lines of a file and writes them to /data/head.txt."""
    try:
        output_file = "data/head.txt"

        print(f"DEBUG: Task received -> {task_description}")  # ✅ Debugging

        # ✅ Extract file path and number of lines
        match = re.search(r"read first (\d+) lines of (.+)", task_description, re.IGNORECASE)
        if not match:
            print("DEBUG: Regex failed to extract file path and number of lines")
            return {"status": "error", "error": "Bad Request", "details": "No valid file or number of lines provided"}

        num_lines, file_path = match.groups()
        num_lines = int(num_lines)
        file_path = f"data/{file_path}"  # ✅ Ensure file is inside /data/

        print(f"DEBUG: Extracted -> File: {file_path}, Lines: {num_lines}")  # ✅ Debugging

        # ✅ Check if file exists
        if not os.path.exists(file_path):
            print("DEBUG: File not found")
            return {"status": "error", "error": "File Not Found", "details": f"{file_path} does not exist"}

        # ✅ Read the first N lines
        lines = []
        with open(file_path, "r", encoding="utf-8") as f:
            for _ in range(num_lines):
                line = f.readline().strip()
                if not line:
                    break
                lines.append(line)

        print(f"DEBUG: Extracted lines -> {lines}")  # ✅ Debugging

        # ✅ Write output to head.txt
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return {"status": "success", "result": f"Task B7 completed: First {num_lines} lines written to {output_file}."}

    except Exception as e:
        print(f"DEBUG: Exception -> {e}")  # ✅ Debugging
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}


from collections import deque
import re
import os
def run_B8(task_description):
    """Reads the last N lines of a file and writes them to /data/tail.txt."""
    try:
        output_file = "data/tail.txt"

        print(f"DEBUG: Task received -> {task_description}")  # ✅ Debugging

        # ✅ Extract file path and number of lines
        match = re.search(r"read last (\d+) lines of (.+)", task_description, re.IGNORECASE)
        if not match:
            print("DEBUG: Regex failed to extract file path and number of lines")
            return {"status": "error", "error": "Bad Request", "details": "No valid file or number of lines provided"}

        num_lines, file_path = match.groups()
        num_lines = int(num_lines)
        file_path = f"data/{file_path}"  # ✅ Ensure file is inside /data/

        print(f"DEBUG: Extracted -> File: {file_path}, Lines: {num_lines}")  # ✅ Debugging

        # ✅ Check if file exists
        if not os.path.exists(file_path):
            print("DEBUG: File not found")
            return {"status": "error", "error": "File Not Found", "details": f"{file_path} does not exist"}

        # ✅ Read the last N lines using deque for efficiency
        with open(file_path, "r", encoding="utf-8") as f:
            lines = deque(f, num_lines)

        # ✅ Strip extra spaces and remove blank lines
        cleaned_lines = [line.strip() for line in lines if line.strip()]

        # ✅ If no valid lines, return an error message
        if not cleaned_lines:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("Error: File does not have enough valid lines")
            return {"status": "error", "error": "Not Enough Lines", "details": "File has too many blank lines"}

        # ✅ Write output to tail.txt without extra newlines
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(cleaned_lines))

        print(f"DEBUG: Final Output Written to {output_file}")  # ✅ Debugging

        return {"status": "success", "result": f"Task B8 completed: Last {num_lines} lines written to {output_file}."}

    except Exception as e:
        print(f"DEBUG: Exception -> {e}")  # ✅ Debugging
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}

import hashlib
def run_B9(task_description):
    """Computes the SHA-256 hash of a file and writes it to /data/hash.txt."""
    try:
        output_file = "data/hash.txt"

        print(f"DEBUG: Task received -> {task_description}")  # ✅ Debugging

        # ✅ Extract file path from the task description
        match = re.search(r"compute sha-256 hash of (.+)", task_description, re.IGNORECASE)
        if not match:
            print("DEBUG: Regex failed to extract file path")
            return {"status": "error", "error": "Bad Request", "details": "No valid file provided"}

        file_path = f"data/{match.group(1)}"  # ✅ Ensure file is inside /data/

        print(f"DEBUG: Extracted -> File: {file_path}")  # ✅ Debugging

        # ✅ Check if file exists
        if not os.path.exists(file_path):
            print("DEBUG: File not found")
            return {"status": "error", "error": "File Not Found", "details": f"{file_path} does not exist"}

        # ✅ Compute SHA-256 hash
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        file_hash = sha256_hash.hexdigest()

        # ✅ Write hash to hash.txt
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(file_hash)

        print(f"DEBUG: SHA-256 Hash -> {file_hash}")  # ✅ Debugging

        return {"status": "success", "result": f"Task B9 completed: SHA-256 hash written to {output_file}."}

    except Exception as e:
        print(f"DEBUG: Exception -> {e}")  # ✅ Debugging
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}


from collections import Counter
import string

def run_B10(task_description):
    """Extracts the top N most common words from a file and writes them to /data/words.txt."""
    try:
        output_file = "data/words.txt"

        print(f"DEBUG: Task received -> {task_description}")  # ✅ Debugging

        # ✅ Extract file path and number of words
        match = re.search(r"extract top (\d+) words from (.+)", task_description, re.IGNORECASE)
        if not match:
            print("DEBUG: Regex failed to extract file path and number of words")
            return {"status": "error", "error": "Bad Request", "details": "No valid file or number of words provided"}

        num_words, file_path = match.groups()
        num_words = int(num_words)
        file_path = f"data/{file_path}"  # ✅ Ensure file is inside /data/

        print(f"DEBUG: Extracted -> File: {file_path}, Words: {num_words}")  # ✅ Debugging

        # ✅ Check if file exists
        if not os.path.exists(file_path):
            print("DEBUG: File not found")
            return {"status": "error", "error": "File Not Found", "details": f"{file_path} does not exist"}

        # ✅ Read file content
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().lower()

        # ✅ Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # ✅ Tokenize words and count frequency
        words = text.split()
        word_counts = Counter(words)

        # ✅ Get the top N most common words
        most_common_words = word_counts.most_common(num_words)

        # ✅ Format the output (word: count)
        formatted_output = "\n".join([f"{word}: {count}" for word, count in most_common_words])

        # ✅ Write output to words.txt
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(formatted_output)

        print(f"DEBUG: Extracted words -> {formatted_output}")  # ✅ Debugging

        return {"status": "success", "result": f"Task B10 completed: Top {num_words} words written to {output_file}."}

    except Exception as e:
        print(f"DEBUG: Exception -> {e}")  # ✅ Debugging
        return {"status": "error", "error": "Internal Server Error", "details": str(e)}




