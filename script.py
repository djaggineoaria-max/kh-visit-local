from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


def run() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
    print("Preview server running at http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    run()
