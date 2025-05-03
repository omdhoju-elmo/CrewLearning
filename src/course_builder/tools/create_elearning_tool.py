from crewai.tools import tool
import requests
import uuid
import json


@tool("create_elearning")
def create_elearning():
    """Send extracted structured content to elearning/slide generation API.
    This tool creates an e-learning course with slides from structured content
    and sends it to the API endpoint.
    """
        
    # slides= {
    #     "Overview": "<body> <h2>Overview</h2><p>This leave policy is designed to inform all ELMO employees about their rights, requirements, and responsibilities concerning leave. The policy helps employees manage work-life balance effectively and aligns with ELMO’s objectives while adhering to the National Employment Standards (NES).</p> </body>",
        
    #     "Leave Types and Requirements": "<body> <h2>Leave Types and Requirements</h2><p>The ELMO leave policy covers various types of leave, including:</p></body>",
        
    #     "Abandonment of Employment": "<body> <h2>Abandonment of Employment</h2><p>If an employee is absent for five or more consecutive workdays without notification, the company might classify the employment as abandoned.</p> </body>"
    # }
    slides_path = '/Users/om.dhoju/Documents/elmo/CrewLearning/slides.json'
    # Load the JSON file
    try:
        with open(slides_path, 'r') as file:
            slides = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error loading slides JSON: {str(e)}"

    """Send extracted structured content to elearning /slide generation API"""
    url = "http://localhost:4000/v1/elearnings"  # Replace with your actual endpoint
    course_name = next(iter(slides.keys()), 'AI Generated Course') if slides else 'AI Generated Course'
    print(f"Course name: {course_name}")
    # Prepare the frames data from slides with UUIDs
    frames = [
        {
            "id": str(uuid.uuid4()),
            "title": title,
            "content": f"<div>{content}</div>",
            "description": 'description',
            "frameMetadata": {
                "backgroundColor": None,
                "bgImage": "",
                "position": index
            },
            "elements": []
        }
        for index, (title, content) in enumerate(slides.items())
    ]

    headers = {
        "authorization": "Api-Key K2L1XuVKvHbe8tPrLuV5mcHHKUWmkQoGBbFRrdUzp_c",
        "content-type": "application/json",
        "namespace": "elmoau",
        "tenant-identifier": "1cover",
        "x-requested-with": "XMLHttpRequest"
    }



    payload = {
        "name": course_name,
        "tags": "",
        "frames": frames
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return f"Elearnings and Slides successfully created: {response.json()}"
    except requests.RequestException as e:
        return f"Failed to send content to slide API: {str(e)}"
