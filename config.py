from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"

# Optional default source. You can also provide --source-url on the command line.
DEFAULT_SOURCE_URL = None

REQUEST_TIMEOUT = 20
MAX_RETRIES = 3

TOP_N = 15

SKILLS = {
    "Python": ["python"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript"],
    "C#": ["c#", "csharp"],
    "C++": ["c++"],
    "SQL": ["sql", "mysql", "postgresql", "postgres"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes", "k8s"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure"],
    "Linux": ["linux"],
    "Git": ["git", "github", "gitlab"],
    "Networking": ["networking", "network", "tcp/ip"],
    "Cybersecurity": ["cybersecurity", "information security", "it security"],
    "Machine Learning": ["machine learning", "ml", "deep learning"],
    "PowerShell": ["powershell"],
    "Bash": ["bash", "shell scripting"],
    "Windows Server": ["windows server", "active directory"],
}
