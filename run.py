from app import create_app


# Run App
app = create_app()


if __name__ == '__main__':
    app.run(host='localhost', port=5005, debug=True)
