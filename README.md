# URL Masking

A minimal Flask web tool for generating URL masking examples from an original URL, display domain, and keywords. The interface uses a clean black-and-white layout with a centered form, subtle card styling, and a modern animated generate button.

## Features

- Minimal black-and-white web interface.
- Original URL, display domain, and keyword inputs.
- Generates masked URL examples using available shortener services.
- Copy button for generated results.
- Responsive centered layout for desktop and mobile.
- Custom SVG favicon and clean browser tab title.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RIFAT068R/url-masking.git
   cd url-masking
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open the app:

   ```text
   http://127.0.0.1:5000
   ```

## Usage

1. Enter an original URL, such as `https://example.com/page`.
2. Enter a display domain, such as `trusted-example.com`.
3. Enter keywords, such as `secure-login`.
4. Click `Generate`.
5. Copy any generated result from the result section.

## Project Structure

```text
url-masking/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── favicon.svg
├── templates/
│   └── index.html
├── vercel.json
├── LICENSE
└── README.md
```

## Dependencies

- Flask
- pyshorteners

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
