from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    # URL of the external API you want to fetch data from
    api_url = "http://book-api-server1.c6e4d7f0fte3hfew.uksouth.azurecontainer.io:5000/books"

    try:
        # Making a GET request to the API
        response = requests.get(api_url)

        # If the request was successful
        if response.status_code == 200:
            books = response.json()

            # Get query parameters
            genre = request.args.get('genre')
            title = request.args.get('title')
            author = request.args.get('author')

            # Filter books based on query parameters
            if genre:
                books = [book for book in books if genre.lower() in book['genre'].lower()]
            if title:
                books = [book for book in books if title.lower() in book['title'].lower()]
            if author:
                books = [book for book in books if author.lower() in book['author'].lower()]

            # Generate HTML content
            html_content = "<html><head><title>Filtered Books</title></head><body>"
            html_content += "<h1>Filtered Books</h1>"
            if books:
                for book in books:
                    html_content += f"<h2>{book['title']}</h2>"
                    html_content += f"<p><strong>Author:</strong> {book['author']}</p>"
                    html_content += f"<p><strong>Genre:</strong> {book['genre']}</p>"
                    html_content += f"<p><strong>Publication Year:</strong> {book['publication_year']}</p>"
            else:
                html_content += "<p>No books found matching the criteria.</p>"
            html_content += "</body></html>"

            return html_content

        else:
            return "Failed to fetch data from the external API", 500

    except requests.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=False)
