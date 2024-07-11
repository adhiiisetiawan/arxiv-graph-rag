import os
import time
import arxiv

# Create directory if not exists
dirpath = "arxiv_papers"
if not os.path.exists(dirpath):
    os.makedirs(dirpath)

# Search arXiv for papers related to "LLM"
client = arxiv.Client()
search = arxiv.Search(
    query="Vision Language Model",
    max_results=20,
    sort_order=arxiv.SortOrder.Descending
)

# Download and save the papers
for result in client.results(search):
    while True:
        try:
            result.download_pdf(dirpath=dirpath)
            print(f"-> Paper id {result.get_short_id()} with title '{result.title}' is downloaded.")
            break
        except (FileNotFoundError, ConnectionResetError) as e:
            print("Error occurred:", e)
            time.sleep(5)