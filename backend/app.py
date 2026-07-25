from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from utils import(
    validate_url,
    fetch_page,
    parse_html,
    extract_title,
    extract_meta_description,
    count_h1,
    count_missing_alt,
    count_words
)

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return {
        "message" : "Page Pulse API Running"
    }

@app.route("/analyze")
def analyze():

    url = request.args.get("url")

    if not url:
        return jsonify({
            "error":"URL parameter is required"
        }), 400

    if not validate_url(url):
        return jsonify({
            "error": "Invalid URL"
        }),400

    try:
        response, response_time = fetch_page(url)

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type.lower():
            return jsonify({
                  "error" : "URL is not an HTML page."
            }), 400

        soup = parse_html(response.text)

        title = extract_title(soup)

        meta = extract_meta_description(soup)

        h1 = count_h1(soup)

        missing_alt = count_missing_alt(soup)

        words = count_words(soup)

        return jsonify({
            "url":url,
            "title":title,
            "meta_description":meta,
            "h1_count":h1,
            "missing_alt_images":missing_alt,
            "word_count":words,
            "response_time":response_time,
            "status_code":response.status_code

        })
    except requests.exceptions.Timeout:
        return jsonify ({
            "error":"Request timed out."
        }), 408

    except requests.exceptions.ConnectionError:
            return jsonify ({
                "error":"Could not connect to website."
            }), 400

    except Exception:
         return jsonify({
              "error":"Unexpected server error."
         }), 500

if __name__ =="__main__":

    app.run(debug = True)