
# Voice-Activated Personal Assistant

This project is a simple voice-activated personal assistant that can perform basic tasks like opening websites, playing music, and searching Wikipedia. The assistant listens for voice commands, processes them, and executes the corresponding actions.

## Features

- Open popular websites like YouTube and Google.
- Play a specific song from a specified directory.
- Search for summaries on Wikipedia.
- Respond with voice feedback using text-to-speech.

## Requirements

To run this project, you need to have Python installed along with the following packages:

- `SpeechRecognition`
- `wikipedia`
- `pyttsx3`
- `webbrowser`
- `os`

## Installation

1. Clone the repository from GitHub:
    ```sh
    git clone https://github.com/Surya22pc/voice-activated-personal-assistant.git
    cd voice-activated-personal-assistant
    ```

2. Install the required packages using `pip`:
    ```sh
    pip install SpeechRecognition wikipedia pyttsx3
    ```

3. Ensure that you have a working microphone connected to your computer.

## Usage

1. Open the terminal and navigate to the project directory.

2. Run the script:
    ```sh
    python assistant.py
    ```

3. The assistant will greet you and wait for your commands. Some example commands are:

    - "Open YouTube"
    - "Open Google"
    - "Play music"
    - "Search for [topic] on Wikipedia"
    

4. The assistant will execute the command and provide a voice response.

## Customization

- **Music Directory**: Update the `music_dir` variable with the path to your music directory.
    ```python
    music_dir = r"C:\MUSIC"  # Change this to your music directory
    ```

- **Voice Settings**: The TTS engine uses a male voice by default. You can change the voice by updating the `engine.setProperty('voice', voices[0].id)` line.

## Troubleshooting

- If the assistant does not recognize your voice, make sure your microphone is working properly and try adjusting the `pause_threshold` for the recognizer.
- For Wikipedia searches, if multiple results are found, the assistant will ask you to be more specific.
- Ensure you have an active internet connection for the speech recognition and web browsing functionalities.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---



This README file provides an overview of the project, installation instructions, usage examples, and customization tips to help users set up and run their own voice-activated personal assistant.
