
# Lyrics Extractor

Lyrics Extractor is a Python GUI application built with tkinter that allows users to fetch song lyrics using the Genius API.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Song and Artist Input:** Enter the name of the song to fetch lyrics.
- **Genius API Integration:** Utilizes the Genius API to fetch lyrics based on user input.
- **GUI Interface:** Simple tkinter-based GUI for easy interaction.
- **Error Handling:** Provides user feedback for invalid inputs or failed lyric retrieval.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Vaishnavi544/LyricsExtractor.git
   cd LyricsExtractor
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Genius API credentials:**

   - Sign up for a Genius API account and obtain your API access token.
   - Replace `'YOUR_GENIUS_API_ACCESS_TOKEN'` in `lyricsex.py` with your actual API token.

## Usage

- Run the application:

  ```bash
  python main.py
  ```

- Enter the name of the song  in the provided fields.
- Click on the "Fetch Lyrics" button to retrieve and display the lyrics.
- Ensure an active internet connection for fetching lyrics from the Genius API.

## Dependencies

- Python 3.x
- tkinter
- requests
- beautifulsoup4

## Contributing

Contributions are welcome! If you'd like to add features, improve code, or fix bugs, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
![image](https://github.com/Vaishnavi544/LyricsExtractor/assets/142041825/00946500-f9a8-40b7-aedd-a736a3fe88aa)


