import time, psutil, requests, random, os, glob
from rich.console import Console
from rich.table import Table

console = Console()

inner_animation = ["¬", "\\", "|", "/", "¬"]
outer_animation = ["*", " °", "."]

messages = [
    "Reality as perceived is but a small part of the truth",
    "We are all connected. We are all the same. You cannot escape",
    "To exist is to be aware, to be aware is to suffer",
    "Perhaps reality is but a self-made illusion",
    "You're gonna carry that weight",
    "You're late to change the past but in time to ruin the future",
    "Life isn't about winning or losing. It's about living"
]

last_rate = None
last_update = 0

def get_usd_mxn_cached():
    global last_rate, last_update
    if time.time() - last_update > 30:  # refresh every 30s
        try:
            r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=MXN", timeout=2)
            last_rate = r.json()["rates"]["MXN"]
            last_update = time.time()
        except:
            pass
    return last_rate


def get_system_stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return cpu, mem

def get_last_git_repo():
    git_dirs = glob.glob(os.path.expanduser("~") + "/**/.git", recursive=True)
    if git_dirs:
        return os.path.dirname(git_dirs[-1])
    return "You haven't referenced anything yet..."

def animated_message_frame(message, frame):
    inner = inner_animation[frame % len(inner_animation)]
    outer = outer_animation[frame % len(outer_animation)]
    return f"{outer} {inner} {message} {inner} {outer}"

def dashboard():
    frame = 0
    while True:
        cpu, mem = get_system_stats()
        usd_mxn = get_usd_mxn_cached()
        repo = get_last_git_repo()
        message = random.choice(messages)

        animated_msg = animated_message_frame(message, frame)

        table = Table(title=f"System Dashboard {inner_animation[frame % len(inner_animation)]}")

        table.add_column("Metric", justify="right")
        table.add_column("Value", justify="left")

        table.add_row("CPU Usage", f"{cpu}%")
        table.add_row("RAM Usage", f"{mem}%")
        table.add_row("Last Git Repo", repo)
        table.add_row("USD/MXN", f"{usd_mxn if usd_mxn else 'N/A'}")
        table.add_row("Message", animated_msg)

        console.clear()
        console.print(table)
        
        frame += 1
        time.sleep(0.2)

if __name__ == "__main__":
    dashboard()
