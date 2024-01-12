from pathlib import Path
from hashlib import md5

class Vote:
    def __init__(self):
        self.votes = {}

    def vote(self, char: str):
        self.votes[char] = self.votes.get(char, 0) + 1

    def result(self):
        return sorted(self.votes.items(), key=lambda x: x[1], reverse=True)[0][0]


base_path = Path("./backups")
disallowed = "{}#$[]§¤@"

byte_count = 3271
file_count = 1000
votes = []
for _ in range(byte_count):
    votes.append(Vote())
    
for i in range(file_count):
    file_name = f"manual.bak.{i:03d}"
    file_path = base_path / file_name
    data = file_path.read_text(encoding="latin-1")
    for j, c in enumerate(data):
        if c not in disallowed:
            votes[j].vote(c)

text = ""
for vote in votes:
    r = vote.result()
    text += r

output_path = Path("./manual")
written = output_path.write_text(text, encoding="latin-1")
print("Wrote", written, "bytes to", output_path)

flag = "PST{" + md5(text.encode("latin-1")).hexdigest() + "}"
print(flag)

