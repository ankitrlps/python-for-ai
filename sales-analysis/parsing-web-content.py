import requests
from bs4 import BeautifulSoup

def print_google_doc_grid(doc_url):
    # Step 1: Fetch the HTML content of the published document
    response = requests.get(doc_url)
    if response.status_code != 200:
        print(f"Failed to retrieve document. Status code: {response.status_code}")
        return

    # Step 2: Parse the HTML table using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print("No table found in the document.")
        return

    grid = {}
    max_x = 0
    max_y = 0

    # Step 3: Iterate through rows (skip the header row)
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            try:
                # Extract and clean text from each cell
                x_text = cols[0].get_text().strip()
                char = cols[1].get_text().strip()
                y_text = cols[2].get_text().strip()

                # Handle empty strings or non-integer headers safely
                x = int(x_text)
                y = int(y_text)

                grid[(x, y)] = char
                max_x = max(max_x, x)
                max_y = max(max_y, y)
            except ValueError:
                # Skip rows that don't contain valid integer coordinates
                continue

    # Step 4: Construct the 2D grid structure (y rows by x columns)
    # Note: Google Doc coordinates typically place (0,0) at the bottom-left,
    # so here print the rows in reverse order (from max_y down to 0).
    for y in range(max_y, -1, -1):
        row_chars = []
        for x in range(max_x + 1):
            row_chars.append(grid.get((x, y), ' '))
        print(''.join(row_chars))

print_google_doc_grid('https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub')